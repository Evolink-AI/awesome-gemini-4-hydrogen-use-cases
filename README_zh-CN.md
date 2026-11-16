<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/cn/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=docs_link)

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

# Gemini 4 Hydrogen 精选指南与应用案例

## 🍌 简介

通过有来源依据的应用、编程工作流和实用对比，探索 Gemini 4 Hydrogen

**225 个案例展示了 Hydrogen 的实际用法和结果的局限**

每个案例均链接至来源并注明作者；演示、服务商示例和创作者对比均在说明中标注；未公开的提示词不会被补写

## 📊 概览

- 共 225 个案例. 11 月 17 日更新核查了 1,304 条 X 帖子，新增 185 个案例. 新增来源在采集时均超过 30 赞
- 五个类别涵盖智能体、学习与应用、电子表格与搜索、交互式 3D，以及对比与局限
- 全库保留 264 个原始视觉素材，包括 168 个带封面的可播放视频和 96 张图片
- Gemini 4 Hydrogen 于 2026 年 11 月 12 日发布；可在 EvoLink 探索该模型及当前访问方式

> [!NOTE]
> 除非另有说明，模型归属、费用、耗时和结果均为来源方的说法；视频审阅采用抽样帧，未进行完整功能测试；代码应用的运行录像不能证明模型具备原生视频生成能力；不同运行框架、推理级别或迭代次数会使对比缺乏受控条件

**官方参考资料: [Google 发布公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**从这里开始: [在 EvoLink 探索 Hydrogen](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [获取 API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ 快速入门

先从 EvoLink 开始，需要将 Hydrogen 集成到应用时，再使用 Gemini 原生 API

1. [在浏览器中查看 Gemini 4 Hydrogen（Browser）](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [创建或管理 EvoLink API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

最简原生 API 请求

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

[阅读 Gemini 原生 API 快速入门](https://evolink.ai/docs/cn/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> 从响应的 candidates[].content.parts[].text 字段读取生成的文本

> [!IMPORTANT]
> 请将 API 密钥保存在环境变量中，切勿提交到仓库；流式输出、推理及其他请求选项请参阅 API 文档

## 📑 目录

| 章节 | 案例 |
|---|---|
| [⚡ 智能体与编程工作流](#agents) | 30 |
| [💻 应用与学习](#apps-learning) | 37 |
| [📊 电子表格与搜索](#data-search) | 9 |
| [🎮 交互式 3D 与用户界面](#interactive-3d) | 48 |
| [🧪 对比与局限](#comparisons-limits) | 101 |
| [相关仓库](#related-repositories) |  |
| [快速入门](#quick-start) |  |
| [致谢](#acknowledge) |  |

| 案例 | 类别 | 可以尝试什么 | 类型 |
|---|---|---|---|
| [在 Antigravity 中维护代码库](#case-1) | 智能体与编程工作流 | 使用范围明确的维护任务，同时评估编辑、工具使用和验证能力 | Demo |
| [并行构建十六个 Canvas 应用](#case-2) | 智能体与编程工作流 | 将构建工作拆分为独立模块，明确规划、实现和质量检查的角色 | Demo |
| [混合模型智能体群构建绯红飞蛾](#case-3) | 智能体与编程工作流 | 为交互式创意编程项目分配独立的编排与实现角色 | Demo |
| [3D Medic 检查与修复](#case-4) | 智能体与编程工作流 | 探索能够检查 3D 文件、发现错误并在导出前提出修复方案的智能体 | Demo |
| [在 Devin 中构建帆船场景](#case-5) | 智能体与编程工作流 | 在你实际计划使用的编程智能体环境中评估模型 | Demo |
| [Lingo City 语言练习](#case-6) | 应用与学习 | 结合记忆卡片与交互式街景，进行情境化语言练习 | Demo |
| [《罗密欧与朱丽叶》3D 纸剧场](#case-7) | 应用与学习 | 将具体课程转化为具有明确学习目标的交互场景 | Demo |
| [从设计图到阅读网站](#case-8) | 应用与学习 | 使用参考设计评估视觉理解和可运行前端的实现能力 | Demo |
| [用二十个模块构建锦鲤庭院](#case-9) | 应用与学习 | 用小模块构建较大场景，而非期待一次提示就得到完整结果 | Demo |
| [质子聚变学习游戏](#case-10) | 应用与学习 | 为科学过程制作交互式讲解原型，然后核查其中的科学内容 | Demo |
| [Google Sheets 中的动态风景](#case-11) | 电子表格与搜索 | 通过非常规的电子表格动画，检查生成代码和单元格级更新 | Demo |
| [Folio 交互式数据网站](#case-12) | 电子表格与搜索 | 在小型网站原型中结合落地页布局与交互式数据可视化 | Demo |
| [多部分搜索问题的可视化回答](#case-13) | 电子表格与搜索 | 测试细致且具有多项约束的搜索请求时，对比回答布局与引用链接 | Demo |
| [Sheets 中的交互式财务预测](#case-14) | 电子表格与搜索 | 构建假设清晰可见的财务模型原型，并检查生成的公式与图表 | Demo |
| [交互式餐厅](#case-15) | 交互式 3D 与用户界面 | 检查物体交互、照明和状态变化，而不是仅凭静态图片评判场景 | Demo |
| [带微缩世界的音量滑块](#case-16) | 交互式 3D 与用户界面 | 通过一个熟悉的控件，同时测试交互设计与动画场景细节 | Demo |
| [Three.js 日式住宅](#case-17) | 交互式 3D 与用户界面 | 评估细致的 3D 漫游时，将代码生成时间与渲染时间分开 | Demo |
| [骑自行车的 3D 鹈鹕](#case-18) | 交互式 3D 与用户界面 | 使用运动角色检查协调性、动作和场景一致性 | Demo |
| [规划优先的行星模拟器](#case-19) | 交互式 3D 与用户界面 | 让编程模型编辑复杂场景之前，先给出具体计划 | Demo |
| [用 Antigravity Swarm 构建港湾岛屿](#case-20) | 交互式 3D 与用户界面 | 通过可导航的小型环境，检查多智能体构建场景的行为 | Demo |
| [埃菲尔铁塔浮空岛](#case-21) | 交互式 3D 与用户界面 | 通过紧凑的地标场景评估构图、镜头运动和模型生成的代码 | Demo |
| [可飞行的未来城市](#case-22) | 交互式 3D 与用户界面 | 测试对程序化世界的后续编辑，不要假定首次输出就是最终结果 | Demo |
| [从日出到夜晚的水上飞机](#case-23) | 交互式 3D 与用户界面 | 检查交互式 3D 场景中的环境控制与光照过渡 | Demo |
| [霓虹火柴人动画：Hydrogen 与 Opus](#case-24) | 对比与局限 | 结合来源所述时间与费用对比最终动画，不要假定运行框架相同 | Evaluation |
| [机器人任务与自行识别失误](#case-25) | 对比与局限 | 在机器人评估中纳入任务完成情况以及识别细小失误的能力 | Evaluation |
| [自然语言驱动的实验室工作单元](#case-26) | 对比与局限 | 将工具执行和失败处理的评估与基准榜单分数分开 | Evaluation |
| [冰山与拖船：Hydrogen 与 Carbon](#case-27) | 对比与局限 | 对比耗时较长的 3D 构建时，记录推理级别与运行框架限制 | Evaluation |
| [果冻锦鲤池：Hydrogen 与 Sonnet](#case-28) | 对比与局限 | 在根据基准排名选择模型前，先检查具体场景 | Evaluation |
| [使用相同提示词的创意编程合集](#case-29) | 对比与局限 | 通过多样化的视觉任务，避免从单个漂亮输出过度概括 | Evaluation |
| [Megamind 体素：成本与质量反例](#case-30) | 对比与局限 | 评估模型是否始终更便宜或视觉效果更强时，保留失败案例 | Limit |
| [穿越四季的杂耍狮子](#case-31) | 对比与局限 | 检查要求的动作，而不只是周围界面的视觉精致程度 | Limit |
| [三模型火柴人格斗：更慢且更贵的结果](#case-32) | 对比与局限 | 对比模型宣传的效率与实际任务报告时，保留反例 | Limit |
| [农场自行车场景：Hydrogen 与 Flash](#case-33) | 对比与局限 | 结合创作者报告的完成时间，对比动作与场景质量 | Evaluation |
| [女孩与猫的双人自行车](#case-34) | 对比与局限 | 对比提示词遵循程度与附加细节，同时明确不同编程运行框架的差异 | Evaluation |
| [四个模型构建 Three.js 马里奥游戏](#case-35) | 对比与局限 | 解读相同提示词的游戏对比前，记录不一致的推理设置 | Evaluation |
| [三个 Gemini 模型绘制游戏手柄](#case-36) | 对比与局限 | 寻找具体任务中的退步与改进，不要假定模型家族存在固定层级 | Evaluation |
| [应用与 Studio 的视觉回答存在差异](#case-37) | 对比与局限 | 依赖视觉结果之前，在计划使用的产品界面中测试相同图片 | Limit |
| [火箭发射场景：Hydrogen 与 Flash](#case-38) | 对比与局限 | 既对比实际发射动画，也对比来源报告的构建耗时 | Evaluation |
| [四项 SVG 动画任务](#case-39) | 对比与局限 | 通过多种交互与动画主题，检查跨任务的一致性 | Evaluation |
| [三个模型制作草原马匹动画](#case-40) | 对比与局限 | 直接检查动作与视觉细节，再判断宽泛的费用或质量说法是否可信 | Evaluation |
| [把太空参考图做成 HTML 场景](#case-41) | 交互式 3D 与用户界面 | 用少量参考图检验生成场景能否呈现可辨识的视觉风格. | Demo |
| [Gemini Canvas 中的一级方程式赛车原型](#case-42) | 交互式 3D 与用户界面 | 给车辆查看器设置几个镜头，从不同角度检查生成模型. | Demo |
| [Hydrogen API 与 Carbon Antigravity 输出](#case-43) | 对比与局限 | 用同一提示词比较视觉效果时，记录各自的运行环境. | Evaluation |
| [Hydrogen 与 Astra 的阴影细节对比](#case-44) | 对比与局限 | 比较两次运行的费用和耗时，同时检查渲染细节. | Evaluation |
| [程序化 3D 动效对比](#case-45) | 对比与局限 | 比较程序化动效的连贯性与构图时，记录生成耗时. | Evaluation |
| [历时 89 分钟的 PokéBench 视觉测试](#case-46) | 对比与局限 | 测试长时视觉代理时，同时记录任务完成情况、回合数和 API 失败次数. | Benchmark |
| [Hydrogen 与 DeepSeek 搭建同一个 3D 场景](#case-47) | 对比与局限 | 对照视觉输出并分别记录耗时和 API 费用. | Evaluation |
| [用 SVG 绘制宝马侧视图](#case-48) | 交互式 3D 与用户界面 | 用车辆 SVG 侧视图检查比例、轮廓和细节. | Demo |
| [天文学家的浮空岛](#case-49) | 交互式 3D 与用户界面 | 给小场景设定明确主题，再检查物件和光照能否强化主题. | Demo |
| [把参考图做成可游览的 3D 地形](#case-50) | 交互式 3D 与用户界面 | 检查图生场景能否同时还原视觉元素并支持移动. | Demo |
| [用 3D 积木搭建微缩景观](#case-51) | 交互式 3D 与用户界面 | 让模型搭建积木微缩景观，检查各形体能否组成完整场景. | Demo |
| [可交互的樱花树](#case-52) | 交互式 3D 与用户界面 | 用一件带动效的物体和几个控件探索微缩场景的实时变化. | Demo |
| [Agent Arena 的单任务耗时和成本](#case-53) | 对比与局限 | 查看总体成功率时，也比较单任务延迟、费用和输出 Token 数. | Benchmark |
| [视觉文档和终端基准测试](#case-54) | 对比与局限 | 分别查看文档与终端测试结果，再决定推理预算. | Benchmark |
| [Vals 指数和 Tax Agent 成绩](#case-55) | 对比与局限 | 结合整体评测和专业任务的分数来判断模型是否适用. | Benchmark |
| [CursorBench 的 Hydrogen 默认推理档](#case-56) | 对比与局限 | 先查看默认推理档的基准成绩，再到自己的仓库里测试. | Benchmark |
| [四款模型制作弓箭手战斗动画](#case-57) | 对比与局限 | 比较各个动画能否清楚表现角色的战斗动作. | Evaluation |
| [15 分钟搭建 Minecraft 风格原型](#case-58) | 应用与学习 | 用体素沙盒检验挖掘、背包等生成系统能否协同工作. | Demo |
| [n8n 中的 Hydrogen 工具调用流程](#case-59) | 智能体与编程工作流 | 让 Hydrogen 在 n8n 中处理工具调用循环，并单独安排规划步骤. | Integration |
| [Box Agent 处理复杂企业文档](#case-60) | 电子表格与搜索 | 在接近真实的文档任务中同时检查准确率、耗时和 Token 用量. | Benchmark |
| [Hydrogen 的 Devin FrontierCode 结果](#case-61) | 对比与局限 | 比较候选补丁能否合并，并记录各自使用的代理环境. | Benchmark |
| [小型交互动画中的光线折射](#case-62) | 交互式 3D 与用户界面 | 先快速预览并调整光学效果，再增加场景复杂度. | Demo |
| [一条向上流的河](#case-63) | 交互式 3D 与用户界面 | 选择运动方向不同寻常的小场景，观察视觉效果. | Demo |
| [禁止联网后仍触发搜索](#case-64) | 对比与局限 | 流程要求离线作答时，检查模型是否真的没有调用工具. | Limit |
| [记录 Antigravity Swarm 的配额用量](#case-65) | 对比与局限 | 测试多代理运行时记录 Token 量和消耗的额度. | Evaluation |
| [专业任务评测中的工具调用](#case-66) | 对比与局限 | 观察代理在执行专业任务前如何收集背景信息. | Benchmark |
| [Hydrogen 生成的 3D 肖像](#case-67) | 交互式 3D 与用户界面 | 用肖像做小型测试，检查 3D 表现能否保留可辨识的主体特征. | Demo |
| [四款模型制作法师斗龙动画](#case-68) | 对比与局限 | 比较同一奇幻场景各版本的调度、动作清晰度和特效. | Evaluation |
| [多代理设置中的认证路径](#case-69) | 智能体与编程工作流 | 代理委派给其他服务时，核对实际发起认证的是哪个客户端. | Limit |
| [一次 Antigravity Goal Mode 运行](#case-70) | 智能体与编程工作流 | 长时间编程时，记录计划、代码修改与测试结果. | Demo |
| [MazeBench 中的低成功率](#case-71) | 对比与局限 | 用迷宫任务检验空间推理，再决定能否依赖它. | Benchmark |
| [三款 Gemini 模型搭建帆船场景](#case-72) | 对比与局限 | 在主题化 Three.js 场景中比较运动效果和环境细节. | Evaluation |
| [Antigravity Orchestrator 中的 Carbon 与 Hydrogen](#case-73) | 智能体与编程工作流 | 让规划模型在快速执行模型卡住时接手排障. | Integration |
| [从 Workspace 数据生成图表和报告](#case-74) | 电子表格与搜索 | 检查追问一轮能否补齐分析、图表或报告. | Demo |
| [识别球衣号码时耗尽推理预算](#case-75) | 对比与局限 | 识别图片中的小细节时，设置推理上限并准备替代方案. | Limit |
| [不同模型系列的 ClutterBench 表现](#case-76) | 对比与局限 | 用专门的杂乱场景基准检验模型的通用优势是否适用于这一任务. | Benchmark |
| [把新闻简报制作成带旁白的短片](#case-77) | 应用与学习 | 先查资料，再将新闻简报做成旁白短片并核查其中的事实. | Demo |
| [Minecraft 风格人体解剖剖面像](#case-78) | 对比与局限 | 检查生成的剖面是否包含指定的内部结构. | Evaluation |
| [三款模型渲染同一件道具](#case-79) | 对比与局限 | 同时记录质量和 Token 用量，检查单价较低的模型是否在该任务中耗用更多 Token. | Evaluation |
| [归纳基准测试与 Token 消耗](#case-80) | 对比与局限 | 评测高难度推理时，将计费输入和输出用量与成绩一起记录. | Benchmark |
| [用不同 Gemini 模式在表格里画像素画](#case-81) | 电子表格与搜索 | 用同一个 Google 表格绘图任务比较不同模型选项. | Evaluation |
| [把参考图中的公寓做成 3D 打印件](#case-82) | 交互式 3D 与用户界面 | 把图生 3D 的测试延伸到打印实物. | Demo |
| [三款模型制作 3D 动物动画](#case-83) | 对比与局限 | 在同一项 3D 动物建模任务中检查身体结构和运动. | Evaluation |
| [Hydrogen 与 Qwen 的 ts-bench 测试](#case-84) | 对比与局限 | 将工具调用错误和总体基准成绩一起查看. | Benchmark |
| [Vending-Bench 商业模拟](#case-85) | 对比与局限 | 比较模拟收入时同时计入代理运行成本. | Benchmark |
| [黄金梅丽号海上场景](#case-86) | 交互式 3D 与用户界面 | 用辨识度高的虚构船只测试风格化海景的构图. | Demo |
| [在 OpenClaw 中使用 Hydrogen](#case-87) | 智能体与编程工作流 | 检查计划采用的代理框架能否选用 Hydrogen. | Integration |
| [游过云海的鲸鱼](#case-88) | 交互式 3D 与用户界面 | 通过一个代码制作的生物场景分别检查流体运动和眼睛设计. | Demo |
| [四款模型搭建微缩岛屿](#case-89) | 对比与局限 | 比较岛屿设计时，一并记录各个环境的耗时和费用. | Evaluation |
| [摄像头空中绘画工具](#case-90) | 应用与学习 | 在镜头前比画笔画，观察绘图界面如何跟随. | Demo |
| [用代码模拟布料撕裂](#case-91) | 对比与局限 | 用同一动画任务检查布料拉伸、撕裂及与毛发的相互作用. | Evaluation |
| [Gemini Canvas 里的海底城市](#case-92) | 交互式 3D 与用户界面 | 从小型 3D 场景起步，通过多轮迭代加入可探索的区域和会动的生物. | Demo |
| [一次生成的网站门户](#case-93) | 应用与学习 | 先用门户布局检查首轮界面，再测试各条操作流程. | Demo |
| [事实核查缺少可追溯来源](#case-94) | 对比与局限 | 依据模型对截图的判断行动之前，要求给出可查验的引用. | Limit |
| [《城市：天际线》风格建城工具](#case-95) | 应用与学习 | 搭建城市模拟原型，观察控件和模拟逻辑如何配合. | Demo |
| [Hydrogen 与 Sol 绘制 2D 鹈鹕](#case-96) | 对比与局限 | 用同一项简单 2D 动画任务对比耗时与动作表现. | Evaluation |
| [用 Blender MCP 重建王座厅](#case-97) | 智能体与编程工作流 | 用 Blender MCP 在编辑器中检查生成场景的构图. | Integration |
| [四款模型搭建蛛丝摆荡游戏](#case-98) | 对比与局限 | 统一使用单文件限制，比较各款游戏的移动和操作. | Evaluation |
| [Three.js 灰阶海盗船](#case-99) | 交互式 3D 与用户界面 | 将 Three.js 场景限定为灰阶，检查光照还能否突出几何形状. | Demo |
| [四款模型渲染建筑微缩景观](#case-100) | 对比与局限 | 用统一的建筑任务比较输出，查看各模型如何打光. | Evaluation |
| [CadXStudio 中的参数化台灯](#case-101) | 交互式 3D 与用户界面 | 检查 CAD 模型中的组件尺寸和可编辑性. | Integration |
| [用 C++ 制作神社参道动画](#case-102) | 交互式 3D 与用户界面 | 用小型原生代码场景检验模型能否在没有 Web 技术栈时写出可运行动画. | Demo |
| [三款模型渲染列车场景](#case-103) | 对比与局限 | 用同一列车场景任务比较各自配置下的完成速度. | Evaluation |
| [用 Extra 档制作雨夜唐人街](#case-104) | 对比与局限 | 给大型动画选择推理档前，记录实际耗时并检查最终画面. | Evaluation |
| [用 30 个模块搭建城镇场景](#case-105) | 交互式 3D 与用户界面 | 按模块分别提示模型，再检查组装后的整体效果. | Demo |
| [三款模型搭建行星可视化界面](#case-106) | 对比与局限 | 用同一提示词比较不同模型制作的科学可视化界面. | Evaluation |
| [四款模型复刻 Chrome 小恐龙](#case-107) | 对比与局限 | 为每次游戏复刻计时，并比较可玩结果. | Evaluation |
| [浮空岛上的邮局](#case-108) | 交互式 3D 与用户界面 | 指定一种微缩建筑，观察材质和光照如何表现主题. | Demo |
| [两款编程代理分别造船](#case-109) | 对比与局限 | 在实际使用的工具中比较首个可用结果和返工成本. | Evaluation |
| [锦鲤庭院里的水与鱼](#case-110) | 交互式 3D 与用户界面 | 用有游鱼的场景检查水面反射与光照是否连贯. | Demo |
| [四款模型制作刚体投石机攻城原型](#case-111) | 对比与局限 | 用同一任务比较可玩的物理原型，并记录推理档. | Evaluation |
| [Gemini 网页端运行交互式 3D 场景](#case-112) | 交互式 3D 与用户界面 | 在 Gemini 网页端快速制作可交互光照和粒子效果. | Demo |
| [浏览器 CAD 中的混凝土搅拌机装配](#case-113) | 智能体与编程工作流 | 把生成的装配体用于 CAD 工作流之前，检查部件树和配合情况. | Integration |
| [在 Blender 中程序化制作斧头](#case-114) | 智能体与编程工作流 | 用轮廓参考图和多轮视口检查来审核程序化 Blender 资产. | Integration |
| [单 HTML 文件里的粉色 3D 场景](#case-115) | 交互式 3D 与用户界面 | 尝试无外部素材的 Three.js 场景，检查构图是否清晰. | Demo |
| [FrontierMemory 的长期记忆测试](#case-116) | 对比与局限 | 为长期代理记忆选模型时，结合评分和单次费用. | Benchmark |
| [故意损坏的 LiveKit 语音代理](#case-117) | 对比与局限 | 引入可控的工具故障，检查语音代理会不会报告无依据的结果. | Evaluation |
| [由 28 个模块组成的 Ember Isle](#case-118) | 智能体与编程工作流 | 把大场景拆成模块，并记录每次生成的耗时. | Demo |
| [纯代码制作的大爆炸模拟](#case-119) | 交互式 3D 与用户界面 | 用短动画快速构建可视化解释，再检查科学表述. | Demo |
| [带装配爆炸视图的直升机](#case-120) | 交互式 3D 与用户界面 | 检查 3D 原型能否把飞行控制与实用的部件查看方式结合起来. | Demo |
| [带透视和线框视图的 Hydrogen Express](#case-121) | 交互式 3D 与用户界面 | 给可操控的 3D 原型加入多种检查模式. | Demo |
| [空中的补给站](#case-122) | 交互式 3D 与用户界面 | 给场景安排有辨识度的移动物体和光照状态，让变化在演示中清晰可见. | Demo |
| [三款 Gemini 模型制作骑行者动画](#case-123) | 对比与局限 | 用统一简报比较短动画，并记录各次运行的耗时. | Evaluation |
| [把化学教材做成交互课程](#case-124) | 应用与学习 | 用提示、语音引导和可选文本搭建自学课程. | Demo |
| [一首 Vocaloid 歌曲原型](#case-125) | 应用与学习 | 检查一次生成的曲目能否符合指定角色和风格. | Demo |
| [两款模型搭建 LEGO 世界](#case-126) | 对比与局限 | 结合耗时比较各模型搭建了多少主题场景. | Evaluation |
| [修复两个仓库里重新植入的缺陷](#case-127) | 对比与局限 | 植入已知缺陷，测量编程代理能找出并修复哪些问题. | Benchmark |
| [两款模型制作火柴人对战光标](#case-128) | 对比与局限 | 比较两份交互动画如何响应鼠标指针. | Evaluation |
| [单 HTML 文件里的水磨坊](#case-129) | 交互式 3D 与用户界面 | 用带醒目运动元素的小景观检查快速生成的 3D 原型. | Demo |
| [两款模型渲染山地景观](#case-130) | 对比与局限 | 在同一类景观动画中分别比较构图、生成耗时和费用. | Evaluation |
| [用自定义环境做英译波斯语评测](#case-131) | 对比与局限 | 用人工参考译文给高难度翻译段落打分. | Evaluation |
| [用 Hydrogen Extra 搭建 Blender 场景](#case-132) | 交互式 3D 与用户界面 | 增加视觉细节之前，先在 Blender 中检查几何与材质. | Demo |
| [四款模型搭建沉船场景](#case-133) | 对比与局限 | 用同一场景分别记录视觉还原、生成时间与开销. | Evaluation |
| [从图片读取复杂积分式](#case-134) | 应用与学习 | 化简长表达式前，检查模型能否识别积分上下限相同. | Evaluation |
| [四款模型的文案盲测](#case-135) | 对比与局限 | 在选用文案之前，隐去模型名称再评判. | Evaluation |
| [不同推理档的视觉检测与读字](#case-136) | 对比与局限 | 在各个推理档分别测量检测准确率、文字识别准确率、费用与延迟. | Benchmark |
| [四款模型重建《飞屋环游记》的房屋](#case-137) | 对比与局限 | 用同一张参考图和简报比较 3D 制作的各项取舍. | Evaluation |
| [用 WebGL2 制作人体细胞百科](#case-138) | 应用与学习 | 通过交互剖面讲解细胞内部的空间关系. | Demo |
| [Hydrogen 制作的两段粒子动画](#case-139) | 交互式 3D 与用户界面 | 用不同粒子场景检验简单特效中的形态和运动. | Demo |
| [Parking Bench 中只看图的对手](#case-140) | 应用与学习 | 只给益智游戏对手棋盘图片，测试它如何读取局面. | Integration |
| [Google 文档的操作教学视频](#case-141) | 应用与学习 | 用屏幕截图和编号标注讲解手机端的编辑步骤. | Demo |
| [微缩世界的昼夜切换开关](#case-142) | 交互式 3D 与用户界面 | 用小型开关测试界面状态切换时动作是否连贯. | Demo |
| [用 65 个模块搭建场景](#case-143) | 交互式 3D 与用户界面 | 随着场景扩展，记录生成耗时和集成工作量. | Demo |
| [固定镜头的舞蹈短片](#case-144) | 对比与局限 | 检查参考图动画能否保留角色设计、构图与镜头位置. | Evaluation |
| [编程代理卡在基线测试](#case-145) | 对比与局限 | 给基线测试设定时限，并检查进度再等待修复方案. | Limit |
| [为 MZ-1500 搭建 BASIC 环境](#case-146) | 应用与学习 | 搭建复古 BASIC 环境原型，并逐一核对外设支持. | Demo |
| [两款模型搭建交互机械臂](#case-147) | 对比与局限 | 操作 Three.js 机械臂时，检查各关节的动作是否连贯. | Evaluation |
| [可交互的 FAA 地面停飞地图](#case-148) | 电子表格与搜索 | 用时间线和地图展示停飞解除后队列为何仍存在. | Demo |
| [微缩宝塔庭院](#case-149) | 交互式 3D 与用户界面 | 检查生成的微缩场景如何平衡建筑和周边绿化. | Demo |
| [用不同模型做规划、执行与审阅](#case-150) | 智能体与编程工作流 | 分别指定规划、执行和审阅角色，并比较各模型的任务统计. | Demo |
| [Hydrogen 与 Sol 搭建雪中村庄](#case-151) | 对比与局限 | 在编程对比中分别记录耗时、费用和场景质量. | Evaluation |
| [High 与 Ultra 档制作 Three.js 岛屿](#case-152) | 对比与局限 | 比较画面和响应速度时，记录推理档并区分不同产品的额度. | Evaluation |
| [二战机场微缩景观](#case-153) | 交互式 3D 与用户界面 | 给 3D 演示提供参考资料与机械运动要求，检验外观之外的表现. | Demo |
| [在编程客户端配置 Hydrogen](#case-154) | 智能体与编程工作流 | 在受支持的客户端中配置 Google API 密钥时，填入准确的模型 ID. | Tutorial |
| [在 SuperARIS 科研团队中使用 Hydrogen](#case-155) | 智能体与编程工作流 | 在多模型团队中给 Hydrogen 分配明确的研究和论文任务. | Integration |
| [四款模型净室重写核心模块](#case-156) | 智能体与编程工作流 | 选择重写任务的代理时，分别比较代码库理解、设计与实现. | Evaluation |
| [对比 3D PS5 手柄细节](#case-157) | 对比与局限 | 比较手柄模型时检查按键阴影及背面硬件细节. | Evaluation |
| [Muse 把任务委派给 Antigravity CLI](#case-158) | 智能体与编程工作流 | 把远程助手连到本地编程环境，并设定默认写作模型. | Integration |
| [CursorBench 中的推理预算对照](#case-159) | 对比与局限 | 选择更快的默认档前，比较不同推理配置下的成功率. | Benchmark |
| [三款模型渲染星核圣殿](#case-160) | 对比与局限 | 在 3D 任务中分别观察渲染稳定性和画面细节. | Evaluation |
| [一分钟制作 HTML 射击游戏原型](#case-161) | 应用与学习 | 在一个 HTML 文件中测试射击游戏的基本输入与反馈循环. | Demo |
| [挑战现有的迁移方案](#case-162) | 对比与局限 | 让编程代理评估迁移是否需要替换现有架构. | Limit |
| [在 AITuber OnAir 让 Hydrogen 和用户对话](#case-163) | 应用与学习 | 试用 Hydrogen 驱动 Live2D 形象背后的聊天. | Integration |
| [纯代码制作宣传片](#case-164) | 应用与学习 | 给编程模型简短的宣传任务，查看生成的动态设计. | Demo |
| [两款模型制作神庙逃脱游戏](#case-165) | 对比与局限 | 在同一游戏概念中比较光照和氛围是否便于看清场景. | Evaluation |
| [三款 Gemini 模型制作拉力车动画](#case-166) | 对比与局限 | 检查车子通过带倾角的弯道时，悬挂运动和轮胎抓地是否合理. | Evaluation |
| [程序化生成的知更鸟飞行动画](#case-167) | 交互式 3D 与用户界面 | 检查生成飞行动画中的翅膀和身体动作. | Demo |
| [如何选择 Antigravity Orchestrator 或 Swarm](#case-168) | 智能体与编程工作流 | 让串行任务走模型交接，可并行任务交给独立工作和验证代理. | Tutorial |
| [两款模型制作 Chasing Views 动画](#case-169) | 对比与局限 | 比较输出和耗时，同时记录各自的推理档. | Evaluation |
| [Design Creativity Bench 的速度和费用](#case-170) | 对比与局限 | 查看创意评分时，一起比较单份设计的生成耗时与费用. | Benchmark |
| [从参考图建立 SolidWorks CAD 零件](#case-171) | 智能体与编程工作流 | 用 3D 参考图评估代理在 SolidWorks 里的建模流程. | Integration |
| [四款模型制作沙漠骏马动画](#case-172) | 对比与局限 | 先比较脚掌着地和重心转移，再看打光和网格细节. | Evaluation |
| [讲解荣格共时性的演示文稿](#case-173) | 应用与学习 | 用需要讲清相关概念的主题测试幻灯片生成流程. | Demo |
| [FrontierCS 2 计算机科学研究评测](#case-174) | 对比与局限 | 在常规编程测试之外使用研究基准，并记录运行环境. | Benchmark |
| [四款模型制作云端里约](#case-175) | 对比与局限 | 用同一个创意简报比较费用、耗时和主观质量. | Evaluation |
| [Hydrogen 在 GBENCH 技术任务中的表现](#case-176) | 对比与局限 | 评估技术工作时，把可核验的编程与非编程结果和价格、耗时一起比较. | Benchmark |
| [训练车辆侧方停车](#case-177) | 对比与局限 | 比较生成模拟中的学习进展和最终成功率. | Evaluation |
| [可操控的线粒体分子马达](#case-178) | 应用与学习 | 用交互图把分子运动和 ATP 产生联系起来. | Demo |
| [Qix 风格的抢地盘游戏](#case-179) | 应用与学习 | 用简短街机任务检验首轮输出是否实现可交互的游戏循环. | Demo |
| [用 Hydrogen 生成 HTML 幻灯片](#case-180) | 应用与学习 | 测试 HTML 生成速度时查看幻灯片的信息层次和布局. | Demo |
| [Hydrogen 在 Terminal-Bench 4.0 中的表现](#case-181) | 对比与局限 | 选命令行编程模型时，一起考虑基准完成率与任务费用. | Benchmark |
| [用单个 HTML 文件绘制插图](#case-182) | 交互式 3D 与用户界面 | 测试代码能否在没有外部素材的情况下重现参考视觉效果. | Demo |
| [三款 Gemini 模型制作章鱼动画](#case-183) | 对比与局限 | 观察触手抓住岩石后是否明显带动身体前进. | Evaluation |
| [用 Chrome 整理结构化 YouTube 摘要](#case-184) | 电子表格与搜索 | 请 Chrome 的 Gemini 面板提供带时间戳的视频摘要和有来源的背景资料. | Tutorial |
| [把课程做成短视频](#case-185) | 应用与学习 | 把一节课转换成视频时，检查解释准确性和节奏. | Demo |
| [从静态场景制作海鹦动画](#case-186) | 交互式 3D 与用户界面 | 把现有 HTML 场景用作程序化动画的首帧. | Demo |
| [一项城堡建模测试](#case-187) | 对比与局限 | 对比多次模型运行的城堡输出和资源用量. | Evaluation |
| [Antigravity Swarm 中的浏览器操作](#case-188) | 智能体与编程工作流 | 评估代理群组时，把浏览器活动和任务记录放在一起查看. | Demo |
| [经 Google Drive 把任务交给 Muse](#case-189) | 智能体与编程工作流 | 把研究结果交给第二个代理时，用受监控的 Drive 文件夹完成交接. | Integration |
| [Gemini Canvas 中的竖笛练习指南](#case-190) | 应用与学习 | 试用高速模式，将乐谱和演奏指引结合成练习工具. | Demo |
| [新增范围后项目估时大幅改变](#case-191) | 对比与局限 | 交付时间发生大幅变化时，要求模型说明项目范围与假设. | Limit |
| [Antigravity Swarm 制作鹈鹕动画](#case-192) | 智能体与编程工作流 | 把动画和声音任务交给编程代理群组，再检查合成的场景. | Demo |
| [考虑闰年边界的日历问题](#case-193) | 对比与局限 | 提出简单换算问题，检查答案是否考虑日历边界情况. | Evaluation |
| [一个 HTML 文件里的 TAJ VICE](#case-194) | 应用与学习 | 限定单文件制作可探索地图，然后测试剩余缺陷. | Demo |
| [通过 Google Cloud 项目连接 Antigravity](#case-195) | 智能体与编程工作流 | 用托管凭据启用 Hydrogen 时，检查代理认证和项目结算方式. | Tutorial |
| [回答引用了过时的订阅额度](#case-196) | 对比与局限 | 评估研究助手时，对照一手来源核实计划条款和模型名称. | Limit |
| [修改 WebGL 动画的叙事](#case-197) | 对比与局限 | 首版技术效果丰富却缺少清楚脉络时，要求增强叙事. | Limit |
| [Carbon 规划、Hydrogen 实现移动应用](#case-198) | 智能体与编程工作流 | 将交互设计分派给规划模型，再把实现工作交给执行模型. | Demo |
| [两款模型用代码制作山间斗龙](#case-199) | 对比与局限 | 比较同一场景中的两方角色互动. | Evaluation |
| [用一条提示词搭建 3D 微缩岛](#case-200) | 交互式 3D 与用户界面 | 检查一次生成的场景能否清楚安排地标、地形与水域. | Demo |
| [可复用的 Three.js 鹈鹕提示词](#case-201) | 对比与局限 | 检查骑行动画中腿、车轮和转向能否同步. | Evaluation |
| [在 T3 Code 中使用 Hydrogen](#case-202) | 智能体与编程工作流 | 在实际编程会话中试用客户端，跟踪滚动额度和周额度. | Integration |
| [手绘风公益短片](#case-203) | 应用与学习 | 用简短的公益主题评估手绘式视觉表现. | Demo |
| [孔雀骑车穿过十种艺术风格](#case-204) | 智能体与编程工作流 | 用混合模型代理群组用代码制作画面过渡并同步声音. | Demo |
| [同一个小屋任务在三种环境中运行](#case-205) | 对比与局限 | 把视觉任务迁移到不同模型档和平台时，检查输出格式. | Evaluation |
| [用同一提示词对比仪表盘](#case-206) | 对比与局限 | 用同一个前端提示词比较界面布局和信息层次. | Evaluation |
| [从参考图复刻 React.gg 网站](#case-207) | 应用与学习 | 从一张图开始复刻，再检查哪些细节还需要调整. | Demo |
| [奇点主题的交互面板](#case-208) | 交互式 3D 与用户界面 | 围绕一个视觉概念制作简短的交互片段. | Demo |
| [两款模型用代码制作横版动画](#case-209) | 对比与局限 | 比较生成的动作场景时，关注动作连续性和制作费用. | Evaluation |
| [让 Gemini 担任跑步教练](#case-210) | 应用与学习 | 把训练记录与模型建议对照，按自己的起点调整目标. | Demo |
| [成绩上链的浏览器游戏](#case-211) | 应用与学习 | 在桌面浏览器中测试游戏，同时单独验证成绩如何记录. | Demo |
| [日语回答里的数学公式未渲染](#case-212) | 对比与局限 | 回答含 TeX 指令时，同时检查内容和公式显示. | Limit |
| [从提示词到 MIDI 的作曲应用](#case-213) | 应用与学习 | 搭建从日语简报到 MIDI、WAV 和钢琴卷帘视图的工具原型. | Demo |
| [测试模型能否遵守保持沉默的指令](#case-214) | 对比与局限 | 流程要求不回复时，检查模型能否真正不产生答复. | Evaluation |
| [一页图文回顾演唱会](#case-215) | 应用与学习 | 把活动信息整理成易于浏览的一页视觉回顾. | Demo |
| [三款模型解释电动机原理](#case-216) | 对比与局限 | 在同一个模拟提示词下，比较画面清晰度与教学控件. | Evaluation |
| [两种模型工作流制作桌面动画](#case-217) | 对比与局限 | 对照原始任务检查画面细节、音量和片尾是否保持静止. | Evaluation |
| [从头像制作日常片段](#case-218) | 应用与学习 | 用一张参考头像和四个日常场景检验短分镜的改编. | Demo |
| [Hydrogen 为 ComfyUI 角色视频做规划](#case-219) | 应用与学习 | 固定服装与背景，在简报中变化角色表情与动作. | Integration |
| [把 Almance Vale 扩展到 100 个模块](#case-220) | 智能体与编程工作流 | 将已有应用移入编程代理，要求添加模块时保留既有风格. | Demo |
| [带程序化音效的 2D 村庄](#case-221) | 对比与局限 | 记录搭建耗时，并检查声音是否随画面中的事件变化. | Evaluation |
| [为歌曲制作宽屏视觉画面](#case-222) | 应用与学习 | 给模型一首歌与画幅要求，观察画面运动如何传递歌曲的能量. | Demo |
| [七个 Hydrogen 子代理搭建尼亚加拉瀑布](#case-223) | 智能体与编程工作流 | 给协调代理可分割的场景组件，让它把实现任务交给子代理. | Demo |
| [两段年代爱情短片的连续性](#case-224) | 应用与学习 | 让第二段短片延续第一段时，明确要保留哪些细节. | Demo |
| [Gemini 应用中的水球](#case-225) | 交互式 3D 与用户界面 | 用简单光学场景观察高光与折射的关系. | Demo |

<a id="agents"></a>
## ⚡ 智能体与编程工作流

<a id="case-1"></a>
### 案例 1: [在 Antigravity 中维护代码库](https://x.com/antigravity/status/2120944334023389476) (作者 [@antigravity](https://x.com/antigravity))

**使用范围明确的维护任务，同时评估编辑、工具使用和验证能力**

Antigravity 的发布演示展示 Hydrogen 维护代码库；这是平台制作的示例，并非独立复现的工程基准测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-2"></a>
### 案例 2: [并行构建十六个 Canvas 应用](https://x.com/shengzheyao/status/2120944141559550409) (作者 [@shengzheyao](https://x.com/shengzheyao))

**将构建工作拆分为独立模块，明确规划、实现和质量检查的角色**

Google DeepMind 的一位 Antigravity CLI 创作者介绍了由 Carbon 协调、验证和集成，由 Hydrogen 构建 16 个零依赖 canvas 小应用的流程；这是混合模型工作流，不能将结果仅归功于 Hydrogen

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-3"></a>
### 案例 3: [混合模型智能体群构建绯红飞蛾](https://x.com/thtbee_/status/2120958666480513310) (作者 [@thtbee_](https://x.com/thtbee_))

**为交互式创意编程项目分配独立的编排与实现角色**

创作者称 Carbon 编排 Antigravity 智能体群，Hydrogen 工作智能体构建绯红飞蛾作品；所述 45 分钟包含整个多模型工作流，未经独立计时

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-4"></a>
### 案例 4: [3D Medic 检查与修复](https://x.com/GoogleAI/status/2120940683233984862) (作者 [@GoogleAI](https://x.com/GoogleAI))

**探索能够检查 3D 文件、发现错误并在导出前提出修复方案的智能体**

Google AI 的 3D Medic 演示使用在 AI Studio 中构建的 Managed Agent 应用；它展示的是文件修复流程，不能证明任意 3D 资产都能被正确修复

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-5"></a>
### 案例 5: [在 Devin 中构建帆船场景](https://x.com/Da7_Tech/status/2120967690722677144) (作者 [@Da7_Tech](https://x.com/Da7_Tech))

**在你实际计划使用的编程智能体环境中评估模型**

来源展示了一个帆船场景，并称其由 Devin 中运行的 Hydrogen 构建；简短帖子没有公开完整提示词、迭代历史或可复现的配置

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-59"></a>
### 案例 59: [n8n 中的 Hydrogen 工具调用流程](https://x.com/n8n_io/status/2120947273534197886) (作者 [@n8n_io](https://x.com/n8n_io))

**让 Hydrogen 在 n8n 中处理工具调用循环，并单独安排规划步骤.**

n8n 介绍了 Hydrogen 支持情况，建议由 Carbon 或 Argon 规划、Hydrogen 执行，并在原帖附上集成设置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-12

---

<a id="case-69"></a>
### 案例 69: [多代理设置中的认证路径](https://x.com/studio_yebisu/status/2120969033260646551) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**代理委派给其他服务时，核对实际发起认证的是哪个客户端.**

作者报告，要求 Claude 通过 Antigravity CLI 使用 Hydrogen 后，Claude Code 直接尝试认证，随后 Antigravity 访问被暂停. 截图显示暂停通知，作者将原因归于客户端认证路径.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-12

---

<a id="case-70"></a>
### 案例 70: [一次 Antigravity Goal Mode 运行](https://x.com/Inmerson/status/2120973427788124345) (作者 [@Inmerson](https://x.com/Inmerson))

**长时间编程时，记录计划、代码修改与测试结果.**

作者报告在 Hydrogen Extra 的 Goal Mode 中运行 105 分钟，完成规划、实现和测试. 测试结果来自作者陈述.

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

类型: Demo | 日期: 2026-11-12

---

<a id="case-73"></a>
### 案例 73: [Antigravity Orchestrator 中的 Carbon 与 Hydrogen](https://x.com/Google/status/2120982566891356279) (作者 [@Google](https://x.com/Google))

**让规划模型在快速执行模型卡住时接手排障.**

Google 介绍由 Carbon 规划和处理卡点、Hydrogen 编辑与测试的流程，并报告 Terminal-Bench 4.0 成功率接近 Carbon，配额用量较低、耗时较短.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

类型: Integration | 日期: 2026-11-12

---

<a id="case-87"></a>
### 案例 87: [在 OpenClaw 中使用 Hydrogen](https://x.com/openclaw/status/2121098531205501401) (作者 [@openclaw](https://x.com/openclaw))

**检查计划采用的代理框架能否选用 Hydrogen.**

OpenClaw 宣布支持 Hydrogen 并附上截图. 原帖未提供基准评分或完整配置记录.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-13

---

<a id="case-97"></a>
### 案例 97: [用 Blender MCP 重建王座厅](https://x.com/ashen_one/status/2121165467821936651) (作者 [@ashen_one](https://x.com/ashen_one))

**用 Blender MCP 在编辑器中检查生成场景的构图.**

创作者将通过 Blender MCP 重建的《权力的游戏》铁王座大厅归功于 Hydrogen，并分享场景录屏.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

类型: Integration | 日期: 2026-11-13

---

<a id="case-113"></a>
### 案例 113: [浏览器 CAD 中的混凝土搅拌机装配](https://x.com/johnsanthosh01/status/2121243197901041869) (作者 [@johnsanthosh01](https://x.com/johnsanthosh01))

**把生成的装配体用于 CAD 工作流之前，检查部件树和配合情况.**

创作者报告，Hydrogen 在 CadX Studio 中根据一条提示词、用 40 分钟生成 265 个部件的搅拌机装配体，未逐件手工建模.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

类型: Integration | 日期: 2026-11-13

---

<a id="case-114"></a>
### 案例 114: [在 Blender 中程序化制作斧头](https://x.com/camperaigg/status/2121252572115951897) (作者 [@camperaigg](https://x.com/camperaigg))

**用轮廓参考图和多轮视口检查来审核程序化 Blender 资产.**

创作者报告在 Antigravity CLI 中用 Hydrogen 通过 Python 模块和反复视口检查制作风格化斧头. 计入录制耗时 51 分钟，报告 API 费用 $5.01.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-13

---

<a id="case-118"></a>
### 案例 118: [由 28 个模块组成的 Ember Isle](https://x.com/IamEmily2050/status/2121258646759952644) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**把大场景拆成模块，并记录每次生成的耗时.**

创作者用 Gemini 应用中的 Hydrogen High 制作 Ember Isle，称共 28 个模块，每个模块用一条提示词，每次 82 至 290 秒.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-150"></a>
### 案例 150: [用不同模型做规划、执行与审阅](https://x.com/naufaldi/status/2121499487999013081) (作者 [@naufaldi](https://x.com/naufaldi))

**分别指定规划、执行和审阅角色，并比较各模型的任务统计.**

作者安排 Opus 5.5 规划、Hydrogen 执行、Sol 后备及 Sol 6.1 审阅. 来源同时提供个人 Antigravity 用量与独立的公开基准对照.

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

类型: Demo | 日期: 2026-11-14

---

<a id="case-154"></a>
### 案例 154: [在编程客户端配置 Hydrogen](https://x.com/k2sbhai/status/2121509825658147041) (作者 [@k2sbhai](https://x.com/k2sbhai))

**在受支持的客户端中配置 Google API 密钥时，填入准确的模型 ID.**

作者介绍如何从 Google AI Studio 获取密钥，并在 OpenCode 或 Cline 选择 gemini-4-hydrogen. 使用资格和速率限制取决于服务商.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

类型: Tutorial | 日期: 2026-11-14

---

<a id="case-155"></a>
### 案例 155: [在 SuperARIS 科研团队中使用 Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**在多模型团队中给 Hydrogen 分配明确的研究和论文任务.**

来源展示安装 SuperARIS 和选择团队配置的步骤，建议 Hydrogen 或 Carbon 负责讨论和写作，并分别设置协调与实现角色. 案例展示集成流程，研究质量未经测量.

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

类型: Integration | 日期: 2026-11-14

---

<a id="case-156"></a>
### 案例 156: [四款模型净室重写核心模块](https://x.com/oasisfeng/status/2121523934831276203) (作者 [@oasisfeng](https://x.com/oasisfeng))

**选择重写任务的代理时，分别比较代码库理解、设计与实现.**

创作者对比 Hydrogen、Argon、GPT-6 Astra 和 Claude Opus 5.5 重写软件核心模块的结果，认为 Hydrogen 执行力强，其他运行则各有架构设计优势.

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

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-158"></a>
### 案例 158: [Muse 把任务委派给 Antigravity CLI](https://x.com/tetumemo/status/2121528823061852166) (作者 [@tetumemo](https://x.com/tetumemo))

**把远程助手连到本地编程环境，并设定默认写作模型.**

作者描述 Muse 把任务发到家中电脑上的 Antigravity CLI 并接收成果. 默认用 Hydrogen，也可选 Argon，示例有日语写作和视觉材料.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-14

---

<a id="case-168"></a>
### 案例 168: [如何选择 Antigravity Orchestrator 或 Swarm](https://x.com/ohayou792/status/2121624258984153452) (作者 [@ohayou792](https://x.com/ohayou792))

**让串行任务走模型交接，可并行任务交给独立工作和验证代理.**

作者用图解说明 Antigravity Orchestrator 如何先由前沿模型规划，再由 Hydrogen 实现，并与独立的 /swarm 协调模式对比，建议按任务依赖选择.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

类型: Tutorial | 日期: 2026-11-14

---

<a id="case-171"></a>
### 案例 171: [从参考图建立 SolidWorks CAD 零件](https://x.com/GoGoFly23/status/2121636952479080713) (作者 [@GoGoFly23](https://x.com/GoGoFly23))

**用 3D 参考图评估代理在 SolidWorks 里的建模流程.**

创作者报告，在 Antigravity 中给 Hydrogen 一张参考图后得到所展示的 SolidWorks 零件. 后续帖说明使用 SolidWorks MCP，几何公差和工程适用性尚未验证.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-14

---

<a id="case-188"></a>
### 案例 188: [Antigravity Swarm 中的浏览器操作](https://x.com/Saboo_Shubham_/status/2121852445756477924) (作者 [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**评估代理群组时，把浏览器活动和任务记录放在一起查看.**

Google 员工分享在 Antigravity Swarm 中使用 Hydrogen 和浏览器的截图. 来源未放出完整任务日志.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-15

---

<a id="case-189"></a>
### 案例 189: [经 Google Drive 把任务交给 Muse](https://x.com/nasuvit_z/status/2121857992702525734) (作者 [@nasuvit_z](https://x.com/nasuvit_z))

**把研究结果交给第二个代理时，用受监控的 Drive 文件夹完成交接.**

作者用 Hydrogen 收集信息并整理成 Drive 文件，再让 Muse 监听 Drive，在文件出现时接手后续任务. 图解展示了交接流程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-15

---

<a id="case-192"></a>
### 案例 192: [Antigravity Swarm 制作鹈鹕动画](https://x.com/chetaslua/status/2121885449509851415) (作者 [@chetaslua](https://x.com/chetaslua))

**把动画和声音任务交给编程代理群组，再检查合成的场景.**

创作者将多种艺术风格之间切换的 JavaScript 鹈鹕场景归功于 Carbon 与 Hydrogen，并称音乐和音效也由代码生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-195"></a>
### 案例 195: [通过 Google Cloud 项目连接 Antigravity](https://x.com/loganlu51268/status/2121911409042719023) (作者 [@loganlu51268](https://x.com/loganlu51268))

**用托管凭据启用 Hydrogen 时，检查代理认证和项目结算方式.**

作者记录通过应用默认凭据将 Antigravity 从个人计划切换到 Google Cloud Agent Platform 项目. 模型选择器包含 Hydrogen，来源还介绍按 SKU 检查项目花费.

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

类型: Tutorial | 日期: 2026-11-15

---

<a id="case-198"></a>
### 案例 198: [Carbon 规划、Hydrogen 实现移动应用](https://x.com/thebuggeddev/status/2121945961555718334) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**将交互设计分派给规划模型，再把实现工作交给执行模型.**

创作者称 Carbon 规划了手机应用，Hydrogen 实现了应用及 Reanimated 物理动效. 作者描述动作流畅，并分享录屏.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-202"></a>
### 案例 202: [在 T3 Code 中使用 Hydrogen](https://x.com/bei351009016/status/2121964293906206916) (作者 [@bei351009016](https://x.com/bei351009016))

**在实际编程会话中试用客户端，跟踪滚动额度和周额度.**

作者称把 Gemini Pro 接入 T3 Code，用 Hydrogen 处理了约半天任务. 截图和原帖记录额度体验，作者分别评价了速度与准确性.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

类型: Integration | 日期: 2026-11-15

---

<a id="case-204"></a>
### 案例 204: [孔雀骑车穿过十种艺术风格](https://x.com/SahilPanhotra/status/2121995488425849064) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**用混合模型代理群组用代码制作画面过渡并同步声音.**

创作者将跨十种艺术风格的孔雀骑车动画归功于 Carbon 和 Hydrogen 的代理群组，并称画面、音乐和音效都由代码制作.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-220"></a>
### 案例 220: [把 Almance Vale 扩展到 100 个模块](https://x.com/IamEmily2050/status/2122257581175410858) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**将已有应用移入编程代理，要求添加模块时保留既有风格.**

创作者把 Almance Vale 从 Gemini 应用迁入 Antigravity，报告在 swarm 模式中用 Hydrogen Extra 遵循原有代码约定，数小时扩展到 100 个模块.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

类型: Demo | 日期: 2026-11-16

---

<a id="case-223"></a>
### 案例 223: [七个 Hydrogen 子代理搭建尼亚加拉瀑布](https://x.com/SahilPanhotra/status/2122311637684424737) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**给协调代理可分割的场景组件，让它把实现任务交给子代理.**

作者将不到一小时、按一条提示词搭建的尼亚加拉瀑布体验归功于 Carbon 与七个 Hydrogen 子代理. 录屏可见水体、游船、多种视角与环境变化.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

类型: Demo | 日期: 2026-11-16

---


<a id="apps-learning"></a>
## 💻 应用与学习

<a id="case-6"></a>
### 案例 6: [Lingo City 语言练习](https://x.com/tulseedoshi/status/2121095754844713427) (作者 [@tulseedoshi](https://x.com/tulseedoshi))

**结合记忆卡片与交互式街景，进行情境化语言练习**

Tulsee Doshi 分享了 Google 的示例：流式生成定制 2D 和 3D 记忆卡片，并让学习者在虚拟城市中练习与店主对话；这是服务商演示，并非独立的学习效果研究

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-7"></a>
### 案例 7: [《罗密欧与朱丽叶》3D 纸剧场](https://x.com/techartist_/status/2120957446202253803) (作者 [@techartist_](https://x.com/techartist_))

**将具体课程转化为具有明确学习目标的交互场景**

创作者为 GCSE 英语文学课程构建了关于《罗密欧与朱丽叶》阳台场景的 3D 纸剧场课程；来源展示了界面，但未衡量学习效果

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-8"></a>
### 案例 8: [从设计图到阅读网站](https://x.com/thebuggeddev/status/2120952661046689992) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**使用参考设计评估视觉理解和可运行前端的实现能力**

创作者称 Hydrogen 用 5 分 27 秒将设计图转化为可运行的阅读管理网站；耗时与完整性均为来源方说法，本合集未进行独立功能测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-9"></a>
### 案例 9: [用二十个模块构建锦鲤庭院](https://x.com/IamEmily2050/status/2120951069874532806) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**用小模块构建较大场景，而非期待一次提示就得到完整结果**

创作者称在 Gemini 应用中用 20 条提示词构建了 20 个模块，每个模块耗时 90–270 秒；作者披露获得了提前访问权限，这一示例明确采用迭代流程，而非一次生成

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-10"></a>
### 案例 10: [质子聚变学习游戏](https://x.com/SidraMiconi/status/2120948703095820743) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**为科学过程制作交互式讲解原型，然后核查其中的科学内容**

创作者的游戏演示年轻恒星内部的质子–质子链反应；所述单条提示词、78 秒运行时间以及约 $0.19 费用均为来源方说法，未经独立复现

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-58"></a>
### 案例 58: [15 分钟搭建 Minecraft 风格原型](https://x.com/RezAIT00/status/2120947124418293876) (作者 [@RezAIT00](https://x.com/RezAIT00))

**用体素沙盒检验挖掘、背包等生成系统能否协同工作.**

创作者报告用 Hydrogen Extra High 在 15 分钟内搭建 Minecraft 风格原型，列出的功能包括放置、挖掘和背包. 录屏只覆盖部分功能.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-77"></a>
### 案例 77: [把新闻简报制作成带旁白的短片](https://x.com/gigabit_million/status/2121011957042163722) (作者 [@gigabit_million](https://x.com/gigabit_million))

**先查资料，再将新闻简报做成旁白短片并核查其中的事实.**

录屏显示 Hydrogen 在 Gemini 手机应用中查询近期新闻、起草提纲，创作者随后要求制作视频. 视频在应用内播放，时长十秒. 耗时与旁白由创作者报告，渲染后端未说明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-90"></a>
### 案例 90: [摄像头空中绘画工具](https://x.com/CodeByPoonam/status/2121121804483969102) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**在镜头前比画笔画，观察绘图界面如何跟随.**

创作者报告在 Hydrogen 早期试用期间搭建了摄像头空中绘画工具，并分享演示录屏.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-93"></a>
### 案例 93: [一次生成的网站门户](https://x.com/kimura_0314/status/2121130305532878979) (作者 [@kimura_0314](https://x.com/kimura_0314))

**先用门户布局检查首轮界面，再测试各条操作流程.**

作者展示在 Antigravity 中用 Hydrogen 一次生成的门户截图. 截图只能用于查看页面外观.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-13

---

<a id="case-95"></a>
### 案例 95: [《城市：天际线》风格建城工具](https://x.com/yohakujpn/status/2121146464466604147) (作者 [@yohakujpn](https://x.com/yohakujpn))

**搭建城市模拟原型，观察控件和模拟逻辑如何配合.**

创作者把视频中的《城市：天际线》风格原型归功于 Hydrogen，并报告生成用时不到 30 分钟.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-124"></a>
### 案例 124: [把化学教材做成交互课程](https://x.com/smalkalbani/status/2121282231759155617) (作者 [@smalkalbani](https://x.com/smalkalbani))

**用提示、语音引导和可选文本搭建自学课程.**

作者展示带语音引导和提示的九年级化学课程. 演示未测量学习成效.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-125"></a>
### 案例 125: [一首 Vocaloid 歌曲原型](https://x.com/peach2k2/status/2121284159565902188) (作者 [@peach2k2](https://x.com/peach2k2))

**检查一次生成的曲目能否符合指定角色和风格.**

作者分享一段歌曲，将作曲归功于 Hydrogen. 来源未说明用什么工具渲染音频.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-134"></a>
### 案例 134: [从图片读取复杂积分式](https://x.com/HarshithLucky3/status/2121303778548908228) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**化简长表达式前，检查模型能否识别积分上下限相同.**

创作者录下 Gemini 应用中的 Hydrogen High 对复杂积分截图作答. 测试重点是模型能否识别外层积分的相同上下限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-138"></a>
### 案例 138: [用 WebGL2 制作人体细胞百科](https://x.com/soumyadesign/status/2121354542344466565) (作者 [@soumyadesign](https://x.com/soumyadesign))

**通过交互剖面讲解细胞内部的空间关系.**

创作者报告在 Antigravity 中用 Hydrogen 搭建 3D 人体细胞百科，使用 WebGL2、无外部库，并重点展示了剖面视图.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-140"></a>
### 案例 140: [Parking Bench 中只看图的对手](https://x.com/agenticjay/status/2121391300822081713) (作者 [@agenticjay](https://x.com/agenticjay))

**只给益智游戏对手棋盘图片，测试它如何读取局面.**

创作者称游戏由 Carbon 搭建，玩家在五关中通过 API 对战 Hydrogen 或 Gemini Decision 1. 两款模型都只接收棋盘 PNG，不接收网格状态数据.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

类型: Integration | 日期: 2026-11-13

---

<a id="case-141"></a>
### 案例 141: [Google 文档的操作教学视频](https://x.com/nin222/status/2121395008863621390) (作者 [@nin222](https://x.com/nin222))

**用屏幕截图和编号标注讲解手机端的编辑步骤.**

作者将一段 Google 文档手机端教程归功于 Hydrogen. 抽样画面显示加注的选取文字、样式、颜色、字体及保存步骤. 来源未说明剪辑方式.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-146"></a>
### 案例 146: [为 MZ-1500 搭建 BASIC 环境](https://x.com/hiromsa/status/2121465784715338065) (作者 [@hiromsa](https://x.com/hiromsa))

**搭建复古 BASIC 环境原型，并逐一核对外设支持.**

作者将演示归功于 Hydrogen，报告用时约 15 分钟. 演示列出 PCG、PSG 与 QuickDisk 支持，其中 QuickDisk 仅支持 LOAD.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-14

---

<a id="case-161"></a>
### 案例 161: [一分钟制作 HTML 射击游戏原型](https://x.com/SahilPanhotra/status/2121561371951399133) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**在一个 HTML 文件中测试射击游戏的基本输入与反馈循环.**

创作者报告 Hydrogen 按一条提示词在一分钟内生成了可玩的射击游戏. 项目只用一个 HTML 文件，无框架或额外设置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-163"></a>
### 案例 163: [在 AITuber OnAir 让 Hydrogen 和用户对话](https://x.com/shinshin86/status/2121571590442017094) (作者 [@shinshin86](https://x.com/shinshin86))

**试用 Hydrogen 驱动 Live2D 形象背后的聊天.**

项目维护者公布 AITuber OnAir 的 Hydrogen 支持，并提供含 Live2D 在内的对话形象示例. 录屏展示了集成效果.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

类型: Integration | 日期: 2026-11-14

---

<a id="case-164"></a>
### 案例 164: [纯代码制作宣传片](https://x.com/xiangning0/status/2121594643540480293) (作者 [@xiangning0](https://x.com/xiangning0))

**给编程模型简短的宣传任务，查看生成的动态设计.**

作者展示一段以 GPT-6.2 Astra 为主题的宣传片，称 Hydrogen 完全用代码制作. 视频展示了代码制作的输出.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-173"></a>
### 案例 173: [讲解荣格共时性的演示文稿](https://x.com/soumyadesign/status/2121676345835241916) (作者 [@soumyadesign](https://x.com/soumyadesign))

**用需要讲清相关概念的主题测试幻灯片生成流程.**

作者将介绍卡尔·荣格共时性和非因果秩序的幻灯片归功于 Hydrogen 与自定义工具，称工具在 Antigravity 中开发，并分享部分输出.

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

类型: Demo | 日期: 2026-11-14

---

<a id="case-178"></a>
### 案例 178: [可操控的线粒体分子马达](https://x.com/SidraMiconi/status/2121745863827697687) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**用交互图把分子运动和 ATP 产生联系起来.**

作者称 Hydrogen High 按一条提示词生成 ATP 合酶应用，随后修正镜头. 模型外形以冷冻电镜坐标为基础，运动过程经过简化.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-179"></a>
### 案例 179: [Qix 风格的抢地盘游戏](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (作者 [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**用简短街机任务检验首轮输出是否实现可交互的游戏循环.**

创作者在免费 Gemini 界面请求制作 Qix 风格的抢地盘游戏，分享演示、标记 Hydrogen，并报告只用了一个请求.

**提示词:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-180"></a>
### 案例 180: [用 Hydrogen 生成 HTML 幻灯片](https://x.com/yamachan_ai_log/status/2121772023710118043) (作者 [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**测试 HTML 生成速度时查看幻灯片的信息层次和布局.**

作者展示 Hydrogen 生成 HTML 幻灯片的过程，认为速度快、细节充分. 录屏展示文稿，原帖未给出对照计时.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-185"></a>
### 案例 185: [把课程做成短视频](https://x.com/smalkalbani/status/2121844887033458954) (作者 [@smalkalbani](https://x.com/smalkalbani))

**把一节课转换成视频时，检查解释准确性和节奏.**

创作者将课程工作流归功于 Hydrogen，并发布两个片段. 实际负责渲染视频的系统未得到确认.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-190"></a>
### 案例 190: [Gemini Canvas 中的竖笛练习指南](https://x.com/nin222/status/2121877676042682538) (作者 [@nin222](https://x.com/nin222))

**试用高速模式，将乐谱和演奏指引结合成练习工具.**

视频展示在 Hydrogen 高速模式下制作的 Canvas 竖笛应用. 创作者称也可以导入乐谱生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-194"></a>
### 案例 194: [一个 HTML 文件里的 TAJ VICE](https://x.com/SahilPanhotra/status/2121909681514074328) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**限定单文件制作可探索地图，然后测试剩余缺陷.**

创作者称用 Hydrogen 在不足 12 小时的会话中制作了受 GTA 启发、以虚构阿格拉为背景的游戏. 项目使用纯 JavaScript 和一个 HTML 文件，无外部资产，仍有玩法缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-203"></a>
### 案例 203: [手绘风公益短片](https://x.com/shengtang135754/status/2121965385356612020) (作者 [@shengtang135754](https://x.com/shengtang135754))

**用简短的公益主题评估手绘式视觉表现.**

创作者分享一段手绘风格的公益短片并归功于 Gemini 4 Hydrogen. 一次成片来自作者陈述，渲染模型和制作步骤未公开.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-207"></a>
### 案例 207: [从参考图复刻 React.gg 网站](https://x.com/thebuggeddev/status/2122019549117911473) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**从一张图开始复刻，再检查哪些细节还需要调整.**

创作者报告给 Hydrogen 一张参考图，通过少量提示复刻 React.gg. 来源链接了演示，并说明还有细节不一致.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-210"></a>
### 案例 210: [让 Gemini 担任跑步教练](https://x.com/ivanleomk/status/2122036783307469199) (作者 [@ivanleomk](https://x.com/ivanleomk))

**把训练记录与模型建议对照，按自己的起点调整目标.**

创作者将跑步指导归功于 Gemini Hydrogen，分享了训练截图，并称完成约一年以来最长的一次跑步. 这是个人使用案例.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-15

---

<a id="case-211"></a>
### 案例 211: [成绩上链的浏览器游戏](https://x.com/itshoseyn/status/2122063851143246140) (作者 [@itshoseyn](https://x.com/itshoseyn))

**在桌面浏览器中测试游戏，同时单独验证成绩如何记录.**

创作者称 Hydrogen 协助搭建与 Base 相连、把成绩写入链上的 Sheytonak 游戏. 来源称为桌面做了优化，移动端仍有问题，游戏也尚有缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-213"></a>
### 案例 213: [从提示词到 MIDI 的作曲应用](https://x.com/Awed_Urshy/status/2122161392828727738) (作者 [@Awed_Urshy](https://x.com/Awed_Urshy))

**搭建从日语简报到 MIDI、WAV 和钢琴卷帘视图的工具原型.**

创作者用 Hydrogen 搭建应用，将日语输入转成英文音乐提示词，写出 MIDI、渲染 WAV，再生成钢琴卷帘视频. 以上是演示应用的功能.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

类型: Demo | 日期: 2026-11-16

---

<a id="case-215"></a>
### 案例 215: [一页图文回顾演唱会](https://x.com/fukubaya/status/2122215495474794640) (作者 [@fukubaya](https://x.com/fukubaya))

**把活动信息整理成易于浏览的一页视觉回顾.**

作者分享 Batten Girls 演唱会的日语图文回顾，将总结归功于 Hydrogen. 来源未展示完整素材或提示词.

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

类型: Demo | 日期: 2026-11-16

---

<a id="case-218"></a>
### 案例 218: [从头像制作日常片段](https://x.com/antiAIvo/status/2122251181112353276) (作者 [@antiAIvo](https://x.com/antiAIvo))

**用一张参考头像和四个日常场景检验短分镜的改编.**

创作者提供 X 头像及学习、吃饭、看手机、运动四个场景，发布约十秒的成果并归因于 Hydrogen，未说明视频渲染后端.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

类型: Demo | 日期: 2026-11-16

---

<a id="case-219"></a>
### 案例 219: [Hydrogen 为 ComfyUI 角色视频做规划](https://x.com/nyapan_mohy/status/2122253350808744004) (作者 [@nyapan_mohy](https://x.com/nyapan_mohy))

**固定服装与背景，在简报中变化角色表情与动作.**

创作者称 Hydrogen 围绕参考角色设计规划短片，通过另一套 ComfyUI MiniMax 图生视频流程渲染，并为变体准备新首帧和含 30 个镜头的提示词.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

类型: Integration | 日期: 2026-11-16

---

<a id="case-222"></a>
### 案例 222: [为歌曲制作宽屏视觉画面](https://x.com/ivy432hz/status/2122283590180589791) (作者 [@ivy432hz](https://x.com/ivy432hz))

**给模型一首歌与画幅要求，观察画面运动如何传递歌曲的能量.**

创作者称只给 Hydrogen XHigh 一首歌，要求 21:9 画幅和速度感. 视频展示高速移动的道路场景，来源未说明渲染流程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

类型: Demo | 日期: 2026-11-16

---

<a id="case-224"></a>
### 案例 224: [两段年代爱情短片的连续性](https://x.com/AvaSinclairAi_/status/2122315627113107670) (作者 [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**让第二段短片延续第一段时，明确要保留哪些细节.**

创作者将远洋客轮上的爱情场景归功于使用 Hydrogen 的 Gemini 工作流，公开了要求保持角色与服装连续的两段简报. 底层视频模型未说明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

类型: Demo | 日期: 2026-11-16

---


<a id="data-search"></a>
## 📊 电子表格与搜索

<a id="case-11"></a>
### 案例 11: [Google Sheets 中的动态风景](https://x.com/Google/status/2121004369617485896) (作者 [@Google](https://x.com/Google))

**通过非常规的电子表格动画，检查生成代码和单元格级更新**

Google 展示了用 Antigravity 编写代码，将海岸列车、云朵与秋叶绘制在表格单元格中的效果；这是官方创意演示，并非电子表格性能基准测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-12"></a>
### 案例 12: [Folio 交互式数据网站](https://x.com/vamsibatchuk/status/2120996342923436188) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**在小型网站原型中结合落地页布局与交互式数据可视化**

一位 Google DeepMind 员工展示了使用 Google AI Studio 构建的 Folio 风格网站和交互动画；帖子未提供完整生成提示词或独立功能测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-13"></a>
### 案例 13: [多部分搜索问题的可视化回答](https://x.com/Google/status/2120960715011883148) (作者 [@Google](https://x.com/Google))

**测试细致且具有多项约束的搜索请求时，对比回答布局与引用链接**

Google 的搜索示例结合了意图理解、视觉布局、对比表格和查询扩展；这些属于服务商描述的产品行为，演示并未证明对发布者排名或流量的影响

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-14"></a>
### 案例 14: [Sheets 中的交互式财务预测](https://x.com/ChanduThota/status/2120942270627414079) (作者 [@ChanduThota](https://x.com/ChanduThota))

**构建假设清晰可见的财务模型原型，并检查生成的公式与图表**

Chandu Thota 展示了 Google Sheets 预测演示；来源所称 canvas 生成速度提升超过 30% 属于服务商说法，并非本仓库进行的受控计时测量

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-60"></a>
### 案例 60: [Box Agent 处理复杂企业文档](https://x.com/levie/status/2120947988143198302) (作者 [@levie](https://x.com/levie))

**在接近真实的文档任务中同时检查准确率、耗时和 Token 用量.**

Box 报告，在早期试用评测的典型任务中，相比 Gemini 3.8 Flash，Hydrogen 准确率提高五个百分点、耗时不到一半、Token 约少 12%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-74"></a>
### 案例 74: [从 Workspace 数据生成图表和报告](https://x.com/nin222/status/2120989168247652674) (作者 [@nin222](https://x.com/nin222))

**检查追问一轮能否补齐分析、图表或报告.**

创作者在 Google Workspace for Education Fundamentals 演示环境中用 Hydrogen 分析数据、生成图表并输出报告文件，称共进行了两轮交流.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-12

---

<a id="case-81"></a>
### 案例 81: [用不同 Gemini 模式在表格里画像素画](https://x.com/kkitase/status/2121041283640926401) (作者 [@kkitase](https://x.com/kkitase))

**用同一个 Google 表格绘图任务比较不同模型选项.**

创作者录下 Hydrogen 在 Google 表格中绘制像素画的过程，并附上 Antigravity Orchestrator、Carbon 和 Argon 的独立运行. 该创作者演示未采用正式评分标准.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-148"></a>
### 案例 148: [可交互的 FAA 地面停飞地图](https://x.com/SidraMiconi/status/2121486870341370204) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**用时间线和地图展示停飞解除后队列为何仍存在.**

创作者报告用 Hydrogen 在 222 秒内制作了可操作的 FAA 运行中断地图，并纠正一处标签. 时间线依据官方通报，交通流量则按常规时刻表模拟.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-184"></a>
### 案例 184: [用 Chrome 整理结构化 YouTube 摘要](https://x.com/studio_yebisu/status/2121835594674561098) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**请 Chrome 的 Gemini 面板提供带时间戳的视频摘要和有来源的背景资料.**

日语原帖演示如何在 Chrome 的 Gemini 面板总结当前打开的 YouTube 视频. 公开提示词要求简述、要点、章节流程、单独注明出处的背景、事实核查与延伸资料.

**提示词:**

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

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

类型: Tutorial | 日期: 2026-11-15

---


<a id="interactive-3d"></a>
## 🎮 交互式 3D 与用户界面

<a id="case-15"></a>
### 案例 15: [交互式餐厅](https://x.com/notjazii/status/2120979811569222137) (作者 [@notjazii](https://x.com/notjazii))

**检查物体交互、照明和状态变化，而不是仅凭静态图片评判场景**

创作者展示了一间餐厅，其中的灯光、台灯、冰箱及内部物品均可交互；所述 30 分钟构建时间未经独立验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-16"></a>
### 案例 16: [带微缩世界的音量滑块](https://x.com/vib3coded/status/2120973294090555890) (作者 [@vib3coded](https://x.com/vib3coded))

**通过一个熟悉的控件，同时测试交互设计与动画场景细节**

来源展示了一个能让微型日式世界动起来的音量滑块；创作者称费用为 $0.19，但未提供账单或完整生成流程

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-17"></a>
### 案例 17: [Three.js 日式住宅](https://x.com/SPAC89/status/2120972954146140409) (作者 [@SPAC89](https://x.com/SPAC89))

**评估细致的 3D 漫游时，将代码生成时间与渲染时间分开**

创作者称该住宅和庭院由 Hydrogen 使用 Three.js 构建，未使用智能体；帖子关于订阅用量和不到两小时的说法仅适用于作者的配置，并非通用的价格或延迟保证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-18"></a>
### 案例 18: [骑自行车的 3D 鹈鹕](https://x.com/nehstrr3/status/2120953932692537722) (作者 [@nehstrr3](https://x.com/nehstrr3))

**使用运动角色检查协调性、动作和场景一致性**

创作者展示了一只骑自行车的 3D 动画鹈鹕，并标注模型为 XHigh 级别的 Hydrogen；帖子展示的是输出成果，并未提供完整可复现提示词或物理验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-19"></a>
### 案例 19: [规划优先的行星模拟器](https://x.com/The_Alex/status/2120950301318582643) (作者 [@The_Alex](https://x.com/The_Alex))

**让编程模型编辑复杂场景之前，先给出具体计划**

获得提前访问权限的创作者展示了行星模拟器，并称提供更详细计划后编辑效果有所改善；来源注明创意来自 ForwardEditor，并描述了迭代工作流

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-20"></a>
### 案例 20: [用 Antigravity Swarm 构建港湾岛屿](https://x.com/ai_for_success/status/2120942147780464660) (作者 [@ai_for_success](https://x.com/ai_for_success))

**通过可导航的小型环境，检查多智能体构建场景的行为**

创作者披露获得了提前访问权限，并展示了在 Antigravity 的 Swarm 功能中使用 Hydrogen 构建的港湾岛屿；公开帖子没有说明完整编排过程或提示词历史

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-21"></a>
### 案例 21: [埃菲尔铁塔浮空岛](https://x.com/RezAIT00/status/2120940988780736973) (作者 [@RezAIT00](https://x.com/RezAIT00))

**通过紧凑的地标场景评估构图、镜头运动和模型生成的代码**

来源展示了埃菲尔铁塔微缩岛屿，并称其由 Hydrogen XHigh 构建；构建加录制耗时六分钟是作者自述，并非独立计时测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-22"></a>
### 案例 22: [可飞行的未来城市](https://x.com/kimmonismus/status/2120940617169826037) (作者 [@kimmonismus](https://x.com/kimmonismus))

**测试对程序化世界的后续编辑，不要假定首次输出就是最终结果**

获得提前访问权限的创作者在 Antigravity 中使用 Hydrogen High，并称经过一次后续提示，生成了包含程序化高楼、雨景和飞行交通的 Three.js 城市；录像展示的是生成代码的运行效果，而非原生视频生成

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-23"></a>
### 案例 23: [从日出到夜晚的水上飞机](https://x.com/LuminaBench/status/2120939312564842663) (作者 [@LuminaBench](https://x.com/LuminaBench))

**检查交互式 3D 场景中的环境控制与光照过渡**

LuminaBench 的原创演示展示了水上飞机与一天中时间的变化，之后被 Google 转发；帖子早于记录中的公开发布界限；其访问途径和模型调用未经独立验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-41"></a>
### 案例 41: [把太空参考图做成 HTML 场景](https://x.com/Inmerson/status/2120482539907559651) (作者 [@Inmerson](https://x.com/Inmerson))

**用少量参考图检验生成场景能否呈现可辨识的视觉风格.**

创作者将太空可视化归功于 Hydrogen，展示了输入的行星图片和带有行星环的 HTML 场景.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-11

---

<a id="case-42"></a>
### 案例 42: [Gemini Canvas 中的一级方程式赛车原型](https://x.com/auricxofficial/status/2120843585914605830) (作者 [@auricxofficial](https://x.com/auricxofficial))

**给车辆查看器设置几个镜头，从不同角度检查生成模型.**

创作者将一款一级方程式赛车查看器归功于首次使用 Canvas 中的 Hydrogen. 录屏显示多个预设镜头和悬挂系统视图.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-48"></a>
### 案例 48: [用 SVG 绘制宝马侧视图](https://x.com/HarshithLucky3/status/2120932649938382894) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**用车辆 SVG 侧视图检查比例、轮廓和细节.**

作者展示一张宝马 M4 CS 的 SVG 侧视图，归因于 Gemini 应用中的 Hydrogen High，并报告生成不到 30 秒.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-12

---

<a id="case-49"></a>
### 案例 49: [天文学家的浮空岛](https://x.com/pankajkumar_dev/status/2120933196221333791) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**给小场景设定明确主题，再检查物件和光照能否强化主题.**

创作者把天文学家浮空岛归因于 Arena 上的 Hydrogen 检查点，并报告生成用时四分钟. 归因限于此次 Arena 运行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-50"></a>
### 案例 50: [把参考图做成可游览的 3D 地形](https://x.com/HarshithLucky3/status/2120935535422374055) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**检查图生场景能否同时还原视觉元素并支持移动.**

创作者展示 Gemini 应用中归因于 Hydrogen 的可操作 3D 地形，并介绍了 GLSL 反射、程序化几何和游泳物理.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-51"></a>
### 案例 51: [用 3D 积木搭建微缩景观](https://x.com/abhinavflac/status/2120936501961969990) (作者 [@abhinavflac](https://x.com/abhinavflac))

**让模型搭建积木微缩景观，检查各形体能否组成完整场景.**

创作者分享了 3D 积木微缩景观的录屏，并将其归功于 Hydrogen. 来源未披露搭建耗时和具体运行设置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-52"></a>
### 案例 52: [可交互的樱花树](https://x.com/hakmgpt/status/2120936640436642231) (作者 [@hakmgpt](https://x.com/hakmgpt))

**用一件带动效的物体和几个控件探索微缩场景的实时变化.**

创作者将截图中的樱花树界面归功于 Hydrogen. 截图可见场景设置控件，实现细节未公开.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-12

---

<a id="case-62"></a>
### 案例 62: [小型交互动画中的光线折射](https://x.com/chanelluuh/status/2120951519470399710) (作者 [@chanelluuh](https://x.com/chanelluuh))

**先快速预览并调整光学效果，再增加场景复杂度.**

创作者将 Small Delights 系列的一段互动小动画归功于 Hydrogen，特地展示折射效果，并介绍了逐步迭代的创作过程.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-63"></a>
### 案例 63: [一条向上流的河](https://x.com/xKaka1456/status/2120952404225265983) (作者 [@xKaka1456](https://x.com/xKaka1456))

**选择运动方向不同寻常的小场景，观察视觉效果.**

作者报告在网页端用 Hydrogen 做出倒流河流并分享录屏. 耗时和订阅额度用量为作者自己的观察.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

类型: Demo | 日期: 2026-11-12

---

<a id="case-67"></a>
### 案例 67: [Hydrogen 生成的 3D 肖像](https://x.com/soyamiruku/status/2120959893943251322) (作者 [@soyamiruku](https://x.com/soyamiruku))

**用肖像做小型测试，检查 3D 表现能否保留可辨识的主体特征.**

作者把为原帖所提人物制作的 3D 肖像归因于 Hydrogen，并分享了结果图. 来源提供的运行细节有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

类型: Demo | 日期: 2026-11-12

---

<a id="case-82"></a>
### 案例 82: [把参考图中的公寓做成 3D 打印件](https://x.com/bijanbowen/status/2121042010928709932) (作者 [@bijanbowen](https://x.com/bijanbowen))

**把图生 3D 的测试延伸到打印实物.**

作者分享《宋飞正传》公寓的参考图和打印实物，将该公寓模型归因于 Hydrogen.

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

类型: Demo | 日期: 2026-11-13

---

<a id="case-86"></a>
### 案例 86: [黄金梅丽号海上场景](https://x.com/xKaka1456/status/2121063351136739388) (作者 [@xKaka1456](https://x.com/xKaka1456))

**用辨识度高的虚构船只测试风格化海景的构图.**

创作者将黄金梅丽号场景归功于 Hydrogen，并分享了船在蓝色海面上的视频. 原帖未说明提示词、工具设置和迭代次数.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-88"></a>
### 案例 88: [游过云海的鲸鱼](https://x.com/xKaka1456/status/2121100318150898144) (作者 [@xKaka1456](https://x.com/xKaka1456))

**通过一个代码制作的生物场景分别检查流体运动和眼睛设计.**

来源展示了代码制作的云海鲸鱼，报告 Hydrogen 用时约两分钟. 速度和配额用量来自作者观察.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-92"></a>
### 案例 92: [Gemini Canvas 里的海底城市](https://x.com/ayyh_18/status/2121128385690693821) (作者 [@ayyh_18](https://x.com/ayyh_18))

**从小型 3D 场景起步，通过多轮迭代加入可探索的区域和会动的生物.**

创作者在 Gemini 应用内多轮迭代，搭建了有鱼群、水母、珊瑚和可游览玻璃穹顶的海底城市. 来源明确提到使用多条提示词.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-99"></a>
### 案例 99: [Three.js 灰阶海盗船](https://x.com/parves075/status/2121172856889618528) (作者 [@parves075](https://x.com/parves075))

**将 Three.js 场景限定为灰阶，检查光照还能否突出几何形状.**

作者在 Antigravity 中用 Hydrogen 搭建 Three.js 灰阶海盗船，录屏用于展示光照和 3D 细节.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-101"></a>
### 案例 101: [CadXStudio 中的参数化台灯](https://x.com/CadX_Studio/status/2121175785356853312) (作者 [@CadX_Studio](https://x.com/CadX_Studio))

**检查 CAD 模型中的组件尺寸和可编辑性.**

工具提供方 CadXStudio 展示了浏览器里的台灯模型，称包含 35 个可编辑零件.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

类型: Integration | 日期: 2026-11-13

---

<a id="case-102"></a>
### 案例 102: [用 C++ 制作神社参道动画](https://x.com/nehstrr3/status/2121184399245128137) (作者 [@nehstrr3](https://x.com/nehstrr3))

**用小型原生代码场景检验模型能否在没有 Web 技术栈时写出可运行动画.**

创作者将穿过神社鸟居的参道动画归功于 Hydrogen Extra High，并称由自编 C++ 实现.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-105"></a>
### 案例 105: [用 30 个模块搭建城镇场景](https://x.com/IamEmily2050/status/2121200010574598655) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**按模块分别提示模型，再检查组装后的整体效果.**

作者称使用 Gemini 应用中的 Hydrogen High，每个模块用一条提示词，共制作 30 个模块.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-108"></a>
### 案例 108: [浮空岛上的邮局](https://x.com/pankajkumar_dev/status/2121220537984954448) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**指定一种微缩建筑，观察材质和光照如何表现主题.**

作者请 Hydrogen 在浮空岛上搭建一座 3D 微缩邮局，分享录屏并指出其中的纹理、颜色和光照.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-110"></a>
### 案例 110: [锦鲤庭院里的水与鱼](https://x.com/SahilPanhotra/status/2121225566779023432) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**用有游鱼的场景检查水面反射与光照是否连贯.**

创作者展示 Hydrogen 在锦鲤庭院测试中的输出，重点说明焦散、反射和游鱼行为，并附上 Carbon 版本.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-112"></a>
### 案例 112: [Gemini 网页端运行交互式 3D 场景](https://x.com/YxzRainy/status/2121232725185339869) (作者 [@YxzRainy](https://x.com/YxzRainy))

**在 Gemini 网页端快速制作可交互光照和粒子效果.**

创作者展示 Hydrogen 在网页端运行的 3D 场景，包含粒子、动态光照和实时控件.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-115"></a>
### 案例 115: [单 HTML 文件里的粉色 3D 场景](https://x.com/SahilPanhotra/status/2121254256288137484) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**尝试无外部素材的 Three.js 场景，检查构图是否清晰.**

创作者将粉色场景归功于 Hydrogen，称仅在一个 HTML 文件中使用纯 Three.js，无外部素材. 链接中的锦鲤庭院是另一个项目.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-119"></a>
### 案例 119: [纯代码制作的大爆炸模拟](https://x.com/ash_twtz/status/2121268140630000020) (作者 [@ash_twtz](https://x.com/ash_twtz))

**用短动画快速构建可视化解释，再检查科学表述.**

创作者把 15 秒大爆炸可视化归功于 Gemini 应用中的 Hydrogen，称完全用代码制作，未使用网页访问、纹理、外部素材或 3D 模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-120"></a>
### 案例 120: [带装配爆炸视图的直升机](https://x.com/LuminaBench/status/2121273297715277930) (作者 [@LuminaBench](https://x.com/LuminaBench))

**检查 3D 原型能否把飞行控制与实用的部件查看方式结合起来.**

创作者展示可操控的直升机及装配和爆炸视图，将原型归功于 Hydrogen Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-121"></a>
### 案例 121: [带透视和线框视图的 Hydrogen Express](https://x.com/LuminaBench/status/2121277060983234788) (作者 [@LuminaBench](https://x.com/LuminaBench))

**给可操控的 3D 原型加入多种检查模式.**

创作者展示具有速度控件、爆炸视图、线框及透视模式的列车，并报告生成约用五分钟.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-122"></a>
### 案例 122: [空中的补给站](https://x.com/doe_naps/status/2121279837512106168) (作者 [@doe_naps](https://x.com/doe_naps))

**给场景安排有辨识度的移动物体和光照状态，让变化在演示中清晰可见.**

创作者分享 Hydrogen 制作的空中补给站，包含复古飞车、旋转涡轮和昼夜交替，报告一次生成完成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-129"></a>
### 案例 129: [单 HTML 文件里的水磨坊](https://x.com/NovaXCode/status/2121294356875509851) (作者 [@NovaXCode](https://x.com/NovaXCode))

**用带醒目运动元素的小景观检查快速生成的 3D 原型.**

创作者称 Hydrogen 用约 30 秒在一个 HTML 文件里搭建水磨坊，并分享输出录屏.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-132"></a>
### 案例 132: [用 Hydrogen Extra 搭建 Blender 场景](https://x.com/SPAC89/status/2121302218347270625) (作者 [@SPAC89](https://x.com/SPAC89))

**增加视觉细节之前，先在 Blender 中检查几何与材质.**

作者展示归因于 Hydrogen Extra 的 Blender 场景，并给出仅适用于该会话的订阅额度估算.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-139"></a>
### 案例 139: [Hydrogen 制作的两段粒子动画](https://x.com/gwammyy/status/2121355401392189746) (作者 [@gwammyy](https://x.com/gwammyy))

**用不同粒子场景检验简单特效中的形态和运动.**

创作者将两段短粒子特效录屏归功于 Hydrogen. 来源仅展示输出，未记录运行设置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

类型: Demo | 日期: 2026-11-13

---

<a id="case-142"></a>
### 案例 142: [微缩世界的昼夜切换开关](https://x.com/vib3coded/status/2121398359395283027) (作者 [@vib3coded](https://x.com/vib3coded))

**用小型开关测试界面状态切换时动作是否连贯.**

创作者展示由开关控制的昼夜过渡，报告本次制作花费 $0.21.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-143"></a>
### 案例 143: [用 65 个模块搭建场景](https://x.com/IamEmily2050/status/2121400396002492781) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**随着场景扩展，记录生成耗时和集成工作量.**

创作者报告在 Gemini 应用中搭建了 65 个模块，每个模块用一条提示词，并分享结果录屏.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-149"></a>
### 案例 149: [微缩宝塔庭院](https://x.com/auricxofficial/status/2121498286926540970) (作者 [@auricxofficial](https://x.com/auricxofficial))

**检查生成的微缩场景如何平衡建筑和周边绿化.**

创作者把积木风格宝塔和庭院的视频归功于 Hydrogen. 视频展示了结果，实现细节未公开.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-153"></a>
### 案例 153: [二战机场微缩景观](https://x.com/doe_naps/status/2121508105947320688) (作者 [@doe_naps](https://x.com/doe_naps))

**给 3D 演示提供参考资料与机械运动要求，检验外观之外的表现.**

创作者报告给 Hydrogen 参考资料和简短任务说明，在一个 HTML 文件中搭建机场微缩景观. 要求包括可动的飞机和坦克.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-167"></a>
### 案例 167: [程序化生成的知更鸟飞行动画](https://x.com/LuminaBench/status/2121620820791562291) (作者 [@LuminaBench](https://x.com/LuminaBench))

**检查生成飞行动画中的翅膀和身体动作.**

创作者将知更鸟飞行动画代码归功于 Hydrogen，并在后续帖展示同一工作的独立 Antigravity swarm 流程图.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

类型: Demo | 日期: 2026-11-14

---

<a id="case-182"></a>
### 案例 182: [用单个 HTML 文件绘制插图](https://x.com/vamsibatchuk/status/2121788887823778297) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**测试代码能否在没有外部素材的情况下重现参考视觉效果.**

DeepMind 员工展示一张单文件插图，称制作过程无外部库、图像生成器、Skill 或嵌入素材.

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

类型: Demo | 日期: 2026-11-15

---

<a id="case-186"></a>
### 案例 186: [从静态场景制作海鹦动画](https://x.com/vamsibatchuk/status/2121846407950639541) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**把现有 HTML 场景用作程序化动画的首帧.**

创作者让 Hydrogen 在一个 HTML 文件里制作后续 50 帧，录屏展示海鹦拿走角色帽子.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-200"></a>
### 案例 200: [用一条提示词搭建 3D 微缩岛](https://x.com/CodeByPoonam/status/2121952483132289270) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**检查一次生成的场景能否清楚安排地标、地形与水域.**

创作者称由 Hydrogen 按一条提示词搭建微缩岛. 画面可见建筑和其他地标.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-208"></a>
### 案例 208: [奇点主题的交互面板](https://x.com/Moleh1ll/status/2122032596263776351) (作者 [@Moleh1ll](https://x.com/Moleh1ll))

**围绕一个视觉概念制作简短的交互片段.**

创作者将奇点主题的交互面板归功于 Hydrogen. 录屏展示结果，实现细节有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

类型: Demo | 日期: 2026-11-15

---

<a id="case-225"></a>
### 案例 225: [Gemini 应用中的水球](https://x.com/Google/status/2122366286659289502) (作者 [@Google](https://x.com/Google))

**用简单光学场景观察高光与折射的关系.**

Google 分享 Gemini 应用中的一张拟水球体图，球上有 Hydrogen 字样，并将成果归于 Hydrogen. 来源展示输出，未说明底层渲染方式.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

类型: Demo | 日期: 2026-11-16

---


<a id="comparisons-limits"></a>
## 🧪 对比与局限

<a id="case-24"></a>
### 案例 24: [霓虹火柴人动画：Hydrogen 与 Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**结合来源所述时间与费用对比最终动画，不要假定运行框架相同**

作者展示了 Hydrogen 和 Opus 5.5 的输出，并报告费用分别为 $1.02 与 $7.43，耗时分别为 10 分 22 秒与 34 分钟；本合集未核验账单、提示词、迭代次数或运行设置的可比性

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-25"></a>
### 案例 25: [机器人任务与自行识别失误](https://x.com/ArtificialAnlys/status/2120995180891508833) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**在机器人评估中纳入任务完成情况以及识别细小失误的能力**

Artificial Analysis 展示了倒液体和整理积木的任务，并称 Hydrogen 注意到了少量洒漏和未关上的盖子；视频及 AA-Robotics v0.1 排名来自评测方，本合集未独立复现

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-26"></a>
### 案例 26: [自然语言驱动的实验室工作单元](https://x.com/danielmckinn0n/status/2120990834246173125) (作者 [@danielmckinn0n](https://x.com/danielmckinn0n))

**将工具执行和失败处理的评估与基准榜单分数分开**

来源展示了由自然语言请求驱动的实验室工作单元，并报告四项实验室相关基准的结果；所述 Hydrogen 的 RareBench 分数低于 Opus 5.5，另外三项更高；这是基准所有者的演示，并非医学验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-27"></a>
### 案例 27: [冰山与拖船：Hydrogen 与 Carbon](https://x.com/EnvolDev/status/2120989670582677930) (作者 [@EnvolDev](https://x.com/EnvolDev))

**对比耗时较长的 3D 构建时，记录推理级别与运行框架限制**

创作者称两个模型均通过 OpenRouter 以 High 级别运行，Hydrogen 费用 $4.27、耗时 1 小时 23 分 40 秒，Carbon 费用 $8.83、耗时 2 小时 39 分 10 秒；这些是来源自述的非受控结果，并非普适的价格或速度比例

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-28"></a>
### 案例 28: [果冻锦鲤池：Hydrogen 与 Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (作者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**在根据基准排名选择模型前，先检查具体场景**

作者对比了 Hydrogen 和 Sonnet 5.5 在 3D 锦鲤池任务上的表现；来源邀请观众评判输出，但未确立匹配的设置或客观质量评分

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-29"></a>
### 案例 29: [使用相同提示词的创意编程合集](https://x.com/kickingkeys/status/2120985358317875222) (作者 [@kickingkeys](https://x.com/kickingkeys))

**通过多样化的视觉任务，避免从单个漂亮输出过度概括**

创作者称给 Hydrogen、Carbon 和 Argon 使用了相同提示词，并将对比放在回复中；主帖素材展示低多边形动物、霓虹街道和水彩风格容器；这不是完整的受控基准测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-30"></a>
### 案例 30: [Megamind 体素：成本与质量反例](https://x.com/thehypedotnews/status/2120980737012670720) (作者 [@thehypedotnews](https://x.com/thehypedotnews))

**评估模型是否始终更便宜或视觉效果更强时，保留失败案例**

来源称 Hydrogen 生成的 Titan 角色整体更不协调，费用却为 $36.07，而 Sonnet 5.5 为 $8.64；帖子包含商业推广，费用与质量判断均为发布者说法

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

类型: Limit | 日期: 2026-11-12

---

<a id="case-31"></a>
### 案例 31: [穿越四季的杂耍狮子](https://x.com/SahilPanhotra/status/2120978349967458704) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**检查要求的动作，而不只是周围界面的视觉精致程度**

作者称 Carbon 处理了交叉的杂耍弧线，而 Hydrogen 让球悬浮在空中，尽管后者的季节过渡与裁切更干净；这一同任务 SVG 对比揭示的是特定动作失败，而非模型综合排名

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

类型: Limit | 日期: 2026-11-12

---

<a id="case-32"></a>
### 案例 32: [三模型火柴人格斗：更慢且更贵的结果](https://x.com/DanielZambrini/status/2120963180461769183) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**对比模型宣传的效率与实际任务报告时，保留反例**

创作者对比 Hydrogen、Carbon 和 Argon，并称本次测试中 Hydrogen 比 Carbon 耗时更长、费用更高；设置、账单和迭代次数未经独立验证

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

类型: Limit | 日期: 2026-11-12

---

<a id="case-33"></a>
### 案例 33: [农场自行车场景：Hydrogen 与 Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**结合创作者报告的完成时间，对比动作与场景质量**

来源对比了 Hydrogen 与 Gemini 3.8 Flash 的农场自行车场景，称耗时分别为 56 秒与超过六分钟；这是单个创作者的测试，并非通用速度基准

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-34"></a>
### 案例 34: [女孩与猫的双人自行车](https://x.com/marcthecreatorr/status/2120956699951628637) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**对比提示词遵循程度与附加细节，同时明确不同编程运行框架的差异**

创作者使用所述相同 SVG 任务，但分别在 Claude Code 中运行 Opus 5.5、在 Cursor 中运行 Hydrogen；所述时间与费用差异很大，但不同运行框架及未披露的迭代使其不能成为仅针对模型的受控对比

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-35"></a>
### 案例 35: [四个模型构建 Three.js 马里奥游戏](https://x.com/StatsWire/status/2120955723396071548) (作者 [@StatsWire](https://x.com/StatsWire))

**解读相同提示词的游戏对比前，记录不一致的推理设置**

来源对比了 High 级别的 Gemini 3.8 Flash、Argon、Carbon 与 XHigh 级别的 Hydrogen，均使用纯 Three.js，不使用外部 3D 模型或纹理；它展示了四个输出，并非推理设置匹配的基准测试

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-36"></a>
### 案例 36: [三个 Gemini 模型绘制游戏手柄](https://x.com/notjazii/status/2120952314873987271) (作者 [@notjazii](https://x.com/notjazii))

**寻找具体任务中的退步与改进，不要假定模型家族存在固定层级**

创作者对比了 Carbon、Argon 和 Hydrogen 的手柄 SVG 输出，并称重新运行过测试；所述耗时和费用均为来源方说法，不能确立模型质量的普遍排序

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-37"></a>
### 案例 37: [应用与 Studio 的视觉回答存在差异](https://x.com/thegenioo/status/2120946497802174688) (作者 [@thegenioo](https://x.com/thegenioo))

**依赖视觉结果之前，在计划使用的产品界面中测试相同图片**

来源展示了据称由 Gemini 应用和 AI Studio 中的 Hydrogen 给出的相互冲突的食物识别回答；该对比未独立核验路由、设置或完整对话上下文是否相同

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

类型: Limit | 日期: 2026-11-12

---

<a id="case-38"></a>
### 案例 38: [火箭发射场景：Hydrogen 与 Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**既对比实际发射动画，也对比来源报告的构建耗时**

创作者展示了 Hydrogen 与 Gemini 3.8 Flash 的输出，并称耗时分别不到一分钟与约三分钟；这一视觉对比仅涉及一个任务，没有独立受控的运行配置

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-39"></a>
### 案例 39: [四项 SVG 动画任务](https://x.com/Angaisb_/status/2120944947193127061) (作者 [@Angaisb_](https://x.com/Angaisb_))

**通过多种交互与动画主题，检查跨任务的一致性**

来源配对展示了 Hydrogen 与 Carbon 在传递、昼夜变化、开箱和变色龙任务中的输出；简短主帖未披露完整提示词、计时证据或客观评分方法

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-40"></a>
### 案例 40: [三个模型制作草原马匹动画](https://x.com/AI_Screening/status/2120944276586823689) (作者 [@AI_Screening](https://x.com/AI_Screening))

**直接检查动作与视觉细节，再判断宽泛的费用或质量说法是否可信**

创作者展示了 Hydrogen、Carbon 和 Argon 的草原马匹场景；关于更快速度、更低费用和高质量的说法仍是来源方评价，并非本合集复现的受控对比

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-43"></a>
### 案例 43: [Hydrogen API 与 Carbon Antigravity 输出](https://x.com/huang18825/status/2120876396264444314) (作者 [@huang18825](https://x.com/huang18825))

**用同一提示词比较视觉效果时，记录各自的运行环境.**

创作者通过 API 运行 Hydrogen、通过 Antigravity 运行 Carbon，并并排展示两份输出. 文中报告的 4 分 47 秒对应此次 Hydrogen 运行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-44"></a>
### 案例 44: [Hydrogen 与 Astra 的阴影细节对比](https://x.com/SPAC89/status/2120911537296515321) (作者 [@SPAC89](https://x.com/SPAC89))

**比较两次运行的费用和耗时，同时检查渲染细节.**

创作者更喜欢带阴影的 Hydrogen 版本，并报告它在该测试环境下更快完成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-45"></a>
### 案例 45: [程序化 3D 动效对比](https://x.com/SPAC89/status/2120923185981915156) (作者 [@SPAC89](https://x.com/SPAC89))

**比较程序化动效的连贯性与构图时，记录生成耗时.**

创作者展示了归因于 Hydrogen High 的条纹 3D 形体，报告制作耗时不到五分钟，并与自己试用的更高价模型对照.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-46"></a>
### 案例 46: [历时 89 分钟的 PokéBench 视觉测试](https://x.com/StatsWire/status/2120923685296988296) (作者 [@StatsWire](https://x.com/StatsWire))

**测试长时视觉代理时，同时记录任务完成情况、回合数和 API 失败次数.**

来源报告，发布前通过 Vertex 以 High 档运行时，Hydrogen 用 365 回合、89 分钟闯过小刚关卡，期间 API 调用失败数为零. 结果对应来源所用的测试环境.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-47"></a>
### 案例 47: [Hydrogen 与 DeepSeek 搭建同一个 3D 场景](https://x.com/AiHubMix/status/2120928687537418581) (作者 [@AiHubMix](https://x.com/AiHubMix))

**对照视觉输出并分别记录耗时和 API 费用.**

AIHubMix 用同一个 3D 场景提示词比较两个模型，各用最高可用推理档. 服务商报告 Hydrogen 用时 3 分钟、花费 $1.30，DeepSeek V4.1 Flash 用时 100 分钟、花费 $0.90.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-53"></a>
### 案例 53: [Agent Arena 的单任务耗时和成本](https://x.com/arena/status/2120940869889175840) (作者 [@arena](https://x.com/arena))

**查看总体成功率时，也比较单任务延迟、费用和输出 Token 数.**

Agent Arena 报告 Hydrogen High 在其评测中的单任务中位耗时为 5.3 分钟，中位费用为 $1.60，输出 Token 多于 Carbon 和 Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-54"></a>
### 案例 54: [视觉文档和终端基准测试](https://x.com/ArtificialAnlys/status/2120941511223185722) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**分别查看文档与终端测试结果，再决定推理预算.**

Artificial Analysis 报告视觉文档表现较强，终端项目的增益不一. Extra 推理提高了科学终端得分，通用 Terminal-Bench 得分仍为 54%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-55"></a>
### 案例 55: [Vals 指数和 Tax Agent 成绩](https://x.com/ValsAI/status/2120943893894303808) (作者 [@ValsAI](https://x.com/ValsAI))

**结合整体评测和专业任务的分数来判断模型是否适用.**

Vals AI 报告，Hydrogen 的综合指数为 68.5%，在测试时的 Tax Agent 项目中排名第一.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-56"></a>
### 案例 56: [CursorBench 的 Hydrogen 默认推理档](https://x.com/cursor_ai/status/2120944639633211619) (作者 [@cursor_ai](https://x.com/cursor_ai))

**先查看默认推理档的基准成绩，再到自己的仓库里测试.**

Cursor 报告，在自家 CursorBench 中，默认推理档的 Hydrogen 得分为 54.3%，Gemini 3.8 Flash 为 39.6%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-57"></a>
### 案例 57: [四款模型制作弓箭手战斗动画](https://x.com/IndependentEco/status/2120945011277590733) (作者 [@IndependentEco](https://x.com/IndependentEco))

**比较各个动画能否清楚表现角色的战斗动作.**

创作者在同一视频中并排展示 Hydrogen、Fable 5.2、GPT-6.1 Sol 和 Carbon 的弓箭手战斗动画.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-61"></a>
### 案例 61: [Hydrogen 的 Devin FrontierCode 结果](https://x.com/cognition/status/2120950876248641588) (作者 [@cognition](https://x.com/cognition))

**比较候选补丁能否合并，并记录各自使用的代理环境.**

Cognition 报告 Hydrogen 在 FrontierCode 2.0 得分为 38.2%. 该模型的测试环境与对照模型使用的 Devin CLI 设置不同.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-64"></a>
### 案例 64: [禁止联网后仍触发搜索](https://x.com/amanunreal/status/2120954045615768054) (作者 [@amanunreal](https://x.com/amanunreal))

**流程要求离线作答时，检查模型是否真的没有调用工具.**

作者报告，尽管提示词要求避开搜索和工具调用，Hydrogen 仍然搜索了网页. 原帖展示一次具体情况，未统计发生频率.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-12

---

<a id="case-65"></a>
### 案例 65: [记录 Antigravity Swarm 的配额用量](https://x.com/HarshithLucky3/status/2120954399971487774) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**测试多代理运行时记录 Token 量和消耗的额度.**

创作者报告，在自己的套餐下使用 Swarm 时用了 1700 万 Token，消耗了五小时额度的 21%. 数字对应此次会话.

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

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-66"></a>
### 案例 66: [专业任务评测中的工具调用](https://x.com/mercor/status/2120957582139642095) (作者 [@mercor](https://x.com/mercor))

**观察代理在执行专业任务前如何收集背景信息.**

Mercor 报告，Hydrogen 在 APEX-Agents 中达到 78.0% Pass@1，平均每项任务调用工具 93 次. 评测涉及法律、咨询和银行业务.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-68"></a>
### 案例 68: [四款模型制作法师斗龙动画](https://x.com/IndependentEco/status/2120964690906161461) (作者 [@IndependentEco](https://x.com/IndependentEco))

**比较同一奇幻场景各版本的调度、动作清晰度和特效.**

对比视频展示 Hydrogen 和三款 Claude 模型生成的法师斗龙场景. 创作者在这次对照中更偏好 Claude 的输出.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-71"></a>
### 案例 71: [MazeBench 中的低成功率](https://x.com/patience_cave/status/2120973681937809766) (作者 [@patience_cave](https://x.com/patience_cave))

**用迷宫任务检验空间推理，再决定能否依赖它.**

公布的 MazeBench 对比在其设置下测得 Hydrogen 1%、Sonnet 5.5 4%、GPT-6.1 Terra 8%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-72"></a>
### 案例 72: [三款 Gemini 模型搭建帆船场景](https://x.com/Octoberry/status/2120974412144902376) (作者 [@Octoberry](https://x.com/Octoberry))

**在主题化 Three.js 场景中比较运动效果和环境细节.**

创作者展示 Hydrogen、Argon 和 Carbon 的帆船输出，更喜欢 Carbon 的细节，并认为这次测试中 Hydrogen 接近 Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-75"></a>
### 案例 75: [识别球衣号码时耗尽推理预算](https://x.com/skalskip92/status/2120994631072776235) (作者 [@skalskip92](https://x.com/skalskip92))

**识别图片中的小细节时，设置推理上限并准备替代方案.**

评测者报告，Hydrogen XHigh 用了 131,069 个推理 Token，运行 9 分 55 秒仍未给出球衣号码.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-12

---

<a id="case-76"></a>
### 案例 76: [不同模型系列的 ClutterBench 表现](https://x.com/AdamHoltererer/status/2121000759118459138) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**用专门的杂乱场景基准检验模型的通用优势是否适用于这一任务.**

作者分享 ClutterBench 成绩. Hydrogen 在图中列出的 Gemini 模型里领先，落后于参与对照的 OpenAI 模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-12

---

<a id="case-78"></a>
### 案例 78: [Minecraft 风格人体解剖剖面像](https://x.com/jan_volad/status/2121026531472339340) (作者 [@jan_volad](https://x.com/jan_volad))

**检查生成的剖面是否包含指定的内部结构.**

创作者让 Hydrogen 和 Argon 各用一次请求制作 Minecraft 风格解剖胸像，并报告在 Hydrogen 输出中看到头骨、肋骨和脊柱.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-79"></a>
### 案例 79: [三款模型渲染同一件道具](https://x.com/luckeyfaraday/status/2121030005899825504) (作者 [@luckeyfaraday](https://x.com/luckeyfaraday))

**同时记录质量和 Token 用量，检查单价较低的模型是否在该任务中耗用更多 Token.**

来源对比 Hydrogen、Carbon 和 Fable 5.2 渲染同一个步枪形道具. 创作者报告 Hydrogen 使用 369 万 Token、花费 $1.62，Carbon 使用 39.8 万 Token、花费 $0.77.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

类型: Evaluation | 日期: 2026-11-12

---

<a id="case-80"></a>
### 案例 80: [归纳基准测试与 Token 消耗](https://x.com/s_batzoglou/status/2121037853258129811) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**评测高难度推理时，将计费输入和输出用量与成绩一起记录.**

评测者报告，Hydrogen 在其 100 道题的归纳基准中列第四，接近 Opus 5.5. 作者记录了 5500 万输出 Token 和 3.07 亿计费输入 Token，计费机制仍待解释.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-83"></a>
### 案例 83: [三款模型制作 3D 动物动画](https://x.com/leo114119/status/2121054098753785915) (作者 [@leo114119](https://x.com/leo114119))

**在同一项 3D 动物建模任务中检查身体结构和运动.**

来源对比 Hydrogen、GPT-6.1 Terra 和 Claude Haiku 5.5. 创作者指出 Hydrogen 输出的不足；观察结果仅对应这项任务.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-84"></a>
### 案例 84: [Hydrogen 与 Qwen 的 ts-bench 测试](https://x.com/gosrum/status/2121058334552060102) (作者 [@gosrum](https://x.com/gosrum))

**将工具调用错误和总体基准成绩一起查看.**

来源在 ts-bench 上对比 Hydrogen 和 Qwen4 Max Preview，并讨论了这几次运行的工具调用可靠性. 截图保留了当次评测结果.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-85"></a>
### 案例 85: [Vending-Bench 商业模拟](https://x.com/andonlabs/status/2121061429889642497) (作者 [@andonlabs](https://x.com/andonlabs))

**比较模拟收入时同时计入代理运行成本.**

Andon Labs 报告，Hydrogen 在 Vending-Bench 2 中排名第三，在其模拟中赚取的收入高于同价位模型.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-89"></a>
### 案例 89: [四款模型搭建微缩岛屿](https://x.com/xKaka1456/status/2121111495358697924) (作者 [@xKaka1456](https://x.com/xKaka1456))

**比较岛屿设计时，一并记录各个环境的耗时和费用.**

来源对比四种微缩岛，报告 Hydrogen 用时 4 分钟，GPT-6.1 Terra 20 分钟，Sol 40 分钟，DeepSeek 60 分钟. 作者所称 Hydrogen 零额外收费与其设置有关.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-91"></a>
### 案例 91: [用代码模拟布料撕裂](https://x.com/MichaelLee009/status/2121126779276402904) (作者 [@MichaelLee009](https://x.com/MichaelLee009))

**用同一动画任务检查布料拉伸、撕裂及与毛发的相互作用.**

创作者对比 Hydrogen 和 Claude Fable 5.2 的代码生成动画，认为后者视觉表现更佳. 来源未给出统一运行设置或独立物理验证.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-94"></a>
### 案例 94: [事实核查缺少可追溯来源](https://x.com/cagrimbakirci/status/2121130756684886279) (作者 [@cagrimbakirci](https://x.com/cagrimbakirci))

**依据模型对截图的判断行动之前，要求给出可查验的引用.**

作者请 Hydrogen 核实一张帖文截图，称模型确认内容、反复打开核查工具，但始终未给出原始来源.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-13

---

<a id="case-96"></a>
### 案例 96: [Hydrogen 与 Sol 绘制 2D 鹈鹕](https://x.com/YxzRainy/status/2121148582166491164) (作者 [@YxzRainy](https://x.com/YxzRainy))

**用同一项简单 2D 动画任务对比耗时与动作表现.**

作者在视频中展示 Hydrogen 和 GPT-6.1 Sol 的 2D 鹈鹕骑车结果，报告分别用时 28 秒和 6 分 51 秒. 两次运行的设置是否一致尚未证实.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-98"></a>
### 案例 98: [四款模型搭建蛛丝摆荡游戏](https://x.com/StatsWire/status/2121172215182065807) (作者 [@StatsWire](https://x.com/StatsWire))

**统一使用单文件限制，比较各款游戏的移动和操作.**

来源展示四款 Gemini 模型制作同一项 3D 蛛丝摆荡挑战，限定单个 HTML 文件且无外部素材. Hydrogen 使用 Extra High，其余 Gemini 3.8 Flash、Argon 和 Carbon 使用 High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-100"></a>
### 案例 100: [四款模型渲染建筑微缩景观](https://x.com/Jackson77li/status/2121172890838352306) (作者 [@Jackson77li](https://x.com/Jackson77li))

**用统一的建筑任务比较输出，查看各模型如何打光.**

创作者称使用同一提示词，对照 Hydrogen、GPT-6.2、Claude Fable 5.2 和 DeepSeek 的建筑微缩景观. 排名和速度评价均属作者感受.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-103"></a>
### 案例 103: [三款模型渲染列车场景](https://x.com/xKaka1456/status/2121193705810104515) (作者 [@xKaka1456](https://x.com/xKaka1456))

**用同一列车场景任务比较各自配置下的完成速度.**

创作者报告 Hydrogen 用时约 3 分钟、GPT-6.1 Terra 20 分钟、Qwen4 Max Preview 68 分钟. 视频展示渲染结果，来源未说明设置和迭代次数.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-104"></a>
### 案例 104: [用 Extra 档制作雨夜唐人街](https://x.com/qingzhoucloud/status/2121198911515967952) (作者 [@qingzhoucloud](https://x.com/qingzhoucloud))

**给大型动画选择推理档前，记录实际耗时并检查最终画面.**

作者用 Hydrogen Extra 执行另一创作者提供的提示词，报告雨夜唐人街 MP4 用时近四小时，并与另一次 Claude Fable 5.2 运行比较. 两次设置的可比性有限.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-106"></a>
### 案例 106: [三款模型搭建行星可视化界面](https://x.com/Stargridcompass/status/2121208957276713181) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**用同一提示词比较不同模型制作的科学可视化界面.**

录屏对比 Claude Fable 5.2、GPT-6.2 Sol 与 Hydrogen 的行星主题输出. 排序是作者的视觉判断，来源未证实统一设置，也没有客观评分.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-107"></a>
### 案例 107: [四款模型复刻 Chrome 小恐龙](https://x.com/noclipepe/status/2121219775170761044) (作者 [@noclipepe](https://x.com/noclipepe))

**为每次游戏复刻计时，并比较可玩结果.**

创作者报告，AI Studio 中的 Hydrogen 用时 18 分 41 秒，Fable 5.2 用时 45 分 30 秒. 录屏也展示 Qwen4-Max-Preview 和 Carbon 及画面评分.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-109"></a>
### 案例 109: [两款编程代理分别造船](https://x.com/marcthecreatorr/status/2121221667619852660) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**在实际使用的工具中比较首个可用结果和返工成本.**

作者以同一提示词在 Claude Code 中运行 Sonnet，在 Cursor 中运行 Hydrogen. 作者报告 Hydrogen 更快完成，但需要第二版.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-111"></a>
### 案例 111: [四款模型制作刚体投石机攻城原型](https://x.com/StatsWire/status/2121226579141386285) (作者 [@StatsWire](https://x.com/StatsWire))

**用同一任务比较可玩的物理原型，并记录推理档.**

创作者让四款 Gemini 模型搭建含数百块石块的投石机场景. 报告 Hydrogen Extra High 用时 10 分 3 秒，Carbon High 为 23 分 33 秒，Gemini 3.8 Flash High 最快.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-116"></a>
### 案例 116: [FrontierMemory 的长期记忆测试](https://x.com/Letta_AI/status/2121255895745351874) (作者 [@Letta_AI](https://x.com/Letta_AI))

**为长期代理记忆选模型时，结合评分和单次费用.**

Letta 报告 Hydrogen 在 FrontierMemory 中获得 64.4%，与 Argon 持平，每次记忆运行约 $100. 在该基准配置下，Carbon 为 71.1%，每次约 $94.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-117"></a>
### 案例 117: [故意损坏的 LiveKit 语音代理](https://x.com/livekit/status/2121256982023672076) (作者 [@livekit](https://x.com/livekit))

**引入可控的工具故障，检查语音代理会不会报告无依据的结果.**

LiveKit 在故意损坏的语音代理里测试 Hydrogen，报告虚假结果为零. 服务商将其与 Gemini 3.8 Flash 对照，并附文字记录.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-123"></a>
### 案例 123: [三款 Gemini 模型制作骑行者动画](https://x.com/AI_Screening/status/2121281026916057443) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用统一简报比较短动画，并记录各次运行的耗时.**

创作者展示 Carbon、Argon 与 Hydrogen 的骑行者动画，报告 Hydrogen 约 90 秒、Argon 超过五分钟，画面更偏好 Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-126"></a>
### 案例 126: [两款模型搭建 LEGO 世界](https://x.com/kepochnik/status/2121286219669836027) (作者 [@kepochnik](https://x.com/kepochnik))

**结合耗时比较各模型搭建了多少主题场景.**

创作者展示 Fable 5.2 和 Hydrogen 的 LEGO 世界版本，分别报告用时 44 和 28 分钟. 结果对应作者自己的运行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-127"></a>
### 案例 127: [修复两个仓库里重新植入的缺陷](https://x.com/PawelHuryn/status/2121286545223086302) (作者 [@PawelHuryn](https://x.com/PawelHuryn))

**植入已知缺陷，测量编程代理能找出并修复哪些问题.**

评测者在两个仓库中植入 105 个缺陷. 在其设置下，Extra High 的 Hydrogen 略落后于同为 Extra High 的 Sonnet 5.5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-128"></a>
### 案例 128: [两款模型制作火柴人对战光标](https://x.com/DanielZambrini/status/2121289822677483740) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**比较两份交互动画如何响应鼠标指针.**

创作者更喜欢 Fable 的火柴人对战光标版本，并认为 Hydrogen 足以用于更低成本的一轮生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-130"></a>
### 案例 130: [两款模型渲染山地景观](https://x.com/ZryMiller/status/2121295750122594440) (作者 [@ZryMiller](https://x.com/ZryMiller))

**在同一类景观动画中分别比较构图、生成耗时和费用.**

创作者分享 Hydrogen 与 Opus 5.5 的山景动画，报告前者用时 20 分 30 秒、花费 $0.50，后者 11 分 23 秒、花费 $2.50.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-131"></a>
### 案例 131: [用自定义环境做英译波斯语评测](https://x.com/MatinSenPai/status/2121296733258887365) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**用人工参考译文给高难度翻译段落打分.**

作者在自定义评测环境下做个人翻译测试，给 Hydrogen 94 分，满分 100. 主观分数取决于这套设置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-133"></a>
### 案例 133: [四款模型搭建沉船场景](https://x.com/remoteugur/status/2121302956741902451) (作者 [@remoteugur](https://x.com/remoteugur))

**用同一场景分别记录视觉还原、生成时间与开销.**

创作者报告 Hydrogen 用时 8.6 分钟、花费 $1.16，Gemini 3.8 Flash 用时 10.8 分钟、花费 $1.06. 还测试了 Carbon 和 Opus 5.5，更偏好 Opus 的真实感.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-135"></a>
### 案例 135: [四款模型的文案盲测](https://x.com/quintanilha/status/2121315967447757299) (作者 [@quintanilha](https://x.com/quintanilha))

**在选用文案之前，隐去模型名称再评判.**

创作者报告对四款模型进行文案盲测，更偏好 Hydrogen 的输出，并在这次测试中发现它比 Carbon 更快、开销更低.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-136"></a>
### 案例 136: [不同推理档的视觉检测与读字](https://x.com/skalskip92/status/2121322414453694489) (作者 [@skalskip92](https://x.com/skalskip92))

**在各个推理档分别测量检测准确率、文字识别准确率、费用与延迟.**

评测者分别报告 Hydrogen、Argon 和 Carbon 的检测和文字识别分数. Hydrogen High 在此次测试中平均每张图 29.3 秒，检测得 64.6 分、文字识别 87.2 分. Carbon High 两项得分都更高，开销和延迟也更高.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-13

---

<a id="case-137"></a>
### 案例 137: [四款模型重建《飞屋环游记》的房屋](https://x.com/noclipepe/status/2121326233044537688) (作者 [@noclipepe](https://x.com/noclipepe))

**用同一张参考图和简报比较 3D 制作的各项取舍.**

作者报告 Hydrogen 在四次运行中最快、最便宜，视觉上更喜欢 Fable. 设置和费用由来源报告.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

类型: Evaluation | 日期: 2026-11-13

---

<a id="case-144"></a>
### 案例 144: [固定镜头的舞蹈短片](https://x.com/notoro_ai/status/2121427503952834562) (作者 [@notoro_ai](https://x.com/notoro_ai))

**检查参考图动画能否保留角色设计、构图与镜头位置.**

作者分享日语提示词及与 Google Gemini 中 Hydrogen 关联的舞蹈视频. 提示词要求固定镜头、保留参考风格，底层视频生成模型尚未确认.

**提示词:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-145"></a>
### 案例 145: [编程代理卡在基线测试](https://x.com/Its_lakshya_ai/status/2121431788266659919) (作者 [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**给基线测试设定时限，并检查进度再等待修复方案.**

创作者展示 Antigravity 中 Hydrogen 长时间仍在执行基线测试的会话. 截图记录了先停止排查、再继续运行的请求.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-14

---

<a id="case-147"></a>
### 案例 147: [两款模型搭建交互机械臂](https://x.com/gmi_cloud/status/2121467337119588834) (作者 [@gmi_cloud](https://x.com/gmi_cloud))

**操作 Three.js 机械臂时，检查各关节的动作是否连贯.**

GMI Cloud 提供 Hydrogen 与 Sonnet 5.5 在 Three.js 机械臂任务上的录屏. 本次对比中服务商更喜欢 Sonnet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-151"></a>
### 案例 151: [Hydrogen 与 Sol 搭建雪中村庄](https://x.com/badboyfoxy/status/2121501015442669866) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**在编程对比中分别记录耗时、费用和场景质量.**

创作者报告 Hydrogen High 用时三分钟、花费 $1.37，Sol High 用时 15 分钟、花费 $4.03. 创作者更喜欢 Sol 的雪村画面.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-152"></a>
### 案例 152: [High 与 Ultra 档制作 Three.js 岛屿](https://x.com/laopai1990/status/2121502334866096160) (作者 [@laopai1990](https://x.com/laopai1990))

**比较画面和响应速度时，记录推理档并区分不同产品的额度.**

作者对比 Hydrogen High 和 GPT-6.1 Sol Ultra，分别报告 Three.js 岛屿耗时约 90 秒和 30 分钟. 费用为估算，推理档不同.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-157"></a>
### 案例 157: [对比 3D PS5 手柄细节](https://x.com/Stargridcompass/status/2121528563254043015) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**比较手柄模型时检查按键阴影及背面硬件细节.**

创作者用 Hydrogen High 和 GPT-6.2 Sol 建模手柄. 来源报告分别约三分钟和十一分钟，作者认为 Sol 对背面及侧面按键的还原更完整.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-159"></a>
### 案例 159: [CursorBench 中的推理预算对照](https://x.com/Beamsters1/status/2121538515909628111) (作者 [@Beamsters1](https://x.com/Beamsters1))

**选择更快的默认档前，比较不同推理配置下的成功率.**

作者报告，增加 Hydrogen 的推理预算时，CursorBench 4.0 成功率显著上升. 结果对应测试配置.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-14

---

<a id="case-160"></a>
### 案例 160: [三款模型渲染星核圣殿](https://x.com/YxzRainy/status/2121551796766376081) (作者 [@YxzRainy](https://x.com/YxzRainy))

**在 3D 任务中分别观察渲染稳定性和画面细节.**

创作者对比 Hydrogen、DeepSeek V4.1 1017 与 Qwen4 Max Preview 的星核主题场景，称 Hydrogen 在本次测试中更快且未黑屏或闪烁，视觉细节则更少.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-162"></a>
### 案例 162: [挑战现有的迁移方案](https://x.com/is_llll/status/2121565725072490559) (作者 [@is_llll](https://x.com/is_llll))

**让编程代理评估迁移是否需要替换现有架构.**

作者展示一次设计审阅，Hydrogen 和 Argon 支持原有方案，Claude Opus 提议替换它并更早迁移. 这是单个项目的判断.

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

类型: Limit | 日期: 2026-11-14

---

<a id="case-165"></a>
### 案例 165: [两款模型制作神庙逃脱游戏](https://x.com/runable_hq/status/2121596515474964556) (作者 [@runable_hq](https://x.com/runable_hq))

**在同一游戏概念中比较光照和氛围是否便于看清场景.**

服务商 Runable 展示 Hydrogen 和 Argon 实现的神庙逃脱游戏，描述前者的光照更有氛围、后者的画面更明亮.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-166"></a>
### 案例 166: [三款 Gemini 模型制作拉力车动画](https://x.com/teddyaisi/status/2121604816380010719) (作者 [@teddyaisi](https://x.com/teddyaisi))

**检查车子通过带倾角的弯道时，悬挂运动和轮胎抓地是否合理.**

创作者用 Carbon、Argon 与 Hydrogen 制作采石场里的 Three.js 越野车动画. 任务要求展示悬挂压缩和在倾斜土路弯道上滑行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-169"></a>
### 案例 169: [两款模型制作 Chasing Views 动画](https://x.com/VulKan42069/status/2121625271493382166) (作者 [@VulKan42069](https://x.com/VulKan42069))

**比较输出和耗时，同时记录各自的推理档.**

创作者展示 Hydrogen Extra High 与 Opus 5.5 High 的 Chasing Views 动画，本次对比分别报告耗时 22 和 18 分钟.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-170"></a>
### 案例 170: [Design Creativity Bench 的速度和费用](https://x.com/Kombaico/status/2121635837180031129) (作者 [@Kombaico](https://x.com/Kombaico))

**查看创意评分时，一起比较单份设计的生成耗时与费用.**

基准运营方报告 Hydrogen 创意得分 49.4，每份设计中位耗时 3.4 分钟、费用 $0.39. 在该评测中 Argon 较慢且较便宜，Carbon 较慢且较贵.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

类型: Benchmark | 日期: 2026-11-14

---

<a id="case-172"></a>
### 案例 172: [四款模型制作沙漠骏马动画](https://x.com/Marlenuii/status/2121664345818235177) (作者 [@Marlenuii](https://x.com/Marlenuii))

**先比较脚掌着地和重心转移，再看打光和网格细节.**

创作者让 Astra、Carbon、Fable 5.2 与 Hydrogen 制作沙漠奔马场景. 作者偏好 Astra 的步态，指出 Hydrogen 的马匹建模有缺陷.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-174"></a>
### 案例 174: [FrontierCS 2 计算机科学研究评测](https://x.com/wenhaocha1/status/2121679887400403308) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**在常规编程测试之外使用研究基准，并记录运行环境.**

来源报告 Hydrogen 用 Antigravity 在 FrontierCS 2 按通过率排第七. 评测涵盖计算机科学研究中的技术问题.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

类型: Benchmark | 日期: 2026-11-14

---

<a id="case-175"></a>
### 案例 175: [四款模型制作云端里约](https://x.com/EnvolDev/status/2121701704139956250) (作者 [@EnvolDev](https://x.com/EnvolDev))

**用同一个创意简报比较费用、耗时和主观质量.**

评测者报告 Hydrogen Extra High 花费 $6.21，是他们最不喜欢的结果. 此次 Astra 用时较少，来源未确认原生视频生成.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-176"></a>
### 案例 176: [Hydrogen 在 GBENCH 技术任务中的表现](https://x.com/leo_linsky/status/2121710421891780864) (作者 [@leo_linsky](https://x.com/leo_linsky))

**评估技术工作时，把可核验的编程与非编程结果和价格、耗时一起比较.**

评测方公布 Hydrogen 的 GBENCH 结果. 非编程任务包括电路设计和抽象推理. 作者称在其测量中，Sol 在相近价格与速度下更有竞争力.

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

类型: Benchmark | 日期: 2026-11-14

---

<a id="case-177"></a>
### 案例 177: [训练车辆侧方停车](https://x.com/noclipepe/status/2121734795738652934) (作者 [@noclipepe](https://x.com/noclipepe))

**比较生成模拟中的学习进展和最终成功率.**

使用同一任务说明，创作者报告 Hydrogen 为 44 辆车中 5 辆成功停车，Fable 5.2 为 40 辆中 26 辆. 两次搭建分别耗时 5.6 和 24 分钟.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

类型: Evaluation | 日期: 2026-11-14

---

<a id="case-181"></a>
### 案例 181: [Hydrogen 在 Terminal-Bench 4.0 中的表现](https://x.com/gosrum/status/2121785156273160558) (作者 [@gosrum](https://x.com/gosrum))

**选命令行编程模型时，一起考虑基准完成率与任务费用.**

这项独立的 Terminal-Bench 4.0 测试对照 Hydrogen、Claude Opus 5.5 和 GPT-6.1 Sol. 评测者报告成绩相近、费用居两者之间，并提醒运行环境的成熟度影响实际采用.

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

类型: Benchmark | 日期: 2026-11-15

---

<a id="case-183"></a>
### 案例 183: [三款 Gemini 模型制作章鱼动画](https://x.com/teddyaisi/status/2121800606406885880) (作者 [@teddyaisi](https://x.com/teddyaisi))

**观察触手抓住岩石后是否明显带动身体前进.**

创作者展示 Carbon、Argon 和 Hydrogen 在同一 Three.js 任务上的结果，其中章鱼抓住礁石边缘并向前拉动自己. 作者请读者比较触手与身体动作的连贯性.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-187"></a>
### 案例 187: [一项城堡建模测试](https://x.com/nemumusitocha/status/2121848375998063012) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**对比多次模型运行的城堡输出和资源用量.**

创作者展示由 Hydrogen 生成的 3D 城堡，并链接往期模型的对照. 其报告的 Google AI Pro 周额度 3% 仅对应本次运行.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-191"></a>
### 案例 191: [新增范围后项目估时大幅改变](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**交付时间发生大幅变化时，要求模型说明项目范围与假设.**

创作者分享对话，要求更现实的工期和完整功能后，预计时间从一个月增加到一年. 对话里没有实际交付记录.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-15

---

<a id="case-193"></a>
### 案例 193: [考虑闰年边界的日历问题](https://x.com/itsvishaltwt/status/2121891117050589249) (作者 [@itsvishaltwt](https://x.com/itsvishaltwt))

**提出简单换算问题，检查答案是否考虑日历边界情况.**

创作者问 Hydrogen High 和 GPT 一年有多少秒. 两份截图都列出平年与闰年的秒数，Hydrogen 还算出了公历平均年的秒数.

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

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-196"></a>
### 案例 196: [回答引用了过时的订阅额度](https://x.com/take14262/status/2121934737539514533) (作者 [@take14262](https://x.com/take14262))

**评估研究助手时，对照一手来源核实计划条款和模型名称.**

作者展示 Hydrogen 混淆相似模型名，且给出过时的 Qwen 套餐额度周期. 截图记录了这几处疑似引用错误.

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

类型: Limit | 日期: 2026-11-15

---

<a id="case-197"></a>
### 案例 197: [修改 WebGL 动画的叙事](https://x.com/snakajima/status/2121939899242996058) (作者 [@snakajima](https://x.com/snakajima))

**首版技术效果丰富却缺少清楚脉络时，要求增强叙事.**

创作者附上 WebGL 初版，指出它嘈杂且缺少故事，再展示给出反馈后的第二版. 作者更喜欢修改版，对照中仍偏好 Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

类型: Limit | 日期: 2026-11-15

---

<a id="case-199"></a>
### 案例 199: [两款模型用代码制作山间斗龙](https://x.com/DrstaOne/status/2121947540509831302) (作者 [@DrstaOne](https://x.com/DrstaOne))

**比较同一场景中的两方角色互动.**

创作者分享 Qwen-4 Max 和 Hydrogen 用代码制作的山寺上空斗龙动画，并注明提示词由另一创作者提供.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-201"></a>
### 案例 201: [可复用的 Three.js 鹈鹕提示词](https://x.com/Aki_LIG/status/2121960943361896596) (作者 [@Aki_LIG](https://x.com/Aki_LIG))

**检查骑行动画中腿、车轮和转向能否同步.**

创作者公布完整日语 Three.js 提示词，录下 Hydrogen 在海岸公路场景中的输出，并称曾将同一提示词交给 GPT-6.1 Terra. 该录屏展示 Hydrogen 这次运行.

**提示词:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-205"></a>
### 案例 205: [同一个小屋任务在三种环境中运行](https://x.com/doe_naps/status/2121999317628330476) (作者 [@doe_naps](https://x.com/doe_naps))

**把视觉任务迁移到不同模型档和平台时，检查输出格式.**

创作者报告，在 Antigravity 中使用 Hydrogen High 和 Carbon High、在 AI Studio 使用 Hydrogen Extra High 都得到静态结果. Arena 标注为 Hydrogen 的一次运行生成了动画 SVG，该检查点身份未被独立核实.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-206"></a>
### 案例 206: [用同一提示词对比仪表盘](https://x.com/fiapp_pro/status/2122014257667846338) (作者 [@fiapp_pro](https://x.com/fiapp_pro))

**用同一个前端提示词比较界面布局和信息层次.**

作者并排发布归因于 GPT-6.1 Sol 与 Hydrogen 的网页界面截图. 截图可供视觉对照，实现、设置和实际功能未说明.

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

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-209"></a>
### 案例 209: [两款模型用代码制作横版动画](https://x.com/rubenssoto_ai/status/2122035198728814753) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**比较生成的动作场景时，关注动作连续性和制作费用.**

创作者对比 Hydrogen 与 GPT-6 Astra 的横版卷轴动画，偏好 Hydrogen 更自然的动作，并报告在两次运行中 Hydrogen 费用更低.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

类型: Evaluation | 日期: 2026-11-15

---

<a id="case-212"></a>
### 案例 212: [日语回答里的数学公式未渲染](https://x.com/ToraMutton/status/2122131489718759930) (作者 [@ToraMutton](https://x.com/ToraMutton))

**回答含 TeX 指令时，同时检查内容和公式显示.**

作者展示切换到 Hydrogen 后的一条日语 Gemini 回答，显示原始数学符号而未排成公式. 截图记录了该界面的一次格式问题.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

类型: Limit | 日期: 2026-11-16

---

<a id="case-214"></a>
### 案例 214: [测试模型能否遵守保持沉默的指令](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**流程要求不回复时，检查模型能否真正不产生答复.**

作者分享不回复测试的截图，报告与 Carbon 和 Argon 的行为不同. 原帖展示了一组测试.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

类型: Evaluation | 日期: 2026-11-16

---

<a id="case-216"></a>
### 案例 216: [三款模型解释电动机原理](https://x.com/analogalok/status/2122221106304352257) (作者 [@analogalok](https://x.com/analogalok))

**在同一个模拟提示词下，比较画面清晰度与教学控件.**

创作者比较 Hydrogen 与两款 Qwen 模型，更偏好 Hydrogen 的 3D 电动机和物理解释. 判断来自一次对照.

**提示词:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

类型: Evaluation | 日期: 2026-11-16

---

<a id="case-217"></a>
### 案例 217: [两种模型工作流制作桌面动画](https://x.com/GeroXBT/status/2122234332102435128) (作者 [@GeroXBT](https://x.com/GeroXBT))

**对照原始任务检查画面细节、音量和片尾是否保持静止.**

创作者以同一提示词通过 API 对照 Hydrogen 与 Astra 辅助制作的桌面动画，认为 Gemini 版本更流畅，片尾仍然在动且音量较低. 渲染流程未说明.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

类型: Evaluation | 日期: 2026-11-16

---

<a id="case-221"></a>
### 案例 221: [带程序化音效的 2D 村庄](https://x.com/marcthecreatorr/status/2122266495216459841) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**记录搭建耗时，并检查声音是否随画面中的事件变化.**

创作者用 Extra High 的 Hydrogen 与 Qwen 4 Max 搭建 2D 村庄，报告 Qwen 约 75 分钟、$0.90，Hydrogen 约 12 分钟、$1.70. 作者更喜欢 Hydrogen 中音乐与事件的配合.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[播放来源视频](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

类型: Evaluation | 日期: 2026-11-16

---

<a id="related-repositories"></a>
## 相关仓库

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon 示例与对比

<a id="acknowledge"></a>
## 🙏 致谢

感谢公开分享 Hydrogen 作品的创作者、开发者和评测者

**来源创作者:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*署名依据所引用的公开来源，未必能够识别最早的创作者；如需更正或请求移除，请提交附有公开来源的 issue*

请按照贡献检查清单，通过 issue 或 pull request 推荐有来源依据的示例
