<div align="center">

<a href="https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/images/banner.png" alt="Awesome Gemini 3.6 Flash guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Gemini 3.6 Flash](https://img.shields.io/badge/Gemini_3.6_Flash-Model_Page-00d4e6)](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=top_badge)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/ja/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=docs_link)

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

# 素晴らしい Gemini 3.6 フラッシュ ガイドと使用例

## 🍌 はじめに

Gemini 3.6 Flash を実際に使用するためのソースに裏付けられたガイドへようこそ

**このリポジトリは、作成者の公開証拠から具体的な Gemini 3.6 Flash ワークフロー、ビルド、評価、比較、および制限を収集します。**

付属のケースはすべて、レビューされたソース パッケージからのものです。タイトルは元の投稿にリンクし、作成者は作成者のプロフィールにリンクし、ソース テキストに実際にそれらが含まれている場合にのみプロンプトが表示されます。

## 📊 概要

- レビューされた 33 のソース投稿から選択された 33 の高信頼ケース
- 対象範囲には、エージェント、コーディング、Web サイト、ゲーム、3D、ベンチマーク スタイルの比較、実際の安全制限が含まれます
- 24 のビデオ ケースすべてに、表示可能なポスターと再生可能な R2 ホスト MP4 が提供されます。画像ケースはレビューされたすべてのソース画像を保存します
- EvoLink は、製品モデル ID を「gemini-3.6-flash」としてリストします。このリポジトリは、現在のモデルと Gemini ネイティブ API サーフェスにリンクします。

> [!NOTE]
> このコレクションは誇大宣伝よりも目に見える証拠を優先します。欠落しているプロンプトを再構築したり、未公開のセットアップ手順を推測したり、1 人の作成者の結果を普遍的なベンチマークに一般化したりすることはありません。

**公式情報: [Google のローンチ発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) · [Google DeepMind モデルカード](https://deepmind.google/models/model-cards/gemini-3-6-flash/)**

**ここから始めましょう: [Gemini 3.6 フラッシュを探索する](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link) · [APIキーを取得する](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key) · [Gemini ネイティブ API ドキュメントを開く](https://evolink.ai/docs/ja/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=docs_link)**

## 📑 メニュー

| セクション | 事例 |
|---|---|
| [⚡ 効率とエージェント](#efficiency-agents) | 8 |
| [💻 コーディングとアプリ](#coding-apps) | 4 |
| [🎮 ウェブ、ゲーム、3D](#web-games-3d) | 10 |
| [🧪 評価と比較](#evaluations) | 8 |
| [🛡️ 安全性と制限](#safety-limits) | 3 |
| [関連リポジトリ](#related-repositories) | 関連リポジトリ |
| [クイックスタート](#quick-start) | クイックスタート |
| [了承する](#acknowledge) | 了承する |

| ケース | カテゴリ | それが示すもの | 種類 |
|---|---|---|---|
| [トークン効率の並列化](#case-1) | 効率とエージェント | エージェント規模のワークロードに Flash モデルを選択する前に、同じワークフローでの出力トークンの使用状況を比較してください。 | Evaluation |
| [反重力におけるレガシーコードの最新化](#case-2) | 効率とエージェント | 制御されたレガシー コード移行タスクを使用して、エージェントの待ち時間、編集品質、完了動作を比較します。 | Evaluation |
| [キャンバストークンの効率テスト](#case-3) | 効率とエージェント | モデルのバージョン間で同じ Canvas タスクを実行し、アーティファクトとトークンの使用状況の両方を検査します。 | Evaluation |
| [ブラウザエージェントベンチマーク](#case-4) | 効率とエージェント | どちらかの指標を単独で最適化するのではなく、ブラウザーとエージェントの成功とコストを合わせてベンチマークします。 | Benchmark |
| [ロングテールファクト検索の効率](#case-5) | 効率とエージェント | 難しい事実検索タスクを使用して、推論ステップと思考トークンのオーバーヘッドを比較します。 | Evaluation |
| [エンタープライズ文書処理](#case-6) | 効率とエージェント | 本番環境のデフォルトを設定する前に、長い特許と文書の解析に対する推論の労力を評価します。 | Benchmark |
| [JetBrains でのエンジニアリング タスクの評価](#case-7) | 効率とエージェント | 客観的なエンジニアリング タスクを構築し、同じ IDE ワークフロー内でモデルの世代を比較します。 | Evaluation |
| [マルチエージェントコードの移行](#case-8) | 効率とエージェント | 同じオーケストレーション プランでコードの移行をテストし、遅延、編集、最終的な品質を比較します。 | Demo |
| [Android ギターチューナー](#case-9) | コーディングとアプリ | 従来のオーディオ ツールと AI 支援の代替チューニングを組み合わせた、焦点を絞ったモバイル ユーティリティのプロトタイプを作成します。 | Demo |
| [信号機シミュレーション](#case-10) | コーディングとアプリ | 生成されたコードがタイミングとランダムなトラフィック動作をキャプチャするかどうかを検査するために、実行可能視覚化のモデルを要求します。 | Demo |
| [キーボードピアノアプリ](#case-11) | コーディングとアプリ | シンプルなインタラクションの概念を、再生可能なキーボード制御の Web アプリケーションに変えます。 | Demo |
| [デスクトップロボット音声アシスタント](#case-12) | コーディングとアプリ | Flash と Flash-Lite の両方を音声アプリケーションに統合し、最初の応答動作を比較します。 | Integration |
| [ゴールデン ゲート ブリッジの HTML エラー](#case-13) | ウェブ、ゲーム、3D | 生成された 3D Web エクスペリエンスを信頼する前に、厳格なファイル配信タスクを使用して、従う指示をテストします。 | Limit |
| [パブリック プロンプトのビジュアル テスト](#case-14) | ウェブ、ゲーム、3D | 作成者の完全なプロンプトが必要な場合は、出力からプロンプトを再構築するのではなく、ソース スレッドを開きます。 | Demo |
| [シングルプロンプトキャンバスゲーム](#case-15) | ウェブ、ゲーム、3D | Canvas で 1 つのプロンプトを使用して、モデルがコンパクトなゲームのコンセプトをインタラクティブな結果にどれだけ早く変換できるかをテストします。 | Demo |
| [ランディング ページのバージョン比較](#case-16) | ウェブ、ゲーム、3D | ランディング ページの実行と視覚的な判断の変更を分離するために、モデルの世代にわたってプロンプトを固定したままにします。 | Evaluation |
| [サブウェイ サーファーズ 3D プロトタイプ](#case-17) | ウェブ、ゲーム、3D | コーディング実験の拡張思考を有効にし、インタラクションの品質と視覚的な忠実性の両方を検査します。 | Demo |
| [1 ページの Web サイト比較](#case-18) | ウェブ、ゲーム、3D | Web サイトのプロンプトと推論レベルを一定に保ち、トークンのコスト、速度、デザインの好みを比較します。 | Evaluation |
| [ワイルドウェストゲームの失敗](#case-19) | ウェブ、ゲーム、3D | 失敗したゲーム生成の出力は、いつモデルを切り替えるか、タスクを修正するかを決定するための証拠として扱います。 | Limit |
| [反重力ゲームのマテリアルの失敗](#case-20) | ウェブ、ゲーム、3D | AI によって生成されたゲーム プロトタイプを受け入れる前に、ビジュアル マテリアルと実際のインタラクション動作の両方を確認してください。 | Limit |
| [ロールス・ロイス SVG の比較](#case-21) | ウェブ、ゲーム、3D | 固定の SVG 主題を使用して、2 つの Flash 世代が形状、詳細、構成をどのように処理するかを比較します。 | Evaluation |
| [リアルな水族館テスト](#case-22) | ウェブ、ゲーム、3D | 境界付き 3D シーンを使用して、モデルのバージョン間でリアリズムと実装の品質を比較します。 | Evaluation |
| [マックス推理でのジェミニ対グロク](#case-23) | 評価と比較 | モデルの評判に依存するのではなく、同じプロンプト設定と最大推論設定を使用して、速度、コスト、出力を比較します。 | Evaluation |
| [最大設定でのジェミニ対ソネット](#case-24) | 評価と比較 | 同一のプロンプトとその最も強力な設定でモデルを比較し、実際に生成されたアーティファクトを検査します。 | Evaluation |
| [視覚理解テスト](#case-25) | 評価と比較 | ビジョン ワークフローにモデルを採用する前に、具体的なイメージ タスクを使用して応答品質と対話スタイルを検査します。 | Demo |
| [ロケットリーグ ゲームのベンチマーク](#case-26) | 評価と比較 | ゲーム生成ベンチマークを繰り返し実行し、ビルド時間と一貫した主観的なランキングの両方を記録します。 | Benchmark |
| [EyeBench の視覚的な比較](#case-27) | 評価と比較 | 安定した視覚的なベンチマークを使用して、増分的な効率の向上と絶対的な品質を区別します。 | Benchmark |
| [切り絵アニメーションの比較](#case-28) | 評価と比較 | クリエイティブ生成を評価する場合は、応答速度と最終的なアニメーションを個別に比較します。 | Evaluation |
| [AI アリーナ生成ベンチマーク](#case-29) | 評価と比較 | 同じアリーナ タスクを使用して、複数のコーディング モデル間でビルド時間、価格、アーティファクトの品質を比較します。 | Benchmark |
| [クロスモデル ゲームのビルド コスト](#case-30) | 評価と比較 | ゲームのプロトタイピング用のモデルを選択する際は、イテレーション数、開発者のエクスペリエンス、機能、コストを合わせて追跡します。 | Benchmark |
| [サイバーセキュリティ拒否ベンチマーク](#case-31) | 安全性と制限 | 攻撃的なリクエストによって防御的なコードレビューがブロックされる可能性があるため、セキュリティツールの評価に拒否動作を含めます。 | Limit |
| [知識の鮮度の低下](#case-32) | 安全性と制限 | 主張されている知識の遮断を信頼するのではなく、検索によって現在の事実を確認します。 | Limit |
| [脱獄レッドチームテスト](#case-33) | 安全性と制限 | ジェイルブレイクの主張は、再利用可能な指示としてではなく、管理された再現と安全性のレビューを必要とするレッドチームの信号として扱います。 | Limit |

<a id="efficiency-agents"></a>
## ⚡ 効率とエージェント

<a id="case-1"></a>
### ケース 1: [トークン効率の並列化](https://x.com/JeffDean/status/2079591562145870043) (によって [@JeffDean](https://x.com/JeffDean))

**エージェント規模のワークロードに Flash モデルを選択する前に、同じワークフローでの出力トークンの使用状況を比較してください。**

Jeff Dean 氏は、Gemini 3.6 フラッシュと 3.5 フラッシュを比較する比較デモを共有し、新しいモデルではトークンの使用量が少ないことを強調しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-01.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-2"></a>
### ケース 2: [反重力におけるレガシーコードの最新化](https://x.com/antigravity/status/2079663375991046351) (によって [@antigravity](https://x.com/antigravity))

**制御されたレガシー コード移行タスクを使用して、エージェントの待ち時間、編集品質、完了動作を比較します。**

Google Antigravity は、レガシー ソフトウェアを再構築する両方の Flash 世代をデモンストレーションし、Gemini 3.6 Flash からのレイテンシと出力の改善により完了が速くなったと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-02.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-3"></a>
### ケース 3: [キャンバストークンの効率テスト](https://x.com/stevibe/status/2079599477216956437) (によって [@stevibe](https://x.com/stevibe))

**モデルのバージョン間で同じ Canvas タスクを実行し、アーティファクトとトークンの使用状況の両方を検査します。**

作成者は、短い Canvas タスクで Gemini 3.6 Flash と 3.5 Flash を比較し、3.6 Flash の方がトークンの使用量が大幅に少ないことを観察しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-03.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-4"></a>
### ケース 4: [ブラウザエージェントベンチマーク](https://x.com/browser_use/status/2079602472516264010) (によって [@browser_use](https://x.com/browser_use))

**どちらかの指標を単独で最適化するのではなく、ブラウザーとエージェントの成功とコストを合わせてベンチマークします。**

ブラウザ使用率では、Gemini 3.6 Flash の BU ベンチマークが 68% であるのに対し、GPT-5.6 Sol は 67%、Sonnet 4.6 は 62%、Opus 4.8 は 74% でした。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-04-01.jpg" alt="Case 4 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-07-21

---

<a id="case-5"></a>
### ケース 5: [ロングテールファクト検索の効率](https://x.com/__apf__/status/2079603658141184134) (によって [@__apf__](https://x.com/__apf__))

**難しい事実検索タスクを使用して、推論ステップと思考トークンのオーバーヘッドを比較します。**

作成者は、複雑なロングテール ファクト検索タスクで Gemini 3.5 と 3.6 Flash を直接実行し、3.6 Flash のステップ数が半分、思考トークンが 75% 少ないと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-05.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-6"></a>
### ケース 6: [エンタープライズ文書処理](https://x.com/databricks/status/2079598684455551326) (によって [@databricks](https://x.com/databricks))

**本番環境のデフォルトを設定する前に、長い特許と文書の解析に対する推論の労力を評価します。**

Databricks は、3.5 Flash よりも文書分類の精度が高く、長い特許で優れた結果が得られ、文書解析では高労力よりも中労力の方が総トークン数が約 32% 少ないと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-06-01.png" alt="Case 6 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-07-21

---

<a id="case-7"></a>
### ケース 7: [JetBrains でのエンジニアリング タスクの評価](https://x.com/jetbrains/status/2079618218587574636) (によって [@jetbrains](https://x.com/jetbrains))

**客観的なエンジニアリング タスクを構築し、同じ IDE ワークフロー内でモデルの世代を比較します。**

JetBrains は、AI Assistant および Junie における Gemini 3.6 フラッシュと前世代のフラッシュに対する客観的なエンジニアリング タスクの評価を発表しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-07.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-8"></a>
### ケース 8: [マルチエージェントコードの移行](https://x.com/CodeByPoonam/status/2079607995861021073) (によって [@CodeByPoonam](https://x.com/CodeByPoonam))

**同じオーケストレーション プランでコードの移行をテストし、遅延、編集、最終的な品質を比較します。**

このデモでは、Gemini 3.6 Flash が Antigravity のマルチエージェント オーケストレーションを通じてコード移行を実行する様子が示されており、3.5 Flash よりも遅延が短く、品質が高いことが報告されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-08.mp4)

種類: Demo | 日付: 2026-07-21

---


<a id="coding-apps"></a>
## 💻 コーディングとアプリ

<a id="case-9"></a>
### ケース 9: [Android ギターチューナー](https://x.com/bijanbowen/status/2079675781794443640) (によって [@bijanbowen](https://x.com/bijanbowen))

**従来のオーディオ ツールと AI 支援の代替チューニングを組み合わせた、焦点を絞ったモバイル ユーティリティのプロトタイプを作成します。**

作成者は Gemini 3.6 Flash を使用して、AI 主導の代替チューニング サポートを備えた Android ギター チューナー アプリケーションを構築しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-09.mp4)

種類: Demo | 日付: 2026-07-21

---

<a id="case-10"></a>
### ケース 10: [信号機シミュレーション](https://x.com/diegocabezas01/status/2079588206513631483) (によって [@diegocabezas01](https://x.com/diegocabezas01))

**生成されたコードがタイミングとランダムなトラフィック動作をキャプチャするかどうかを検査するために、実行可能視覚化のモデルを要求します。**

公開プロンプトは、ランダムな速度で車が到着する一方通行の信号機を視覚化する Python コードを要求し、投稿には結果のデモンストレーションが含まれています。

**プロンプト:**

```text
write a python code that visualizes how a traffic light works in a one way street with cars entering at random rate.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-10.mp4)

種類: Demo | 日付: 2026-07-21

---

<a id="case-11"></a>
### ケース 11: [キーボードピアノアプリ](https://x.com/Majin_AppSheet/status/2079734240540041230) (によって [@Majin_AppSheet](https://x.com/Majin_AppSheet))

**シンプルなインタラクションの概念を、再生可能なキーボード制御の Web アプリケーションに変えます。**

作成者は、コンピュータのキーボードから演奏できるピアノ アプリケーションを Gemini 3.6 Flash で構築し、子供たちが探索できるアプリとして組み立てました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-11.mp4)

種類: Demo | 日付: 2026-07-22

---

<a id="case-12"></a>
### ケース 12: [デスクトップロボット音声アシスタント](https://x.com/AILogDev/status/2079716688745132044) (によって [@AILogDev](https://x.com/AILogDev))

**Flash と Flash-Lite の両方を音声アプリケーションに統合し、最初の応答動作を比較します。**

作成者は、デスクトップ ロボット用の音声ダイアログ アプリケーションに Gemini 3.6 Flash と Gemini 3.5 Flash-Lite を追加し、初期応答が少し遅いように感じられるものの、使用できると指摘しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-12.mp4)

種類: Integration | 日付: 2026-07-21

---


<a id="web-games-3d"></a>
## 🎮 ウェブ、ゲーム、3D

<a id="case-13"></a>
### ケース 13: [ゴールデン ゲート ブリッジの HTML エラー](https://x.com/LuminaXspace/status/2079597030922465407) (によって [@LuminaXspace](https://x.com/LuminaXspace))

**生成された 3D Web エクスペリエンスを信頼する前に、厳格なファイル配信タスクを使用して、従う指示をテストします。**

テスターは 3 つのプロンプトを必要とし、モデルが要求された HTML ファイルの代わりにアプリ内シミュレーションと Web 画像応答を試行するのを確認し、最終的な 3D ブリッジ出力が Gemini 3.1 Pro よりも大幅に弱いと判断しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-13.mp4)

種類: Limit | 日付: 2026-07-21

---

<a id="case-14"></a>
### ケース 14: [パブリック プロンプトのビジュアル テスト](https://x.com/Motion_Viz/status/2079592671530938537) (によって [@Motion_Viz](https://x.com/Motion_Viz))

**作成者の完全なプロンプトが必要な場合は、出力からプロンプトを再構築するのではなく、ソース スレッドを開きます。**

MotionViz は、メディア付きの Gemini 3.6 Flash ビジュアル テストを公開し、完全なプロンプトがソース スレッドで利用できることを示しました。このリポジトリは、ソース パッケージに存在しないプロンプト テキストを再構築しません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-14.mp4)

種類: Demo | 日付: 2026-07-21

---

<a id="case-15"></a>
### ケース 15: [シングルプロンプトキャンバスゲーム](https://x.com/ozansihay/status/2079599565565468672) (によって [@ozansihay](https://x.com/ozansihay))

**Canvas で 1 つのプロンプトを使用して、モデルがコンパクトなゲームのコンセプトをインタラクティブな結果にどれだけ早く変換できるかをテストします。**

作成者は Gemini 3.6 Flash を早期アクセスでテストし、単一の Canvas プロンプトを使用してプレイ可能なゲームのデモを作成しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-15.mp4)

種類: Demo | 日付: 2026-07-21

---

<a id="case-16"></a>
### ケース 16: [ランディング ページのバージョン比較](https://x.com/nemumusitocha/status/2079596099854307650) (によって [@nemumusitocha](https://x.com/nemumusitocha))

**ランディング ページの実行と視覚的な判断の変更を分離するために、モデルの世代にわたってプロンプトを固定したままにします。**

作成者は、Gemini 3.6 Flash を同じプロンプトのランディング ページ アーカイブに追加し、新しい結果が Gemini 3 および 3.5 の出力よりも悪いと判断しました。

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-01.jpg" alt="Case 16 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-02.jpg" alt="Case 16 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-16-03.jpg" alt="Case 16 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-17"></a>
### ケース 17: [サブウェイ サーファーズ 3D プロトタイプ](https://x.com/itsPaulAi/status/2079597536155668890) (によって [@itsPaulAi](https://x.com/itsPaulAi))

**コーディング実験の拡張思考を有効にし、インタラクションの品質と視覚的な忠実性の両方を検査します。**

作成者は Gemini 3.6 Flash を使用してシンプルな 3D Subway Surfers スタイルのレプリカを構築し、コーディング タスクに拡張思考を推奨しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-17.mp4)

種類: Demo | 日付: 2026-07-21

---

<a id="case-18"></a>
### ケース 18: [1 ページの Web サイト比較](https://x.com/SaiNemani1/status/2079606113306325496) (によって [@SaiNemani1](https://x.com/SaiNemani1))

**Web サイトのプロンプトと推論レベルを一定に保ち、トークンのコスト、速度、デザインの好みを比較します。**

同じ 1 ページの Web サイトのプロンプトで、作成者は、Gemini 3.6 Flash のトークンが約 6,100 であるのに対し、3.5 Flash のトークンは約 9,300 であると報告しましたが、個人的には古いモデルの外観を好みました。

**プロンプト:**

```text
create a modern website! Should look amazing! One-code page
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-18.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-19"></a>
### ケース 19: [ワイルドウェストゲームの失敗](https://x.com/Mr_Salio/status/2079635008424169901) (によって [@Mr_Salio](https://x.com/Mr_Salio))

**失敗したゲーム生成の出力は、いつモデルを切り替えるか、タスクを修正するかを決定するための証拠として扱います。**

テスターは Wild West ゲーム生成プロンプトを使用し、観察された結果に基づいて Gemini 3.6 Flash が GPT-5.6、Kimi K3、および Fable 5 より大幅に劣っていると判断しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-19.mp4)

種類: Limit | 日付: 2026-07-21

---

<a id="case-20"></a>
### ケース 20: [反重力ゲームのマテリアルの失敗](https://x.com/Conor_D_Dart/status/2079592731211399460) (によって [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**AI によって生成されたゲーム プロトタイプを受け入れる前に、ビジュアル マテリアルと実際のインタラクション動作の両方を確認してください。**

2 回目の反重力ゲーム テストで、作成者は木のテクスチャが弱く、見た目は似ているものの機能しないままの大理石の要素を発見しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-20.mp4)

種類: Limit | 日付: 2026-07-21

---

<a id="case-21"></a>
### ケース 21: [ロールス・ロイス SVG の比較](https://x.com/ggg78g89/status/2079610251444437335) (によって [@ggg78g89](https://x.com/ggg78g89))

**固定の SVG 主題を使用して、2 つの Flash 世代が形状、詳細、構成をどのように処理するかを比較します。**

この投稿では、同じロールスロイス SVG タスクに対して Gemini 3.6 フラッシュ出力と 3.5 フラッシュ出力を並べて配置しています。

**プロンプト:**

```text
SVG of a Rolls Royce
```

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-01.png" alt="Case 21 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-21-02.png" alt="Case 21 source image 2" width="100%"></a>
</td>
</tr>
</table>

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-22"></a>
### ケース 22: [リアルな水族館テスト](https://x.com/intheworldofai/status/2079681107516170431) (によって [@intheworldofai](https://x.com/intheworldofai))

**境界付き 3D シーンを使用して、モデルのバージョン間でリアリズムと実装の品質を比較します。**

作成者は、Gemini 3.6 Flash にリアルな水族館を構築するよう依頼しましたが、3.5 Flash よりもわずかに優れているだけだと判断しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-22.mp4)

種類: Evaluation | 日付: 2026-07-21

---


<a id="evaluations"></a>
## 🧪 評価と比較

<a id="case-23"></a>
### ケース 23: [マックス推理でのジェミニ対グロク](https://x.com/notjazii/status/2079609162431181193) (によって [@notjazii](https://x.com/notjazii))

**モデルの評判に依存するのではなく、同じプロンプト設定と最大推論設定を使用して、速度、コスト、出力を比較します。**

作成者は、Gemini 3.6 Flash と Grok 4.5 を同じプロンプトと最大推論設定で実行し、どちらも高速であり、Grok の方がわずかに高速で安価であることを観察しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-23.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-24"></a>
### ケース 24: [最大設定でのジェミニ対ソネット](https://x.com/notjazii/status/2079617706693902416) (によって [@notjazii](https://x.com/notjazii))

**同一のプロンプトとその最も強力な設定でモデルを比較し、実際に生成されたアーティファクトを検査します。**

作成者は、最大設定で同じプロンプトを使用して Gemini 3.6 Flash と Sonnet 5 をテストし、示されているタスクでは Gemini の出力を優先しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-24.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-25"></a>
### ケース 25: [視覚理解テスト](https://x.com/HarshithLucky3/status/2079607042403381313) (によって [@HarshithLucky3](https://x.com/HarshithLucky3))

**ビジョン ワークフローにモデルを採用する前に、具体的なイメージ タスクを使用して応答品質と対話スタイルを検査します。**

作成者は、Gemini 3.6 Flash が合格した視力テストを提示し、観察された体験の一部としての反応の性格を強調しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-25-01.jpg" alt="Case 25 source image 1" height="360"></a>

種類: Demo | 日付: 2026-07-21

---

<a id="case-26"></a>
### ケース 26: [ロケットリーグ ゲームのベンチマーク](https://x.com/LLMJunky/status/2079712480683790743) (によって [@LLMJunky](https://x.com/LLMJunky))

**ゲーム生成ベンチマークを繰り返し実行し、ビルド時間と一貫した主観的なランキングの両方を記録します。**

作成者は、ロケット リーグ スタイルのタスクで Gemini 3.6 Flash をテストし、個人的なリーダーボードで 3 位にランク付けし、2 分以内に完了したと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-26.mp4)

種類: Benchmark | 日付: 2026-07-21

---

<a id="case-27"></a>
### ケース 27: [EyeBench の視覚的な比較](https://x.com/adonis_singh/status/2079631807817933222) (によって [@adonis_singh](https://x.com/adonis_singh))

**安定した視覚的なベンチマークを使用して、増分的な効率の向上と絶対的な品質を区別します。**

EyeBench では、作成者は Gemini 3.6 Flash が 3.5 Flash よりわずかに優れているものの、Gemini 3.1 Pro Preview よりはまだ悪いと判断しましたが、トークン効率の向上についても言及しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-27-01.jpg" alt="Case 27 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-07-21

---

<a id="case-28"></a>
### ケース 28: [切り絵アニメーションの比較](https://x.com/OriSilver/status/2079603778441957776) (によって [@OriSilver](https://x.com/OriSilver))

**クリエイティブ生成を評価する場合は、応答速度と最終的なアニメーションを個別に比較します。**

作成者は、紙切りアニメーションのタスクに関して Gemini 3.6 Flash と Fable 5 を比較し、Gemini のほぼ即時の反応を賞賛しましたが、結果については懸念を表明しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-28.mp4)

種類: Evaluation | 日付: 2026-07-21

---

<a id="case-29"></a>
### ケース 29: [AI アリーナ生成ベンチマーク](https://x.com/OmedVibeCodes/status/2079663080049660220) (によって [@OmedVibeCodes](https://x.com/OmedVibeCodes))

**同じアリーナ タスクを使用して、複数のコーディング モデル間でビルド時間、価格、アーティファクトの品質を比較します。**

作成者は、Grok 4.5、Gemini 3.6 Flash、および GPT-5.6 Luna を 1 つの AI Arena タスクでテストし、その実行では Gemini の結果が最も弱いと判断しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-29.mp4)

種類: Benchmark | 日付: 2026-07-21

---

<a id="case-30"></a>
### ケース 30: [クロスモデル ゲームのビルド コスト](https://x.com/naymur_dev/status/2079710299918401907) (によって [@naymur_dev](https://x.com/naymur_dev))

**ゲームのプロトタイピング用のモデルを選択する際は、イテレーション数、開発者のエクスペリエンス、機能、コストを合わせて追跡します。**

同じ設計ワークフローを使用して、作成者は、Gemini が生成したジャンプ アンド フォールのバグを修正するには 6 ～ 7 回の反復が必要であると報告し、比較スコアとともに 0.15 ドルの実行コストをリストしました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[ソースビデオを再生する](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-30.mp4)

種類: Benchmark | 日付: 2026-07-21

---


<a id="safety-limits"></a>
## 🛡️ 安全性と制限

<a id="case-31"></a>
### ケース 31: [サイバーセキュリティ拒否ベンチマーク](https://x.com/pilvar222/status/2079602157779566836) (によって [@pilvar222](https://x.com/pilvar222))

**攻撃的なリクエストによって防御的なコードレビューがブロックされる可能性があるため、セキュリティツールの評価に拒否動作を含めます。**

サイバーセキュリティ ベンチマークの実行が拒否されたため、評価者は、テストされたポリシーが防御コードの脆弱性発見動作と悪意のある使用をブロックしたと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-31-01.jpg" alt="Case 31 source image 1" height="360"></a>

種類: Limit | 日付: 2026-07-21

---

<a id="case-32"></a>
### ケース 32: [知識の鮮度の低下](https://x.com/ggg78g89/status/2079587359851737339) (によって [@ggg78g89](https://x.com/ggg78g89))

**主張されている知識の遮断を信頼するのではなく、検索によって現在の事実を確認します。**

テスターは現在の主力モデルを要求し、古い名前を受け取りましたが、その後、このモデルは 2026 年 3 月の生産終了を主張しているにもかかわらず、2025 年初頭までの知識しか認めていないと報告しました。

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-01.jpg" alt="Case 32 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-02.jpg" alt="Case 32 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-03.jpg" alt="Case 32 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-32-04.png" alt="Case 32 source image 4" width="100%"></a>
</td>
</tr>
</table>

種類: Limit | 日付: 2026-07-21

---

<a id="case-33"></a>
### ケース 33: [脱獄レッドチームテスト](https://x.com/Ubannoblesse/status/2079711268899086484) (によって [@Ubannoblesse](https://x.com/Ubannoblesse))

**ジェイルブレイクの主張は、再利用可能な指示としてではなく、管理された再現と安全性のレビューを必要とするレッドチームの信号として扱います。**

この投稿では、Gemini アプリと API 全体でジェイルブレイクを行ったと主張し、テストされた有害なコンテンツのカテゴリをリストしています。このリポジトリは、エクスプロイト命令を再現することなく安全信号を記録します。

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-01.jpg" alt="Case 33 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-02.jpg" alt="Case 33 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-03.jpg" alt="Case 33 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/media/source-cases/case-33-04.jpg" alt="Case 33 source image 4" width="100%"></a>
</td>
</tr>
</table>

種類: Limit | 日付: 2026-07-21

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini Omni Flash API Skill](https://github.com/Evolink-AI/gemini-omni-flash-api-skill) — 検証済みの Gemini 系 API クイックスタートとインストール可能なエージェントスキル
- この公開中に、専用のインストール可能な Gemini 3.6 Flash スキルは個別に検証されていません

<a id="quick-start"></a>
## ⚡ クイックスタート

以下の検証済みパブリック サーフェスを使用して、モデル ID `gemini-3.6-flash` から始めます。

1. [Gemini 3.6 Flash モデル ページを開く](https://evolink.ai/gemini-3-6-flash?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=model_link)
2. [EvoLink API キーを作成または管理する](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=api_key)
3. [Gemini ネイティブ API クイック スタートに従ってください](https://evolink.ai/docs/ja/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-3-6-flash-guide-and-use-cases&utm_content=first_run)

検証済みの最小リクエストを実行します

```bash
export EVOLINK_API_KEY="your_api_key_here"

curl --fail-with-body --silent --show-error \
  --request POST \
  --url "https://direct.evolink.ai/v1beta/models/gemini-3.6-flash:generateContent" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"contents":[{"role":"user","parts":[{"text":"Reply exactly: OK"}]}],"generationConfig":{"candidateCount":1,"maxOutputTokens":128,"temperature":0}}'
```

> [!TIP]
> 期待される結果: 表示テキストが `OK` の JSON レスポンス

> [!IMPORTANT]
> このリクエストは実稼働 endpoint で HTTP 200 と表示結果 `OK` を確認済みです。キーは環境変数に保持し、commit には含めないでください

<a id="acknowledge"></a>
## 🙏 了承する

このコレクションは、作成者と実践者が Gemini 3.6 Flash の作品を公的に共有したために存在します。

**ここに代表されるソース作成者に感謝します:**

[@JeffDean](https://x.com/JeffDean), [@antigravity](https://x.com/antigravity), [@stevibe](https://x.com/stevibe), [@browser_use](https://x.com/browser_use), [@__apf__](https://x.com/__apf__), [@databricks](https://x.com/databricks), [@jetbrains](https://x.com/jetbrains), [@CodeByPoonam](https://x.com/CodeByPoonam), [@bijanbowen](https://x.com/bijanbowen), [@diegocabezas01](https://x.com/diegocabezas01), [@Majin_AppSheet](https://x.com/Majin_AppSheet), [@AILogDev](https://x.com/AILogDev), [@LuminaXspace](https://x.com/LuminaXspace), [@Motion_Viz](https://x.com/Motion_Viz), [@ozansihay](https://x.com/ozansihay), [@nemumusitocha](https://x.com/nemumusitocha), [@itsPaulAi](https://x.com/itsPaulAi), [@SaiNemani1](https://x.com/SaiNemani1), [@Mr_Salio](https://x.com/Mr_Salio), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@ggg78g89](https://x.com/ggg78g89), [@intheworldofai](https://x.com/intheworldofai), [@notjazii](https://x.com/notjazii), [@HarshithLucky3](https://x.com/HarshithLucky3), [@LLMJunky](https://x.com/LLMJunky), [@adonis_singh](https://x.com/adonis_singh), [@OriSilver](https://x.com/OriSilver), [@OmedVibeCodes](https://x.com/OmedVibeCodes), [@naymur_dev](https://x.com/naymur_dev), [@pilvar222](https://x.com/pilvar222), [@Ubannoblesse](https://x.com/Ubannoblesse)

*すべての投稿が最も古いオリジナルの作成者であることを保証することはできません。帰属、翻訳、または表現を修正する必要がある場合は、公開情報源に修正の問題を提起してください*

ソースに裏付けられた別のケースを提案するには、問題またはプルリクエストを開いて、貢献チェックリストに従ってください。
