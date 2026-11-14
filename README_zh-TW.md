<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API (English)](https://img.shields.io/badge/Gemini_Native_API-English-f22f3d)](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=docs_link)

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

# Gemini 4 Hydrogen 精選指南與應用程式案例

## 🍌 簡介

通過有來源依據的應用程式、程式設計工作流和實用對比，探索 Gemini 4 Hydrogen

**40 個精選示例展示人們構建了甚麼、如何操作，以及結果有哪些不足**

每個案例均連結至來源並注明作者；演示、供應商示例和創作者對比均在說明中標注；未公開的提示詞不會被補寫

## 📊 概覽

- 從最多收集 500 條 X 貼文的資料中審閱了 75 條演示貼文，精選 40 個案例，資料採集於 2026 年 11 月 13 日
- 五個類別涵蓋代理程式、學習與應用程式、電子錶格與搜索、互動式 3D，以及對比與局限
- 完整保留全部 41 項選定來源視覺素材：38 段帶封面的可播放影片和 3 張圖片
- Gemini 4 Hydrogen 於 2026 年 11 月 12 日發佈；可在 EvoLink 探索該模型及當前訪問方式

> [!NOTE]
> 除非另有說明，模型歸屬、費用、耗時和結果均為來源方的說法；影片審閱採用抽樣幀，未進行完整功能測試；程式碼應用程式的執行錄像不能證明模型具備原生影片生成能力；不同執行框架、推理級別或迭代次數會使對比缺乏受控條件

**官方參考資料: [Google 發佈公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**從這裡開始: [在 EvoLink 探索 Hydrogen](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [獲取 API 密鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ 快速入門

先從 EvoLink 開始，需要將 Hydrogen 集成到應用程式時，再使用 Gemini 原生 API

1. [在瀏覽器中查看 Gemini 4 Hydrogen](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [建立或管理 EvoLink API 金鑰](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

最簡原生 API 請求

```bash
export EVOLINK_API_KEY="your_api_key_here"

curl --fail-with-body --silent --show-error \
  --request POST \
  --url "https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"contents":[{"role":"user","parts":[{"text":"Reply exactly: OK"}]}],"generationConfig":{"candidateCount":1,"maxOutputTokens":2048,"temperature":0,"thinkingConfig":{"thinkingLevel":"low"}}}'
```

`POST https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent`

[閱讀 Gemini 原生 API 快速入門（英文）](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> 從回應的 candidates[].content.parts[].text 欄位讀取生成的文本

> [!IMPORTANT]
> 請將 API 密鑰保存在環境變數中，切勿提交到儲存庫；流式輸出、推理及其他請求選項請參閱 API 文件

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [⚡ 代理程式與程式設計工作流](#agents) | 5 |
| [💻 應用程式與學習](#apps-learning) | 5 |
| [📊 電子錶格與搜索](#data-search) | 4 |
| [🎮 互動式 3D 與使用者介面](#interactive-3d) | 9 |
| [🧪 對比與局限](#comparisons-limits) | 17 |
| [相關儲存庫](#related-repositories) |  |
| [快速入門](#quick-start) |  |
| [致謝](#acknowledge) |  |

| 案例 | 類別 | 可以嘗試甚麼 | 類型 |
|---|---|---|---|
| [在 Antigravity 中維護程式碼庫](#case-1) | 代理程式與程式設計工作流 | 使用範圍明確的維護任務，同時評估編輯、工具使用和驗證能力 | Demo |
| [並行構建十六個 Canvas 應用程式](#case-2) | 代理程式與程式設計工作流 | 將構建工作拆分為獨立模塊，明確規劃、實現和品質檢查的角色 | Demo |
| [混合模型代理程式群構建緋紅飛蛾](#case-3) | 代理程式與程式設計工作流 | 為互動式創意程式設計項目分配獨立的編排與實現角色 | Demo |
| [3D Medic 檢查與修復](#case-4) | 代理程式與程式設計工作流 | 探索能夠檢查 3D 檔案、發現錯誤並在導出前提出修復方案的代理程式 | Demo |
| [在 Devin 中構建帆船場景](#case-5) | 代理程式與程式設計工作流 | 在你實際計劃使用的程式設計代理程式環境中評估模型 | Demo |
| [Lingo City 語言練習](#case-6) | 應用程式與學習 | 結合學習字卡與互動式街景，進行情境化語言練習 | Demo |
| [《羅密歐與朱麗葉》3D 紙劇場](#case-7) | 應用程式與學習 | 將具體課程轉化為具有明確學習目標的互動場景 | Demo |
| [從設計圖到閱讀網站](#case-8) | 應用程式與學習 | 使用參考設計評估視覺理解和可執行前端的實現能力 | Demo |
| [用二十個模塊構建錦鯉庭院](#case-9) | 應用程式與學習 | 用小模塊構建較大場景，而非期待一次提示就得到完整結果 | Demo |
| [質子聚變學習游戲](#case-10) | 應用程式與學習 | 為科學過程製作互動式講解原型，然後核查其中的科學內容 | Demo |
| [Google Sheets 中的動態風景](#case-11) | 電子錶格與搜索 | 通過非常規的電子錶格動畫，檢查生成程式碼和單元格級更新 | Demo |
| [Folio 互動式資料網站](#case-12) | 電子錶格與搜索 | 在小型網站原型中結合落地頁佈局與互動式資料視覺化 | Demo |
| [多部分搜索問題的視覺化回答](#case-13) | 電子錶格與搜索 | 測試細緻且具有多項約束的搜索請求時，對比回答佈局與引用連結 | Demo |
| [Sheets 中的互動式財務預測](#case-14) | 電子錶格與搜索 | 構建假設清晰可見的財務模型原型，並檢查生成的公式與圖表 | Demo |
| [互動式餐廳](#case-15) | 互動式 3D 與使用者介面 | 檢查物體互動、照明和狀態變化，而不是僅憑靜態圖片評判場景 | Demo |
| [帶微縮世界的音量滑塊](#case-16) | 互動式 3D 與使用者介面 | 通過一個熟悉的控件，同時測試互動設計與動畫場景細節 | Demo |
| [Three.js 日式住宅](#case-17) | 互動式 3D 與使用者介面 | 評估細緻的 3D 漫游時，將程式碼生成時間與渲染時間分開 | Demo |
| [騎自行車的 3D 鵜鶘](#case-18) | 互動式 3D 與使用者介面 | 使用運動角色檢查協調性、動作和場景一致性 | Demo |
| [規劃優先的行星模擬器](#case-19) | 互動式 3D 與使用者介面 | 讓程式設計模型編輯複雜場景之前，先給出具體計劃 | Demo |
| [用 Antigravity Swarm 構建港灣島嶼](#case-20) | 互動式 3D 與使用者介面 | 通過可導航的小型環境，檢查多代理程式構建場景的行為 | Demo |
| [埃菲爾鐵塔浮空島](#case-21) | 互動式 3D 與使用者介面 | 通過緊湊的地標場景評估構圖、鏡頭運動和模型生成的程式碼 | Demo |
| [可飛行的未來城市](#case-22) | 互動式 3D 與使用者介面 | 測試對程序化世界的後續編輯，不要假定首次輸出就是最終結果 | Demo |
| [從日出到夜晚的水上飛機](#case-23) | 互動式 3D 與使用者介面 | 檢查互動式 3D 場景中的環境控制與光照過渡 | Demo |
| [霓虹火柴人動畫：Hydrogen 與 Opus](#case-24) | 對比與局限 | 結合來源所述時間與費用對比最終動畫，不要假定執行框架相同 | Evaluation |
| [機器人任務與自行識別失誤](#case-25) | 對比與局限 | 在機器人評估中納入任務完成情況以及識別細小失誤的能力 | Evaluation |
| [自然語言驅動的實驗室工作單元](#case-26) | 對比與局限 | 將工具執行和失敗處理的評估與基準榜單分數分開 | Evaluation |
| [冰山與拖船：Hydrogen 與 Carbon](#case-27) | 對比與局限 | 對比耗時較長的 3D 構建時，記錄推理級別與執行框架限制 | Evaluation |
| [果凍錦鯉池：Hydrogen 與 Sonnet](#case-28) | 對比與局限 | 在根據基準排名選擇模型前，先檢查具體場景 | Evaluation |
| [使用相同提示詞的創意程式設計合集](#case-29) | 對比與局限 | 通過多樣化的視覺任務，避免從單個漂亮輸出過度概括 | Evaluation |
| [Megamind 體素：成本與品質反例](#case-30) | 對比與局限 | 評估模型是否始終更便宜或視覺效果更強時，保留失敗案例 | Limit |
| [穿越四季的雜耍獅子](#case-31) | 對比與局限 | 檢查要求的動作，而不只是周圍介面的視覺精致程度 | Limit |
| [三模型火柴人格鬥：更慢且更貴的結果](#case-32) | 對比與局限 | 對比模型宣傳的效率與實際任務報告時，保留反例 | Limit |
| [農場自行車場景：Hydrogen 與 Flash](#case-33) | 對比與局限 | 結合創作者報告的完成時間，對比動作與場景品質 | Evaluation |
| [女孩與貓的雙人自行車](#case-34) | 對比與局限 | 對比提示詞遵循程度與附加細節，同時明確不同程式設計執行框架的差異 | Evaluation |
| [四個模型構建 Three.js 馬里奧游戲](#case-35) | 對比與局限 | 解讀相同提示詞的游戲對比前，記錄不一致的推理設置 | Evaluation |
| [三個 Gemini 模型繪制游戲手柄](#case-36) | 對比與局限 | 尋找具體任務中的退步與改進，不要假定模型家族存在固定層級 | Evaluation |
| [應用程式與 Studio 的視覺回答存在差異](#case-37) | 對比與局限 | 依賴視覺結果之前，在計劃使用的產品介面中測試相同圖片 | Limit |
| [火箭發射場景：Hydrogen 與 Flash](#case-38) | 對比與局限 | 既對比實際發射動畫，也對比來源報告的構建耗時 | Evaluation |
| [四項 SVG 動畫任務](#case-39) | 對比與局限 | 通過多種互動與動畫主題，檢查跨任務的一致性 | Evaluation |
| [三個模型製作草原馬匹動畫](#case-40) | 對比與局限 | 直接檢查動作與視覺細節，再判斷寬泛的費用或品質說法是否可信 | Evaluation |

<a id="agents"></a>
## ⚡ 代理程式與程式設計工作流

<a id="case-1"></a>
### 案例 1: [在 Antigravity 中維護程式碼庫](https://x.com/antigravity/status/2120944334023389476) (作者 [@antigravity](https://x.com/antigravity))

**使用範圍明確的維護任務，同時評估編輯、工具使用和驗證能力**

Antigravity 的發佈演示展示 Hydrogen 維護程式碼庫；這是平台製作的示例，並非獨立復現的工程基準測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-2"></a>
### 案例 2: [並行構建十六個 Canvas 應用程式](https://x.com/shengzheyao/status/2120944141559550409) (作者 [@shengzheyao](https://x.com/shengzheyao))

**將構建工作拆分為獨立模塊，明確規劃、實現和品質檢查的角色**

Google DeepMind 的一位 Antigravity CLI 創作者介紹了由 Carbon 協調、驗證和集成，由 Hydrogen 構建 16 個零依賴 canvas 小應用程式的流程；這是混合模型工作流，不能將結果僅歸功於 Hydrogen

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-3"></a>
### 案例 3: [混合模型代理程式群構建緋紅飛蛾](https://x.com/thtbee_/status/2120958666480513310) (作者 [@thtbee_](https://x.com/thtbee_))

**為互動式創意程式設計項目分配獨立的編排與實現角色**

創作者稱 Carbon 編排 Antigravity 代理程式群，Hydrogen 工作代理程式構建緋紅飛蛾作品；所述 45 分鐘包含整個多模型工作流，未經獨立計時

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-4"></a>
### 案例 4: [3D Medic 檢查與修復](https://x.com/GoogleAI/status/2120940683233984862) (作者 [@GoogleAI](https://x.com/GoogleAI))

**探索能夠檢查 3D 檔案、發現錯誤並在導出前提出修復方案的代理程式**

Google AI 的 3D Medic 演示使用在 AI Studio 中構建的 Managed Agent 應用程式；它展示的是檔案修復流程，不能證明任意 3D 資產都能被正確修復

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-5"></a>
### 案例 5: [在 Devin 中構建帆船場景](https://x.com/Da7_Tech/status/2120967690722677144) (作者 [@Da7_Tech](https://x.com/Da7_Tech))

**在你實際計劃使用的程式設計代理程式環境中評估模型**

來源展示了一個帆船場景，並稱其由 Devin 中執行的 Hydrogen 構建；簡短貼文沒有公開完整提示詞、迭代歷史或可復現的配置

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

類型: Demo | 日期: 2026-11-12

---


<a id="apps-learning"></a>
## 💻 應用程式與學習

<a id="case-6"></a>
### 案例 6: [Lingo City 語言練習](https://x.com/tulseedoshi/status/2121095754844713427) (作者 [@tulseedoshi](https://x.com/tulseedoshi))

**結合學習字卡與互動式街景，進行情境化語言練習**

Tulsee Doshi 分享了 Google 的示例：流式生成定制 2D 和 3D 學習字卡，並讓學習者在虛擬城市中練習與店主對話；這是供應商演示，並非獨立的學習效果研究

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-7"></a>
### 案例 7: [《羅密歐與朱麗葉》3D 紙劇場](https://x.com/techartist_/status/2120957446202253803) (作者 [@techartist_](https://x.com/techartist_))

**將具體課程轉化為具有明確學習目標的互動場景**

創作者為 GCSE 英語文學課程構建了關於《羅密歐與朱麗葉》陽台場景的 3D 紙劇場課程；來源展示了介面，但未衡量學習效果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-8"></a>
### 案例 8: [從設計圖到閱讀網站](https://x.com/thebuggeddev/status/2120952661046689992) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**使用參考設計評估視覺理解和可執行前端的實現能力**

創作者稱 Hydrogen 用 5 分 27 秒將設計圖轉化為可執行的閱讀管理網站；耗時與完整性均為來源方說法，本合集未進行獨立功能測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-9"></a>
### 案例 9: [用二十個模塊構建錦鯉庭院](https://x.com/IamEmily2050/status/2120951069874532806) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**用小模塊構建較大場景，而非期待一次提示就得到完整結果**

創作者稱在 Gemini 應用程式中用 20 條提示詞構建了 20 個模塊，每個模塊耗時 90–270 秒；作者披露獲得了提前訪問權限，這一示例明確採用迭代流程，而非一次生成

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-10"></a>
### 案例 10: [質子聚變學習游戲](https://x.com/SidraMiconi/status/2120948703095820743) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**為科學過程製作互動式講解原型，然後核查其中的科學內容**

創作者的游戲演示年輕恆星內部的質子–質子鏈反應；所述單條提示詞、78 秒執行時間以及約 $0.19 費用均為來源方說法，未經獨立復現

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

類型: Demo | 日期: 2026-11-12

---


<a id="data-search"></a>
## 📊 電子錶格與搜索

<a id="case-11"></a>
### 案例 11: [Google Sheets 中的動態風景](https://x.com/Google/status/2121004369617485896) (作者 [@Google](https://x.com/Google))

**通過非常規的電子錶格動畫，檢查生成程式碼和單元格級更新**

Google 展示了用 Antigravity 編寫程式碼，將海岸列車、雲朵與秋葉繪制在表格單元格中的效果；這是官方創意演示，並非電子錶格性能基準測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-12"></a>
### 案例 12: [Folio 互動式資料網站](https://x.com/vamsibatchuk/status/2120996342923436188) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**在小型網站原型中結合落地頁佈局與互動式資料視覺化**

一位 Google DeepMind 員工展示了使用 Google AI Studio 構建的 Folio 風格網站和互動動畫；貼文未提供完整生成提示詞或獨立功能測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-13"></a>
### 案例 13: [多部分搜索問題的視覺化回答](https://x.com/Google/status/2120960715011883148) (作者 [@Google](https://x.com/Google))

**測試細緻且具有多項約束的搜索請求時，對比回答佈局與引用連結**

Google 的搜索示例結合了意圖理解、視覺佈局、對比表格和查詢擴展；這些屬於供應商描述的產品行為，演示並未證明對發佈者排名或流量的影響

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-14"></a>
### 案例 14: [Sheets 中的互動式財務預測](https://x.com/ChanduThota/status/2120942270627414079) (作者 [@ChanduThota](https://x.com/ChanduThota))

**構建假設清晰可見的財務模型原型，並檢查生成的公式與圖表**

Chandu Thota 展示了 Google Sheets 預測演示；來源所稱 canvas 生成速度提升超過 30% 屬於供應商說法，並非本儲存庫進行的受控計時測量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

類型: Demo | 日期: 2026-11-12

---


<a id="interactive-3d"></a>
## 🎮 互動式 3D 與使用者介面

<a id="case-15"></a>
### 案例 15: [互動式餐廳](https://x.com/notjazii/status/2120979811569222137) (作者 [@notjazii](https://x.com/notjazii))

**檢查物體互動、照明和狀態變化，而不是僅憑靜態圖片評判場景**

創作者展示了一間餐廳，其中的燈光、台燈、冰箱及內部物品均可互動；所述 30 分鐘構建時間未經獨立驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-16"></a>
### 案例 16: [帶微縮世界的音量滑塊](https://x.com/vib3coded/status/2120973294090555890) (作者 [@vib3coded](https://x.com/vib3coded))

**通過一個熟悉的控件，同時測試互動設計與動畫場景細節**

來源展示了一個能讓微型日式世界動起來的音量滑塊；創作者稱費用為 $0.19，但未提供賬單或完整生成流程

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-17"></a>
### 案例 17: [Three.js 日式住宅](https://x.com/SPAC89/status/2120972954146140409) (作者 [@SPAC89](https://x.com/SPAC89))

**評估細緻的 3D 漫游時，將程式碼生成時間與渲染時間分開**

創作者稱該住宅和庭院由 Hydrogen 使用 Three.js 構建，未使用代理程式；貼文關於訂閱用量和不到兩小時的說法僅適用於作者的配置，並非通用的價格或延遲保證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-18"></a>
### 案例 18: [騎自行車的 3D 鵜鶘](https://x.com/nehstrr3/status/2120953932692537722) (作者 [@nehstrr3](https://x.com/nehstrr3))

**使用運動角色檢查協調性、動作和場景一致性**

創作者展示了一隻騎自行車的 3D 動畫鵜鶘，並標注模型為 XHigh 級別的 Hydrogen；貼文展示的是輸出成果，並未提供完整可復現提示詞或物理驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-19"></a>
### 案例 19: [規劃優先的行星模擬器](https://x.com/The_Alex/status/2120950301318582643) (作者 [@The_Alex](https://x.com/The_Alex))

**讓程式設計模型編輯複雜場景之前，先給出具體計劃**

獲得提前訪問權限的創作者展示了行星模擬器，並稱提供更詳細計劃後編輯效果有所改善；來源注明創意來自 ForwardEditor，並描述了迭代工作流

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-20"></a>
### 案例 20: [用 Antigravity Swarm 構建港灣島嶼](https://x.com/ai_for_success/status/2120942147780464660) (作者 [@ai_for_success](https://x.com/ai_for_success))

**通過可導航的小型環境，檢查多代理程式構建場景的行為**

創作者披露獲得了提前訪問權限，並展示了在 Antigravity 的 Swarm 功能中使用 Hydrogen 構建的港灣島嶼；公開貼文沒有說明完整編排過程或提示詞歷史

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-21"></a>
### 案例 21: [埃菲爾鐵塔浮空島](https://x.com/RezAIT00/status/2120940988780736973) (作者 [@RezAIT00](https://x.com/RezAIT00))

**通過緊湊的地標場景評估構圖、鏡頭運動和模型生成的程式碼**

來源展示了埃菲爾鐵塔微縮島嶼，並稱其由 Hydrogen XHigh 構建；構建加錄制耗時六分鐘是作者自述，並非獨立計時測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-22"></a>
### 案例 22: [可飛行的未來城市](https://x.com/kimmonismus/status/2120940617169826037) (作者 [@kimmonismus](https://x.com/kimmonismus))

**測試對程序化世界的後續編輯，不要假定首次輸出就是最終結果**

獲得提前訪問權限的創作者在 Antigravity 中使用 Hydrogen High，並稱經過一次後續提示，生成了包含程序化高樓、雨景和飛行交通的 Three.js 城市；錄像展示的是生成程式碼的執行效果，而非原生影片生成

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-23"></a>
### 案例 23: [從日出到夜晚的水上飛機](https://x.com/LuminaBench/status/2120939312564842663) (作者 [@LuminaBench](https://x.com/LuminaBench))

**檢查互動式 3D 場景中的環境控制與光照過渡**

LuminaBench 的原創演示展示了水上飛機與一天中時間的變化，之後被 Google 轉發；貼文早於記錄中的公開發佈界限；其訪問途徑和模型調用未經獨立驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

類型: Demo | 日期: 2026-11-12

---


<a id="comparisons-limits"></a>
## 🧪 對比與局限

<a id="case-24"></a>
### 案例 24: [霓虹火柴人動畫：Hydrogen 與 Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**結合來源所述時間與費用對比最終動畫，不要假定執行框架相同**

作者展示了 Hydrogen 和 Opus 5.5 的輸出，並報告費用分別為 $1.02 與 $7.43，耗時分別為 10 分 22 秒與 34 分鐘；本合集未核驗賬單、提示詞、迭代次數或執行設置的可比性

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-25"></a>
### 案例 25: [機器人任務與自行識別失誤](https://x.com/ArtificialAnlys/status/2120995180891508833) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**在機器人評估中納入任務完成情況以及識別細小失誤的能力**

Artificial Analysis 展示了倒液體和整理積木的任務，並稱 Hydrogen 注意到了少量灑漏和未關上的蓋子；影片及 AA-Robotics v0.1 排名來自評測方，本合集未獨立復現

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-26"></a>
### 案例 26: [自然語言驅動的實驗室工作單元](https://x.com/danielmckinn0n/status/2120990834246173125) (作者 [@danielmckinn0n](https://x.com/danielmckinn0n))

**將工具執行和失敗處理的評估與基準榜單分數分開**

來源展示了由自然語言請求驅動的實驗室工作單元，並報告四項實驗室相關基準的結果；所述 Hydrogen 的 RareBench 分數低於 Opus 5.5，另外三項更高；這是基準所有者的演示，並非醫學驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-27"></a>
### 案例 27: [冰山與拖船：Hydrogen 與 Carbon](https://x.com/EnvolDev/status/2120989670582677930) (作者 [@EnvolDev](https://x.com/EnvolDev))

**對比耗時較長的 3D 構建時，記錄推理級別與執行框架限制**

創作者稱兩個模型均通過 OpenRouter 以 High 級別執行，Hydrogen 費用 $4.27、耗時 1 小時 23 分 40 秒，Carbon 費用 $8.83、耗時 2 小時 39 分 10 秒；這些是來源自述的非受控結果，並非普適的價格或速度比例

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-28"></a>
### 案例 28: [果凍錦鯉池：Hydrogen 與 Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (作者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**在根據基準排名選擇模型前，先檢查具體場景**

作者對比了 Hydrogen 和 Sonnet 5.5 在 3D 錦鯉池任務上的表現；來源邀請觀眾評判輸出，但未確立匹配的設置或客觀品質評分

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-29"></a>
### 案例 29: [使用相同提示詞的創意程式設計合集](https://x.com/kickingkeys/status/2120985358317875222) (作者 [@kickingkeys](https://x.com/kickingkeys))

**通過多樣化的視覺任務，避免從單個漂亮輸出過度概括**

創作者稱給 Hydrogen、Carbon 和 Argon 使用了相同提示詞，並將對比放在回復中；主貼文素材展示低多邊形動物、霓虹街道和水彩風格容器；這不是完整的受控基準測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-30"></a>
### 案例 30: [Megamind 體素：成本與品質反例](https://x.com/thehypedotnews/status/2120980737012670720) (作者 [@thehypedotnews](https://x.com/thehypedotnews))

**評估模型是否始終更便宜或視覺效果更強時，保留失敗案例**

來源稱 Hydrogen 生成的 Titan 角色整體更不協調，費用卻為 $36.07，而 Sonnet 5.5 為 $8.64；貼文包含商業推廣，費用與品質判斷均為發佈者說法

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

類型: Limit | 日期: 2026-11-12

---

<a id="case-31"></a>
### 案例 31: [穿越四季的雜耍獅子](https://x.com/SahilPanhotra/status/2120978349967458704) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**檢查要求的動作，而不只是周圍介面的視覺精致程度**

作者稱 Carbon 處理了交叉的雜耍弧線，而 Hydrogen 讓球懸浮在空中，儘管後者的季節過渡與裁切更乾淨；這一同任務 SVG 對比揭示的是特定動作失敗，而非模型綜合排名

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

類型: Limit | 日期: 2026-11-12

---

<a id="case-32"></a>
### 案例 32: [三模型火柴人格鬥：更慢且更貴的結果](https://x.com/DanielZambrini/status/2120963180461769183) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**對比模型宣傳的效率與實際任務報告時，保留反例**

創作者對比 Hydrogen、Carbon 和 Argon，並稱本次測試中 Hydrogen 比 Carbon 耗時更長、費用更高；設置、賬單和迭代次數未經獨立驗證

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

類型: Limit | 日期: 2026-11-12

---

<a id="case-33"></a>
### 案例 33: [農場自行車場景：Hydrogen 與 Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**結合創作者報告的完成時間，對比動作與場景品質**

來源對比了 Hydrogen 與 Gemini 3.8 Flash 的農場自行車場景，稱耗時分別為 56 秒與超過六分鐘；這是單個創作者的測試，並非通用速度基準

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-34"></a>
### 案例 34: [女孩與貓的雙人自行車](https://x.com/marcthecreatorr/status/2120956699951628637) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**對比提示詞遵循程度與附加細節，同時明確不同程式設計執行框架的差異**

創作者使用所述相同 SVG 任務，但分別在 Claude Code 中執行 Opus 5.5、在 Cursor 中執行 Hydrogen；所述時間與費用差異很大，但不同執行框架及未披露的迭代使其不能成為僅針對模型的受控對比

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-35"></a>
### 案例 35: [四個模型構建 Three.js 馬里奧游戲](https://x.com/StatsWire/status/2120955723396071548) (作者 [@StatsWire](https://x.com/StatsWire))

**解讀相同提示詞的游戲對比前，記錄不一致的推理設置**

來源對比了 High 級別的 Gemini 3.8 Flash、Argon、Carbon 與 XHigh 級別的 Hydrogen，均使用純 Three.js，不使用外部 3D 模型或紋理；它展示了四個輸出，並非推理設置匹配的基準測試

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-36"></a>
### 案例 36: [三個 Gemini 模型繪制游戲手柄](https://x.com/notjazii/status/2120952314873987271) (作者 [@notjazii](https://x.com/notjazii))

**尋找具體任務中的退步與改進，不要假定模型家族存在固定層級**

創作者對比了 Carbon、Argon 和 Hydrogen 的手柄 SVG 輸出，並稱重新執行過測試；所述耗時和費用均為來源方說法，不能確立模型品質的普遍排序

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-37"></a>
### 案例 37: [應用程式與 Studio 的視覺回答存在差異](https://x.com/thegenioo/status/2120946497802174688) (作者 [@thegenioo](https://x.com/thegenioo))

**依賴視覺結果之前，在計劃使用的產品介面中測試相同圖片**

來源展示了據稱由 Gemini 應用程式和 AI Studio 中的 Hydrogen 給出的相互衝突的食物識別回答；該對比未獨立核驗路由、設置或完整對話上下文是否相同

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-01.jpg" alt="Case 37 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-02.jpg" alt="Case 37 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Limit | 日期: 2026-11-12

---

<a id="case-38"></a>
### 案例 38: [火箭發射場景：Hydrogen 與 Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**既對比實際發射動畫，也對比來源報告的構建耗時**

創作者展示了 Hydrogen 與 Gemini 3.8 Flash 的輸出，並稱耗時分別不到一分鐘與約三分鐘；這一視覺對比僅涉及一個任務，沒有獨立受控的執行配置

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-39"></a>
### 案例 39: [四項 SVG 動畫任務](https://x.com/Angaisb_/status/2120944947193127061) (作者 [@Angaisb_](https://x.com/Angaisb_))

**通過多種互動與動畫主題，檢查跨任務的一致性**

來源配對展示了 Hydrogen 與 Carbon 在傳遞、晝夜變化、開箱和變色龍任務中的輸出；簡短主貼文未披露完整提示詞、計時證據或客觀評分方法

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-40"></a>
### 案例 40: [三個模型製作草原馬匹動畫](https://x.com/AI_Screening/status/2120944276586823689) (作者 [@AI_Screening](https://x.com/AI_Screening))

**直接檢查動作與視覺細節，再判斷寬泛的費用或品質說法是否可信**

創作者展示了 Hydrogen、Carbon 和 Argon 的草原馬匹場景；關於更快速度、更低費用和高品質的說法仍是來源方評價，並非本合集復現的受控對比

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="related-repositories"></a>
## 相關儲存庫

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon 示例與對比

<a id="acknowledge"></a>
## 🙏 致謝

感謝公開分享 Hydrogen 作品的創作者、開發者和評測者

**來源創作者:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening)

*署名依據所引用的公開來源，未必能夠識別最早的創作者；如需更正或請求移除，請提交附有公開來源的 issue*

請按照貢獻檢查清單，通過 issue 或 pull request 推薦有來源依據的示例
