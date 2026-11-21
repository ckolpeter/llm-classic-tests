#!/usr/bin/env python3
"""Embed tests.json into index.html so the page works offline (double-click to open).

Usage:
    python build.py          # update index.html from tests.json
    python build.py --check  # exit 1 if index.html is out of date or tests.json is invalid
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests.json"
PAGE = ROOT / "index.html"
START, END = "<!-- TESTS:START -->", "<!-- TESTS:END -->"

CATEGORIES_REQUIRED = {"id", "zh", "en"}
DIFFICULTIES = {"easy", "medium", "hard"}
PROMPT_TYPES = {"main", "followup", "variant"}
LANGS = {"zh", "en"}


def validate(data):
    errors = []
    cats = {c.get("id") for c in data.get("categories", [])}
    for c in data.get("categories", []):
        if not CATEGORIES_REQUIRED <= c.keys():
            errors.append(f"category {c} needs id, zh, en")
    seen = set()
    for i, t in enumerate(data.get("tests", [])):
        where = f"tests[{i}] ({t.get('id', '?')})"
        if not re.fullmatch(r"[a-z0-9-]+", t.get("id", "")):
            errors.append(f"{where}: id must be lowercase letters, digits and dashes")
        if t.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(t.get("id"))
        if t.get("category") not in cats:
            errors.append(f"{where}: unknown category {t.get('category')!r}")
        if t.get("difficulty") not in DIFFICULTIES:
            errors.append(f"{where}: difficulty must be one of {sorted(DIFFICULTIES)}")
        for field in ("source", "name", "about", "answer"):
            v = t.get(field)
            if not isinstance(v, dict) or not v.get("zh") or not v.get("en"):
                errors.append(f"{where}: {field} needs both zh and en text")
        prompts = t.get("prompts") or []
        if not any(p.get("type") == "main" for p in prompts):
            errors.append(f"{where}: needs at least one main prompt")
        for p in prompts:
            if p.get("type") not in PROMPT_TYPES or p.get("lang") not in LANGS or not p.get("text"):
                errors.append(f"{where}: bad prompt {p}")
    return errors


def render(data, page):
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    block = f'{START}\n<script id="tests-data" type="application/json">{payload}</script>\n{END}'
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(page):
        sys.exit("index.html is missing the TESTS:START / TESTS:END markers")
    return pattern.sub(lambda _: block, page)


def main():
    data = json.loads(TESTS.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("tests.json has problems:\n  " + "\n  ".join(errors))
        sys.exit(1)
    page = PAGE.read_text(encoding="utf-8")
    new = render(data, page)
    if "--check" in sys.argv:
        if new != page:
            print("index.html is out of date. Run: python build.py")
            sys.exit(1)
        print(f"OK: {len(data['tests'])} tests, index.html is up to date")
        return
    PAGE.write_text(new, encoding="utf-8")
    print(f"Embedded {len(data['tests'])} tests into index.html")


if __name__ == "__main__":
    main()
