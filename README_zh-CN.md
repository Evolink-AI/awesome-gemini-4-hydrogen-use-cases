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

# Awesome Gemini 3.6 Flash 指南与用例

## 🍌 简介

欢迎阅读这份有公开来源证据支撑的 Gemini 3.6 Flash 实践指南

**本仓库收集公开创作者证据中的 Gemini 3.6 Flash 工作流、构建成果、评估对比与实际限制**

每个案例都来自经过审查的来源包，标题链接到原始帖子，作者链接到创作者主页，只有来源文本确实包含 prompt 时才会收录

## 📊 概述

- 从 33 个经过审查的来源帖子中选出 33 个高可信度案例
- 覆盖范围包括代理、编码、网站、游戏、3D、基准式比较和实际安全限制
- 所有 24 个视频案例均提供可见的海报和可播放的 R2 托管 MP4；图像案例保留每一个经过审查的源图像
- EvoLink 标注的正式 model ID 是 `gemini-3.6-flash`，本仓库链接到当前模型页与 Gemini Native API 接入文档

> [!NOTE]
> 本合集优先保留可观察证据，不重建缺失的 prompt，不推断未公开的设置步骤，也不把单个创作者的结果泛化为通用 benchmark

**从这里开始: [探索Gemini 3.6 Flash](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link) · [获取 API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key) · [打开 Gemini Native API 文档](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=first_run)**

## 📑 菜单

| 部分 | 案例 |
|---|---|
| [⚡ 效率与代理](#efficiency-agents) | 8 |
| [💻 编码和应用程序](#coding-apps) | 4 |
| [🎮 网页、游戏和 3D](#web-games-3d) | 10 |
| [🧪 评估与比较](#evaluations) | 8 |
| [🛡️ 安全与限制](#safety-limits) | 3 |
| [相关存储库](#related-repositories) | 相关存储库 |
| [快速入门](#quick-start) | 快速入门 |
| [致谢](#acknowledge) | 致谢 |

| 案例 | 类别 | 它显示了什么 | 类型 |
|---|---|---|---|
| [token效率并存](#case-1) | 效率与代理 | 在为代理规模工作负载选择 Flash 模型之前，请比较同一工作流程上的输出令牌使用情况 | Evaluation |
| [Antigravity遗留代码的现代化](#case-2) | 效率与代理 | 使用受控的遗留代码迁移任务来比较代理延迟、编辑质量和完成行为 | Evaluation |
| [Canvas token效率测试](#case-3) | 效率与代理 | 跨模型版本运行相同的 Canvas 任务并检查工件和令牌的使用情况 | Evaluation |
| [浏览器代理基准](#case-4) | 效率与代理 | 对浏览器代理的成功和成本进行基准测试，而不是单独优化任一指标 | Benchmark |
| [长尾事实检索效率](#case-5) | 效率与代理 | 使用困难的事实检索任务来比较推理步骤和思考 token开销 | Evaluation |
| [企业文档处理](#case-6) | 效率与代理 | 在设置生产默认值之前评估长专利和文档解析的推理工作 | Benchmark |
| [JetBrains 中的工程任务评估](#case-7) | 效率与代理 | 构建客观的工程任务并在同一 IDE 工作流程中比较模型生成 | Evaluation |
| [多代理代码迁移](#case-8) | 效率与代理 | 使用相同的编排计划测试代码迁移，并比较延迟、编辑和最终质量 | Demo |
| [Android 吉他调音器](#case-9) | 编码和应用程序 | 构建一个专注的移动实用程序原型，将传统音频工具与人工智能辅助的替代调音相结合 | Demo |
| [交通灯模拟](#case-10) | 编码和应用程序 | 要求模型提供可执行的可视化，以检查生成的代码是否捕获定时和随机流量行为 | Demo |
| [键盘钢琴应用程序](#case-11) | 编码和应用程序 | 将简单的交互概念转变为可玩的键盘控制的 Web 应用程序 | Demo |
| [桌面机器人语音助手](#case-12) | 编码和应用程序 | 将 Flash 和 Flash-Lite 集成到语音应用程序中并比较第一响应行为 | Integration |
| [金门大桥 HTML 故障](#case-13) | 网页、游戏和 3D | 在信任生成的 3D Web 体验之前，使用严格的文件传递任务来测试指令遵循情况 | Limit |
| [公共提示视觉测试](#case-14) | 网页、游戏和 3D | 当您需要创建者的完整提示而不是从输出中重建它时，请打开源线程 | Demo |
| [单提示画布游戏](#case-15) | 网页、游戏和 3D | 使用 Canvas 中的一个提示来测试模型将紧凑的游戏概念转变为交互式结果的速度 | Demo |
| [登陆页面版本比较](#case-16) | 网页、游戏和 3D | 保持模型各代之间的提示固定，以隔离登陆页面执行和视觉判断中的变化 | Evaluation |
| [地铁跑酷 3D 原型](#case-17) | 网页、游戏和 3D | 为编码实验提供扩展思维，并检查交互质量和视觉保真度 | Demo |
| [一页网站比较](#case-18) | 网页、游戏和 3D | 保持网站提示和推理水平不变，然后比较令牌成本、速度和设计偏好 | Evaluation |
| [狂野西部游戏失败](#case-19) | 网页、游戏和 3D | 将失败的游戏生成输出视为决定何时切换模型或修改任务的证据 | Limit |
| [Antigravity游戏材料失效](#case-20) | 网页、游戏和 3D | 在接受人工智能生成的游戏原型之前，请检查视觉材料和实际交互行为 | Limit |
| [劳斯莱斯 SVG 比较](#case-21) | 网页、游戏和 3D | 使用固定的 SVG 主题来比较两代 Flash 如何处理形状、细节和构图 | Evaluation |
| [现实水族馆测试](#case-22) | 网页、游戏和 3D | 使用有界 3D 场景来比较模型版本之间的真实感和实现质量 | Evaluation |
| [Max Reasoning 中的 Gemini 与 Grok](#case-23) | 评估与比较 | 使用相同的提示和最大推理设置来比较速度、成本和输出，而不是依赖模型声誉 | Evaluation |
| [Gemini与Sonnet在最大设置](#case-24) | 评估与比较 | 比较相同提示及其最强设置的模型，然后检查实际生成的工件 | Evaluation |
| [视觉理解测试](#case-25) | 评估与比较 | 在采用视觉工作流程模型之前，使用具体的图像任务来检查响应质量和交互风格 | Demo |
| [火箭联盟游戏基准](#case-26) | 评估与比较 | 运行重复的游戏生成基准并记录构建时间和一致的主观排名 | Benchmark |
| [EyeBench 视觉比较](#case-27) | 评估与比较 | 使用稳定的视觉基准将增量效率增益与绝对质量分开 | Benchmark |
| [剪纸动画对比](#case-28) | 评估与比较 | 在评估创意生成时，分别比较响应速度和最终动画 | Evaluation |
| [AI Arena 生成基准](#case-29) | 评估与比较 | 使用相同的 arena 任务来比较多个编码模型的构建时间、价格和工件质量 | Benchmark |
| [跨模型游戏构建成本](#case-30) | 评估与比较 | 在选择游戏原型设计模型时，一起跟踪迭代次数、开发人员经验、功能和成本 | Benchmark |
| [网络安全拒绝基准](#case-31) | 安全与限制 | 在安全工具评估中包括拒绝行为，因为防御性代码审查可能会被攻击性请求阻止 | Limit |
| [知识新鲜度失败](#case-32) | 安全与限制 | 通过检索来验证当前事实，而不是相信声称的知识截止点 | Limit |
| [越狱红队测试](#case-33) | 安全与限制 | 将越狱声明视为需要受控复制和安全审查的红队信号，而不是可重复使用的指令 | Limit |

<a id="efficiency-agents"></a>
## ⚡ 效率与代理

<a id="case-1"></a>
### 案例 1: [token效率并存](https://x.com/JeffDean/status/2079591562145870043) (作者 [@JeffDean](https://x.com/JeffDean))

**在为代理规模工作负载选择 Flash 模型之前，请比较同一工作流程上的输出令牌使用情况**

Jeff Dean 分享了一个并排演示，比较了 Gemini 3.6 Flash 和 3.5 Flash，并强调了新模型中较低的token使用量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-2"></a>
### 案例 2: [Antigravity遗留代码的现代化](https://x.com/antigravity/status/2079663375991046351) (作者 [@antigravity](https://x.com/antigravity))

**使用受控的遗留代码迁移任务来比较代理延迟、编辑质量和完成行为**

Google Antigravity 展示了两代 Flash 重建遗留软件的能力，并报告称 Gemini 3.6 Flash 的延迟和输出得到改善，完成速度更快

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-3"></a>
### 案例 3: [Canvas token效率测试](https://x.com/stevibe/status/2079599477216956437) (作者 [@stevibe](https://x.com/stevibe))

**跨模型版本运行相同的 Canvas 任务并检查工件和令牌的使用情况**

创建者在一个简短的 Canvas 任务上对 Gemini 3.6 Flash 和 3.5 Flash 进行了比较，发现 3.6 Flash 的token使用率明显较低

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-4"></a>
### 案例 4: [浏览器代理基准](https://x.com/browser_use/status/2079602472516264010) (作者 [@browser_use](https://x.com/browser_use))

**对浏览器代理的成功和成本进行基准测试，而不是单独优化任一指标**

根据其 BU 基准测试，Gemini 3.6 Flash 的浏览器使用率为 68%，而 GPT-5.6 Sol 为 67%，Sonnet 4.6 为 62%，Opus 4.8 为 74%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg" alt="Case 4 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-07-21

---

<a id="case-5"></a>
### 案例 5: [长尾事实检索效率](https://x.com/__apf__/status/2079603658141184134) (作者 [@__apf__](https://x.com/__apf__))

**使用困难的事实检索任务来比较推理步骤和思考 token开销**

创建者在一项复杂的长尾事实检索任务上运行 Gemini 3.5 和 3.6 Flash，并报告说 3.6 Flash 的步骤数量减半，思考 token减少了 75%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-6"></a>
### 案例 6: [企业文档处理](https://x.com/databricks/status/2079598684455551326) (作者 [@databricks](https://x.com/databricks))

**在设置生产默认值之前评估长专利和文档解析的推理工作**

Databricks 报告称，文档分类准确度高于 3.5 Flash，在长专利上取得了出色的结果，并且中等工作量的文档解析总标记比高工作量的文档解析少约 32%

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png" alt="Case 6 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-07-21

---

<a id="case-7"></a>
### 案例 7: [JetBrains 中的工程任务评估](https://x.com/jetbrains/status/2079618218587574636) (作者 [@jetbrains](https://x.com/jetbrains))

**构建客观的工程任务并在同一 IDE 工作流程中比较模型生成**

JetBrains 在 AI Assistant 和 Junie 中对 Gemini 3.6 Flash 与上一代 Flash 进行了客观的工程任务评估

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-8"></a>
### 案例 8: [多代理代码迁移](https://x.com/CodeByPoonam/status/2079607995861021073) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**使用相同的编排计划测试代码迁移，并比较延迟、编辑和最终质量**

该演示显示 Gemini 3.6 Flash 通过 Antigravity 中的多代理编排执行代码迁移，并报告比 3.5 Flash 更低的延迟和更高的质量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4)

类型: Demo | 日期: 2026-07-21

---


<a id="coding-apps"></a>
## 💻 编码和应用程序

<a id="case-9"></a>
### 案例 9: [Android 吉他调音器](https://x.com/bijanbowen/status/2079675781794443640) (作者 [@bijanbowen](https://x.com/bijanbowen))

**构建一个专注的移动实用程序原型，将传统音频工具与人工智能辅助的替代调音相结合**

创建者使用 Gemini 3.6 Flash 构建了一个 Android 吉他调音器应用程序，并提供 AI 驱动的替代调音支持

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4)

类型: Demo | 日期: 2026-07-21

---

<a id="case-10"></a>
### 案例 10: [交通灯模拟](https://x.com/diegocabezas01/status/2079588206513631483) (作者 [@diegocabezas01](https://x.com/diegocabezas01))

**要求模型提供可执行的可视化，以检查生成的代码是否捕获定时和随机流量行为**

公共提示要求使用 Python 代码来可视化单向街道交通信号灯，其中汽车以随机速率到达，该帖子包含了最终的演示

**提示词:**

```text
write a python code that visualizes how a traffic light works in a one way street with cars entering at random rate.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4)

类型: Demo | 日期: 2026-07-21

---

<a id="case-11"></a>
### 案例 11: [键盘钢琴应用程序](https://x.com/Majin_AppSheet/status/2079734240540041230) (作者 [@Majin_AppSheet](https://x.com/Majin_AppSheet))

**将简单的交互概念转变为可玩的键盘控制的 Web 应用程序**

创建者使用 Gemini 3.6 Flash 构建了一个可以通过计算机键盘弹奏的钢琴应用程序，并将其设计为儿童可以探索的应用程序

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4)

类型: Demo | 日期: 2026-07-22

---

<a id="case-12"></a>
### 案例 12: [桌面机器人语音助手](https://x.com/AILogDev/status/2079716688745132044) (作者 [@AILogDev](https://x.com/AILogDev))

**将 Flash 和 Flash-Lite 集成到语音应用程序中并比较第一响应行为**

创建者将 Gemini 3.6 Flash 和 Gemini 3.5 Flash-Lite 添加到桌面机器人的语音对话应用程序中，并指出最初的响应感觉稍慢但可用

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4)

类型: Integration | 日期: 2026-07-21

---


<a id="web-games-3d"></a>
## 🎮 网页、游戏和 3D

<a id="case-13"></a>
### 案例 13: [金门大桥 HTML 故障](https://x.com/LuminaXspace/status/2079597030922465407) (作者 [@LuminaXspace](https://x.com/LuminaXspace))

**在信任生成的 3D Web 体验之前，使用严格的文件传递任务来测试指令遵循情况**

测试人员需要三个提示，看到模型尝试应用内模拟和网络图像响应而不是请求的 HTML 文件，并判断最终的 3D 桥输出明显弱于 Gemini 3.1 Pro

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4)

类型: Limit | 日期: 2026-07-21

---

<a id="case-14"></a>
### 案例 14: [公共提示视觉测试](https://x.com/Motion_Viz/status/2079592671530938537) (作者 [@Motion_Viz](https://x.com/Motion_Viz))

**当您需要创建者的完整提示而不是从输出中重建它时，请打开源线程**

MotionViz 发布了 Gemini 3.6 Flash 媒体视觉测试，并表示完整的提示在源线程中可用；此存储库不会重建源包中不存在的提示文本

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4)

类型: Demo | 日期: 2026-07-21

---

<a id="case-15"></a>
### 案例 15: [单提示画布游戏](https://x.com/ozansihay/status/2079599565565468672) (作者 [@ozansihay](https://x.com/ozansihay))

**使用 Canvas 中的一个提示来测试模型将紧凑的游戏概念转变为交互式结果的速度**

创建者在早期访问中测试了 Gemini 3.6 Flash，并使用单个 Canvas 提示来制作可玩的游戏演示

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4)

类型: Demo | 日期: 2026-07-21

---

<a id="case-16"></a>
### 案例 16: [登陆页面版本比较](https://x.com/nemumusitocha/status/2079596099854307650) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**保持模型各代之间的提示固定，以隔离登陆页面执行和视觉判断中的变化**

创建者将 Gemini 3.6 Flash 添加到相同提示的登陆页面存档中，并判断新结果比 Gemini 3 和 3.5 输出更差

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg" alt="Case 16 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg" alt="Case 16 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg" alt="Case 16 source image 3" height="360"></a>

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-17"></a>
### 案例 17: [地铁跑酷 3D 原型](https://x.com/itsPaulAi/status/2079597536155668890) (作者 [@itsPaulAi](https://x.com/itsPaulAi))

**为编码实验提供扩展思维，并检查交互质量和视觉保真度**

创建者使用 Gemini 3.6 Flash 构建了一个简单的 3D 地铁跑酷风格的复制品，并建议对编码任务进行扩展思维

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4)

类型: Demo | 日期: 2026-07-21

---

<a id="case-18"></a>
### 案例 18: [一页网站比较](https://x.com/SaiNemani1/status/2079606113306325496) (作者 [@SaiNemani1](https://x.com/SaiNemani1))

**保持网站提示和推理水平不变，然后比较令牌成本、速度和设计偏好**

在同一个一页的网站提示中，创建者报告了 Gemini 3.6 Flash 的token约为 6,100 个，而 3.5 Flash 的token约为 9,300 个，而个人更喜欢旧型号的外观

**提示词:**

```text
create a modern website! Should look amazing! One-code page
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-19"></a>
### 案例 19: [狂野西部游戏失败](https://x.com/Mr_Salio/status/2079635008424169901) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**将失败的游戏生成输出视为决定何时切换模型或修改任务的证据**

测试人员使用 Wild West 游戏生成提示，根据观察结果判断 Gemini 3.6 Flash 明显落后于 GPT-5.6、Kimi K3 和 Fable 5

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4)

类型: Limit | 日期: 2026-07-21

---

<a id="case-20"></a>
### 案例 20: [Antigravity游戏材料失效](https://x.com/Conor_D_Dart/status/2079592731211399460) (作者 [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**在接受人工智能生成的游戏原型之前，请检查视觉材料和实际交互行为**

在第二次Antigravity游戏测试中，创作者发现较弱的木质纹理和看起来相似但仍然不起作用的大理石元素

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4)

类型: Limit | 日期: 2026-07-21

---

<a id="case-21"></a>
### 案例 21: [劳斯莱斯 SVG 比较](https://x.com/ggg78g89/status/2079610251444437335) (作者 [@ggg78g89](https://x.com/ggg78g89))

**使用固定的 SVG 主题来比较两代 Flash 如何处理形状、细节和构图**

该帖子将 Gemini 3.6 Flash 和 3.5 Flash 输出并排放置，以执行相同的劳斯莱斯 SVG 任务

**提示词:**

```text
SVG of a Rolls Royce
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png" alt="Case 21 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png" alt="Case 21 source image 2" height="360"></a>

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-22"></a>
### 案例 22: [现实水族馆测试](https://x.com/intheworldofai/status/2079681107516170431) (作者 [@intheworldofai](https://x.com/intheworldofai))

**使用有界 3D 场景来比较模型版本之间的真实感和实现质量**

创作者要求 Gemini 3.6 Flash 建造一个逼真的水族馆，并认为它只比 3.5 Flash 好一点点

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4)

类型: Evaluation | 日期: 2026-07-21

---


<a id="evaluations"></a>
## 🧪 评估与比较

<a id="case-23"></a>
### 案例 23: [Max Reasoning 中的 Gemini 与 Grok](https://x.com/notjazii/status/2079609162431181193) (作者 [@notjazii](https://x.com/notjazii))

**使用相同的提示和最大推理设置来比较速度、成本和输出，而不是依赖模型声誉**

创建者在相同的提示和最大推理设置下运行 Gemini 3.6 Flash 和 Grok 4.5，观察到两者都很快，而 Grok 稍快一些且更便宜

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-24"></a>
### 案例 24: [Gemini与Sonnet在最大设置](https://x.com/notjazii/status/2079617706693902416) (作者 [@notjazii](https://x.com/notjazii))

**比较相同提示及其最强设置的模型，然后检查实际生成的工件**

创建者在最大设置下使用相同的提示测试了 Gemini 3.6 Flash 和 Sonnet 5，并在所示任务中首选 Gemini 输出

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-25"></a>
### 案例 25: [视觉理解测试](https://x.com/HarshithLucky3/status/2079607042403381313) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**在采用视觉工作流程模型之前，使用具体的图像任务来检查响应质量和交互风格**

创建者展示了 Gemini 3.6 Flash 通过的视力测试，并强调了响应个性作为观察体验的一部分

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg" alt="Case 25 source image 1" height="360"></a>

类型: Demo | 日期: 2026-07-21

---

<a id="case-26"></a>
### 案例 26: [火箭联盟游戏基准](https://x.com/LLMJunky/status/2079712480683790743) (作者 [@LLMJunky](https://x.com/LLMJunky))

**运行重复的游戏生成基准并记录构建时间和一致的主观排名**

创建者在火箭联盟式的任务中测试了 Gemini 3.6 Flash，在个人排行榜上排名第三，并报告在不到两分钟的时间内完成了任务

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4)

类型: Benchmark | 日期: 2026-07-21

---

<a id="case-27"></a>
### 案例 27: [EyeBench 视觉比较](https://x.com/adonis_singh/status/2079631807817933222) (作者 [@adonis_singh](https://x.com/adonis_singh))

**使用稳定的视觉基准将增量效率增益与绝对质量分开**

在 EyeBench 上，创建者认为 Gemini 3.6 Flash 略好于 3.5 Flash，但仍差于 Gemini 3.1 Pro Preview，同时注意到token效率有所提高

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg" alt="Case 27 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-07-21

---

<a id="case-28"></a>
### 案例 28: [剪纸动画对比](https://x.com/OriSilver/status/2079603778441957776) (作者 [@OriSilver](https://x.com/OriSilver))

**在评估创意生成时，分别比较响应速度和最终动画**

作者在剪纸动画任务中将 Gemini 3.6 Flash 与《神鬼寓言 5》进行了比较，称赞 Gemini 近乎即时的响应，但对结果表示保留

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4)

类型: Evaluation | 日期: 2026-07-21

---

<a id="case-29"></a>
### 案例 29: [AI Arena 生成基准](https://x.com/OmedVibeCodes/status/2079663080049660220) (作者 [@OmedVibeCodes](https://x.com/OmedVibeCodes))

**使用相同的 arena 任务来比较多个编码模型的构建时间、价格和工件质量**

创建者在一项 AI Arena 任务中测试了 Grok 4.5、Gemini 3.6 Flash 和 GPT-5.6 Luna，并判断 Gemini 在该运行中的结果最弱

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4)

类型: Benchmark | 日期: 2026-07-21

---

<a id="case-30"></a>
### 案例 30: [跨模型游戏构建成本](https://x.com/naymur_dev/status/2079710299918401907) (作者 [@naymur_dev](https://x.com/naymur_dev))

**在选择游戏原型设计模型时，一起跟踪迭代次数、开发人员经验、功能和成本**

使用相同的设计工作流程，创建者报告需要六到七次迭代来修复 Gemini 生成的跳跃和坠落错误，并列出了 0.15 美元的运行成本以及比较分数

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[播放源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4)

类型: Benchmark | 日期: 2026-07-21

---


<a id="safety-limits"></a>
## 🛡️ 安全与限制

<a id="case-31"></a>
### 案例 31: [网络安全拒绝基准](https://x.com/pilvar222/status/2079602157779566836) (作者 [@pilvar222](https://x.com/pilvar222))

**在安全工具评估中包括拒绝行为，因为防御性代码审查可能会被攻击性请求阻止**

网络安全基准测试被拒绝，导致评估人员报告称，经过测试的策略阻止了防御性代码的漏洞查找行为以及恶意使用

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg" alt="Case 31 source image 1" height="360"></a>

类型: Limit | 日期: 2026-07-21

---

<a id="case-32"></a>
### 案例 32: [知识新鲜度失败](https://x.com/ggg78g89/status/2079587359851737339) (作者 [@ggg78g89](https://x.com/ggg78g89))

**通过检索来验证当前事实，而不是相信声称的知识截止点**

测试人员询问当前的旗舰型号并收到较旧的名称，然后报告说该型号承认仅到 2025 年初的知识，尽管声称截止日期为 2026 年 3 月

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg" alt="Case 32 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg" alt="Case 32 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg" alt="Case 32 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png" alt="Case 32 source image 4" height="360"></a>

类型: Limit | 日期: 2026-07-21

---

<a id="case-33"></a>
### 案例 33: [越狱红队测试](https://x.com/Ubannoblesse/status/2079711268899086484) (作者 [@Ubannoblesse](https://x.com/Ubannoblesse))

**将越狱声明视为需要受控复制和安全审查的红队信号，而不是可重复使用的指令**

该帖子声称 Gemini 应用程序和 API 已越狱，并列出了经过测试的有害内容类别；该存储库记录安全信号，而不复制漏洞利用指令

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg" alt="Case 33 source image 1" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg" alt="Case 33 source image 2" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg" alt="Case 33 source image 3" height="360"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg" alt="Case 33 source image 4" height="360"></a>

类型: Limit | 日期: 2026-07-21

---

<a id="related-repositories"></a>
## 相关存储库

- [EvoLink-AI on GitHub](https://github.com/Evolink-AI) — 来自 EvoLink 的更多模型指南和 API 示例
- [Gemini 3.6 Flash official launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
- [Gemini 3.6 Flash model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)
- 在本出版物中，没有独立验证专用的可安装 Gemini 3.6 Flash 技能

<a id="quick-start"></a>
## ⚡ 快速入门

通过下方经过验证的公开入口开始使用 model ID `gemini-3.6-flash`

1. [打开Gemini 3.6 Flash模型页面](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link)
2. [创建或管理 EvoLink API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key)
3. [遵循 Gemini Native API 快速入门](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=first_run)

> [!IMPORTANT]
> 公开路由与 model ID 已有文档依据，但在真实测试完成或获得明确豁免前，本仓库不会声称已执行消耗额度的 first call

<a id="acknowledge"></a>
## 🙏 致谢

该合集的存在是因为创作者和实践者公开分享了他们的 Gemini 3.6 Flash 作品

**感谢这里代表的来源创作者:**

[@JeffDean](https://x.com/JeffDean), [@antigravity](https://x.com/antigravity), [@stevibe](https://x.com/stevibe), [@browser_use](https://x.com/browser_use), [@__apf__](https://x.com/__apf__), [@databricks](https://x.com/databricks), [@jetbrains](https://x.com/jetbrains), [@CodeByPoonam](https://x.com/CodeByPoonam), [@bijanbowen](https://x.com/bijanbowen), [@diegocabezas01](https://x.com/diegocabezas01), [@Majin_AppSheet](https://x.com/Majin_AppSheet), [@AILogDev](https://x.com/AILogDev), [@LuminaXspace](https://x.com/LuminaXspace), [@Motion_Viz](https://x.com/Motion_Viz), [@ozansihay](https://x.com/ozansihay), [@nemumusitocha](https://x.com/nemumusitocha), [@itsPaulAi](https://x.com/itsPaulAi), [@SaiNemani1](https://x.com/SaiNemani1), [@Mr_Salio](https://x.com/Mr_Salio), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@ggg78g89](https://x.com/ggg78g89), [@intheworldofai](https://x.com/intheworldofai), [@notjazii](https://x.com/notjazii), [@HarshithLucky3](https://x.com/HarshithLucky3), [@LLMJunky](https://x.com/LLMJunky), [@adonis_singh](https://x.com/adonis_singh), [@OriSilver](https://x.com/OriSilver), [@OmedVibeCodes](https://x.com/OmedVibeCodes), [@naymur_dev](https://x.com/naymur_dev), [@pilvar222](https://x.com/pilvar222), [@Ubannoblesse](https://x.com/Ubannoblesse)

*我们无法保证每条帖子都指向最早的原创者，如归属、翻译或措辞需要修正，请提交带公开来源的 correction issue*

要提出另一个由源支持的案例，请打开问题或拉取请求并遵循贡献清单
