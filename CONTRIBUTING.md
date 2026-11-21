# 參與貢獻 / Contributing

感謝你願意幫忙！這份文件說明怎麼新增測試、修改題目或改善網頁。
English version below.

## 新增或修改測試

所有測試題目都在 [`tests.json`](tests.json)。最簡單的方式是[開一個「新增測試」Issue](../../issues/new/choose)，填好表單，維護者會幫你加進去。想自己發 Pull Request 的話：

1. Fork 這個 repo，編輯 `tests.json`，在 `tests` 陣列裡加一筆：

```json
{
  "id": "my-new-test",
  "category": "reasoning",
  "difficulty": "medium",
  "saturated": false,
  "source": { "zh": "出處（作者、年份）", "en": "Source (author, year)" },
  "name":   { "zh": "中文名稱", "en": "English name" },
  "about":  { "zh": "這題在考什麼", "en": "What this tests" },
  "answer": { "zh": "<b>正確答案：</b>……", "en": "<b>Answer:</b> ..." },
  "prompts": [
    { "type": "main", "lang": "en", "text": "English original prompt" },
    { "type": "main", "lang": "zh", "text": "中文版提示詞" }
  ]
}
```

2. 執行 `python build.py`，把資料內嵌進 `index.html`（這一步也會檢查格式）。
3. 用瀏覽器打開 `index.html` 確認顯示正常，然後送出 Pull Request。

### 欄位說明

| 欄位 | 說明 |
| --- | --- |
| `id` | 唯一代號，只能用小寫英文、數字和 `-` |
| `category` | `draw`、`reasoning`、`instruction`、`chinese`、`knowledge`、`longctx` 其中之一 |
| `difficulty` | `easy`、`medium`、`hard` |
| `saturated` | 近年新模型是否大多已能通過（`true` 會顯示「新模型多已通過」） |
| `source` / `name` / `about` / `answer` | 都要有 `zh` 和 `en`。`answer` 可以用 `<b>` 和 `<br>` |
| `prompts` | `type` 是 `main`（主要）、`followup`（延伸追問）或 `variant`（中文變化版）；`lang` 是 `en` 或 `zh` |

### 自動判分（選填）

答案固定的題目可以加一個 `grader` 欄位，網頁上就會出現「自動判分」。正規表達式使用 JavaScript 語法，比對時不分大小寫。

| `type` | 用途 | 欄位 |
| --- | --- | --- |
| `choice` | 在回答的結論處，看「正確答案」和「常見錯誤答案」哪個先出現 | `ok`、`fail`（正規表達式）、選填 `note` |
| `contains` | 回答必須包含所有 `all`，以及 `any` 其中之一 | `all`、`any`、選填 `failNote` |
| `exact` | 去掉格式後，回答裡要出現標準答案 | `expect`（陣列）、`normalize`：`digits`／`alnum`／`text` |
| `sudoku` | 取回答中最後 81 個數字和解答比對 | `solution` |
| `sentences` | 每個句子都要以指定的詞結尾 | `count`、`options`（`label`、`word`） |
| `lipogram` | 全文不能出現指定的字 | `options`（`label`、`chars`） |

`build.py` 會檢查格式。也可以在瀏覽器的開發者工具裡用 `LLMTests.grade(grader, 回答文字)` 試試看判分結果。

### 隨機變體（選填）

隨機變體寫在 `index.html` 的 `GEN` 物件裡，用測試的 `id` 當 key。函式回傳新的 `prompts`、`answer`，以及（選填）新的 `grader`，會取代原題同類型的提示詞。範例圖如果能跟著變體更新，在 `FIG` 裡加上 `va:true`，`html(v)` 會收到變體資料。

### 收錄原則

- **要有出處**：網路上真的有人在用的測試，請附上來源。改編版也請註明改編自哪一題。
- **要能判斷對錯**：寫清楚正確答案，或具體的評分重點。
- **提示詞保留原文**：英文原版請照原始出處一字不改；中文版要意思相同。
- **不收**：需要付費資料、涉及真實個人隱私，或可能造成傷害的題目。

### 範例圖

範例圖寫在 `index.html` 的 `FIG` 物件裡，用測試的 `id` 當 key。每個範例圖要有 `html`（回傳 SVG 或 canvas）、`cap`（中英說明），以及選用的 `init`（啟動動畫）。請使用 CSS 變數上色，讓深色模式也看得清楚。

---

## Contributing (English)

All tests live in [`tests.json`](tests.json). The easiest way to suggest one is to [open a "New test" issue](../../issues/new/choose). To send a pull request instead:

1. Fork the repo and add an entry to the `tests` array in `tests.json` (see the example and field table above).
2. Run `python build.py` to embed the data into `index.html`; it also validates the format.
3. Open `index.html` in a browser to check it, then open a pull request.

Guidelines: include a source for every test (and say what a variant is based on), give a clear answer or concrete grading criteria, keep English prompts exactly as originally published, make the Chinese version equivalent in meaning, and don't submit tests that rely on paid data, private individuals, or could cause harm.

Example figures live in the `FIG` object in `index.html`, keyed by test `id`, each with `html` (returning SVG or a canvas), a bilingual `cap`, and an optional `init` for animation. Use the CSS variables for colours so they work in dark mode.

**Auto-grading (optional).** Tests with a fixed answer can have a `grader` field (see the table above for the types `choice`, `contains`, `exact`, `sudoku`, `sentences`, `lipogram`). Regexes use JavaScript syntax and are matched case-insensitively. `build.py` validates the format, and you can try a grader in the browser console with `LLMTests.grade(grader, replyText)`.

**Random variants (optional).** Generators live in the `GEN` object in `index.html`, keyed by test `id`. Each returns new `prompts`, an `answer` and optionally a `grader`; generated prompts replace the original prompts of the same type. If a figure can follow the variant, set `va:true` in `FIG` and its `html(v)` receives the variant data.
