<div align="center">

<a href="https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/images/banner.png" alt="Awesome Gemini 3.6 Flash guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Gemini 3.6 Flash](https://img.shields.io/badge/Gemini_3.6_Flash-Model_Page-00d4e6)](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_badge)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=docs_badge)

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-577590)](README_ru.md)

</div>

# Awesome Gemini 3.6 Flash 指南與用例

## 🍌 簡介

歡迎閱讀這份有公開來源證據支撐的 Gemini 3.6 Flash 實踐指南

**本倉庫收集公開創作者證據中的 Gemini 3.6 Flash 工作流、建置成果、評估比較與實際限制**

每個案例都來自經過審查的來源包，標題連結到原始貼文，作者連結到創作者主頁，只有來源文字確實包含 prompt 時才會收錄

## 📊 概述

- 從 33 個經過審查的來源貼文中選出 33 個高可信度案例
- 涵蓋範圍包括代理、編碼、網站、遊戲、3D、基準式比較和實際安全限制
- 所有 24 個影片案例均提供可見的海報和可播放的 R2 託管 MP4；圖像案例保留每個經過審查的來源圖像
- EvoLink 標註的正式 model ID 是 `gemini-3.6-flash`，本倉庫連結到目前模型頁與 Gemini Native API 接入文件

> [!NOTE]
> 本合集優先保留可觀察證據，不重建缺失的 prompt，不推斷未公開的設定步驟，也不把單一創作者的結果泛化為通用 benchmark

**從這裡開始: [探索Gemini 3.6 Flash](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link) · [取得 API 金鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key) · [開啟 Gemini Native API 文檔](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=first_run)**

## 📑 選單

| 部分 | 案例 |
|---|---|
| [⚡ 效率與代理](#efficiency-agents) | 8 |
| [💻 編碼和應用程式](#coding-apps) | 4 |
| [🎮 網頁、遊戲和 3D](#web-games-3d) | 10 |
| [🧪 評估與比較](#evaluations) | 8 |
| [🛡️ 安全與限制](#safety-limits) | 3 |
| [相關儲存庫](#related-repositories) | 相關儲存庫 |
| [快速入門](#quick-start) | 快速入門 |
| [致謝](#acknowledge) | 致謝 |

| 案例 | 類別 | 它顯示了什麼 | 類型 |
|---|---|---|---|
| [token效率並存](#case-1) | 效率與代理 | 在為代理程式規模工作負載選擇 Flash 模型之前，請先比較相同工作流程上的輸出令牌使用情況 | Evaluation |
| [Antigravity遺留程式碼的現代化](#case-2) | 效率與代理 | 使用受控的遺留程式碼遷移任務來比較代理延遲、編輯品質和完成行為 | Evaluation |
| [Canvas token效率測試](#case-3) | 效率與代理 | 跨模型版本執行相同的 Canvas 任務並檢查工件和令牌的使用情況 | Evaluation |
| [瀏覽器代理基準](#case-4) | 效率與代理 | 對瀏覽器代理程式的成功和成本進行基準測試，而不是單獨優化任一指標 | Benchmark |
| [長尾事實檢索效率](#case-5) | 效率與代理 | 使用困難的事實檢索任務來比較推理步驟和思考 token開銷 | Evaluation |
| [企業文件處理](#case-6) | 效率與代理 | 在設定生產預設值之前評估長專利和文件解析的推理工作 | Benchmark |
| [JetBrains 中的工程任務評估](#case-7) | 效率與代理 | 建立客觀的工程任務並在同一 IDE 工作流程中比較模型產生 | Evaluation |
| [多代理程式碼遷移](#case-8) | 效率與代理 | 使用相同的編排計劃測試程式碼遷移，並比較延遲、編輯和最終品質 | Demo |
| [Android 吉他調音器](#case-9) | 編碼和應用程式 | 建立一個專注的行動實用程式原型，將傳統音訊工具與人工智慧輔助的替代調音相結合 | Demo |
| [交通燈模擬](#case-10) | 編碼和應用程式 | 要求模型提供可執行的視覺化，以檢查產生的程式碼是否捕捉定時和隨機流量行為 | Demo |
| [鍵盤鋼琴應用程式](#case-11) | 編碼和應用程式 | 將簡單的互動概念轉變為可玩的鍵盤控制的 Web 應用程式 | Demo |
| [桌上機器人語音助手](#case-12) | 編碼和應用程式 | 將 Flash 和 Flash-Lite 整合到語音應用程式中並比較第一個回應行為 | Integration |
| [金門大橋 HTML 故障](#case-13) | 網頁、遊戲和 3D | 在信任產生的 3D Web 體驗之前，使用嚴格的文件傳遞任務來測試指令遵循 | Limit |
| [公共提示視覺測試](#case-14) | 網頁、遊戲和 3D | 當您需要創建者的完整提示而不是從輸出重建它時，請打開來源執行緒 | Demo |
| [單提示畫布遊戲](#case-15) | 網頁、遊戲和 3D | 使用 Canvas 中的一個提示來測試模型將緊湊的遊戲概念轉變為互動式結果的速度 | Demo |
| [登陸頁版本比較](#case-16) | 網頁、遊戲和 3D | 保持模型各世代之間的提示固定，以隔離登陸頁面執行和視覺判斷中的變化 | Evaluation |
| [地鐵跑酷 3D 原型](#case-17) | 網頁、遊戲和 3D | 為編碼實驗提供擴展思維，並檢查互動品質和視覺保真度 | Demo |
| [一頁網站比較](#case-18) | 網頁、遊戲和 3D | 保持網站提示和推理水準不變，然後比較令牌成本、速度和設計偏好 | Evaluation |
| [狂野西部遊戲失敗](#case-19) | 網頁、遊戲和 3D | 將失敗的遊戲生成輸出視為決定何時切換模型或修改任務的證據 | Limit |
| [Antigravity遊戲素材失效](#case-20) | 網頁、遊戲和 3D | 在接受人工智慧生成的遊戲原型之前，請檢查視覺材料和實際互動行為 | Limit |
| [勞斯萊斯 SVG 比較](#case-21) | 網頁、遊戲和 3D | 使用固定的 SVG 主題來比較兩代 Flash 如何處理形狀、細節和構圖 | Evaluation |
| [現實水族館測試](#case-22) | 網頁、遊戲和 3D | 使用有界 3D 場景來比較模型版本之間的真實感和實現品質 | Evaluation |
| [Max Reasoning 中的 Gemini 與 Grok](#case-23) | 評估與比較 | 使用相同的提示和最大推理設定來比較速度、成本和輸出，而不是依賴模型聲譽 | Evaluation |
| [Gemini與Sonnet在最大設置](#case-24) | 評估與比較 | 比較相同提示及其最強設定的模型，然後檢查實際產生的工件 | Evaluation |
| [視覺理解測試](#case-25) | 評估與比較 | 在採用視覺工作流程模型之前，使用具體的影像任務來檢查回應品質和互動風格 | Demo |
| [火箭聯盟遊戲基準](#case-26) | 評估與比較 | 運行重複的遊戲產生基準並記錄建立時間和一致的主觀排名 | Benchmark |
| [EyeBench 視覺比較](#case-27) | 評估與比較 | 使用穩定的視覺基準將增量效率增益與絕對品質分開 | Benchmark |
| [剪紙動畫對比](#case-28) | 評估與比較 | 在評估創意生成時，分別比較反應速度和最終動畫 | Evaluation |
| [AI Arena 產生基準](#case-29) | 評估與比較 | 使用相同的 arena 任務來比較多個編碼模型的建造時間、價格和工件品質 | Benchmark |
| [跨模型遊戲建構成本](#case-30) | 評估與比較 | 在選擇遊戲原型設計模型時，一起追蹤迭代次數、開發人員經驗、功能和成本 | Benchmark |
| [網路安全拒絕基準](#case-31) | 安全與限制 | 在安全工具評估中包含拒絕行為，因為防禦性程式碼審查可能會被攻擊性請求阻止 | Limit |
| [知識新鮮度失敗](#case-32) | 安全與限制 | 透過檢索來驗證當前事實，而不是相信聲稱的知識截止點 | Limit |
| [越獄紅隊測試](#case-33) | 安全與限制 | 將越獄聲明視為需要受控複製和安全審查的紅隊訊號，而不是可重複使用的指示 | Limit |

<a id="efficiency-agents"></a>
## ⚡ 效率與代理

<a id="case-1"></a>
### 案例 1: [token效率並存](https://x.com/JeffDean/status/2079591562145870043) (作者 [@JeffDean](https://x.com/JeffDean))

**在為代理程式規模工作負載選擇 Flash 模型之前，請先比較相同工作流程上的輸出令牌使用情況**

Jeff Dean 分享了一個並排演示，比較了 Gemini 3.6 Flash 和 3.5 Flash，並強調了新模型中較低的token使用量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-2"></a>
### 案例 2: [Antigravity遺留程式碼的現代化](https://x.com/antigravity/status/2079663375991046351) (作者 [@antigravity](https://x.com/antigravity))

**使用受控的遺留程式碼遷移任務來比較代理延遲、編輯品質和完成行為**

Google Antigravity 展示了兩代 Flash 重建遺留軟體的能力，並報告指出 Gemini 3.6 Flash 的延遲和輸出得到改善，完成速度更快

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-3"></a>
### 案例 3: [Canvas token效率測試](https://x.com/stevibe/status/2079599477216956437) (作者 [@stevibe](https://x.com/stevibe))

**跨模型版本執行相同的 Canvas 任務並檢查工件和令牌的使用情況**

創作者在一個簡短的 Canvas 任務上對 Gemini 3.6 Flash 和 3.5 Flash 進行了比較，發現 3.6 Flash 的token使用率明顯較低

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-4"></a>
### 案例 4: [瀏覽器代理基準](https://x.com/browser_use/status/2079602472516264010) (作者 [@browser_use](https://x.com/browser_use))

**對瀏覽器代理程式的成功和成本進行基準測試，而不是單獨優化任一指標**

根據其 BU 基準測試，Gemini 3.6 Flash 的瀏覽器使用率為 68%，而 GPT-5.6 Sol 為 67%，Sonnet 4.6 為 62%，Opus 4.8 為 74%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg" alt="Case 4 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-07-21

---

<a id="case-5"></a>
### 案例 5: [長尾事實檢索效率](https://x.com/__apf__/status/2079603658141184134) (作者 [@__apf__](https://x.com/__apf__))

**使用困難的事實檢索任務來比較推理步驟和思考 token開銷**

創建者在一項複雜的長尾事實檢索任務上執行 Gemini 3.5 和 3.6 Flash，並報告 3.6 Flash 的步驟數量減半，思考 token減少了 75%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-6"></a>
### 案例 6: [企業文件處理](https://x.com/databricks/status/2079598684455551326) (作者 [@databricks](https://x.com/databricks))

**在設定生產預設值之前評估長專利和文件解析的推理工作**

Databricks 報告稱，文件分類準確度高於 3.5 Flash，在長專利上取得了出色的結果，且中等工作量的文件解析總標記比高工作量的文件解析少約 32%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png" alt="Case 6 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-07-21

---

<a id="case-7"></a>
### 案例 7: [JetBrains 中的工程任務評估](https://x.com/jetbrains/status/2079618218587574636) (作者 [@jetbrains](https://x.com/jetbrains))

**建立客觀的工程任務並在同一 IDE 工作流程中比較模型產生**

JetBrains 在 AI Assistant 和 Junie 中對 Gemini 3.6 Flash 與上一代 Flash 進行了客觀的工程任務評估

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-8"></a>
### 案例 8: [多代理程式碼遷移](https://x.com/CodeByPoonam/status/2079607995861021073) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**使用相同的編排計劃測試程式碼遷移，並比較延遲、編輯和最終品質**

該演示顯示 Gemini 3.6 Flash 透過 Antigravity 中的多代理程式編排執行程式碼遷移，並報告比 3.5 Flash 更低的延遲和更高的品質

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4)

類型: Demo | 日期: 2026-07-21

---


<a id="coding-apps"></a>
## 💻 編碼和應用程式

<a id="case-9"></a>
### 案例 9: [Android 吉他調音器](https://x.com/bijanbowen/status/2079675781794443640) (作者 [@bijanbowen](https://x.com/bijanbowen))

**建立一個專注的行動實用程式原型，將傳統音訊工具與人工智慧輔助的替代調音相結合**

創建者使用 Gemini 3.6 Flash 構建了一個 Android 吉他調音器應用程序，並提供 AI 驅動的替代調音支援

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4)

類型: Demo | 日期: 2026-07-21

---

<a id="case-10"></a>
### 案例 10: [交通燈模擬](https://x.com/diegocabezas01/status/2079588206513631483) (作者 [@diegocabezas01](https://x.com/diegocabezas01))

**要求模型提供可執行的視覺化，以檢查產生的程式碼是否捕捉定時和隨機流量行為**

公共提示要求使用 Python 程式碼來視覺化單向街道交通號誌燈，其中汽車以隨機速率到達，該貼文包含了最終的演示

**提示詞:**

```text
write a python code that visualizes how a traffic light works in a one way street with cars entering at random rate.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4)

類型: Demo | 日期: 2026-07-21

---

<a id="case-11"></a>
### 案例 11: [鍵盤鋼琴應用程式](https://x.com/Majin_AppSheet/status/2079734240540041230) (作者 [@Majin_AppSheet](https://x.com/Majin_AppSheet))

**將簡單的互動概念轉變為可玩的鍵盤控制的 Web 應用程式**

創作者使用 Gemini 3.6 Flash 建立了一個可以透過電腦鍵盤彈奏的鋼琴應用程序，並將其設計為兒童可以探索的應用程式

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4)

類型: Demo | 日期: 2026-07-22

---

<a id="case-12"></a>
### 案例 12: [桌上機器人語音助手](https://x.com/AILogDev/status/2079716688745132044) (作者 [@AILogDev](https://x.com/AILogDev))

**將 Flash 和 Flash-Lite 整合到語音應用程式中並比較第一個回應行為**

創作者將 Gemini 3.6 Flash 和 Gemini 3.5 Flash-Lite 添加到桌面機器人的語音對話應用程式中，並指出最初的回應感覺稍慢但可用

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4)

類型: Integration | 日期: 2026-07-21

---


<a id="web-games-3d"></a>
## 🎮 網頁、遊戲和 3D

<a id="case-13"></a>
### 案例 13: [金門大橋 HTML 故障](https://x.com/LuminaXspace/status/2079597030922465407) (作者 [@LuminaXspace](https://x.com/LuminaXspace))

**在信任產生的 3D Web 體驗之前，使用嚴格的文件傳遞任務來測試指令遵循**

測試人員需要三個提示，看到模型嘗試應用內模擬和網絡圖像響應而不是請求的 HTML 文件，並判斷最終的 3D 橋接器輸出明顯弱於 Gemini 3.1 Pro

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4)

類型: Limit | 日期: 2026-07-21

---

<a id="case-14"></a>
### 案例 14: [公共提示視覺測試](https://x.com/Motion_Viz/status/2079592671530938537) (作者 [@Motion_Viz](https://x.com/Motion_Viz))

**當您需要創建者的完整提示而不是從輸出重建它時，請打開來源執行緒**

MotionViz 發布了 Gemini 3.6 Flash 媒體視覺測試，並表示完整的提示在來源執行緒中可用；此儲存庫不會重建來源套件中不存在的提示文字

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4)

類型: Demo | 日期: 2026-07-21

---

<a id="case-15"></a>
### 案例 15: [單提示畫布遊戲](https://x.com/ozansihay/status/2079599565565468672) (作者 [@ozansihay](https://x.com/ozansihay))

**使用 Canvas 中的一個提示來測試模型將緊湊的遊戲概念轉變為互動式結果的速度**

創作者在早期訪問中測試了 Gemini 3.6 Flash，並使用單一 Canvas 提示來製作可玩的遊戲演示

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4)

類型: Demo | 日期: 2026-07-21

---

<a id="case-16"></a>
### 案例 16: [登陸頁版本比較](https://x.com/nemumusitocha/status/2079596099854307650) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**保持模型各世代之間的提示固定，以隔離登陸頁面執行和視覺判斷中的變化**

創作者將 Gemini 3.6 Flash 新增至相同提示的登陸頁面檔案中，並判斷新結果比 Gemini 3 和 3.5 輸出更差

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg" alt="Case 16 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg" alt="Case 16 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg" alt="Case 16 source image 3" height="360"></a>

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-17"></a>
### 案例 17: [地鐵跑酷 3D 原型](https://x.com/itsPaulAi/status/2079597536155668890) (作者 [@itsPaulAi](https://x.com/itsPaulAi))

**為編碼實驗提供擴展思維，並檢查互動品質和視覺保真度**

創作者使用 Gemini 3.6 Flash 構建了一個簡單的 3D 地鐵跑酷風格的複製品，並建議對編碼任務進行擴展思維

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4)

類型: Demo | 日期: 2026-07-21

---

<a id="case-18"></a>
### 案例 18: [一頁網站比較](https://x.com/SaiNemani1/status/2079606113306325496) (作者 [@SaiNemani1](https://x.com/SaiNemani1))

**保持網站提示和推理水準不變，然後比較令牌成本、速度和設計偏好**

在同一個一頁的網站提示中，創建者報告了 Gemini 3.6 Flash 的token約為 6,100 個，而 3.5 Flash 的token約為 9,300 個，而個人更喜歡舊型號的外觀

**提示詞:**

```text
create a modern website! Should look amazing! One-code page
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-19"></a>
### 案例 19: [狂野西部遊戲失敗](https://x.com/Mr_Salio/status/2079635008424169901) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**將失敗的遊戲生成輸出視為決定何時切換模型或修改任務的證據**

測試者使用 Wild West 遊戲產生提示，根據觀察結果判斷 Gemini 3.6 Flash 明顯落後於 GPT-5.6、Kimi K3 和 Fable 5

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4)

類型: Limit | 日期: 2026-07-21

---

<a id="case-20"></a>
### 案例 20: [Antigravity遊戲素材失效](https://x.com/Conor_D_Dart/status/2079592731211399460) (作者 [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**在接受人工智慧生成的遊戲原型之前，請檢查視覺材料和實際互動行為**

在第二次Antigravity遊戲測試中，創作者發現較弱的木質紋理和看起來相似但仍然不起作用的大理石元素

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4)

類型: Limit | 日期: 2026-07-21

---

<a id="case-21"></a>
### 案例 21: [勞斯萊斯 SVG 比較](https://x.com/ggg78g89/status/2079610251444437335) (作者 [@ggg78g89](https://x.com/ggg78g89))

**使用固定的 SVG 主題來比較兩代 Flash 如何處理形狀、細節和構圖**

該貼文將 Gemini 3.6 Flash 和 3.5 Flash 輸出並排放置，以執行相同的勞斯萊斯 SVG 任務

**提示詞:**

```text
SVG of a Rolls Royce
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png" alt="Case 21 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png" alt="Case 21 source image 2" height="360"></a>

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-22"></a>
### 案例 22: [現實水族館測試](https://x.com/intheworldofai/status/2079681107516170431) (作者 [@intheworldofai](https://x.com/intheworldofai))

**使用有界 3D 場景來比較模型版本之間的真實感和實現品質**

創作者要求 Gemini 3.6 Flash 建造一個逼真的水族館，並認為它只比 3.5 Flash 好一點

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4)

類型: Evaluation | 日期: 2026-07-21

---


<a id="evaluations"></a>
## 🧪 評估與比較

<a id="case-23"></a>
### 案例 23: [Max Reasoning 中的 Gemini 與 Grok](https://x.com/notjazii/status/2079609162431181193) (作者 [@notjazii](https://x.com/notjazii))

**使用相同的提示和最大推理設定來比較速度、成本和輸出，而不是依賴模型聲譽**

創作者在相同的提示和最大推理設定下運行 Gemini 3.6 Flash 和 Grok 4.5，觀察到兩者都很快，而 Grok 稍快且更便宜

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-24"></a>
### 案例 24: [Gemini與Sonnet在最大設置](https://x.com/notjazii/status/2079617706693902416) (作者 [@notjazii](https://x.com/notjazii))

**比較相同提示及其最強設定的模型，然後檢查實際產生的工件**

創建者在最大設定下使用相同的提示測試了 Gemini 3.6 Flash 和 Sonnet 5，並在所示任務中首選 Gemini 輸出

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-25"></a>
### 案例 25: [視覺理解測試](https://x.com/HarshithLucky3/status/2079607042403381313) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**在採用視覺工作流程模型之前，使用具體的影像任務來檢查回應品質和互動風格**

創作者展示了 Gemini 3.6 Flash 通過的視力測試，並強調了回應個性作為觀察體驗的一部分

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg" alt="Case 25 source image 1" height="360"></a>

類型: Demo | 日期: 2026-07-21

---

<a id="case-26"></a>
### 案例 26: [火箭聯盟遊戲基準](https://x.com/LLMJunky/status/2079712480683790743) (作者 [@LLMJunky](https://x.com/LLMJunky))

**運行重複的遊戲產生基準並記錄建立時間和一致的主觀排名**

創作者在火箭聯盟式的任務中測試了 Gemini 3.6 Flash，在個人排行榜上排名第三，並報告在不到兩分鐘的時間內完成了任務

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4)

類型: Benchmark | 日期: 2026-07-21

---

<a id="case-27"></a>
### 案例 27: [EyeBench 視覺比較](https://x.com/adonis_singh/status/2079631807817933222) (作者 [@adonis_singh](https://x.com/adonis_singh))

**使用穩定的視覺基準將增量效率增益與絕對品質分開**

在 EyeBench 上，創作者認為 Gemini 3.6 Flash 略好於 3.5 Flash，但仍差於 Gemini 3.1 Pro Preview，同時注意到token效率有所提高

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg" alt="Case 27 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-07-21

---

<a id="case-28"></a>
### 案例 28: [剪紙動畫對比](https://x.com/OriSilver/status/2079603778441957776) (作者 [@OriSilver](https://x.com/OriSilver))

**在評估創意生成時，分別比較反應速度和最終動畫**

作者在剪紙動畫任務中將 Gemini 3.6 Flash 與《神鬼寓言 5》進行了比較，稱讚 Gemini 近乎即時的回應，但對結果表示保留

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4)

類型: Evaluation | 日期: 2026-07-21

---

<a id="case-29"></a>
### 案例 29: [AI Arena 產生基準](https://x.com/OmedVibeCodes/status/2079663080049660220) (作者 [@OmedVibeCodes](https://x.com/OmedVibeCodes))

**使用相同的 arena 任務來比較多個編碼模型的建造時間、價格和工件品質**

創作者在一項 AI Arena 任務中測試了 Grok 4.5、Gemini 3.6 Flash 和 GPT-5.6 Luna，並判斷 Gemini 在該運行中的結果最弱

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4)

類型: Benchmark | 日期: 2026-07-21

---

<a id="case-30"></a>
### 案例 30: [跨模型遊戲建構成本](https://x.com/naymur_dev/status/2079710299918401907) (作者 [@naymur_dev](https://x.com/naymur_dev))

**在選擇遊戲原型設計模型時，一起追蹤迭代次數、開發人員經驗、功能和成本**

使用相同的設計工作流程，創建者報告需要六到七次迭代來修復 Gemini 產生的跳躍和墜落錯誤，並列出了 0.15 美元的運行成本以及比較分數

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4)

類型: Benchmark | 日期: 2026-07-21

---


<a id="safety-limits"></a>
## 🛡️ 安全與限制

<a id="case-31"></a>
### 案例 31: [網路安全拒絕基準](https://x.com/pilvar222/status/2079602157779566836) (作者 [@pilvar222](https://x.com/pilvar222))

**在安全工具評估中包含拒絕行為，因為防禦性程式碼審查可能會被攻擊性請求阻止**

網路安全基準測試被拒絕，導致評估人員報告稱，經過測試的策略阻止了防禦性程式碼的漏洞查找行為以及惡意使用

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg" alt="Case 31 source image 1" height="360"></a>

類型: Limit | 日期: 2026-07-21

---

<a id="case-32"></a>
### 案例 32: [知識新鮮度失敗](https://x.com/ggg78g89/status/2079587359851737339) (作者 [@ggg78g89](https://x.com/ggg78g89))

**透過檢索來驗證當前事實，而不是相信聲稱的知識截止點**

測試人員詢問當前的旗艦型號並收到較舊的名稱，然後報告說該型號承認僅到 2025 年初的知識，儘管聲稱截止日期為 2026 年 3 月

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg" alt="Case 32 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg" alt="Case 32 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg" alt="Case 32 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png" alt="Case 32 source image 4" height="360"></a>

類型: Limit | 日期: 2026-07-21

---

<a id="case-33"></a>
### 案例 33: [越獄紅隊測試](https://x.com/Ubannoblesse/status/2079711268899086484) (作者 [@Ubannoblesse](https://x.com/Ubannoblesse))

**將越獄聲明視為需要受控複製和安全審查的紅隊訊號，而不是可重複使用的指示**

該貼文聲稱 Gemini 應用程式和 API 已越獄，並列出了經過測試的有害內容類別；該儲存庫記錄安全訊號，而不複製漏洞利用指令

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg" alt="Case 33 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg" alt="Case 33 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg" alt="Case 33 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg" alt="Case 33 source image 4" height="360"></a>

類型: Limit | 日期: 2026-07-21

---

<a id="related-repositories"></a>
## 相關儲存庫

- [EvoLink-AI on GitHub](https://github.com/Evolink-AI) — 來自 EvoLink 的更多模型指南和 API 範例
- [Gemini 3.6 Flash official launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
- [Gemini 3.6 Flash model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)
- 在本出版品中，沒有獨立驗證專用的可安裝 Gemini 3.6 Flash 技能

<a id="quick-start"></a>
## ⚡ 快速入門

透過下方經過驗證的公開入口開始使用 model ID `gemini-3.6-flash`

1. [開啟Gemini 3.6 Flash模型頁面](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link)
2. [建立或管理 EvoLink API 金鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key)
3. [遵循 Gemini Native API 快速入門](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=first_run)

> [!IMPORTANT]
> 公開路由與 model ID 已有文件依據，但在真實測試完成或獲得明確豁免前，本倉庫不會聲稱已執行消耗額度的 first call

<a id="acknowledge"></a>
## 🙏 致謝

該合集的存在是因為創作者和實踐者公開分享了他們的 Gemini 3.6 Flash 作品

**感謝這裡代表的來源創作者:**

[@JeffDean](https://x.com/JeffDean), [@antigravity](https://x.com/antigravity), [@stevibe](https://x.com/stevibe), [@browser_use](https://x.com/browser_use), [@__apf__](https://x.com/__apf__), [@databricks](https://x.com/databricks), [@jetbrains](https://x.com/jetbrains), [@CodeByPoonam](https://x.com/CodeByPoonam), [@bijanbowen](https://x.com/bijanbowen), [@diegocabezas01](https://x.com/diegocabezas01), [@Majin_AppSheet](https://x.com/Majin_AppSheet), [@AILogDev](https://x.com/AILogDev), [@LuminaXspace](https://x.com/LuminaXspace), [@Motion_Viz](https://x.com/Motion_Viz), [@ozansihay](https://x.com/ozansihay), [@nemumusitocha](https://x.com/nemumusitocha), [@itsPaulAi](https://x.com/itsPaulAi), [@SaiNemani1](https://x.com/SaiNemani1), [@Mr_Salio](https://x.com/Mr_Salio), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@ggg78g89](https://x.com/ggg78g89), [@intheworldofai](https://x.com/intheworldofai), [@notjazii](https://x.com/notjazii), [@HarshithLucky3](https://x.com/HarshithLucky3), [@LLMJunky](https://x.com/LLMJunky), [@adonis_singh](https://x.com/adonis_singh), [@OriSilver](https://x.com/OriSilver), [@OmedVibeCodes](https://x.com/OmedVibeCodes), [@naymur_dev](https://x.com/naymur_dev), [@pilvar222](https://x.com/pilvar222), [@Ubannoblesse](https://x.com/Ubannoblesse)

*我們無法保證每則貼文都指向最早的原創者，如歸屬、翻譯或措辭需要修正，請提交附公開來源的 correction issue*

若要提出另一個由來源支援的案例，請開啟問題或拉取請求並遵循貢獻清單
