# 模型測試：經典 AI 模型測試合集

收錄網路上流傳的經典大型語言模型（LLM）測試，整理成一個打開就能用的網頁。每個測試都有：

- **名稱與出處**
- **測試重點**：這題在考模型什麼能力
- **完整提示詞**：英文原版＋中文版，一鍵複製
- **正確答案或評分重點**
- **範例圖**：繪圖和程式題附上能實際運作的範例動畫，推理題附上解題示意圖

## 使用方式

1. 下載 `index.html`，用瀏覽器打開即可，不需要安裝任何東西，也不需要網路連線。
2. 也可以開啟本專案的 GitHub Pages 網址，直接在線上使用。
3. 挑一個測試，按「複製」，貼到你想測試的 AI 模型對話框裡。
4. 對照「正確答案／評分重點」判斷模型表現。

> 建議每次都開新對話測試；同一題可以多跑幾次，看結果是否穩定。題目流傳越久，越可能被模型「背」起來，可以試著換掉數字或名詞（例如把鵜鶘換成章魚）再測。

## 收錄的測試

| 分類 | 測試 |
| --- | --- |
| 繪圖與程式 | 鵜鶘騎腳踏車、旋轉六邊形裡的彈跳球、旋轉七邊形 20 顆球（進階版）、一次寫出能玩的貪食蛇 |
| 推理陷阱 | Strawberry 有幾個 r、9.11 和 9.9 哪個大、愛麗絲問題（AIW）、改編版過河問題、透明門的三門問題、一磅鐵和兩磅羽毛、沒有矛盾的外科醫生謎題、大數乘法心算、單字倒著拼 |
| 指令遵循 | 每句都以 apple 結尾、不能用某個字母或字 |
| 中文理解 | 「我差點沒摔倒」 |
| 知識與幻覺 | 不存在的論文（幻覺測試） |
| 長文處理 | 長文找針（Needle in a haystack） |

## 這些測試的意義與限制

這類小測試好上手、結果一眼就看得懂，能補足正式基準測試（benchmark）看不到的地方，例如模型是否只是套用背過的答案。但它們題數少、每次結果可能不同，也可能已經混進訓練資料，**不適合當作嚴謹的模型評比**。真的要比較模型，請搭配正式評測與實際使用經驗。

## 參與貢獻

歡迎開 Issue 或 Pull Request：

- 新增經典測試（請附上出處、完整提示詞、正確答案）
- 修正提示詞原文或翻譯
- 改善範例圖或介面

測試資料都寫在 `index.html` 的 `T`（題目）與 `ZH`（中文版提示詞）兩個陣列中，範例圖在 `FIG` 物件裡。

## 出處與致謝

- 鵜鶘騎腳踏車：[Simon Willison](https://simonwillison.net/tags/pelican-riding-a-bicycle/)
- 旋轉形狀彈跳球：X（Twitter）社群、[TechCrunch 報導](https://techcrunch.com/2025/01/24/people-are-benchmarking-ai-by-having-it-make-balls-bounce-in-rotating-shapes)、[Artificial Analysis MicroEvals](https://artificialanalysis.ai/microevals/balls-bouncing-inside-a-spinning-hexagon-1750176234580)
- 旋轉七邊形 20 顆球：Reddit r/LocalLLaMA 社群
- 愛麗絲問題：論文 *Alice in Wonderland: Simple Tasks Showing Complete Reasoning Breakdown in State-Of-the-Art Large Language Models*（2024）
- 長文找針：Greg Kamradt
- 其他題目為網路社群流傳的經典題或其改編版

各測試的原始創意屬於原作者；本專案的整理、翻譯、網頁與範例圖以 MIT 授權釋出。

## 授權

[MIT License](LICENSE)
