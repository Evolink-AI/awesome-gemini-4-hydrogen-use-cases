<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API via the Hydrogen model page](https://img.shields.io/badge/Gemini_Native_API-Model_Page-f22f3d)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

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

**225 個案例呈現 Hydrogen 的實際用法與結果的限制**

每個案例均連結至來源並注明作者；演示、供應商示例和創作者對比均在說明中標注；未公開的提示詞不會被補寫

## 📊 概覽

- 共 225 個案例. 11 月 17 日更新查核了 1,304 則 X 貼文，新增 185 個案例. 新增來源在蒐集時皆超過 30 個喜歡
- 五個類別涵蓋代理程式、學習與應用程式、電子錶格與搜索、互動式 3D，以及對比與局限
- 全庫保留 264 個原始視覺素材，包括 168 部附封面且可播放的影片和 96 張圖片
- Gemini 4 Hydrogen 於 2026 年 11 月 12 日發佈；可在 EvoLink 探索該模型及當前訪問方式

> [!NOTE]
> 除非另有說明，模型歸屬、費用、耗時和結果均為來源方的說法；影片審閱採用抽樣幀，未進行完整功能測試；程式碼應用程式的執行錄像不能證明模型具備原生影片生成能力；不同執行框架、推理級別或迭代次數會使對比缺乏受控條件

**官方參考資料: [Google 發佈公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**從這裡開始: [在 EvoLink 探索 Hydrogen](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [獲取 API 密鑰 (從模型詳情頁進入)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)**

<a id="quick-start"></a>
## ⚡ 快速入門

先從 EvoLink 開始，需要將 Hydrogen 集成到應用程式時，再使用 Gemini 原生 API

1. [在瀏覽器中查看 Gemini 4 Hydrogen](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [建立或管理 EvoLink API 金鑰 (從模型詳情頁進入)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)

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

[閱讀 Gemini 原生 API 快速入門（英文） (從模型詳情頁進入)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

> [!TIP]
> 從回應的 candidates[].content.parts[].text 欄位讀取生成的文本

> [!IMPORTANT]
> 請將 API 密鑰保存在環境變數中，切勿提交到儲存庫；流式輸出、推理及其他請求選項請參閱 API 文件

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [⚡ 代理程式與程式設計工作流](#agents) | 30 |
| [💻 應用程式與學習](#apps-learning) | 37 |
| [📊 電子錶格與搜索](#data-search) | 9 |
| [🎮 互動式 3D 與使用者介面](#interactive-3d) | 48 |
| [🧪 對比與局限](#comparisons-limits) | 101 |
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
| [把太空參考圖做成 HTML 場景](#case-41) | 互動式 3D 與使用者介面 | 用少量參考圖檢驗生成場景能否呈現可辨識的視覺風格. | Demo |
| [Gemini Canvas 中的F1 賽車原型](#case-42) | 互動式 3D 與使用者介面 | 給車輛檢視介面設定幾個鏡頭，從不同角度檢查生成模型. | Demo |
| [Hydrogen API 與 Carbon Antigravity 輸出](#case-43) | 對比與局限 | 用同一提示詞比較視覺效果時，記錄各自的執行環境. | Evaluation |
| [Hydrogen 與 Astra 的陰影細節對比](#case-44) | 對比與局限 | 比較兩次執行的費用和耗時，同時檢查渲染細節. | Evaluation |
| [程式化 3D 動效對比](#case-45) | 對比與局限 | 比較程式化動效的連貫性與構圖時，記錄生成耗時. | Evaluation |
| [歷時 89 分鐘的 PokéBench 視覺測試](#case-46) | 對比與局限 | 測試長時視覺代理時，同時記錄任務完成情況、回合數和 API 失敗次數. | Benchmark |
| [Hydrogen 與 DeepSeek 建構同一個 3D 場景](#case-47) | 對比與局限 | 對照視覺輸出並分別記錄耗時和 API 費用. | Evaluation |
| [用 SVG 繪製BMW側視圖](#case-48) | 互動式 3D 與使用者介面 | 用車輛 SVG 側視圖檢查比例、輪廓和細節. | Demo |
| [天文學家的浮空島](#case-49) | 互動式 3D 與使用者介面 | 給小場景設定明確主題，再檢查物件和光照能否強化主題. | Demo |
| [把參考圖做成可探索的 3D 地形](#case-50) | 互動式 3D 與使用者介面 | 檢查圖生場景能否同時還原視覺元素並支援移動. | Demo |
| [用 3D 積木建構微縮景觀](#case-51) | 互動式 3D 與使用者介面 | 讓模型建構積木微縮景觀，檢查各形體能否組成完整場景. | Demo |
| [可互動的櫻花樹](#case-52) | 互動式 3D 與使用者介面 | 用一件帶動效的物體和幾個控制元件探索微縮場景的即時變化. | Demo |
| [Agent Arena 的單任務耗時和成本](#case-53) | 對比與局限 | 檢視整體成功率時，也比較單任務延遲、費用和輸出 Token 數. | Benchmark |
| [視覺文件和終端基準測試](#case-54) | 對比與局限 | 分別檢視文件與終端測試結果，再決定推理預算. | Benchmark |
| [Vals 指數和 Tax Agent 成績](#case-55) | 對比與局限 | 結合整體評估和專業任務分數來判斷模型是否適用. | Benchmark |
| [CursorBench 的 Hydrogen 預設推理等級](#case-56) | 對比與局限 | 先檢視預設推理等級的基準成績，再到自己的倉庫裡測試. | Benchmark |
| [四款模型製作弓箭手戰鬥動畫](#case-57) | 對比與局限 | 比較各個動畫能否清楚表現角色的戰鬥動作. | Evaluation |
| [15 分鐘建構 Minecraft 風格原型](#case-58) | 應用程式與學習 | 用體素沙盒檢驗挖掘、背包等生成系統能否協同工作. | Demo |
| [n8n 中的 Hydrogen 工具呼叫流程](#case-59) | 代理程式與程式設計工作流 | 讓 Hydrogen 在 n8n 中處理工具呼叫迴圈，並單獨安排規劃步驟. | Integration |
| [Box Agent 處理複雜企業文件](#case-60) | 電子錶格與搜索 | 在接近真實的文件任務中同時檢查準確率、耗時和 Token 用量. | Benchmark |
| [Hydrogen 的 Devin FrontierCode 結果](#case-61) | 對比與局限 | 比較候選補丁能否合併，並記錄各自使用的代理環境. | Benchmark |
| [小型互動動畫中的光線折射](#case-62) | 互動式 3D 與使用者介面 | 先快速預覽並調整光學效果，再增加場景複雜度. | Demo |
| [一條向上流的河](#case-63) | 互動式 3D 與使用者介面 | 選擇運動方向不同尋常的小場景，觀察視覺效果. | Demo |
| [禁止聯網後仍觸發搜尋](#case-64) | 對比與局限 | 流程要求離線作答時，檢查模型是否真的沒有呼叫工具. | Limit |
| [記錄 Antigravity Swarm 的配額用量](#case-65) | 對比與局限 | 測試多代理執行時記錄 Token 量和消耗的額度. | Evaluation |
| [專業任務評估中的工具呼叫](#case-66) | 對比與局限 | 觀察代理在執行專業任務前如何收集背景資訊. | Benchmark |
| [Hydrogen 生成的 3D 肖像](#case-67) | 互動式 3D 與使用者介面 | 用肖像做小型測試，檢查 3D 表現能否保留可辨識的主體特徵. | Demo |
| [四款模型製作法師鬥龍動畫](#case-68) | 對比與局限 | 比較同一奇幻場景各版本的排程、動作清晰度和特效. | Evaluation |
| [多代理設定中的認證路徑](#case-69) | 代理程式與程式設計工作流 | 代理委派給其他服務時，核對實際發起認證的是哪個用戶端. | Limit |
| [一次 Antigravity Goal Mode 執行](#case-70) | 代理程式與程式設計工作流 | 長時間程式設計時，記錄計劃、程式碼修改與測試結果. | Demo |
| [MazeBench 中的低成功率](#case-71) | 對比與局限 | 用迷宮任務檢驗空間推理，再決定能否依賴它. | Benchmark |
| [三款 Gemini 模型建構帆船場景](#case-72) | 對比與局限 | 在主題化 Three.js 場景中比較運動效果和環境細節. | Evaluation |
| [Antigravity Orchestrator 中的 Carbon 與 Hydrogen](#case-73) | 代理程式與程式設計工作流 | 讓規劃模型在快速執行模型卡住時接手排障. | Integration |
| [從 Workspace 資料生成圖表和報告](#case-74) | 電子錶格與搜索 | 檢查追問一輪能否補齊分析、圖表或報告. | Demo |
| [識別球衣號碼時耗盡推理預算](#case-75) | 對比與局限 | 識別圖片中的小細節時，設定推理上限並準備替代方案. | Limit |
| [不同模型系列的 ClutterBench 表現](#case-76) | 對比與局限 | 用專門的雜亂場景基準檢驗模型的通用優勢是否適用於這一任務. | Benchmark |
| [把新聞簡報製作成帶旁白的短片](#case-77) | 應用程式與學習 | 先查資料，再將新聞簡報做成旁白短片並核查其中的事實. | Demo |
| [Minecraft 風格人體解剖剖面像](#case-78) | 對比與局限 | 檢查生成的剖面是否包含指定的內部結構. | Evaluation |
| [三款模型渲染同一件道具](#case-79) | 對比與局限 | 同時記錄質量和 Token 用量，檢查單價較低的模型是否在該任務中消耗更多 Token. | Evaluation |
| [歸納基準測試與 Token 消耗](#case-80) | 對比與局限 | 評估高難度推理時，將計費輸入和輸出用量與成績一起記錄. | Benchmark |
| [用不同 Gemini 模式在表格裡畫畫素畫](#case-81) | 電子錶格與搜索 | 用同一個 Google 表格繪圖任務比較不同模型選項. | Evaluation |
| [把參考圖中的公寓做成 3D 列印件](#case-82) | 互動式 3D 與使用者介面 | 把圖生 3D 的測試延伸到列印實物. | Demo |
| [三款模型製作 3D 動物動畫](#case-83) | 對比與局限 | 在同一項 3D 動物建模任務中檢查身體結構和運動. | Evaluation |
| [Hydrogen 與 Qwen 的 ts-bench 測試](#case-84) | 對比與局限 | 將工具呼叫錯誤和整體基準成績一起檢視. | Benchmark |
| [Vending-Bench 商業模擬](#case-85) | 對比與局限 | 比較模擬收入時同時計入代理執行成本. | Benchmark |
| [黃金梅麗號海上場景](#case-86) | 互動式 3D 與使用者介面 | 用辨識度高的虛構船隻測試風格化海景的構圖. | Demo |
| [在 OpenClaw 中使用 Hydrogen](#case-87) | 代理程式與程式設計工作流 | 檢查計劃採用的代理框架能否選用 Hydrogen. | Integration |
| [遊過雲海的鯨魚](#case-88) | 互動式 3D 與使用者介面 | 透過一個程式碼製作的生物場景分別檢查流體運動和眼睛設計. | Demo |
| [四款模型建構微縮島嶼](#case-89) | 對比與局限 | 比較島嶼設計時，一併記錄各個環境的耗時和費用. | Evaluation |
| [攝像頭空中繪畫工具](#case-90) | 應用程式與學習 | 在鏡頭前比畫筆畫，觀察繪圖介面如何跟隨. | Demo |
| [用程式碼模擬布料撕裂](#case-91) | 對比與局限 | 用同一動畫任務檢查布料拉伸、撕裂及與毛髮的相互作用. | Evaluation |
| [Gemini Canvas 裡的海底城市](#case-92) | 互動式 3D 與使用者介面 | 從小型 3D 場景起步，透過多輪迭代加入可探索的區域和會動的生物. | Demo |
| [一次生成的網站門戶](#case-93) | 應用程式與學習 | 先用門戶佈局檢查首輪介面，再測試各條操作流程. | Demo |
| [事實核查缺少可追溯來源](#case-94) | 對比與局限 | 依據模型對截圖的判斷行動之前，要求給出可查驗的引用. | Limit |
| [《城市：天際線》風格建城工具](#case-95) | 應用程式與學習 | 建構城市模擬原型，觀察控制元件和模擬邏輯如何配合. | Demo |
| [Hydrogen 與 Sol 繪製 2D 鵜鶘](#case-96) | 對比與局限 | 用同一項簡單 2D 動畫任務對比耗時與動作表現. | Evaluation |
| [用 Blender MCP 重建王座廳](#case-97) | 代理程式與程式設計工作流 | 用 Blender MCP 在編輯器中檢查生成場景的構圖. | Integration |
| [四款模型建構蛛絲擺盪遊戲](#case-98) | 對比與局限 | 統一使用單檔案限制，比較各款遊戲的移動和操作. | Evaluation |
| [Three.js 灰階海盜船](#case-99) | 互動式 3D 與使用者介面 | 將 Three.js 場景限定為灰階，檢查光照還能否突出幾何形狀. | Demo |
| [四款模型渲染建築微縮景觀](#case-100) | 對比與局限 | 用統一的建築任務比較輸出，檢視各模型如何打光. | Evaluation |
| [CadXStudio 中的引數化檯燈](#case-101) | 互動式 3D 與使用者介面 | 檢查 CAD 模型中的元件尺寸和可編輯性. | Integration |
| [用 C++ 製作神社參道動畫](#case-102) | 互動式 3D 與使用者介面 | 用小型原生程式碼場景檢驗模型能否在沒有 Web 技術棧時寫出可執行動畫. | Demo |
| [三款模型渲染列車場景](#case-103) | 對比與局限 | 用同一列車場景任務比較各自配置下的完成速度. | Evaluation |
| [用 Extra 等級製作雨夜唐人街](#case-104) | 對比與局限 | 給大型動畫選擇推理等級前，記錄實際耗時並檢查最終畫面. | Evaluation |
| [用 30 個模組建構城鎮場景](#case-105) | 互動式 3D 與使用者介面 | 按模組分別提示模型，再檢查組裝後的整體效果. | Demo |
| [三款模型建構行星視覺化介面](#case-106) | 對比與局限 | 用同一提示詞比較不同模型製作的科學視覺化介面. | Evaluation |
| [四款模型復刻 Chrome 小恐龍](#case-107) | 對比與局限 | 為每次遊戲復刻計時，並比較可玩結果. | Evaluation |
| [浮空島上的郵局](#case-108) | 互動式 3D 與使用者介面 | 指定一種微縮建築，觀察材質和光照如何表現主題. | Demo |
| [兩款程式開發代理分別造船](#case-109) | 對比與局限 | 在實際使用的工具中比較首個可用結果和返工成本. | Evaluation |
| [錦鯉庭院裡的水與魚](#case-110) | 互動式 3D 與使用者介面 | 用有游魚的場景檢查水面反射與光照是否連貫. | Demo |
| [四款模型製作剛體投石機攻城原型](#case-111) | 對比與局限 | 用同一任務比較可玩的物理原型，並記錄推理等級. | Evaluation |
| [Gemini 網頁端執行互動式 3D 場景](#case-112) | 互動式 3D 與使用者介面 | 在 Gemini 網頁端快速製作可互動光照和粒子效果. | Demo |
| [瀏覽器 CAD 中的混凝土攪拌機裝配](#case-113) | 代理程式與程式設計工作流 | 把生成的裝配體用於 CAD 工作流之前，檢查零件樹和配合情況. | Integration |
| [在 Blender 中程式化製作斧頭](#case-114) | 代理程式與程式設計工作流 | 用輪廓參考圖和多輪視口檢查來稽核程式化 Blender 資產. | Integration |
| [單 HTML 檔案裡的粉色 3D 場景](#case-115) | 互動式 3D 與使用者介面 | 嘗試無外部素材的 Three.js 場景，檢查構圖是否清晰. | Demo |
| [FrontierMemory 的長期記憶測試](#case-116) | 對比與局限 | 為長期代理記憶選模型時，結合評分和單次費用. | Benchmark |
| [故意損壞的 LiveKit 語音代理](#case-117) | 對比與局限 | 引入可控的工具故障，檢查語音代理會不會報告無依據的結果. | Evaluation |
| [由 28 個模組組成的 Ember Isle](#case-118) | 代理程式與程式設計工作流 | 把大場景拆成模組，並記錄每次生成的耗時. | Demo |
| [純程式碼製作的大爆炸模擬](#case-119) | 互動式 3D 與使用者介面 | 用短動畫快速構建視覺化解釋，再檢查科學表述. | Demo |
| [帶裝配爆炸圖的直升機](#case-120) | 互動式 3D 與使用者介面 | 檢查 3D 原型能否把飛行控制與實用的零件檢視方式結合起來. | Demo |
| [帶透視和線框檢視的 Hydrogen Express](#case-121) | 互動式 3D 與使用者介面 | 給可操控的 3D 原型加入多種檢查模式. | Demo |
| [空中的補給站](#case-122) | 互動式 3D 與使用者介面 | 給場景安排有辨識度的移動物體和光照狀態，讓變化在演示中清晰可見. | Demo |
| [三款 Gemini 模型製作騎行者動畫](#case-123) | 對比與局限 | 用統一簡報比較短動畫，並記錄各次執行的耗時. | Evaluation |
| [把化學教材做成互動課程](#case-124) | 應用程式與學習 | 用提示、語音引導和可選文本建構自學課程. | Demo |
| [一首 Vocaloid 歌曲原型](#case-125) | 應用程式與學習 | 檢查一次生成的曲目能否符合指定角色和風格. | Demo |
| [兩款模型建構 LEGO 世界](#case-126) | 對比與局限 | 結合耗時比較各模型建構了多少主題場景. | Evaluation |
| [修復兩個倉庫裡重新植入的缺陷](#case-127) | 對比與局限 | 植入已知缺陷，測量程式開發代理能找出並修復哪些問題. | Benchmark |
| [兩款模型製作火柴人對戰游標](#case-128) | 對比與局限 | 比較兩份互動動畫如何響應滑鼠指標. | Evaluation |
| [單 HTML 檔案裡的水磨坊](#case-129) | 互動式 3D 與使用者介面 | 用帶醒目運動元素的小景觀檢查快速生成的 3D 原型. | Demo |
| [兩款模型渲染山地景觀](#case-130) | 對比與局限 | 在同一類景觀動畫中分別比較構圖、生成耗時和費用. | Evaluation |
| [用自定義環境做英譯波斯語評估](#case-131) | 對比與局限 | 用人工參考譯文給高難度翻譯段落打分. | Evaluation |
| [用 Hydrogen Extra 建構 Blender 場景](#case-132) | 互動式 3D 與使用者介面 | 增加視覺細節之前，先在 Blender 中檢查幾何與材質. | Demo |
| [四款模型建構沉船場景](#case-133) | 對比與局限 | 用同一場景分別記錄視覺還原、生成時間與成本. | Evaluation |
| [從圖片讀取複雜積分式](#case-134) | 應用程式與學習 | 化簡長表示式前，檢查模型能否識別積分上下限相同. | Evaluation |
| [四款模型的文案盲測](#case-135) | 對比與局限 | 在選用文案之前，隱去模型名稱再評判. | Evaluation |
| [不同推理等級的視覺檢測與讀字](#case-136) | 對比與局限 | 在各個推理等級分別測量檢測準確率、文字識別準確率、費用與延遲. | Benchmark |
| [四款模型重建《飛屋環遊記》的房屋](#case-137) | 對比與局限 | 用同一張參考圖和簡報比較 3D 製作的各項取捨. | Evaluation |
| [用 WebGL2 製作人體細胞百科](#case-138) | 應用程式與學習 | 透過互動剖面講解細胞內部的空間關係. | Demo |
| [Hydrogen 製作的兩段粒子動畫](#case-139) | 互動式 3D 與使用者介面 | 用不同粒子場景檢驗簡單特效中的形態和運動. | Demo |
| [Parking Bench 中只看圖的對手](#case-140) | 應用程式與學習 | 只給益智遊戲對手棋盤圖片，測試它如何讀取局面. | Integration |
| [Google 文件的操作教學影片](#case-141) | 應用程式與學習 | 用螢幕截圖和編號標註講解手機端的編輯步驟. | Demo |
| [微縮世界的晝夜切換開關](#case-142) | 互動式 3D 與使用者介面 | 用小型開關測試介面狀態切換時動作是否連貫. | Demo |
| [用 65 個模組建構場景](#case-143) | 互動式 3D 與使用者介面 | 隨著場景擴充套件，記錄生成耗時和整合工作量. | Demo |
| [固定鏡頭的舞蹈短片](#case-144) | 對比與局限 | 檢查參考圖動畫能否保留角色設計、構圖與鏡頭位置. | Evaluation |
| [程式開發代理卡在基線測試](#case-145) | 對比與局限 | 給基線測試設定時限，並檢查進度再等待修復方案. | Limit |
| [為 MZ-1500 建構 BASIC 環境](#case-146) | 應用程式與學習 | 建構復古 BASIC 環境原型，並逐一核對外設支援. | Demo |
| [兩款模型建構互動機械臂](#case-147) | 對比與局限 | 操作 Three.js 機械臂時，檢查各關節的動作是否連貫. | Evaluation |
| [可互動的 FAA 地面停飛地圖](#case-148) | 電子錶格與搜索 | 用時間線和地圖展示停飛解除後佇列為何仍存在. | Demo |
| [微縮寶塔庭院](#case-149) | 互動式 3D 與使用者介面 | 檢查生成的微縮場景如何平衡建築和周邊綠化. | Demo |
| [用不同模型做規劃、執行與審閱](#case-150) | 代理程式與程式設計工作流 | 分別指定規劃、執行和審閱角色，並比較各模型的任務統計. | Demo |
| [Hydrogen 與 Sol 建構雪中村莊](#case-151) | 對比與局限 | 在程式設計對比中分別記錄耗時、費用和場景質量. | Evaluation |
| [High 與 Ultra 檔製作 Three.js 島嶼](#case-152) | 對比與局限 | 比較畫面和響應速度時，記錄推理等級並區分不同產品的額度. | Evaluation |
| [二戰機場微縮景觀](#case-153) | 互動式 3D 與使用者介面 | 給 3D 演示提供參考資料與機械運動要求，檢驗外觀之外的表現. | Demo |
| [在程式設計用戶端配置 Hydrogen](#case-154) | 代理程式與程式設計工作流 | 在受支援的用戶端中配置 Google API 金鑰時，填入準確的模型 ID. | Tutorial |
| [在 SuperARIS 科研團隊中使用 Hydrogen](#case-155) | 代理程式與程式設計工作流 | 在多模型團隊中給 Hydrogen 分配明確的研究和論文任務. | Integration |
| [四款模型淨室重寫核心模組](#case-156) | 代理程式與程式設計工作流 | 選擇重寫任務的代理時，分別比較程式碼庫理解、設計與實現. | Evaluation |
| [對比 3D PS5 手柄細節](#case-157) | 對比與局限 | 比較手柄模型時檢查按鈕陰影及背面硬體細節. | Evaluation |
| [Muse 把任務委派給 Antigravity CLI](#case-158) | 代理程式與程式設計工作流 | 把遠端助手連到本地程式設計環境，並設定預設寫作模型. | Integration |
| [CursorBench 中的推理預算對照](#case-159) | 對比與局限 | 選擇更快的預設檔前，比較不同推理配置下的成功率. | Benchmark |
| [三款模型渲染星核聖殿](#case-160) | 對比與局限 | 在 3D 任務中分別觀察渲染穩定性和畫面細節. | Evaluation |
| [一分鐘製作 HTML 射擊遊戲原型](#case-161) | 應用程式與學習 | 在一個 HTML 檔案中測試射擊遊戲的基本輸入與反饋迴圈. | Demo |
| [挑戰現有的遷移方案](#case-162) | 對比與局限 | 讓程式開發代理評估遷移是否需要替換現有架構. | Limit |
| [在 AITuber OnAir 讓 Hydrogen 和使用者對話](#case-163) | 應用程式與學習 | 試用 Hydrogen 驅動 Live2D 形象背後的聊天. | Integration |
| [純程式碼製作宣傳片](#case-164) | 應用程式與學習 | 給程式開發模型簡短的宣傳任務，檢視生成的動態設計. | Demo |
| [兩款模型製作神廟逃脫遊戲](#case-165) | 對比與局限 | 在同一遊戲概念中比較光照和氛圍是否便於看清場景. | Evaluation |
| [三款 Gemini 模型製作拉力車動畫](#case-166) | 對比與局限 | 檢查車輛透過帶傾角的彎道時，懸掛運動和輪胎抓地是否合理. | Evaluation |
| [程式化生成的知更鳥飛行動畫](#case-167) | 互動式 3D 與使用者介面 | 檢查生成飛行動畫中的翅膀和身體動作. | Demo |
| [如何選擇 Antigravity Orchestrator 或 Swarm](#case-168) | 代理程式與程式設計工作流 | 讓序列任務走模型交接，可並行任務交給獨立工作和驗證代理. | Tutorial |
| [兩款模型製作 Chasing Views 動畫](#case-169) | 對比與局限 | 比較輸出和耗時，同時記錄各自的推理等級. | Evaluation |
| [Design Creativity Bench 的速度和費用](#case-170) | 對比與局限 | 檢視創意評分時，一起比較單份設計的生成耗時與費用. | Benchmark |
| [從參考圖建立 SolidWorks CAD 零件](#case-171) | 代理程式與程式設計工作流 | 用 3D 參考圖評估代理在 SolidWorks 裡的建模流程. | Integration |
| [四款模型製作沙漠駿馬動畫](#case-172) | 對比與局限 | 先比較腳掌著地和重心轉移，再看打光和網格細節. | Evaluation |
| [講解榮格共時性的簡報](#case-173) | 應用程式與學習 | 用需要講清相關概念的主題測試幻燈片生成流程. | Demo |
| [FrontierCS 2 計算機科學研究評估](#case-174) | 對比與局限 | 在常規程式設計測試之外使用研究基準，並記錄執行環境. | Benchmark |
| [四款模型製作雲端里約](#case-175) | 對比與局限 | 用同一個創意簡報比較費用、耗時和主觀質量. | Evaluation |
| [Hydrogen 在 GBENCH 技術任務中的表現](#case-176) | 對比與局限 | 評估技術工作時，把可核驗的程式設計與非程式設計結果和價格、耗時一起比較. | Benchmark |
| [訓練車輛側方停車](#case-177) | 對比與局限 | 比較生成模擬中的學習進展和最終成功率. | Evaluation |
| [可操控的線粒體分子馬達](#case-178) | 應用程式與學習 | 用互動圖把分子運動和 ATP 產生聯絡起來. | Demo |
| [Qix 風格的圈地遊戲](#case-179) | 應用程式與學習 | 用簡短大型電玩任務檢驗首輪輸出是否實現可互動的遊戲迴圈. | Demo |
| [用 Hydrogen 生成 HTML 幻燈片](#case-180) | 應用程式與學習 | 測試 HTML 生成速度時檢視幻燈片的資訊層次和佈局. | Demo |
| [Hydrogen 在 Terminal-Bench 4.0 中的表現](#case-181) | 對比與局限 | 選命令列程式開發模型時，一起考慮基準完成率與任務費用. | Benchmark |
| [用單個 HTML 檔案繪製插圖](#case-182) | 互動式 3D 與使用者介面 | 測試程式碼能否在沒有外部素材的情況下重現參考視覺效果. | Demo |
| [三款 Gemini 模型製作章魚動畫](#case-183) | 對比與局限 | 觀察觸手抓住岩石後是否明顯帶動身體前進. | Evaluation |
| [用 Chrome 整理結構化 YouTube 摘要](#case-184) | 電子錶格與搜索 | 請 Chrome 的 Gemini 面板提供帶時間戳的影片摘要和有來源的背景資料. | Tutorial |
| [把課程做成短影片](#case-185) | 應用程式與學習 | 把一節課轉換成影片時，檢查解釋準確性和節奏. | Demo |
| [從靜態場景製作海鸚動畫](#case-186) | 互動式 3D 與使用者介面 | 把現有 HTML 場景用作程式化動畫的第一影格. | Demo |
| [一項城堡建模測試](#case-187) | 對比與局限 | 對比多次模型執行的城堡輸出和資源用量. | Evaluation |
| [Antigravity Swarm 中的瀏覽器操作](#case-188) | 代理程式與程式設計工作流 | 評估代理群組時，把瀏覽器活動和任務記錄放在一起檢視. | Demo |
| [經 Google Drive 把任務交給 Muse](#case-189) | 代理程式與程式設計工作流 | 把研究結果交給第二個代理時，用受監控的 Drive 資料夾完成交接. | Integration |
| [Gemini Canvas 中的直笛練習指南](#case-190) | 應用程式與學習 | 試用高速模式，將樂譜和演奏指引結合成練習工具. | Demo |
| [新增範圍後項目估時大幅改變](#case-191) | 對比與局限 | 交付時間發生大幅變化時，要求模型說明專案範圍與假設. | Limit |
| [Antigravity Swarm 製作鵜鶘動畫](#case-192) | 代理程式與程式設計工作流 | 把動畫和音效製作交給程式開發代理群組，再檢查合成的場景. | Demo |
| [考慮閏年邊界的日曆問題](#case-193) | 對比與局限 | 提出簡單換算問題，檢查答案是否考慮日曆邊界情況. | Evaluation |
| [一個 HTML 檔案裡的 TAJ VICE](#case-194) | 應用程式與學習 | 限定單檔案製作可探索地圖，然後測試剩餘缺陷. | Demo |
| [透過 Google Cloud 專案連線 Antigravity](#case-195) | 代理程式與程式設計工作流 | 用託管憑據啟用 Hydrogen 時，檢查代理認證和專案結算方式. | Tutorial |
| [回答引用了過時的訂閱額度](#case-196) | 對比與局限 | 評估研究助手時，對照一手來源核實計劃條款和模型名稱. | Limit |
| [修改 WebGL 動畫的敘事](#case-197) | 對比與局限 | 首版技術效果豐富卻缺少清楚脈絡時，要求增強敘事. | Limit |
| [Carbon 規劃、Hydrogen 實現移動應用](#case-198) | 代理程式與程式設計工作流 | 將互動設計分派給規劃模型，再把實現工作交給執行模型. | Demo |
| [兩款模型用程式碼製作山間鬥龍](#case-199) | 對比與局限 | 比較同一場景中的兩方角色互動. | Evaluation |
| [用一則提示詞建構 3D 微縮島](#case-200) | 互動式 3D 與使用者介面 | 檢查一次生成的場景能否清楚安排地標、地形與水域. | Demo |
| [可複用的 Three.js 鵜鶘提示詞](#case-201) | 對比與局限 | 檢查騎行動畫中腿、車輪和轉向能否同步. | Evaluation |
| [在 T3 Code 中使用 Hydrogen](#case-202) | 代理程式與程式設計工作流 | 在實際程式設計會話中試用用戶端，跟蹤滾動用量上限和每週額度. | Integration |
| [手繪風公益短片](#case-203) | 應用程式與學習 | 用簡短的公益主題評估手繪式視覺表現. | Demo |
| [孔雀騎車穿過十種藝術風格](#case-204) | 代理程式與程式設計工作流 | 用混合模型代理群組用程式碼製作畫面過渡並同步聲音. | Demo |
| [同一個小屋任務在三種環境中執行](#case-205) | 對比與局限 | 把視覺任務遷移到不同模型檔和平臺時，檢查輸出格式. | Evaluation |
| [用同一提示詞對比儀表盤](#case-206) | 對比與局限 | 用同一個前端提示詞比較介面佈局和資訊層次. | Evaluation |
| [從參考圖復刻 React.gg 網站](#case-207) | 應用程式與學習 | 從一張圖開始復刻，再檢查哪些細節還需要調整. | Demo |
| [奇點主題的互動面板](#case-208) | 互動式 3D 與使用者介面 | 圍繞一個視覺概念製作簡短的互動片段. | Demo |
| [兩款模型用程式碼製作橫版動畫](#case-209) | 對比與局限 | 比較生成的動作場景時，關注動作連續性和製作費用. | Evaluation |
| [讓 Gemini 擔任跑步教練](#case-210) | 應用程式與學習 | 把訓練記錄與模型建議對照，按自己的起點調整目標. | Demo |
| [成績上鍊的瀏覽器遊戲](#case-211) | 應用程式與學習 | 在桌面瀏覽器中測試遊戲，同時單獨驗證成績如何記錄. | Demo |
| [日語回答裡的數學公式未渲染](#case-212) | 對比與局限 | 回答含 TeX 指令時，同時檢查內容和公式顯示. | Limit |
| [從提示詞到 MIDI 的作曲應用](#case-213) | 應用程式與學習 | 建構從日語簡報到 MIDI、WAV 和鋼琴捲簾檢視的工具原型. | Demo |
| [測試模型能否遵守保持沉默的指令](#case-214) | 對比與局限 | 流程要求不回覆時，檢查模型能否真正不產生答覆. | Evaluation |
| [一頁圖文回顧演唱會](#case-215) | 應用程式與學習 | 把活動資訊整理成易於瀏覽的一頁視覺回顧. | Demo |
| [三款模型解釋電動機原理](#case-216) | 對比與局限 | 在同一個模擬提示詞下，比較畫面清晰度與教學控制元件. | Evaluation |
| [兩種模型工作流製作桌面動畫](#case-217) | 對比與局限 | 對照原始任務檢查畫面細節、音量和片尾是否保持靜止. | Evaluation |
| [從頭像製作日常片段](#case-218) | 應用程式與學習 | 用一張參考頭像和四個日常場景檢驗短分鏡的改編. | Demo |
| [Hydrogen 為 ComfyUI 角色影片做規劃](#case-219) | 應用程式與學習 | 固定服裝與背景，在簡報中變化角色表情與動作. | Integration |
| [把 Almance Vale 擴充套件到 100 個模組](#case-220) | 代理程式與程式設計工作流 | 將已有應用移入程式開發代理，要求新增模組時保留既有風格. | Demo |
| [帶程序式音效的 2D 村莊](#case-221) | 對比與局限 | 記錄建構耗時，並檢查聲音是否隨畫面中的事件變化. | Evaluation |
| [為歌曲製作寬屏視覺畫面](#case-222) | 應用程式與學習 | 給模型一首歌與畫幅要求，觀察畫面運動如何傳遞歌曲的能量. | Demo |
| [七個 Hydrogen 子代理建構尼亞加拉瀑布](#case-223) | 代理程式與程式設計工作流 | 給協調代理可分割的場景元件，讓它把實現任務交給子代理. | Demo |
| [兩段年代愛情短片的連續性](#case-224) | 應用程式與學習 | 讓第二段短片延續第一段時，明確要保留哪些細節. | Demo |
| [Gemini App 中的水球](#case-225) | 互動式 3D 與使用者介面 | 用簡單光學場景觀察高光與折射的關係. | Demo |

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

<a id="case-59"></a>
### 案例 59: [n8n 中的 Hydrogen 工具呼叫流程](https://x.com/n8n_io/status/2120947273534197886) (作者 [@n8n_io](https://x.com/n8n_io))

**讓 Hydrogen 在 n8n 中處理工具呼叫迴圈，並單獨安排規劃步驟.**

n8n 介紹了 Hydrogen 支援情況，建議由 Carbon 或 Argon 規劃、Hydrogen 執行，並在原帖附上整合設定.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-12

---

<a id="case-69"></a>
### 案例 69: [多代理設定中的認證路徑](https://x.com/studio_yebisu/status/2120969033260646551) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**代理委派給其他服務時，核對實際發起認證的是哪個用戶端.**

作者報告，要求 Claude 透過 Antigravity CLI 使用 Hydrogen 後，Claude Code 直接嘗試認證，隨後 Antigravity 訪問被暫停. 截圖顯示暫停通知，作者將原因歸於用戶端認證路徑.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-12

---

<a id="case-70"></a>
### 案例 70: [一次 Antigravity Goal Mode 執行](https://x.com/Inmerson/status/2120973427788124345) (作者 [@Inmerson](https://x.com/Inmerson))

**長時間程式設計時，記錄計劃、程式碼修改與測試結果.**

作者報告在 Hydrogen Extra 的 Goal Mode 中執行 105 分鐘，完成規劃、實現和測試. 測試結果來自作者陳述.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-1-url-d2827ec85ec0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-1-url-d2827ec85ec0.png" alt="Case 70 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-2-url-352705a2d20c.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-2-url-352705a2d20c.png" alt="Case 70 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Demo | 日期: 2026-11-12

---

<a id="case-73"></a>
### 案例 73: [Antigravity Orchestrator 中的 Carbon 與 Hydrogen](https://x.com/Google/status/2120982566891356279) (作者 [@Google](https://x.com/Google))

**讓規劃模型在快速執行模型卡住時接手排障.**

Google 介紹由 Carbon 規劃和處理卡點、Hydrogen 編輯與測試的流程，並報告 Terminal-Bench 4.0 成功率接近 Carbon，配額用量較低、耗時較短.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

類型: Integration | 日期: 2026-11-12

---

<a id="case-87"></a>
### 案例 87: [在 OpenClaw 中使用 Hydrogen](https://x.com/openclaw/status/2121098531205501401) (作者 [@openclaw](https://x.com/openclaw))

**檢查計劃採用的代理框架能否選用 Hydrogen.**

OpenClaw 宣佈支援 Hydrogen 並附上截圖. 原帖未提供基準評分或完整配置記錄.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-13

---

<a id="case-97"></a>
### 案例 97: [用 Blender MCP 重建王座廳](https://x.com/ashen_one/status/2121165467821936651) (作者 [@ashen_one](https://x.com/ashen_one))

**用 Blender MCP 在編輯器中檢查生成場景的構圖.**

創作者將透過 Blender MCP 重建的《權力的遊戲》鐵王座大廳歸功於 Hydrogen，並分享場景螢幕錄影.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

類型: Integration | 日期: 2026-11-13

---

<a id="case-113"></a>
### 案例 113: [瀏覽器 CAD 中的混凝土攪拌機裝配](https://x.com/johnsanthosh01/status/2121243197901041869) (作者 [@johnsanthosh01](https://x.com/johnsanthosh01))

**把生成的裝配體用於 CAD 工作流之前，檢查零件樹和配合情況.**

創作者報告，Hydrogen 在 CadX Studio 中根據一則提示詞、用 40 分鐘生成 265 個零件的攪拌機裝配體，未逐件手工建模.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

類型: Integration | 日期: 2026-11-13

---

<a id="case-114"></a>
### 案例 114: [在 Blender 中程式化製作斧頭](https://x.com/camperaigg/status/2121252572115951897) (作者 [@camperaigg](https://x.com/camperaigg))

**用輪廓參考圖和多輪視口檢查來稽核程式化 Blender 資產.**

創作者報告在 Antigravity CLI 中用 Hydrogen 透過 Python 模組和反覆視口檢查製作風格化斧頭. 計入錄製耗時 51 分鐘，報告 API 費用 $5.01.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-13

---

<a id="case-118"></a>
### 案例 118: [由 28 個模組組成的 Ember Isle](https://x.com/IamEmily2050/status/2121258646759952644) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**把大場景拆成模組，並記錄每次生成的耗時.**

創作者用 Gemini App 中的 Hydrogen High 製作 Ember Isle，稱共 28 個模組，每個模組用一則提示詞，每次 82 至 290 秒.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-150"></a>
### 案例 150: [用不同模型做規劃、執行與審閱](https://x.com/naufaldi/status/2121499487999013081) (作者 [@naufaldi](https://x.com/naufaldi))

**分別指定規劃、執行和審閱角色，並比較各模型的任務統計.**

作者安排 Opus 5.5 規劃、Hydrogen 執行、Sol 後備及 Sol 6.1 審閱. 來源同時提供個人 Antigravity 用量與獨立的公開基準對照.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-1-url-4838b2ba0b61.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-1-url-4838b2ba0b61.jpg" alt="Case 150 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-2-url-e7c778cfcf91.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-2-url-e7c778cfcf91.jpg" alt="Case 150 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-3-url-5d627806345d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-3-url-5d627806345d.jpg" alt="Case 150 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

類型: Demo | 日期: 2026-11-14

---

<a id="case-154"></a>
### 案例 154: [在程式設計用戶端配置 Hydrogen](https://x.com/k2sbhai/status/2121509825658147041) (作者 [@k2sbhai](https://x.com/k2sbhai))

**在受支援的用戶端中配置 Google API 金鑰時，填入準確的模型 ID.**

作者介紹如何從 Google AI Studio 獲取金鑰，並在 OpenCode 或 Cline 選擇 gemini-4-hydrogen. 使用資格和速率限制取決於服務商.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

類型: Tutorial | 日期: 2026-11-14

---

<a id="case-155"></a>
### 案例 155: [在 SuperARIS 科研團隊中使用 Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**在多模型團隊中給 Hydrogen 分配明確的研究和論文任務.**

來源展示安裝 SuperARIS 和選擇團隊配置的步驟，建議 Hydrogen 或 Carbon 負責討論和寫作，並分別設定協調與實現角色. 案例展示整合流程，研究質量未經測量.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-1-url-724d48461bd4.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-1-url-724d48461bd4.jpg" alt="Case 155 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-2-url-dd4a1c6d1650.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-2-url-dd4a1c6d1650.jpg" alt="Case 155 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-3-url-a70f7661d1c1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-3-url-a70f7661d1c1.jpg" alt="Case 155 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-4-url-8cdfdaf95c58.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-4-url-8cdfdaf95c58.jpg" alt="Case 155 source image 4" width="100%"></a>
</td>
</tr>
</table>

類型: Integration | 日期: 2026-11-14

---

<a id="case-156"></a>
### 案例 156: [四款模型淨室重寫核心模組](https://x.com/oasisfeng/status/2121523934831276203) (作者 [@oasisfeng](https://x.com/oasisfeng))

**選擇重寫任務的代理時，分別比較程式碼庫理解、設計與實現.**

創作者對比 Hydrogen、Argon、GPT-6 Astra 和 Claude Opus 5.5 重寫軟體核心模組的結果，認為 Hydrogen 執行力強，其他執行則各有架構設計優勢.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-1-url-729f1441593f.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-1-url-729f1441593f.png" alt="Case 156 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-2-url-4f4c6848310c.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-2-url-4f4c6848310c.png" alt="Case 156 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-158"></a>
### 案例 158: [Muse 把任務委派給 Antigravity CLI](https://x.com/tetumemo/status/2121528823061852166) (作者 [@tetumemo](https://x.com/tetumemo))

**把遠端助手連到本地程式設計環境，並設定預設寫作模型.**

作者描述 Muse 把任務發到家中電腦上的 Antigravity CLI 並接收成果. 預設用 Hydrogen，也可選 Argon，示例有日語寫作和視覺材料.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-14

---

<a id="case-168"></a>
### 案例 168: [如何選擇 Antigravity Orchestrator 或 Swarm](https://x.com/ohayou792/status/2121624258984153452) (作者 [@ohayou792](https://x.com/ohayou792))

**讓序列任務走模型交接，可並行任務交給獨立工作和驗證代理.**

作者用圖解說明 Antigravity Orchestrator 如何先由前沿模型規劃，再由 Hydrogen 實現，並與獨立的 /swarm 協調模式對比，建議按任務依賴選擇.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

類型: Tutorial | 日期: 2026-11-14

---

<a id="case-171"></a>
### 案例 171: [從參考圖建立 SolidWorks CAD 零件](https://x.com/GoGoFly23/status/2121636952479080713) (作者 [@GoGoFly23](https://x.com/GoGoFly23))

**用 3D 參考圖評估代理在 SolidWorks 裡的建模流程.**

創作者報告，在 Antigravity 中給 Hydrogen 一張參考圖後得到所展示的 SolidWorks 零件. 後續帖說明使用 SolidWorks MCP，幾何公差和工程適用性尚未驗證.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-14

---

<a id="case-188"></a>
### 案例 188: [Antigravity Swarm 中的瀏覽器操作](https://x.com/Saboo_Shubham_/status/2121852445756477924) (作者 [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**評估代理群組時，把瀏覽器活動和任務記錄放在一起檢視.**

Google 員工分享在 Antigravity Swarm 中使用 Hydrogen 和瀏覽器的截圖. 來源未放出完整任務日誌.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-15

---

<a id="case-189"></a>
### 案例 189: [經 Google Drive 把任務交給 Muse](https://x.com/nasuvit_z/status/2121857992702525734) (作者 [@nasuvit_z](https://x.com/nasuvit_z))

**把研究結果交給第二個代理時，用受監控的 Drive 資料夾完成交接.**

作者用 Hydrogen 收集資訊並整理成 Drive 檔案，再讓 Muse 監聽 Drive，在檔案出現時接手後續任務. 圖解展示了交接流程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-15

---

<a id="case-192"></a>
### 案例 192: [Antigravity Swarm 製作鵜鶘動畫](https://x.com/chetaslua/status/2121885449509851415) (作者 [@chetaslua](https://x.com/chetaslua))

**把動畫和音效製作交給程式開發代理群組，再檢查合成的場景.**

創作者將多種藝術風格之間切換的 JavaScript 鵜鶘場景歸功於 Carbon 與 Hydrogen，並稱音樂和音效也由程式碼生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-195"></a>
### 案例 195: [透過 Google Cloud 專案連線 Antigravity](https://x.com/loganlu51268/status/2121911409042719023) (作者 [@loganlu51268](https://x.com/loganlu51268))

**用託管憑據啟用 Hydrogen 時，檢查代理認證和專案結算方式.**

作者記錄透過應用預設憑據將 Antigravity 從個人計劃切換到 Google Cloud Agent Platform 專案. 模型選擇器包含 Hydrogen，來源還介紹按 SKU 檢查專案花費.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-1-url-c86f9942da03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-1-url-c86f9942da03.png" alt="Case 195 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-2-url-7695f3eaa9a3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-2-url-7695f3eaa9a3.jpg" alt="Case 195 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-3-url-6bad19f93237.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-3-url-6bad19f93237.jpg" alt="Case 195 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-4-url-99834386815e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-4-url-99834386815e.jpg" alt="Case 195 source image 4" width="100%"></a>
</td>
</tr>
</table>

類型: Tutorial | 日期: 2026-11-15

---

<a id="case-198"></a>
### 案例 198: [Carbon 規劃、Hydrogen 實現移動應用](https://x.com/thebuggeddev/status/2121945961555718334) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**將互動設計分派給規劃模型，再把實現工作交給執行模型.**

創作者稱 Carbon 規劃了手機應用，Hydrogen 實現了應用及 Reanimated 物理動效. 作者描述動作流暢，並分享螢幕錄影.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-202"></a>
### 案例 202: [在 T3 Code 中使用 Hydrogen](https://x.com/bei351009016/status/2121964293906206916) (作者 [@bei351009016](https://x.com/bei351009016))

**在實際程式設計會話中試用用戶端，跟蹤滾動用量上限和每週額度.**

作者稱把 Gemini Pro 接入 T3 Code，用 Hydrogen 處理了約半天任務. 截圖和原帖記錄額度體驗，作者分別評價了速度與準確性.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

類型: Integration | 日期: 2026-11-15

---

<a id="case-204"></a>
### 案例 204: [孔雀騎車穿過十種藝術風格](https://x.com/SahilPanhotra/status/2121995488425849064) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**用混合模型代理群組用程式碼製作畫面過渡並同步聲音.**

創作者將跨十種藝術風格的孔雀騎車動畫歸功於 Carbon 和 Hydrogen 的代理群組，並稱畫面、音樂和音效都由程式碼製作.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-220"></a>
### 案例 220: [把 Almance Vale 擴充套件到 100 個模組](https://x.com/IamEmily2050/status/2122257581175410858) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**將已有應用移入程式開發代理，要求新增模組時保留既有風格.**

創作者把 Almance Vale 從 Gemini 應用遷入 Antigravity，報告在 swarm 模式中用 Hydrogen Extra 遵循原有程式碼約定，數小時擴充套件到 100 個模組.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

類型: Demo | 日期: 2026-11-16

---

<a id="case-223"></a>
### 案例 223: [七個 Hydrogen 子代理建構尼亞加拉瀑布](https://x.com/SahilPanhotra/status/2122311637684424737) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**給協調代理可分割的場景元件，讓它把實現任務交給子代理.**

作者將不到一小時、按一則提示詞建構的尼亞加拉瀑布體驗歸功於 Carbon 與七個 Hydrogen 子代理. 螢幕錄影可見水體、遊船、多種視角與環境變化.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

類型: Demo | 日期: 2026-11-16

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

<a id="case-58"></a>
### 案例 58: [15 分鐘建構 Minecraft 風格原型](https://x.com/RezAIT00/status/2120947124418293876) (作者 [@RezAIT00](https://x.com/RezAIT00))

**用體素沙盒檢驗挖掘、背包等生成系統能否協同工作.**

創作者報告用 Hydrogen Extra High 在 15 分鐘內建構 Minecraft 風格原型，列出的功能包括放置、挖掘和背包. 螢幕錄影只覆蓋部分功能.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-77"></a>
### 案例 77: [把新聞簡報製作成帶旁白的短片](https://x.com/gigabit_million/status/2121011957042163722) (作者 [@gigabit_million](https://x.com/gigabit_million))

**先查資料，再將新聞簡報做成旁白短片並核查其中的事實.**

螢幕錄影顯示 Hydrogen 在 Gemini 手機應用中查詢近期新聞、起草提綱，創作者隨後要求製作影片. 影片在應用內播放，時長十秒. 耗時與旁白由創作者報告，渲染後端未說明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-90"></a>
### 案例 90: [攝像頭空中繪畫工具](https://x.com/CodeByPoonam/status/2121121804483969102) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**在鏡頭前比畫筆畫，觀察繪圖介面如何跟隨.**

創作者報告在 Hydrogen 早期試用期間建構了攝像頭空中繪畫工具，並分享演示螢幕錄影.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-93"></a>
### 案例 93: [一次生成的網站門戶](https://x.com/kimura_0314/status/2121130305532878979) (作者 [@kimura_0314](https://x.com/kimura_0314))

**先用門戶佈局檢查首輪介面，再測試各條操作流程.**

作者展示在 Antigravity 中用 Hydrogen 一次生成的門戶截圖. 截圖只能用於檢視頁面外觀.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-13

---

<a id="case-95"></a>
### 案例 95: [《城市：天際線》風格建城工具](https://x.com/yohakujpn/status/2121146464466604147) (作者 [@yohakujpn](https://x.com/yohakujpn))

**建構城市模擬原型，觀察控制元件和模擬邏輯如何配合.**

創作者把影片中的《城市：天際線》風格原型歸功於 Hydrogen，並報告生成用時不到 30 分鐘.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-124"></a>
### 案例 124: [把化學教材做成互動課程](https://x.com/smalkalbani/status/2121282231759155617) (作者 [@smalkalbani](https://x.com/smalkalbani))

**用提示、語音引導和可選文本建構自學課程.**

作者展示帶語音引導和提示的九年級化學課程. 演示未測量學習成效.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-125"></a>
### 案例 125: [一首 Vocaloid 歌曲原型](https://x.com/peach2k2/status/2121284159565902188) (作者 [@peach2k2](https://x.com/peach2k2))

**檢查一次生成的曲目能否符合指定角色和風格.**

作者分享一段歌曲，將作曲歸功於 Hydrogen. 來源未說明用什麼工具渲染音訊.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-134"></a>
### 案例 134: [從圖片讀取複雜積分式](https://x.com/HarshithLucky3/status/2121303778548908228) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**化簡長表示式前，檢查模型能否識別積分上下限相同.**

創作者錄製 Gemini App 中的 Hydrogen High 對複雜積分截圖作答. 測試重點是模型能否識別外層積分的相同上下限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-138"></a>
### 案例 138: [用 WebGL2 製作人體細胞百科](https://x.com/soumyadesign/status/2121354542344466565) (作者 [@soumyadesign](https://x.com/soumyadesign))

**透過互動剖面講解細胞內部的空間關係.**

創作者報告在 Antigravity 中用 Hydrogen 建構 3D 人體細胞百科，使用 WebGL2、無外部庫，並重點展示了剖面檢視.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-140"></a>
### 案例 140: [Parking Bench 中只看圖的對手](https://x.com/agenticjay/status/2121391300822081713) (作者 [@agenticjay](https://x.com/agenticjay))

**只給益智遊戲對手棋盤圖片，測試它如何讀取局面.**

創作者稱遊戲由 Carbon 建構，玩家在五關中透過 API 對戰 Hydrogen 或 Gemini Decision 1. 兩款模型都只接收棋盤 PNG，不接收網格狀態資料.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

類型: Integration | 日期: 2026-11-13

---

<a id="case-141"></a>
### 案例 141: [Google 文件的操作教學影片](https://x.com/nin222/status/2121395008863621390) (作者 [@nin222](https://x.com/nin222))

**用螢幕截圖和編號標註講解手機端的編輯步驟.**

作者將一段 Google 文件手機端教學歸功於 Hydrogen. 抽樣畫面顯示加註的選取文字、樣式、顏色、字型及儲存步驟. 來源未說明剪輯方式.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-146"></a>
### 案例 146: [為 MZ-1500 建構 BASIC 環境](https://x.com/hiromsa/status/2121465784715338065) (作者 [@hiromsa](https://x.com/hiromsa))

**建構復古 BASIC 環境原型，並逐一核對外設支援.**

作者將演示歸功於 Hydrogen，報告用時約 15 分鐘. 演示列出 PCG、PSG 與 QuickDisk 支援，其中 QuickDisk 僅支援 LOAD.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-14

---

<a id="case-161"></a>
### 案例 161: [一分鐘製作 HTML 射擊遊戲原型](https://x.com/SahilPanhotra/status/2121561371951399133) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**在一個 HTML 檔案中測試射擊遊戲的基本輸入與反饋迴圈.**

創作者報告 Hydrogen 按一則提示詞在一分鐘內生成了可玩的射擊遊戲. 專案只用一個 HTML 檔案，無框架或額外設定.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-163"></a>
### 案例 163: [在 AITuber OnAir 讓 Hydrogen 和使用者對話](https://x.com/shinshin86/status/2121571590442017094) (作者 [@shinshin86](https://x.com/shinshin86))

**試用 Hydrogen 驅動 Live2D 形象背後的聊天.**

專案維護者公佈 AITuber OnAir 的 Hydrogen 支援，並提供含 Live2D 在內的對話形象示例. 螢幕錄影展示了整合效果.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

類型: Integration | 日期: 2026-11-14

---

<a id="case-164"></a>
### 案例 164: [純程式碼製作宣傳片](https://x.com/xiangning0/status/2121594643540480293) (作者 [@xiangning0](https://x.com/xiangning0))

**給程式開發模型簡短的宣傳任務，檢視生成的動態設計.**

作者展示一段以 GPT-6.2 Astra 為主題的宣傳片，稱 Hydrogen 完全用程式碼製作. 影片展示了程式碼製作的輸出.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-173"></a>
### 案例 173: [講解榮格共時性的簡報](https://x.com/soumyadesign/status/2121676345835241916) (作者 [@soumyadesign](https://x.com/soumyadesign))

**用需要講清相關概念的主題測試幻燈片生成流程.**

作者將介紹卡爾·榮格共時性和非因果秩序的幻燈片歸功於 Hydrogen 與自定義工具，稱工具在 Antigravity 中開發，並分享部分輸出.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-1-url-da309a9b81ad.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-1-url-da309a9b81ad.jpg" alt="Case 173 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-2-url-04e00cd024a5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-2-url-04e00cd024a5.jpg" alt="Case 173 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-3-url-12da69202041.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-3-url-12da69202041.jpg" alt="Case 173 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-4-url-520c28ccff68.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-4-url-520c28ccff68.jpg" alt="Case 173 source image 4" width="100%"></a>
</td>
</tr>
</table>

類型: Demo | 日期: 2026-11-14

---

<a id="case-178"></a>
### 案例 178: [可操控的線粒體分子馬達](https://x.com/SidraMiconi/status/2121745863827697687) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**用互動圖把分子運動和 ATP 產生聯絡起來.**

作者稱 Hydrogen High 按一則提示詞生成 ATP 合酶應用，隨後修正鏡頭. 模型外形以冷凍電子顯微鏡座標為基礎，運動過程經過簡化.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-179"></a>
### 案例 179: [Qix 風格的圈地遊戲](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (作者 [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**用簡短大型電玩任務檢驗首輪輸出是否實現可互動的遊戲迴圈.**

創作者在免費 Gemini 介面請求製作 Qix 風格的圈地遊戲，分享演示、標記 Hydrogen，並報告只用了一個請求.

**提示詞:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-180"></a>
### 案例 180: [用 Hydrogen 生成 HTML 幻燈片](https://x.com/yamachan_ai_log/status/2121772023710118043) (作者 [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**測試 HTML 生成速度時檢視幻燈片的資訊層次和佈局.**

作者展示 Hydrogen 生成 HTML 幻燈片的過程，認為速度快、細節充分. 螢幕錄影展示文稿，原帖未給出對照計時.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-185"></a>
### 案例 185: [把課程做成短影片](https://x.com/smalkalbani/status/2121844887033458954) (作者 [@smalkalbani](https://x.com/smalkalbani))

**把一節課轉換成影片時，檢查解釋準確性和節奏.**

創作者將課程工作流歸功於 Hydrogen，併發布兩個片段. 實際負責渲染影片的系統未得到確認.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-190"></a>
### 案例 190: [Gemini Canvas 中的直笛練習指南](https://x.com/nin222/status/2121877676042682538) (作者 [@nin222](https://x.com/nin222))

**試用高速模式，將樂譜和演奏指引結合成練習工具.**

影片展示在 Hydrogen 高速模式下製作的 Canvas 直笛應用. 創作者稱也可以匯入樂譜生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-194"></a>
### 案例 194: [一個 HTML 檔案裡的 TAJ VICE](https://x.com/SahilPanhotra/status/2121909681514074328) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**限定單檔案製作可探索地圖，然後測試剩餘缺陷.**

創作者稱用 Hydrogen 在不足 12 小時的會話中製作了受 GTA 啟發、以虛構阿格拉為背景的遊戲. 專案使用純 JavaScript 和一個 HTML 檔案，無外部資產，仍有玩法缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-203"></a>
### 案例 203: [手繪風公益短片](https://x.com/shengtang135754/status/2121965385356612020) (作者 [@shengtang135754](https://x.com/shengtang135754))

**用簡短的公益主題評估手繪式視覺表現.**

創作者分享一段手繪風格的公益短片並歸功於 Gemini 4 Hydrogen. 一次成片來自作者陳述，渲染模型和製作步驟未公開.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-207"></a>
### 案例 207: [從參考圖復刻 React.gg 網站](https://x.com/thebuggeddev/status/2122019549117911473) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**從一張圖開始復刻，再檢查哪些細節還需要調整.**

創作者報告給 Hydrogen 一張參考圖，透過少量提示覆刻 React.gg. 來源連結了演示，並說明還有細節不一致.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-210"></a>
### 案例 210: [讓 Gemini 擔任跑步教練](https://x.com/ivanleomk/status/2122036783307469199) (作者 [@ivanleomk](https://x.com/ivanleomk))

**把訓練記錄與模型建議對照，按自己的起點調整目標.**

創作者將跑步指導歸功於 Gemini Hydrogen，分享了訓練截圖，並稱完成約一年以來最長的一次跑步. 這是個人使用案例.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-15

---

<a id="case-211"></a>
### 案例 211: [成績上鍊的瀏覽器遊戲](https://x.com/itshoseyn/status/2122063851143246140) (作者 [@itshoseyn](https://x.com/itshoseyn))

**在桌面瀏覽器中測試遊戲，同時單獨驗證成績如何記錄.**

創作者稱 Hydrogen 協助建構與 Base 相連、把成績寫入鏈上的 Sheytonak 遊戲. 來源稱為桌面做了最佳化，移動端仍有問題，遊戲也尚有缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-213"></a>
### 案例 213: [從提示詞到 MIDI 的作曲應用](https://x.com/Awed_Urshy/status/2122161392828727738) (作者 [@Awed_Urshy](https://x.com/Awed_Urshy))

**建構從日語簡報到 MIDI、WAV 和鋼琴捲簾檢視的工具原型.**

創作者用 Hydrogen 建構應用，將日語輸入轉成英文音樂提示詞，寫出 MIDI、渲染 WAV，再生成鋼琴捲簾影片. 以上是演示應用的功能.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

類型: Demo | 日期: 2026-11-16

---

<a id="case-215"></a>
### 案例 215: [一頁圖文回顧演唱會](https://x.com/fukubaya/status/2122215495474794640) (作者 [@fukubaya](https://x.com/fukubaya))

**把活動資訊整理成易於瀏覽的一頁視覺回顧.**

作者分享 Batten Girls 演唱會的日語圖文回顧，將總結歸功於 Hydrogen. 來源未展示完整素材或提示詞.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-1-url-d73e46e74edb.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-1-url-d73e46e74edb.jpg" alt="Case 215 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-2-url-2f2363fb51b2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-2-url-2f2363fb51b2.jpg" alt="Case 215 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Demo | 日期: 2026-11-16

---

<a id="case-218"></a>
### 案例 218: [從頭像製作日常片段](https://x.com/antiAIvo/status/2122251181112353276) (作者 [@antiAIvo](https://x.com/antiAIvo))

**用一張參考頭像和四個日常場景檢驗短分鏡的改編.**

創作者提供 X 頭像及學習、吃飯、看手機、運動四個場景，釋出約十秒的成果並歸因於 Hydrogen，未說明影片渲染後端.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

類型: Demo | 日期: 2026-11-16

---

<a id="case-219"></a>
### 案例 219: [Hydrogen 為 ComfyUI 角色影片做規劃](https://x.com/nyapan_mohy/status/2122253350808744004) (作者 [@nyapan_mohy](https://x.com/nyapan_mohy))

**固定服裝與背景，在簡報中變化角色表情與動作.**

創作者稱 Hydrogen 圍繞參考角色設計規劃短片，透過另一套 ComfyUI MiniMax 圖生影片流程渲染，併為變體準備新第一影格和含 30 個鏡頭的提示詞.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

類型: Integration | 日期: 2026-11-16

---

<a id="case-222"></a>
### 案例 222: [為歌曲製作寬屏視覺畫面](https://x.com/ivy432hz/status/2122283590180589791) (作者 [@ivy432hz](https://x.com/ivy432hz))

**給模型一首歌與畫幅要求，觀察畫面運動如何傳遞歌曲的能量.**

創作者稱只給 Hydrogen XHigh 一首歌，要求 21:9 畫幅和速度感. 影片展示高速移動的道路場景，來源未說明渲染流程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

類型: Demo | 日期: 2026-11-16

---

<a id="case-224"></a>
### 案例 224: [兩段年代愛情短片的連續性](https://x.com/AvaSinclairAi_/status/2122315627113107670) (作者 [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**讓第二段短片延續第一段時，明確要保留哪些細節.**

創作者將遠洋客輪上的愛情場景歸功於使用 Hydrogen 的 Gemini 工作流，公開了要求保持角色與服裝連續的兩段簡報. 底層影片模型未說明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

類型: Demo | 日期: 2026-11-16

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

<a id="case-60"></a>
### 案例 60: [Box Agent 處理複雜企業文件](https://x.com/levie/status/2120947988143198302) (作者 [@levie](https://x.com/levie))

**在接近真實的文件任務中同時檢查準確率、耗時和 Token 用量.**

Box 報告，在早期試用評估的典型任務中，相比 Gemini 3.8 Flash，Hydrogen 準確率提高五個百分點、耗時不到一半、Token 約少 12%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-74"></a>
### 案例 74: [從 Workspace 資料生成圖表和報告](https://x.com/nin222/status/2120989168247652674) (作者 [@nin222](https://x.com/nin222))

**檢查追問一輪能否補齊分析、圖表或報告.**

創作者在 Google Workspace for Education Fundamentals 演示環境中用 Hydrogen 分析資料、生成圖表並輸出報告檔案，稱共進行了兩輪交流.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-12

---

<a id="case-81"></a>
### 案例 81: [用不同 Gemini 模式在表格裡畫畫素畫](https://x.com/kkitase/status/2121041283640926401) (作者 [@kkitase](https://x.com/kkitase))

**用同一個 Google 表格繪圖任務比較不同模型選項.**

創作者錄製 Hydrogen 在 Google 表格中繪製畫素畫的過程，並附上 Antigravity Orchestrator、Carbon 和 Argon 的獨立執行. 該創作者演示未採用正式評分標準.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-148"></a>
### 案例 148: [可互動的 FAA 地面停飛地圖](https://x.com/SidraMiconi/status/2121486870341370204) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**用時間線和地圖展示停飛解除後佇列為何仍存在.**

創作者報告用 Hydrogen 在 222 秒內製作了可操作的 FAA 執行中斷地圖，並糾正一處標籤. 時間線依據官方通報，交通流量則按常規時刻表模擬.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-184"></a>
### 案例 184: [用 Chrome 整理結構化 YouTube 摘要](https://x.com/studio_yebisu/status/2121835594674561098) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**請 Chrome 的 Gemini 面板提供帶時間戳的影片摘要和有來源的背景資料.**

日語原帖演示如何在 Chrome 的 Gemini 面板總結當前開啟的 YouTube 影片. 公開提示詞要求簡述、要點、各段落的脈絡、單獨註明出處的背景、事實核查與延伸資料.

**提示詞:**

```
今開いている動画の内容を、初めて見る人にも分かるように要約してください。

# 出力の構成
1. **ひとことで**：この動画が何を伝えているかを1〜2文で。
2. **要点**：重要なポイントを5〜8個の箇条書きで。可能ならタイムスタンプ（例 03:12）を付ける。
3. **詳しい流れ**：話の展開を章ごとに整理。専門用語は初出時にかみ砕いて説明する。
4. **関連情報**：動画内で触れられた人物・製品・研究・出来事について、背景知識や最新の関連情報をWebから補足する。動画内の情報と外部情報ははっきり区別し、外部情報には出典URLを付ける。
5. **注意点**：動画の主張で事実と異なる・古い・議論がある部分があれば指摘する。
6. **さらに知りたい人へ**：次に読む・見るとよいリソースを3つ。

# ルール
- 日本語で、中学生にも伝わる平易な言葉で書く。
- 推測で埋めず、動画で言っていないことは「動画内では言及なし」と書く。
- 数字・固有名詞は正確に残す。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-poster-1c98bb7de426.jpg" alt="Case 184 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

類型: Tutorial | 日期: 2026-11-15

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

<a id="case-41"></a>
### 案例 41: [把太空參考圖做成 HTML 場景](https://x.com/Inmerson/status/2120482539907559651) (作者 [@Inmerson](https://x.com/Inmerson))

**用少量參考圖檢驗生成場景能否呈現可辨識的視覺風格.**

創作者將太空視覺化歸功於 Hydrogen，展示了輸入的行星圖片和帶有行星環的 HTML 場景.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-11

---

<a id="case-42"></a>
### 案例 42: [Gemini Canvas 中的F1 賽車原型](https://x.com/auricxofficial/status/2120843585914605830) (作者 [@auricxofficial](https://x.com/auricxofficial))

**給車輛檢視介面設定幾個鏡頭，從不同角度檢查生成模型.**

創作者將一款F1 賽車檢視器歸功於首次使用 Canvas 中的 Hydrogen. 螢幕錄影顯示多個預設鏡頭和懸吊系統檢視.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-48"></a>
### 案例 48: [用 SVG 繪製BMW側視圖](https://x.com/HarshithLucky3/status/2120932649938382894) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**用車輛 SVG 側視圖檢查比例、輪廓和細節.**

作者展示一張BMW M4 CS 的 SVG 側視圖，歸因於 Gemini App 中的 Hydrogen High，並報告生成不到 30 秒.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-12

---

<a id="case-49"></a>
### 案例 49: [天文學家的浮空島](https://x.com/pankajkumar_dev/status/2120933196221333791) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**給小場景設定明確主題，再檢查物件和光照能否強化主題.**

創作者把天文學家浮空島歸因於 Arena 上的 Hydrogen 檢查點，並報告生成用時四分鐘. 歸因限於此次 Arena 執行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-50"></a>
### 案例 50: [把參考圖做成可探索的 3D 地形](https://x.com/HarshithLucky3/status/2120935535422374055) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**檢查圖生場景能否同時還原視覺元素並支援移動.**

創作者展示 Gemini 應用中歸因於 Hydrogen 的可操作 3D 地形，並介紹了 GLSL 反射、程式化幾何和游泳物理.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-51"></a>
### 案例 51: [用 3D 積木建構微縮景觀](https://x.com/abhinavflac/status/2120936501961969990) (作者 [@abhinavflac](https://x.com/abhinavflac))

**讓模型建構積木微縮景觀，檢查各形體能否組成完整場景.**

創作者分享了 3D 積木微縮景觀的螢幕錄影，並將其歸功於 Hydrogen. 來源未披露建構耗時和具體執行設定.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-52"></a>
### 案例 52: [可互動的櫻花樹](https://x.com/hakmgpt/status/2120936640436642231) (作者 [@hakmgpt](https://x.com/hakmgpt))

**用一件帶動效的物體和幾個控制元件探索微縮場景的即時變化.**

創作者將截圖中的櫻花樹介面歸功於 Hydrogen. 截圖可見場景設定控制元件，實現細節未公開.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-12

---

<a id="case-62"></a>
### 案例 62: [小型互動動畫中的光線折射](https://x.com/chanelluuh/status/2120951519470399710) (作者 [@chanelluuh](https://x.com/chanelluuh))

**先快速預覽並調整光學效果，再增加場景複雜度.**

創作者將 Small Delights 系列的一段互動小動畫歸功於 Hydrogen，特地展示折射效果，並介紹了逐步迭代的創作過程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-63"></a>
### 案例 63: [一條向上流的河](https://x.com/xKaka1456/status/2120952404225265983) (作者 [@xKaka1456](https://x.com/xKaka1456))

**選擇運動方向不同尋常的小場景，觀察視覺效果.**

作者報告在網頁端用 Hydrogen 做出倒流河流並分享螢幕錄影. 耗時和訂閱額度用量為作者自己的觀察.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

類型: Demo | 日期: 2026-11-12

---

<a id="case-67"></a>
### 案例 67: [Hydrogen 生成的 3D 肖像](https://x.com/soyamiruku/status/2120959893943251322) (作者 [@soyamiruku](https://x.com/soyamiruku))

**用肖像做小型測試，檢查 3D 表現能否保留可辨識的主體特徵.**

作者把為原帖所提人物製作的 3D 肖像歸因於 Hydrogen，並分享了結果圖. 來源提供的執行細節有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

類型: Demo | 日期: 2026-11-12

---

<a id="case-82"></a>
### 案例 82: [把參考圖中的公寓做成 3D 列印件](https://x.com/bijanbowen/status/2121042010928709932) (作者 [@bijanbowen](https://x.com/bijanbowen))

**把圖生 3D 的測試延伸到列印實物.**

作者分享《宋飛正傳》公寓的參考圖和列印實物，將該公寓模型歸因於 Hydrogen.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-1-url-c8d62f93f433.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-1-url-c8d62f93f433.jpg" alt="Case 82 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-2-url-e864ca91b00a.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-2-url-e864ca91b00a.png" alt="Case 82 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Demo | 日期: 2026-11-13

---

<a id="case-86"></a>
### 案例 86: [黃金梅麗號海上場景](https://x.com/xKaka1456/status/2121063351136739388) (作者 [@xKaka1456](https://x.com/xKaka1456))

**用辨識度高的虛構船隻測試風格化海景的構圖.**

創作者將黃金梅麗號場景歸功於 Hydrogen，並分享了船在藍色海面上的影片. 原帖未說明提示詞、工具設定和反覆調整的次數.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-88"></a>
### 案例 88: [遊過雲海的鯨魚](https://x.com/xKaka1456/status/2121100318150898144) (作者 [@xKaka1456](https://x.com/xKaka1456))

**透過一個程式碼製作的生物場景分別檢查流體運動和眼睛設計.**

來源展示了程式碼製作的雲海鯨魚，報告 Hydrogen 用時約兩分鐘. 速度和配額用量來自作者觀察.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-92"></a>
### 案例 92: [Gemini Canvas 裡的海底城市](https://x.com/ayyh_18/status/2121128385690693821) (作者 [@ayyh_18](https://x.com/ayyh_18))

**從小型 3D 場景起步，透過多輪迭代加入可探索的區域和會動的生物.**

創作者在 Gemini 應用內多輪迭代，建構了有魚群、水母、珊瑚和可探索玻璃穹頂的海底城市. 來源明確提到使用多條提示詞.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-99"></a>
### 案例 99: [Three.js 灰階海盜船](https://x.com/parves075/status/2121172856889618528) (作者 [@parves075](https://x.com/parves075))

**將 Three.js 場景限定為灰階，檢查光照還能否突出幾何形狀.**

作者在 Antigravity 中用 Hydrogen 建構 Three.js 灰階海盜船，螢幕錄影用於展示光照和 3D 細節.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-101"></a>
### 案例 101: [CadXStudio 中的引數化檯燈](https://x.com/CadX_Studio/status/2121175785356853312) (作者 [@CadX_Studio](https://x.com/CadX_Studio))

**檢查 CAD 模型中的元件尺寸和可編輯性.**

工具提供方 CadXStudio 展示了瀏覽器內的檯燈模型，稱包含 35 個可編輯零件.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

類型: Integration | 日期: 2026-11-13

---

<a id="case-102"></a>
### 案例 102: [用 C++ 製作神社參道動畫](https://x.com/nehstrr3/status/2121184399245128137) (作者 [@nehstrr3](https://x.com/nehstrr3))

**用小型原生程式碼場景檢驗模型能否在沒有 Web 技術棧時寫出可執行動畫.**

創作者將穿過神社鳥居的參道動畫歸功於 Hydrogen Extra High，並稱由自編 C++ 實現.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-105"></a>
### 案例 105: [用 30 個模組建構城鎮場景](https://x.com/IamEmily2050/status/2121200010574598655) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**按模組分別提示模型，再檢查組裝後的整體效果.**

作者稱使用 Gemini App 中的 Hydrogen High，每個模組用一則提示詞，共製作 30 個模組.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-108"></a>
### 案例 108: [浮空島上的郵局](https://x.com/pankajkumar_dev/status/2121220537984954448) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**指定一種微縮建築，觀察材質和光照如何表現主題.**

作者請 Hydrogen 在浮空島上建構一座 3D 微縮郵局，分享螢幕錄影並指出其中的紋理、顏色和光照.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-110"></a>
### 案例 110: [錦鯉庭院裡的水與魚](https://x.com/SahilPanhotra/status/2121225566779023432) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**用有游魚的場景檢查水面反射與光照是否連貫.**

創作者展示 Hydrogen 在錦鯉庭院測試中的輸出，重點說明焦散、反射和游魚行為，並附上 Carbon 版本.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-112"></a>
### 案例 112: [Gemini 網頁端執行互動式 3D 場景](https://x.com/YxzRainy/status/2121232725185339869) (作者 [@YxzRainy](https://x.com/YxzRainy))

**在 Gemini 網頁端快速製作可互動光照和粒子效果.**

創作者展示 Hydrogen 在網頁端執行的 3D 場景，包含粒子、動態光照和即時控制元件.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-115"></a>
### 案例 115: [單 HTML 檔案裡的粉色 3D 場景](https://x.com/SahilPanhotra/status/2121254256288137484) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**嘗試無外部素材的 Three.js 場景，檢查構圖是否清晰.**

創作者將粉色場景歸功於 Hydrogen，稱僅在一個 HTML 檔案中使用純 Three.js，無外部素材. 連結中的錦鯉庭院是另一個專案.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-119"></a>
### 案例 119: [純程式碼製作的大爆炸模擬](https://x.com/ash_twtz/status/2121268140630000020) (作者 [@ash_twtz](https://x.com/ash_twtz))

**用短動畫快速構建視覺化解釋，再檢查科學表述.**

創作者把 15 秒大爆炸視覺化歸功於 Gemini App 中的 Hydrogen，稱完全用程式碼製作，未使用網頁訪問、紋理、外部素材或 3D 模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-120"></a>
### 案例 120: [帶裝配爆炸圖的直升機](https://x.com/LuminaBench/status/2121273297715277930) (作者 [@LuminaBench](https://x.com/LuminaBench))

**檢查 3D 原型能否把飛行控制與實用的零件檢視方式結合起來.**

創作者展示可操控的直升機及裝配和爆炸圖，將原型歸功於 Hydrogen Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-121"></a>
### 案例 121: [帶透視和線框檢視的 Hydrogen Express](https://x.com/LuminaBench/status/2121277060983234788) (作者 [@LuminaBench](https://x.com/LuminaBench))

**給可操控的 3D 原型加入多種檢查模式.**

創作者展示具有速度控制元件、爆炸圖、線框及透視模式的列車，並報告生成約用五分鐘.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-122"></a>
### 案例 122: [空中的補給站](https://x.com/doe_naps/status/2121279837512106168) (作者 [@doe_naps](https://x.com/doe_naps))

**給場景安排有辨識度的移動物體和光照狀態，讓變化在演示中清晰可見.**

創作者分享 Hydrogen 製作的空中補給站，包含復古飛車、旋轉渦輪和晝夜交替，報告一次生成完成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-129"></a>
### 案例 129: [單 HTML 檔案裡的水磨坊](https://x.com/NovaXCode/status/2121294356875509851) (作者 [@NovaXCode](https://x.com/NovaXCode))

**用帶醒目運動元素的小景觀檢查快速生成的 3D 原型.**

創作者稱 Hydrogen 用約 30 秒在一個 HTML 檔案裡建構水磨坊，並分享輸出螢幕錄影.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-132"></a>
### 案例 132: [用 Hydrogen Extra 建構 Blender 場景](https://x.com/SPAC89/status/2121302218347270625) (作者 [@SPAC89](https://x.com/SPAC89))

**增加視覺細節之前，先在 Blender 中檢查幾何與材質.**

作者展示歸因於 Hydrogen Extra 的 Blender 場景，並給出僅適用於該會話的訂閱額度估算.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-139"></a>
### 案例 139: [Hydrogen 製作的兩段粒子動畫](https://x.com/gwammyy/status/2121355401392189746) (作者 [@gwammyy](https://x.com/gwammyy))

**用不同粒子場景檢驗簡單特效中的形態和運動.**

創作者將兩段短粒子特效螢幕錄影歸功於 Hydrogen. 來源僅展示輸出，未記錄執行設定.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

類型: Demo | 日期: 2026-11-13

---

<a id="case-142"></a>
### 案例 142: [微縮世界的晝夜切換開關](https://x.com/vib3coded/status/2121398359395283027) (作者 [@vib3coded](https://x.com/vib3coded))

**用小型開關測試介面狀態切換時動作是否連貫.**

創作者展示由開關控制的晝夜過渡，報告本次製作花費 $0.21.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-143"></a>
### 案例 143: [用 65 個模組建構場景](https://x.com/IamEmily2050/status/2121400396002492781) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**隨著場景擴充套件，記錄生成耗時和整合工作量.**

創作者報告在 Gemini 應用中建構了 65 個模組，每個模組用一則提示詞，並分享結果螢幕錄影.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-149"></a>
### 案例 149: [微縮寶塔庭院](https://x.com/auricxofficial/status/2121498286926540970) (作者 [@auricxofficial](https://x.com/auricxofficial))

**檢查生成的微縮場景如何平衡建築和周邊綠化.**

創作者把積木風格寶塔和庭院的影片歸功於 Hydrogen. 影片展示了結果，實現細節未公開.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-153"></a>
### 案例 153: [二戰機場微縮景觀](https://x.com/doe_naps/status/2121508105947320688) (作者 [@doe_naps](https://x.com/doe_naps))

**給 3D 演示提供參考資料與機械運動要求，檢驗外觀之外的表現.**

創作者報告給 Hydrogen 參考資料和簡短任務說明，在一個 HTML 檔案中建構機場微縮景觀. 要求包括可動的飛機和坦克.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-167"></a>
### 案例 167: [程式化生成的知更鳥飛行動畫](https://x.com/LuminaBench/status/2121620820791562291) (作者 [@LuminaBench](https://x.com/LuminaBench))

**檢查生成飛行動畫中的翅膀和身體動作.**

創作者將知更鳥飛行動畫程式碼歸功於 Hydrogen，並在後續帖展示同一工作的獨立 Antigravity swarm 流程圖.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

類型: Demo | 日期: 2026-11-14

---

<a id="case-182"></a>
### 案例 182: [用單個 HTML 檔案繪製插圖](https://x.com/vamsibatchuk/status/2121788887823778297) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**測試程式碼能否在沒有外部素材的情況下重現參考視覺效果.**

DeepMind 員工展示一張單檔案插圖，稱制作過程無外部庫、影像生成器、Skill 或嵌入素材.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-1-url-1de77cd76ae3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-1-url-1de77cd76ae3.jpg" alt="Case 182 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-2-url-5e02ddf0aad5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-2-url-5e02ddf0aad5.jpg" alt="Case 182 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-3-url-3da151834158.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-3-url-3da151834158.jpg" alt="Case 182 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-4-url-3c008316ab34.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-4-url-3c008316ab34.jpg" alt="Case 182 source image 4" width="100%"></a>
</td>
</tr>
</table>

類型: Demo | 日期: 2026-11-15

---

<a id="case-186"></a>
### 案例 186: [從靜態場景製作海鸚動畫](https://x.com/vamsibatchuk/status/2121846407950639541) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**把現有 HTML 場景用作程式化動畫的第一影格.**

創作者讓 Hydrogen 在一個 HTML 檔案裡製作後續 50 幀，螢幕錄影展示海鸚拿走角色帽子.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-200"></a>
### 案例 200: [用一則提示詞建構 3D 微縮島](https://x.com/CodeByPoonam/status/2121952483132289270) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**檢查一次生成的場景能否清楚安排地標、地形與水域.**

創作者稱由 Hydrogen 按一則提示詞建構微縮島. 畫面可見建築和其他地標.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-208"></a>
### 案例 208: [奇點主題的互動面板](https://x.com/Moleh1ll/status/2122032596263776351) (作者 [@Moleh1ll](https://x.com/Moleh1ll))

**圍繞一個視覺概念製作簡短的互動片段.**

創作者將奇點主題的互動面板歸功於 Hydrogen. 螢幕錄影展示結果，實現細節有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

類型: Demo | 日期: 2026-11-15

---

<a id="case-225"></a>
### 案例 225: [Gemini App 中的水球](https://x.com/Google/status/2122366286659289502) (作者 [@Google](https://x.com/Google))

**用簡單光學場景觀察高光與折射的關係.**

Google 分享 Gemini App 中的一張擬水球體圖，球上有 Hydrogen 字樣，並將成果歸於 Hydrogen. 來源展示輸出，未說明底層渲染方式.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

類型: Demo | 日期: 2026-11-16

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

<a id="case-43"></a>
### 案例 43: [Hydrogen API 與 Carbon Antigravity 輸出](https://x.com/huang18825/status/2120876396264444314) (作者 [@huang18825](https://x.com/huang18825))

**用同一提示詞比較視覺效果時，記錄各自的執行環境.**

創作者透過 API 執行 Hydrogen、透過 Antigravity 執行 Carbon，並並排展示兩份輸出. 文中報告的 4 分 47 秒對應此次 Hydrogen 執行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-44"></a>
### 案例 44: [Hydrogen 與 Astra 的陰影細節對比](https://x.com/SPAC89/status/2120911537296515321) (作者 [@SPAC89](https://x.com/SPAC89))

**比較兩次執行的費用和耗時，同時檢查渲染細節.**

創作者更喜歡帶陰影的 Hydrogen 版本，並報告它在該測試環境下更快完成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-45"></a>
### 案例 45: [程式化 3D 動效對比](https://x.com/SPAC89/status/2120923185981915156) (作者 [@SPAC89](https://x.com/SPAC89))

**比較程式化動效的連貫性與構圖時，記錄生成耗時.**

創作者展示了歸因於 Hydrogen High 的條紋 3D 形體，報告製作耗時不到五分鐘，並與自己試用的更高價模型對照.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-46"></a>
### 案例 46: [歷時 89 分鐘的 PokéBench 視覺測試](https://x.com/StatsWire/status/2120923685296988296) (作者 [@StatsWire](https://x.com/StatsWire))

**測試長時視覺代理時，同時記錄任務完成情況、回合數和 API 失敗次數.**

來源報告，發布前透過 Vertex 以 High 等級執行時，Hydrogen 用 365 回合、89 分鐘闖過小剛關卡，期間 API 呼叫失敗數為零. 結果對應來源所用的測試環境.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-47"></a>
### 案例 47: [Hydrogen 與 DeepSeek 建構同一個 3D 場景](https://x.com/AiHubMix/status/2120928687537418581) (作者 [@AiHubMix](https://x.com/AiHubMix))

**對照視覺輸出並分別記錄耗時和 API 費用.**

AIHubMix 用同一個 3D 場景提示詞比較兩個模型，各用最高可用推理等級. 服務商報告 Hydrogen 用時 3 分鐘、花費 $1.30，DeepSeek V4.1 Flash 用時 100 分鐘、花費 $0.90.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-53"></a>
### 案例 53: [Agent Arena 的單任務耗時和成本](https://x.com/arena/status/2120940869889175840) (作者 [@arena](https://x.com/arena))

**檢視整體成功率時，也比較單任務延遲、費用和輸出 Token 數.**

Agent Arena 報告 Hydrogen High 在其評估中的單任務中位耗時為 5.3 分鐘，中位費用為 $1.60，輸出 Token 多於 Carbon 和 Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-54"></a>
### 案例 54: [視覺文件和終端基準測試](https://x.com/ArtificialAnlys/status/2120941511223185722) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**分別檢視文件與終端測試結果，再決定推理預算.**

Artificial Analysis 報告視覺文件表現較強，終端專案的增益不一. Extra 推理提高了科學終端得分，通用 Terminal-Bench 得分仍為 54%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-55"></a>
### 案例 55: [Vals 指數和 Tax Agent 成績](https://x.com/ValsAI/status/2120943893894303808) (作者 [@ValsAI](https://x.com/ValsAI))

**結合整體評估和專業任務分數來判斷模型是否適用.**

Vals AI 報告，Hydrogen 的綜合指數為 68.5%，在測試時的 Tax Agent 專案中排名第一.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-56"></a>
### 案例 56: [CursorBench 的 Hydrogen 預設推理等級](https://x.com/cursor_ai/status/2120944639633211619) (作者 [@cursor_ai](https://x.com/cursor_ai))

**先檢視預設推理等級的基準成績，再到自己的倉庫裡測試.**

Cursor 報告，在自家 CursorBench 中，預設推理等級的 Hydrogen 得分為 54.3%，Gemini 3.8 Flash 為 39.6%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-57"></a>
### 案例 57: [四款模型製作弓箭手戰鬥動畫](https://x.com/IndependentEco/status/2120945011277590733) (作者 [@IndependentEco](https://x.com/IndependentEco))

**比較各個動畫能否清楚表現角色的戰鬥動作.**

創作者在同一影片中並排展示 Hydrogen、Fable 5.2、GPT-6.1 Sol 和 Carbon 的弓箭手戰鬥動畫.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-61"></a>
### 案例 61: [Hydrogen 的 Devin FrontierCode 結果](https://x.com/cognition/status/2120950876248641588) (作者 [@cognition](https://x.com/cognition))

**比較候選補丁能否合併，並記錄各自使用的代理環境.**

Cognition 報告 Hydrogen 在 FrontierCode 2.0 得分為 38.2%. 該模型的測試環境與對照模型使用的 Devin CLI 設定不同.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-64"></a>
### 案例 64: [禁止聯網後仍觸發搜尋](https://x.com/amanunreal/status/2120954045615768054) (作者 [@amanunreal](https://x.com/amanunreal))

**流程要求離線作答時，檢查模型是否真的沒有呼叫工具.**

作者報告，儘管提示詞要求避開搜尋和工具呼叫，Hydrogen 仍然搜尋了網頁. 原帖展示一次具體情況，未統計發生頻率.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-12

---

<a id="case-65"></a>
### 案例 65: [記錄 Antigravity Swarm 的配額用量](https://x.com/HarshithLucky3/status/2120954399971487774) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**測試多代理執行時記錄 Token 量和消耗的額度.**

創作者報告，在自己的套餐下使用 Swarm 時用了 1700 萬 Token，消耗了五小時額度的 21%. 數字對應此次會話.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-1-url-a6fefd498713.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-1-url-a6fefd498713.png" alt="Case 65 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-2-url-b4f5e4dfa2e9.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-2-url-b4f5e4dfa2e9.png" alt="Case 65 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-66"></a>
### 案例 66: [專業任務評估中的工具呼叫](https://x.com/mercor/status/2120957582139642095) (作者 [@mercor](https://x.com/mercor))

**觀察代理在執行專業任務前如何收集背景資訊.**

Mercor 報告，Hydrogen 在 APEX-Agents 中達到 78.0% Pass@1，平均每項任務呼叫工具 93 次. 評估涉及法律、諮詢和銀行業務.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-68"></a>
### 案例 68: [四款模型製作法師鬥龍動畫](https://x.com/IndependentEco/status/2120964690906161461) (作者 [@IndependentEco](https://x.com/IndependentEco))

**比較同一奇幻場景各版本的排程、動作清晰度和特效.**

對比影片展示 Hydrogen 和三款 Claude 模型生成的法師鬥龍場景. 創作者在這次對照中更偏好 Claude 的輸出.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-71"></a>
### 案例 71: [MazeBench 中的低成功率](https://x.com/patience_cave/status/2120973681937809766) (作者 [@patience_cave](https://x.com/patience_cave))

**用迷宮任務檢驗空間推理，再決定能否依賴它.**

公佈的 MazeBench 對比在其設定下測得 Hydrogen 1%、Sonnet 5.5 4%、GPT-6.1 Terra 8%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-72"></a>
### 案例 72: [三款 Gemini 模型建構帆船場景](https://x.com/Octoberry/status/2120974412144902376) (作者 [@Octoberry](https://x.com/Octoberry))

**在主題化 Three.js 場景中比較運動效果和環境細節.**

創作者展示 Hydrogen、Argon 和 Carbon 的帆船輸出，更喜歡 Carbon 的細節，並認為這次測試中 Hydrogen 接近 Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-75"></a>
### 案例 75: [識別球衣號碼時耗盡推理預算](https://x.com/skalskip92/status/2120994631072776235) (作者 [@skalskip92](https://x.com/skalskip92))

**識別圖片中的小細節時，設定推理上限並準備替代方案.**

評估者報告，Hydrogen XHigh 用了 131,069 個推理 Token，執行 9 分 55 秒仍未給出球衣號碼.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-12

---

<a id="case-76"></a>
### 案例 76: [不同模型系列的 ClutterBench 表現](https://x.com/AdamHoltererer/status/2121000759118459138) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**用專門的雜亂場景基準檢驗模型的通用優勢是否適用於這一任務.**

作者分享 ClutterBench 成績. Hydrogen 在圖中列出的 Gemini 模型裡領先，落後於參與對照的 OpenAI 模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-12

---

<a id="case-78"></a>
### 案例 78: [Minecraft 風格人體解剖剖面像](https://x.com/jan_volad/status/2121026531472339340) (作者 [@jan_volad](https://x.com/jan_volad))

**檢查生成的剖面是否包含指定的內部結構.**

創作者讓 Hydrogen 和 Argon 各用一次請求製作 Minecraft 風格解剖胸像，並報告在 Hydrogen 輸出中看到頭骨、肋骨和脊柱.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-79"></a>
### 案例 79: [三款模型渲染同一件道具](https://x.com/luckeyfaraday/status/2121030005899825504) (作者 [@luckeyfaraday](https://x.com/luckeyfaraday))

**同時記錄質量和 Token 用量，檢查單價較低的模型是否在該任務中消耗更多 Token.**

來源對比 Hydrogen、Carbon 和 Fable 5.2 渲染同一個步槍形道具. 創作者報告 Hydrogen 使用 369 萬 Token、花費 $1.62，Carbon 使用 39.8 萬 Token、花費 $0.77.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

類型: Evaluation | 日期: 2026-11-12

---

<a id="case-80"></a>
### 案例 80: [歸納基準測試與 Token 消耗](https://x.com/s_batzoglou/status/2121037853258129811) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**評估高難度推理時，將計費輸入和輸出用量與成績一起記錄.**

評估者報告，Hydrogen 在其 100 道題的歸納基準中列第四，接近 Opus 5.5. 作者記錄了 5500 萬輸出 Token 和 3.07 億計費輸入 Token，計費機制仍待解釋.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-83"></a>
### 案例 83: [三款模型製作 3D 動物動畫](https://x.com/leo114119/status/2121054098753785915) (作者 [@leo114119](https://x.com/leo114119))

**在同一項 3D 動物建模任務中檢查身體結構和運動.**

來源對比 Hydrogen、GPT-6.1 Terra 和 Claude Haiku 5.5. 創作者指出 Hydrogen 輸出的不足；觀察結果僅對應這項任務.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-84"></a>
### 案例 84: [Hydrogen 與 Qwen 的 ts-bench 測試](https://x.com/gosrum/status/2121058334552060102) (作者 [@gosrum](https://x.com/gosrum))

**將工具呼叫錯誤和整體基準成績一起檢視.**

來源在 ts-bench 上對比 Hydrogen 和 Qwen4 Max Preview，並討論了這幾次執行的工具呼叫可靠性. 截圖保留了當次評估結果.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-85"></a>
### 案例 85: [Vending-Bench 商業模擬](https://x.com/andonlabs/status/2121061429889642497) (作者 [@andonlabs](https://x.com/andonlabs))

**比較模擬收入時同時計入代理執行成本.**

Andon Labs 報告，Hydrogen 在 Vending-Bench 2 中排名第三，在其模擬中賺取的收入高於同價位模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-89"></a>
### 案例 89: [四款模型建構微縮島嶼](https://x.com/xKaka1456/status/2121111495358697924) (作者 [@xKaka1456](https://x.com/xKaka1456))

**比較島嶼設計時，一併記錄各個環境的耗時和費用.**

來源對比四種微縮島，報告 Hydrogen 用時 4 分鐘，GPT-6.1 Terra 20 分鐘，Sol 40 分鐘，DeepSeek 60 分鐘. 作者所稱 Hydrogen 零額外收費與其設定有關.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-91"></a>
### 案例 91: [用程式碼模擬布料撕裂](https://x.com/MichaelLee009/status/2121126779276402904) (作者 [@MichaelLee009](https://x.com/MichaelLee009))

**用同一動畫任務檢查布料拉伸、撕裂及與毛髮的相互作用.**

創作者對比 Hydrogen 和 Claude Fable 5.2 的程式碼生成動畫，認為後者視覺表現更佳. 來源未給出統一執行設定或獨立物理驗證.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-94"></a>
### 案例 94: [事實核查缺少可追溯來源](https://x.com/cagrimbakirci/status/2121130756684886279) (作者 [@cagrimbakirci](https://x.com/cagrimbakirci))

**依據模型對截圖的判斷行動之前，要求給出可查驗的引用.**

作者請 Hydrogen 核實一張帖文截圖，稱模型確認內容、反覆開啟核查工具，但始終未給出原始來源.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-13

---

<a id="case-96"></a>
### 案例 96: [Hydrogen 與 Sol 繪製 2D 鵜鶘](https://x.com/YxzRainy/status/2121148582166491164) (作者 [@YxzRainy](https://x.com/YxzRainy))

**用同一項簡單 2D 動畫任務對比耗時與動作表現.**

作者在影片中展示 Hydrogen 和 GPT-6.1 Sol 的 2D 鵜鶘騎車結果，報告分別用時 28 秒和 6 分 51 秒. 兩次執行的設定是否一致尚未證實.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-98"></a>
### 案例 98: [四款模型建構蛛絲擺盪遊戲](https://x.com/StatsWire/status/2121172215182065807) (作者 [@StatsWire](https://x.com/StatsWire))

**統一使用單檔案限制，比較各款遊戲的移動和操作.**

來源展示四款 Gemini 模型製作同一項 3D 蛛絲擺盪挑戰，限定單個 HTML 檔案且無外部素材. Hydrogen 使用 Extra High，其餘 Gemini 3.8 Flash、Argon 和 Carbon 使用 High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-100"></a>
### 案例 100: [四款模型渲染建築微縮景觀](https://x.com/Jackson77li/status/2121172890838352306) (作者 [@Jackson77li](https://x.com/Jackson77li))

**用統一的建築任務比較輸出，檢視各模型如何打光.**

創作者稱使用同一提示詞，對照 Hydrogen、GPT-6.2、Claude Fable 5.2 和 DeepSeek 的建築微縮景觀. 排名和速度評價均屬作者感受.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-103"></a>
### 案例 103: [三款模型渲染列車場景](https://x.com/xKaka1456/status/2121193705810104515) (作者 [@xKaka1456](https://x.com/xKaka1456))

**用同一列車場景任務比較各自配置下的完成速度.**

創作者報告 Hydrogen 用時約 3 分鐘、GPT-6.1 Terra 20 分鐘、Qwen4 Max Preview 68 分鐘. 影片展示渲染結果，來源未說明設定和反覆調整的次數.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-104"></a>
### 案例 104: [用 Extra 等級製作雨夜唐人街](https://x.com/qingzhoucloud/status/2121198911515967952) (作者 [@qingzhoucloud](https://x.com/qingzhoucloud))

**給大型動畫選擇推理等級前，記錄實際耗時並檢查最終畫面.**

作者用 Hydrogen Extra 執行另一創作者提供的提示詞，報告雨夜唐人街 MP4 用時近四小時，並與另一次 Claude Fable 5.2 執行比較. 兩次設定的可比性有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-106"></a>
### 案例 106: [三款模型建構行星視覺化介面](https://x.com/Stargridcompass/status/2121208957276713181) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**用同一提示詞比較不同模型製作的科學視覺化介面.**

螢幕錄影對比 Claude Fable 5.2、GPT-6.2 Sol 與 Hydrogen 的行星主題輸出. 排序是作者的視覺判斷，來源未證實統一設定，也沒有客觀評分.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-107"></a>
### 案例 107: [四款模型復刻 Chrome 小恐龍](https://x.com/noclipepe/status/2121219775170761044) (作者 [@noclipepe](https://x.com/noclipepe))

**為每次遊戲復刻計時，並比較可玩結果.**

創作者報告，AI Studio 中的 Hydrogen 用時 18 分 41 秒，Fable 5.2 用時 45 分 30 秒. 螢幕錄影也展示 Qwen4-Max-Preview 和 Carbon 及畫面評分.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-109"></a>
### 案例 109: [兩款程式開發代理分別造船](https://x.com/marcthecreatorr/status/2121221667619852660) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**在實際使用的工具中比較首個可用結果和返工成本.**

作者以同一提示詞在 Claude Code 中執行 Sonnet，在 Cursor 中執行 Hydrogen. 作者報告 Hydrogen 更快完成，但需要第二版.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-111"></a>
### 案例 111: [四款模型製作剛體投石機攻城原型](https://x.com/StatsWire/status/2121226579141386285) (作者 [@StatsWire](https://x.com/StatsWire))

**用同一任務比較可玩的物理原型，並記錄推理等級.**

創作者讓四款 Gemini 模型建構含數百塊石塊的投石機場景. 報告 Hydrogen Extra High 用時 10 分 3 秒，Carbon High 為 23 分 33 秒，Gemini 3.8 Flash High 最快.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-116"></a>
### 案例 116: [FrontierMemory 的長期記憶測試](https://x.com/Letta_AI/status/2121255895745351874) (作者 [@Letta_AI](https://x.com/Letta_AI))

**為長期代理記憶選模型時，結合評分和單次費用.**

Letta 報告 Hydrogen 在 FrontierMemory 中獲得 64.4%，與 Argon 持平，每次記憶執行約 $100. 在該基準配置下，Carbon 為 71.1%，每次約 $94.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-117"></a>
### 案例 117: [故意損壞的 LiveKit 語音代理](https://x.com/livekit/status/2121256982023672076) (作者 [@livekit](https://x.com/livekit))

**引入可控的工具故障，檢查語音代理會不會報告無依據的結果.**

LiveKit 在故意損壞的語音代理裡測試 Hydrogen，報告虛假結果為零. 服務商將其與 Gemini 3.8 Flash 對照，並附文字記錄.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-123"></a>
### 案例 123: [三款 Gemini 模型製作騎行者動畫](https://x.com/AI_Screening/status/2121281026916057443) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用統一簡報比較短動畫，並記錄各次執行的耗時.**

創作者展示 Carbon、Argon 與 Hydrogen 的騎行者動畫，報告 Hydrogen 約 90 秒、Argon 超過五分鐘，畫面更偏好 Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-126"></a>
### 案例 126: [兩款模型建構 LEGO 世界](https://x.com/kepochnik/status/2121286219669836027) (作者 [@kepochnik](https://x.com/kepochnik))

**結合耗時比較各模型建構了多少主題場景.**

創作者展示 Fable 5.2 和 Hydrogen 的 LEGO 世界版本，分別報告用時 44 和 28 分鐘. 結果對應作者自己的執行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-127"></a>
### 案例 127: [修復兩個倉庫裡重新植入的缺陷](https://x.com/PawelHuryn/status/2121286545223086302) (作者 [@PawelHuryn](https://x.com/PawelHuryn))

**植入已知缺陷，測量程式開發代理能找出並修復哪些問題.**

評估者在兩個倉庫中植入 105 個缺陷. 在其設定下，Extra High 的 Hydrogen 略落後於同為 Extra High 的 Sonnet 5.5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-128"></a>
### 案例 128: [兩款模型製作火柴人對戰游標](https://x.com/DanielZambrini/status/2121289822677483740) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**比較兩份互動動畫如何響應滑鼠指標.**

創作者更喜歡 Fable 的火柴人對戰游標版本，並認為 Hydrogen 足以用於更低成本的一輪生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-130"></a>
### 案例 130: [兩款模型渲染山地景觀](https://x.com/ZryMiller/status/2121295750122594440) (作者 [@ZryMiller](https://x.com/ZryMiller))

**在同一類景觀動畫中分別比較構圖、生成耗時和費用.**

創作者分享 Hydrogen 與 Opus 5.5 的山景動畫，報告前者用時 20 分 30 秒、花費 $0.50，後者 11 分 23 秒、花費 $2.50.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-131"></a>
### 案例 131: [用自定義環境做英譯波斯語評估](https://x.com/MatinSenPai/status/2121296733258887365) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**用人工參考譯文給高難度翻譯段落打分.**

作者在自定義評估環境下做個人翻譯測試，給 Hydrogen 94 分，滿分 100. 主觀分數取決於這套設定.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-133"></a>
### 案例 133: [四款模型建構沉船場景](https://x.com/remoteugur/status/2121302956741902451) (作者 [@remoteugur](https://x.com/remoteugur))

**用同一場景分別記錄視覺還原、生成時間與成本.**

創作者報告 Hydrogen 用時 8.6 分鐘、花費 $1.16，Gemini 3.8 Flash 用時 10.8 分鐘、花費 $1.06. 還測試了 Carbon 和 Opus 5.5，更偏好 Opus 的真實感.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-135"></a>
### 案例 135: [四款模型的文案盲測](https://x.com/quintanilha/status/2121315967447757299) (作者 [@quintanilha](https://x.com/quintanilha))

**在選用文案之前，隱去模型名稱再評判.**

創作者報告對四款模型進行文案盲測，更偏好 Hydrogen 的輸出，並在這次測試中發現它比 Carbon 更快、成本更低.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-136"></a>
### 案例 136: [不同推理等級的視覺檢測與讀字](https://x.com/skalskip92/status/2121322414453694489) (作者 [@skalskip92](https://x.com/skalskip92))

**在各個推理等級分別測量檢測準確率、文字識別準確率、費用與延遲.**

評估者分別報告 Hydrogen、Argon 和 Carbon 的檢測和文字識別分數. Hydrogen High 在此次測試中平均每張圖 29.3 秒，檢測得 64.6 分、文字識別 87.2 分. Carbon High 兩項得分都更高，成本和延遲也更高.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-13

---

<a id="case-137"></a>
### 案例 137: [四款模型重建《飛屋環遊記》的房屋](https://x.com/noclipepe/status/2121326233044537688) (作者 [@noclipepe](https://x.com/noclipepe))

**用同一張參考圖和簡報比較 3D 製作的各項取捨.**

作者報告 Hydrogen 在四次執行中最快、最便宜，視覺上更喜歡 Fable. 設定和費用由來源報告.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

類型: Evaluation | 日期: 2026-11-13

---

<a id="case-144"></a>
### 案例 144: [固定鏡頭的舞蹈短片](https://x.com/notoro_ai/status/2121427503952834562) (作者 [@notoro_ai](https://x.com/notoro_ai))

**檢查參考圖動畫能否保留角色設計、構圖與鏡頭位置.**

作者分享日語提示詞及與 Google Gemini 中 Hydrogen 關聯的舞蹈影片. 提示詞要求固定鏡頭、保留參考風格，底層影片生成模型尚未確認.

**提示詞:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-145"></a>
### 案例 145: [程式開發代理卡在基線測試](https://x.com/Its_lakshya_ai/status/2121431788266659919) (作者 [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**給基線測試設定時限，並檢查進度再等待修復方案.**

創作者展示 Antigravity 中 Hydrogen 長時間仍在執行基線測試的會話. 截圖記錄了先停止排查、再繼續執行的請求.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-14

---

<a id="case-147"></a>
### 案例 147: [兩款模型建構互動機械臂](https://x.com/gmi_cloud/status/2121467337119588834) (作者 [@gmi_cloud](https://x.com/gmi_cloud))

**操作 Three.js 機械臂時，檢查各關節的動作是否連貫.**

GMI Cloud 提供 Hydrogen 與 Sonnet 5.5 在 Three.js 機械臂任務上的螢幕錄影. 本次對比中服務商更喜歡 Sonnet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-151"></a>
### 案例 151: [Hydrogen 與 Sol 建構雪中村莊](https://x.com/badboyfoxy/status/2121501015442669866) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**在程式設計對比中分別記錄耗時、費用和場景質量.**

創作者報告 Hydrogen High 用時三分鐘、花費 $1.37，Sol High 用時 15 分鐘、花費 $4.03. 創作者更喜歡 Sol 的雪村畫面.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-152"></a>
### 案例 152: [High 與 Ultra 檔製作 Three.js 島嶼](https://x.com/laopai1990/status/2121502334866096160) (作者 [@laopai1990](https://x.com/laopai1990))

**比較畫面和響應速度時，記錄推理等級並區分不同產品的額度.**

作者對比 Hydrogen High 和 GPT-6.1 Sol Ultra，分別報告 Three.js 島嶼耗時約 90 秒和 30 分鐘. 費用為估算，推理等級不同.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-157"></a>
### 案例 157: [對比 3D PS5 手柄細節](https://x.com/Stargridcompass/status/2121528563254043015) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**比較手柄模型時檢查按鈕陰影及背面硬體細節.**

創作者用 Hydrogen High 和 GPT-6.2 Sol 建模手柄. 來源報告分別約三分鐘和十一分鐘，作者認為 Sol 對背面及側面按鈕的還原更完整.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-159"></a>
### 案例 159: [CursorBench 中的推理預算對照](https://x.com/Beamsters1/status/2121538515909628111) (作者 [@Beamsters1](https://x.com/Beamsters1))

**選擇更快的預設檔前，比較不同推理配置下的成功率.**

作者報告，增加 Hydrogen 的推理預算時，CursorBench 4.0 成功率顯著上升. 結果對應測試配置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-14

---

<a id="case-160"></a>
### 案例 160: [三款模型渲染星核聖殿](https://x.com/YxzRainy/status/2121551796766376081) (作者 [@YxzRainy](https://x.com/YxzRainy))

**在 3D 任務中分別觀察渲染穩定性和畫面細節.**

創作者對比 Hydrogen、DeepSeek V4.1 1017 與 Qwen4 Max Preview 的星核主題場景，稱 Hydrogen 在本次測試中更快且未黑屏或閃爍，視覺細節則更少.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-162"></a>
### 案例 162: [挑戰現有的遷移方案](https://x.com/is_llll/status/2121565725072490559) (作者 [@is_llll](https://x.com/is_llll))

**讓程式開發代理評估遷移是否需要替換現有架構.**

作者展示一次設計審閱，Hydrogen 和 Argon 支援原有方案，Claude Opus 建議替換該方案並更早遷移. 這是單個專案的判斷.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-1-url-56675d463c82.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-1-url-56675d463c82.jpg" alt="Case 162 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-2-url-beda96ffecef.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-2-url-beda96ffecef.jpg" alt="Case 162 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Limit | 日期: 2026-11-14

---

<a id="case-165"></a>
### 案例 165: [兩款模型製作神廟逃脫遊戲](https://x.com/runable_hq/status/2121596515474964556) (作者 [@runable_hq](https://x.com/runable_hq))

**在同一遊戲概念中比較光照和氛圍是否便於看清場景.**

服務商 Runable 展示 Hydrogen 和 Argon 實現的神廟逃脫遊戲，描述前者的光照更有氛圍、後者的畫面更明亮.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-166"></a>
### 案例 166: [三款 Gemini 模型製作拉力車動畫](https://x.com/teddyaisi/status/2121604816380010719) (作者 [@teddyaisi](https://x.com/teddyaisi))

**檢查車輛透過帶傾角的彎道時，懸掛運動和輪胎抓地是否合理.**

創作者用 Carbon、Argon 與 Hydrogen 製作採石場裡的 Three.js 越野車動畫. 任務要求展示懸掛壓縮和在傾斜土路彎道上滑行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-169"></a>
### 案例 169: [兩款模型製作 Chasing Views 動畫](https://x.com/VulKan42069/status/2121625271493382166) (作者 [@VulKan42069](https://x.com/VulKan42069))

**比較輸出和耗時，同時記錄各自的推理等級.**

創作者展示 Hydrogen Extra High 與 Opus 5.5 High 的 Chasing Views 動畫，本次對比分別報告耗時 22 和 18 分鐘.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-170"></a>
### 案例 170: [Design Creativity Bench 的速度和費用](https://x.com/Kombaico/status/2121635837180031129) (作者 [@Kombaico](https://x.com/Kombaico))

**檢視創意評分時，一起比較單份設計的生成耗時與費用.**

基準運營方報告 Hydrogen 創意得分 49.4，每份設計中位耗時 3.4 分鐘、費用 $0.39. 在該評估中 Argon 較慢且較便宜，Carbon 較慢且較貴.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

類型: Benchmark | 日期: 2026-11-14

---

<a id="case-172"></a>
### 案例 172: [四款模型製作沙漠駿馬動畫](https://x.com/Marlenuii/status/2121664345818235177) (作者 [@Marlenuii](https://x.com/Marlenuii))

**先比較腳掌著地和重心轉移，再看打光和網格細節.**

創作者讓 Astra、Carbon、Fable 5.2 與 Hydrogen 製作沙漠奔馬場景. 作者偏好 Astra 的步態，指出 Hydrogen 的馬匹建模有缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-174"></a>
### 案例 174: [FrontierCS 2 計算機科學研究評估](https://x.com/wenhaocha1/status/2121679887400403308) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**在常規程式設計測試之外使用研究基準，並記錄執行環境.**

來源報告 Hydrogen 用 Antigravity 在 FrontierCS 2 按透過率排第七. 評估涵蓋計算機科學研究中的技術問題.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

類型: Benchmark | 日期: 2026-11-14

---

<a id="case-175"></a>
### 案例 175: [四款模型製作雲端里約](https://x.com/EnvolDev/status/2121701704139956250) (作者 [@EnvolDev](https://x.com/EnvolDev))

**用同一個創意簡報比較費用、耗時和主觀質量.**

評估者報告 Hydrogen Extra High 花費 $6.21，是他們最不喜歡的結果. 此次 Astra 用時較少，來源未確認原生影片生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-176"></a>
### 案例 176: [Hydrogen 在 GBENCH 技術任務中的表現](https://x.com/leo_linsky/status/2121710421891780864) (作者 [@leo_linsky](https://x.com/leo_linsky))

**評估技術工作時，把可核驗的程式設計與非程式設計結果和價格、耗時一起比較.**

評估方公佈 Hydrogen 的 GBENCH 結果. 非程式設計任務包括電路設計和抽象推理. 作者稱在其測量中，Sol 在相近價格與速度下更有競爭力.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-1-url-eb704fc94009.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-1-url-eb704fc94009.jpg" alt="Case 176 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-2-url-36e5f1c98a86.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-2-url-36e5f1c98a86.png" alt="Case 176 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-3-url-8ab372b95cb1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-3-url-8ab372b95cb1.jpg" alt="Case 176 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

類型: Benchmark | 日期: 2026-11-14

---

<a id="case-177"></a>
### 案例 177: [訓練車輛側方停車](https://x.com/noclipepe/status/2121734795738652934) (作者 [@noclipepe](https://x.com/noclipepe))

**比較生成模擬中的學習進展和最終成功率.**

使用同一任務說明，創作者報告 Hydrogen 為 44 輛車中 5 輛成功停車，Fable 5.2 為 40 輛中 26 輛. 兩次建構分別耗時 5.6 和 24 分鐘.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

類型: Evaluation | 日期: 2026-11-14

---

<a id="case-181"></a>
### 案例 181: [Hydrogen 在 Terminal-Bench 4.0 中的表現](https://x.com/gosrum/status/2121785156273160558) (作者 [@gosrum](https://x.com/gosrum))

**選命令列程式開發模型時，一起考慮基準完成率與任務費用.**

這項獨立的 Terminal-Bench 4.0 測試對照 Hydrogen、Claude Opus 5.5 和 GPT-6.1 Sol. 評估者報告成績相近、費用居兩者之間，並提醒執行環境的成熟度影響實際採用.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-1-url-cd8ea8d294e1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-1-url-cd8ea8d294e1.jpg" alt="Case 181 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-2-url-485667e4cf89.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-2-url-485667e4cf89.jpg" alt="Case 181 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Benchmark | 日期: 2026-11-15

---

<a id="case-183"></a>
### 案例 183: [三款 Gemini 模型製作章魚動畫](https://x.com/teddyaisi/status/2121800606406885880) (作者 [@teddyaisi](https://x.com/teddyaisi))

**觀察觸手抓住岩石後是否明顯帶動身體前進.**

創作者展示 Carbon、Argon 和 Hydrogen 在同一 Three.js 任務上的結果，其中章魚抓住礁石邊緣並向前拉動自己. 作者請讀者比較觸手與身體動作的連貫性.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-187"></a>
### 案例 187: [一項城堡建模測試](https://x.com/nemumusitocha/status/2121848375998063012) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**對比多次模型執行的城堡輸出和資源用量.**

創作者展示由 Hydrogen 生成的 3D 城堡，並連結往期模型的對照. 其報告的 Google AI Pro 每週額度 3% 僅對應本次執行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-2-url-7651a5296a9f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-2-url-7651a5296a9f.jpg" alt="Case 187 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-3-url-1d59eac2a5b7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-3-url-1d59eac2a5b7.jpg" alt="Case 187 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-4-url-00e8a6b2fc60.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-4-url-00e8a6b2fc60.jpg" alt="Case 187 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-191"></a>
### 案例 191: [新增範圍後項目估時大幅改變](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**交付時間發生大幅變化時，要求模型說明專案範圍與假設.**

創作者分享對話，要求更現實的工期和完整功能後，預計時間從一個月增加到一年. 對話裡沒有實際交付記錄.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-15

---

<a id="case-193"></a>
### 案例 193: [考慮閏年邊界的日曆問題](https://x.com/itsvishaltwt/status/2121891117050589249) (作者 [@itsvishaltwt](https://x.com/itsvishaltwt))

**提出簡單換算問題，檢查答案是否考慮日曆邊界情況.**

創作者詢問 Hydrogen High 和 GPT，一年有多少秒. 兩份截圖都列出平年與閏年的秒數，Hydrogen 也計算了公曆平均年的秒數.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-1-url-b2270fbaacb0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-1-url-b2270fbaacb0.jpg" alt="Case 193 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-2-url-cf9b4c45a1e3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-2-url-cf9b4c45a1e3.jpg" alt="Case 193 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-196"></a>
### 案例 196: [回答引用了過時的訂閱額度](https://x.com/take14262/status/2121934737539514533) (作者 [@take14262](https://x.com/take14262))

**評估研究助手時，對照一手來源核實計劃條款和模型名稱.**

作者展示 Hydrogen 混淆相似模型名，且給出過時的 Qwen 套餐額度週期. 截圖記錄了這幾處疑似引用錯誤.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-1-url-c51825192acc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-1-url-c51825192acc.png" alt="Case 196 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-2-url-ae838791b312.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-2-url-ae838791b312.png" alt="Case 196 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Limit | 日期: 2026-11-15

---

<a id="case-197"></a>
### 案例 197: [修改 WebGL 動畫的敘事](https://x.com/snakajima/status/2121939899242996058) (作者 [@snakajima](https://x.com/snakajima))

**首版技術效果豐富卻缺少清楚脈絡時，要求增強敘事.**

創作者附上 WebGL 初版，指出它嘈雜且缺少故事，再展示給出反饋後的第二版. 作者更喜歡修改版，對照中仍偏好 Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

類型: Limit | 日期: 2026-11-15

---

<a id="case-199"></a>
### 案例 199: [兩款模型用程式碼製作山間鬥龍](https://x.com/DrstaOne/status/2121947540509831302) (作者 [@DrstaOne](https://x.com/DrstaOne))

**比較同一場景中的兩方角色互動.**

創作者分享 Qwen-4 Max 和 Hydrogen 用程式碼製作的山寺上空鬥龍動畫，並註明提示詞由另一創作者提供.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-201"></a>
### 案例 201: [可複用的 Three.js 鵜鶘提示詞](https://x.com/Aki_LIG/status/2121960943361896596) (作者 [@Aki_LIG](https://x.com/Aki_LIG))

**檢查騎行動畫中腿、車輪和轉向能否同步.**

創作者公佈完整日語 Three.js 提示詞，錄製 Hydrogen 在海岸公路場景中的輸出，並稱曾將同一提示詞交給 GPT-6.1 Terra. 該螢幕錄影展示 Hydrogen 這次執行.

**提示詞:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-205"></a>
### 案例 205: [同一個小屋任務在三種環境中執行](https://x.com/doe_naps/status/2121999317628330476) (作者 [@doe_naps](https://x.com/doe_naps))

**把視覺任務遷移到不同模型檔和平臺時，檢查輸出格式.**

創作者報告，在 Antigravity 中使用 Hydrogen High 和 Carbon High、在 AI Studio 使用 Hydrogen Extra High 都得到靜態結果. Arena 標註為 Hydrogen 的一次執行生成了動畫 SVG，該檢查點身份未被獨立核實.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-2-url-61c8ea9c30fc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-2-url-61c8ea9c30fc.jpg" alt="Case 205 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-3-url-e52b66f1cf3f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-3-url-e52b66f1cf3f.jpg" alt="Case 205 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-4-url-c4376faa6be5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-4-url-c4376faa6be5.jpg" alt="Case 205 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-206"></a>
### 案例 206: [用同一提示詞對比儀表盤](https://x.com/fiapp_pro/status/2122014257667846338) (作者 [@fiapp_pro](https://x.com/fiapp_pro))

**用同一個前端提示詞比較介面佈局和資訊層次.**

作者並排釋出歸因於 GPT-6.1 Sol 與 Hydrogen 的網頁介面截圖. 截圖可供視覺對照，實現、設定和實際功能未說明.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-1-url-a5bc19cd8b96.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-1-url-a5bc19cd8b96.jpg" alt="Case 206 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-2-url-41c8d506d533.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-2-url-41c8d506d533.jpg" alt="Case 206 source image 2" width="100%"></a>
</td>
</tr>
</table>

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-209"></a>
### 案例 209: [兩款模型用程式碼製作橫版動畫](https://x.com/rubenssoto_ai/status/2122035198728814753) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**比較生成的動作場景時，關注動作連續性和製作費用.**

創作者對比 Hydrogen 與 GPT-6 Astra 的橫版卷軸動畫，偏好 Hydrogen 更自然的動作，並報告在兩次執行中 Hydrogen 費用更低.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

類型: Evaluation | 日期: 2026-11-15

---

<a id="case-212"></a>
### 案例 212: [日語回答裡的數學公式未渲染](https://x.com/ToraMutton/status/2122131489718759930) (作者 [@ToraMutton](https://x.com/ToraMutton))

**回答含 TeX 指令時，同時檢查內容和公式顯示.**

作者展示切換到 Hydrogen 後的一條日語 Gemini 回答，顯示原始數學符號而未排成公式. 截圖記錄了該介面的一次格式問題.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

類型: Limit | 日期: 2026-11-16

---

<a id="case-214"></a>
### 案例 214: [測試模型能否遵守保持沉默的指令](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**流程要求不回覆時，檢查模型能否真正不產生答覆.**

作者分享不回覆測試的截圖，報告與 Carbon 和 Argon 的行為不同. 原帖展示了一組測試.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

類型: Evaluation | 日期: 2026-11-16

---

<a id="case-216"></a>
### 案例 216: [三款模型解釋電動機原理](https://x.com/analogalok/status/2122221106304352257) (作者 [@analogalok](https://x.com/analogalok))

**在同一個模擬提示詞下，比較畫面清晰度與教學控制元件.**

創作者比較 Hydrogen 與兩款 Qwen 模型，更偏好 Hydrogen 的 3D 電動機和物理解釋. 判斷來自一次對照.

**提示詞:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

類型: Evaluation | 日期: 2026-11-16

---

<a id="case-217"></a>
### 案例 217: [兩種模型工作流製作桌面動畫](https://x.com/GeroXBT/status/2122234332102435128) (作者 [@GeroXBT](https://x.com/GeroXBT))

**對照原始任務檢查畫面細節、音量和片尾是否保持靜止.**

創作者以同一提示詞透過 API 對照 Hydrogen 與 Astra 輔助製作的桌面動畫，認為 Gemini 版本更流暢，片尾仍然在動且音量較低. 渲染流程未說明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

類型: Evaluation | 日期: 2026-11-16

---

<a id="case-221"></a>
### 案例 221: [帶程序式音效的 2D 村莊](https://x.com/marcthecreatorr/status/2122266495216459841) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**記錄建構耗時，並檢查聲音是否隨畫面中的事件變化.**

創作者用 Extra High 的 Hydrogen 與 Qwen 4 Max 建構 2D 村莊，報告 Qwen 約 75 分鐘、$0.90，Hydrogen 約 12 分鐘、$1.70. 作者更喜歡 Hydrogen 中音樂與事件的配合.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[播放來源影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

類型: Evaluation | 日期: 2026-11-16

---

<a id="related-repositories"></a>
## 相關儲存庫

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon 示例與對比

<a id="acknowledge"></a>
## 🙏 致謝

感謝公開分享 Hydrogen 作品的創作者、開發者和評測者

**來源創作者:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*署名依據所引用的公開來源，未必能夠識別最早的創作者；如需更正或請求移除，請提交附有公開來源的 issue*

請按照貢獻檢查清單，通過 issue 或 pull request 推薦有來源依據的示例
