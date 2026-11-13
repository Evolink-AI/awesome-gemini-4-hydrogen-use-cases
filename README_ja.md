<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/ja/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=docs_link)

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

# Gemini 4 Hydrogen 活用ガイドと厳選事例

## 🍌 はじめに

出典に基づくアプリケーション、コーディングのワークフロー、実践的な比較を通じて Gemini 4 Hydrogen を探ります。

**厳選した40の事例で、何が作られ、どのように作業が進み、結果にどんな不足があったかを紹介します。**

各事例に出典リンクと作者を記載しています。デモ、提供元の事例、制作者による比較は注記で区別し、未公開のプロンプトは再構成していません。

## 📊 概要

- 2026年11月13日に収集した、最大500件の X 投稿の中から75件のデモ投稿を確認し、40事例を選びました。
- エージェント、学習とアプリ、スプレッドシートと検索、インタラクティブ3D、比較と限界の5分野を扱います。
- 選定した出典のビジュアル素材41点をすべて保存しています。ポスター画像付きの再生可能な動画38本と画像3点です。
- Gemini 4 Hydrogen は2026年11月12日に発表されました。モデルと現在の利用方法は EvoLink で確認できます。

> [!NOTE]
> 特に断りがない限り、モデルの帰属、費用、所要時間、結果は出典側の主張です。動画は抽出フレームで確認しており、完全な機能テストは行っていません。コードで作られたアプリの録画は、ネイティブ動画生成の証拠ではありません。実行環境、推論レベル、反復回数が異なる比較は、条件を統制した比較ではありません。

**公式資料: [Google の発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind のモデルカード](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**ここから始める: [EvoLink で Hydrogen を探る](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [API キーを取得](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ クイックスタート

まず EvoLink から始め、Hydrogen をアプリに組み込む際は Gemini ネイティブ API を利用してください。

1. [ブラウザで Gemini 4 Hydrogen を見る](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [EvoLink API キーを作成・管理](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

最小構成のネイティブ API リクエスト

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

[Gemini ネイティブ API クイックスタートを読む](https://evolink.ai/docs/ja/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> レスポンスの candidates[].content.parts[].text フィールドから生成テキストを読み取ります。

> [!IMPORTANT]
> API キーは環境変数に保存し、決してコミットしないでください。ストリーミング、推論、その他のリクエストオプションは API ドキュメントを参照してください。

## 📑 目次

| セクション | 事例 |
|---|---|
| [⚡ エージェントとコーディングのワークフロー](#agents) | 5 |
| [💻 アプリと学習](#apps-learning) | 5 |
| [📊 スプレッドシートと検索](#data-search) | 4 |
| [🎮 インタラクティブ3DとUI](#interactive-3d) | 9 |
| [🧪 比較と限界](#comparisons-limits) | 17 |
| [関連リポジトリ](#related-repositories) |  |
| [クイックスタート](#quick-start) |  |
| [謝辞](#acknowledge) |  |

| 事例 | 分類 | 試すこと | 種類 |
|---|---|---|---|
| [Antigravity でのコードベース保守](#case-1) | エージェントとコーディングのワークフロー | 範囲を限定した保守タスクで、編集、ツール利用、検証をまとめて評価します。 | Demo |
| [16個の Canvas アプリを並列構築](#case-2) | エージェントとコーディングのワークフロー | 構築作業を独立したモジュールに分け、計画、実装、品質確認の役割を明確にします。 | Demo |
| [複数モデルの群で作る深紅の蛾](#case-3) | エージェントとコーディングのワークフロー | 対話型のクリエイティブコーディングで、統括と実装を別の役割に分けます。 | Demo |
| [3D Medic による検査と修復](#case-4) | エージェントとコーディングのワークフロー | 3D ファイルを検査してエラーを発見し、エクスポート前に修復案を示すエージェントを試します。 | Demo |
| [Devin で構築した帆船の風景](#case-5) | エージェントとコーディングのワークフロー | 実際に使う予定のコーディングエージェント環境でモデルを評価します。 | Demo |
| [Lingo City で語学練習](#case-6) | アプリと学習 | フラッシュカードと対話型の街並みを組み合わせ、文脈のある語学練習を行います。 | Demo |
| [3D 紙芝居で学ぶロミオとジュリエット](#case-7) | アプリと学習 | 明確な学習目標を持つ授業を、対話型の場面に変えます。 | Demo |
| [デザイン画像から読書管理サイトへ](#case-8) | アプリと学習 | 参考デザインを使い、視覚理解と動作するフロントエンドの実装を評価します。 | Demo |
| [20モジュールで作る錦鯉の庭](#case-9) | アプリと学習 | 一度のプロンプトで完成を期待せず、小さなモジュールで大きな風景を構築します。 | Demo |
| [陽子核融合を学ぶゲーム](#case-10) | アプリと学習 | 科学的過程を対話的に説明する試作を作り、科学的内容を確認します。 | Demo |
| [Google Sheets の動く風景](#case-11) | スプレッドシートと検索 | 変わったスプレッドシートアニメーションで、生成コードとセル単位の更新を確認します。 | Demo |
| [Folio 風の対話型データサイト](#case-12) | スプレッドシートと検索 | 小さなウェブ試作で、ランディングページと対話型データ可視化を組み合わせます。 | Demo |
| [複数条件の検索質問への視覚的回答](#case-13) | スプレッドシートと検索 | 細かな条件を複数含む検索依頼で、回答の配置と引用リンクを比較します。 | Demo |
| [Sheets の対話型財務予測](#case-14) | スプレッドシートと検索 | 前提を見える形で財務モデルを試作し、生成された数式やグラフを調べます。 | Demo |
| [操作できるダイニングルーム](#case-15) | インタラクティブ3DとUI | 静止画だけで判断せず、物体の操作、照明、状態変化を確認します。 | Demo |
| [小さな世界を備えた音量スライダー](#case-16) | インタラクティブ3DとUI | 身近な操作部品で、操作設計と動く風景の細部を一緒に試します。 | Demo |
| [Three.js の日本家屋](#case-17) | インタラクティブ3DとUI | 詳細な3Dウォークスルーを評価するときは、コード生成と描画の時間を分けます。 | Demo |
| [自転車に乗る3Dペリカン](#case-18) | インタラクティブ3DとUI | 動くキャラクターで、協調動作、動き、場面の一貫性を確認します。 | Demo |
| [計画を先に与える惑星シミュレーター](#case-19) | インタラクティブ3DとUI | 複雑な場面の編集を頼む前に、コーディングモデルに具体的な計画を渡します。 | Demo |
| [Antigravity Swarm で作る港の島](#case-20) | インタラクティブ3DとUI | 小さく移動可能な環境で、複数エージェントによる場面構築を確認します。 | Demo |
| [エッフェル塔の浮島](#case-21) | インタラクティブ3DとUI | 小さなランドマークの場面で、構図、カメラの動き、生成コードを評価します。 | Demo |
| [飛行できる未来都市](#case-22) | インタラクティブ3DとUI | 最初の出力を完成品とみなさず、手続き的に作られた世界への追加編集を試します。 | Demo |
| [日の出から夜までの水上飛行機](#case-23) | インタラクティブ3DとUI | 対話型3D場面の環境操作と照明の移り変わりを調べます。 | Demo |
| [ネオン棒人間アニメーション：Hydrogen と Opus](#case-24) | 比較と限界 | 実行環境が同じだと仮定せず、完成アニメーションと報告された時間・費用を比較します。 | Evaluation |
| [ロボットの作業と自ら認識したミス](#case-25) | 比較と限界 | ロボット評価に、作業の完了と小さなミスの認識を含めます。 | Evaluation |
| [自然言語で動く実験室ワークセル](#case-26) | 比較と限界 | ツールの実行と失敗への対応を、ベンチマークの代表的な点数とは分けて評価します。 | Evaluation |
| [氷山とタグボート：Hydrogen と Carbon](#case-27) | 比較と限界 | 長時間の3D構築を比べるときは、推論レベルと実行環境の制約を記録します。 | Evaluation |
| [ゼリーの錦鯉池：Hydrogen と Sonnet](#case-28) | 比較と限界 | ベンチマーク順位からモデルを選ぶ前に、具体的な場面を調べます。 | Evaluation |
| [同じプロンプトを使う創作コード集](#case-29) | 比較と限界 | 多様な視覚課題を使い、魅力的な一つの出力からの過度な一般化を避けます。 | Evaluation |
| [Megamind のボクセル：費用と品質の反例](#case-30) | 比較と限界 | モデルが常に安いか、視覚的に優れるかを評価するときは失敗例も残します。 | Limit |
| [四季を巡るジャグリングのライオン](#case-31) | 比較と限界 | 周辺画面の美しさだけでなく、指定された動きを確認します。 | Limit |
| [3モデルの棒人間格闘：遅く高価な結果](#case-32) | 比較と限界 | 宣伝される効率と実際の作業報告を比較するときは、反例も残します。 | Limit |
| [農場の自転車風景：Hydrogen と Flash](#case-33) | 比較と限界 | 制作者の報告した完了時間とともに、動きや風景の品質を比較します。 | Evaluation |
| [タンデム自転車の少女と猫](#case-34) | 比較と限界 | 異なるコーディング環境を明示しながら、指示への忠実さと追加の細部を比較します。 | Evaluation |
| [4モデルが作る Three.js マリオゲーム](#case-35) | 比較と限界 | 同じプロンプトによるゲーム比較を解釈する前に、異なる推論設定を記録します。 | Evaluation |
| [3つの Gemini モデルが描くコントローラー](#case-36) | 比較と限界 | 系列内の序列を決めつけず、課題ごとの退歩と改善を探します。 | Evaluation |
| [アプリと Studio で異なる画像認識の回答](#case-37) | 比較と限界 | 画像認識の結果を頼る前に、使う予定の製品画面で同じ画像を試します。 | Limit |
| [ロケット打ち上げ：Hydrogen と Flash](#case-38) | 比較と限界 | 報告された構築時間に加え、実際の打ち上げアニメーションも比較します。 | Evaluation |
| [4つの SVG アニメーション課題](#case-39) | 比較と限界 | 複数の操作・アニメーションの題材で、課題をまたいだ一貫性を確認します。 | Evaluation |
| [3モデルが動かすサバンナの馬](#case-40) | 比較と限界 | 広い範囲の費用や品質の主張を受け入れる前に、動きと視覚的細部を直接確認します。 | Evaluation |

<a id="agents"></a>
## ⚡ エージェントとコーディングのワークフロー

<a id="case-1"></a>
### 事例 1: [Antigravity でのコードベース保守](https://x.com/antigravity/status/2120944334023389476) (作者 [@antigravity](https://x.com/antigravity))

**範囲を限定した保守タスクで、編集、ツール利用、検証をまとめて評価します。**

Antigravity の公開デモは Hydrogen によるコードベース保守を示しています。プラットフォームが制作した事例であり、独立して再現されたエンジニアリングのベンチマークではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-2"></a>
### 事例 2: [16個の Canvas アプリを並列構築](https://x.com/shengzheyao/status/2120944141559550409) (作者 [@shengzheyao](https://x.com/shengzheyao))

**構築作業を独立したモジュールに分け、計画、実装、品質確認の役割を明確にします。**

Google DeepMind の Antigravity CLI 制作者は、Carbon が調整・検証・統合を担当し、Hydrogen が依存関係のない16個の canvas ミニアプリを構築したと説明しています。複数モデルのワークフローなので、成果を Hydrogen だけに帰属させるべきではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-3"></a>
### 事例 3: [複数モデルの群で作る深紅の蛾](https://x.com/thtbee_/status/2120958666480513310) (作者 [@thtbee_](https://x.com/thtbee_))

**対話型のクリエイティブコーディングで、統括と実装を別の役割に分けます。**

制作者によると、Carbon が Antigravity の群を統括し、Hydrogen のワーカーが深紅の蛾の作品を構築しました。報告された45分には複数モデルの作業が含まれ、独立した計時は行われていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-4"></a>
### 事例 4: [3D Medic による検査と修復](https://x.com/GoogleAI/status/2120940683233984862) (作者 [@GoogleAI](https://x.com/GoogleAI))

**3D ファイルを検査してエラーを発見し、エクスポート前に修復案を示すエージェントを試します。**

Google AI の 3D Medic デモは、AI Studio で作られた Managed Agent アプリを使用しています。ファイル修復の流れを示すもので、任意の3Dアセットを正しく修復できる証拠ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-5"></a>
### 事例 5: [Devin で構築した帆船の風景](https://x.com/Da7_Tech/status/2120967690722677144) (作者 [@Da7_Tech](https://x.com/Da7_Tech))

**実際に使う予定のコーディングエージェント環境でモデルを評価します。**

出典は Devin 内で動く Hydrogen によるものとして帆船の風景を紹介しています。短い投稿には完全なプロンプト、反復履歴、再現可能な設定は記載されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

種類: Demo | 日付: 2026-11-12

---


<a id="apps-learning"></a>
## 💻 アプリと学習

<a id="case-6"></a>
### 事例 6: [Lingo City で語学練習](https://x.com/tulseedoshi/status/2121095754844713427) (作者 [@tulseedoshi](https://x.com/tulseedoshi))

**フラッシュカードと対話型の街並みを組み合わせ、文脈のある語学練習を行います。**

Tulsee Doshi は、独自の2D・3Dフラッシュカードをストリーミングし、仮想都市で店主との会話を練習できる Google の事例を紹介しています。提供元のデモであり、独立した学習効果の研究ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-7"></a>
### 事例 7: [3D 紙芝居で学ぶロミオとジュリエット](https://x.com/techartist_/status/2120957446202253803) (作者 [@techartist_](https://x.com/techartist_))

**明確な学習目標を持つ授業を、対話型の場面に変えます。**

制作者は GCSE 英文学向けに、ロミオとジュリエットのバルコニー場面を扱う3D紙芝居の授業を作りました。出典は画面を示していますが、学習効果は測定していません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-8"></a>
### 事例 8: [デザイン画像から読書管理サイトへ](https://x.com/thebuggeddev/status/2120952661046689992) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**参考デザインを使い、視覚理解と動作するフロントエンドの実装を評価します。**

制作者は Hydrogen がデザイン画像から動作する読書管理サイトを5分27秒で作ったと述べています。時間と完成度は出典の主張であり、本コレクションでは独立した機能テストを行っていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-9"></a>
### 事例 9: [20モジュールで作る錦鯉の庭](https://x.com/IamEmily2050/status/2120951069874532806) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**一度のプロンプトで完成を期待せず、小さなモジュールで大きな風景を構築します。**

制作者は Gemini アプリ内で20のプロンプトから20モジュールを作り、各90–270秒かかったと報告しています。早期アクセスの提供を明示しており、一度で完成した例ではなく、反復を前提とした事例です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-10"></a>
### 事例 10: [陽子核融合を学ぶゲーム](https://x.com/SidraMiconi/status/2120948703095820743) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**科学的過程を対話的に説明する試作を作り、科学的内容を確認します。**

制作者のゲームは若い恒星内部の陽子–陽子連鎖反応をたどります。1プロンプト、実行時間78秒、約 $0.19 という数値は出典の主張であり、独立して再現した結果ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

種類: Demo | 日付: 2026-11-12

---


<a id="data-search"></a>
## 📊 スプレッドシートと検索

<a id="case-11"></a>
### 事例 11: [Google Sheets の動く風景](https://x.com/Google/status/2121004369617485896) (作者 [@Google](https://x.com/Google))

**変わったスプレッドシートアニメーションで、生成コードとセル単位の更新を確認します。**

Google は Antigravity で書いたコードを使い、セルに海辺の列車、雲、紅葉を描いています。公式の創作デモであり、スプレッドシートの性能ベンチマークではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-12"></a>
### 事例 12: [Folio 風の対話型データサイト](https://x.com/vamsibatchuk/status/2120996342923436188) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**小さなウェブ試作で、ランディングページと対話型データ可視化を組み合わせます。**

Google DeepMind の社員が、Google AI Studio で構築した Folio 風サイトと対話型アニメーションを紹介しています。完全な生成プロンプトや独立した機能テストは公開されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-13"></a>
### 事例 13: [複数条件の検索質問への視覚的回答](https://x.com/Google/status/2120960715011883148) (作者 [@Google](https://x.com/Google))

**細かな条件を複数含む検索依頼で、回答の配置と引用リンクを比較します。**

Google の検索例は、意図理解、視覚的配置、比較表、クエリの展開を組み合わせています。これらは提供元が説明する製品の動作であり、掲載元の順位や流入への影響を実証するものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-14"></a>
### 事例 14: [Sheets の対話型財務予測](https://x.com/ChanduThota/status/2120942270627414079) (作者 [@ChanduThota](https://x.com/ChanduThota))

**前提を見える形で財務モデルを試作し、生成された数式やグラフを調べます。**

Chandu Thota が Google Sheets の予測デモを紹介しています。canvas の生成が30%以上速いという出典の記述は提供元の主張であり、本リポジトリで行った統制された計時測定ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

種類: Demo | 日付: 2026-11-12

---


<a id="interactive-3d"></a>
## 🎮 インタラクティブ3DとUI

<a id="case-15"></a>
### 事例 15: [操作できるダイニングルーム](https://x.com/notjazii/status/2120979811569222137) (作者 [@notjazii](https://x.com/notjazii))

**静止画だけで判断せず、物体の操作、照明、状態変化を確認します。**

制作者は照明、ランプ、冷蔵庫、その中の物品を操作できる部屋を示しています。構築に30分かかったという報告は独立して確認されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-16"></a>
### 事例 16: [小さな世界を備えた音量スライダー](https://x.com/vib3coded/status/2120973294090555890) (作者 [@vib3coded](https://x.com/vib3coded))

**身近な操作部品で、操作設計と動く風景の細部を一緒に試します。**

出典は小さな和風世界が動く音量スライダーを示しています。制作者は費用を $0.19 としていますが、請求明細や完全な生成手順は示していません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-17"></a>
### 事例 17: [Three.js の日本家屋](https://x.com/SPAC89/status/2120972954146140409) (作者 [@SPAC89](https://x.com/SPAC89))

**詳細な3Dウォークスルーを評価するときは、コード生成と描画の時間を分けます。**

制作者はエージェントを使わず、Hydrogen が Three.js で家と庭を作ったとしています。定額契約の使用量や2時間未満という記述は作者の環境に固有で、一般的な価格や待ち時間を保証するものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-18"></a>
### 事例 18: [自転車に乗る3Dペリカン](https://x.com/nehstrr3/status/2120953932692537722) (作者 [@nehstrr3](https://x.com/nehstrr3))

**動くキャラクターで、協調動作、動き、場面の一貫性を確認します。**

制作者は自転車に乗る3Dアニメーションのペリカンを紹介し、モデルを Hydrogen の XHigh としています。成果のデモであり、完全に再現可能なプロンプトや物理検証ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-19"></a>
### 事例 19: [計画を先に与える惑星シミュレーター](https://x.com/The_Alex/status/2120950301318582643) (作者 [@The_Alex](https://x.com/The_Alex))

**複雑な場面の編集を頼む前に、コーディングモデルに具体的な計画を渡します。**

早期アクセスを得た制作者は惑星シミュレーターを示し、詳しい計画を渡すと編集結果が改善したと報告しています。着想の出典を ForwardEditor とし、反復型の作業を説明しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-20"></a>
### 事例 20: [Antigravity Swarm で作る港の島](https://x.com/ai_for_success/status/2120942147780464660) (作者 [@ai_for_success](https://x.com/ai_for_success))

**小さく移動可能な環境で、複数エージェントによる場面構築を確認します。**

制作者は早期アクセスを明示し、Antigravity の Swarm 機能内で Hydrogen が作った港の島を示しています。公開投稿では統括手順やプロンプト履歴の全体は説明されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-21"></a>
### 事例 21: [エッフェル塔の浮島](https://x.com/RezAIT00/status/2120940988780736973) (作者 [@RezAIT00](https://x.com/RezAIT00))

**小さなランドマークの場面で、構図、カメラの動き、生成コードを評価します。**

出典はエッフェル塔のミニチュア島を示し、Hydrogen XHigh の成果としています。構築と録画が6分というのは作者の報告であり、独立した計時テストではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-22"></a>
### 事例 22: [飛行できる未来都市](https://x.com/kimmonismus/status/2120940617169826037) (作者 [@kimmonismus](https://x.com/kimmonismus))

**最初の出力を完成品とみなさず、手続き的に作られた世界への追加編集を試します。**

早期アクセスを得た制作者は Antigravity で Hydrogen High を使い、1回の追加指示で手続き的な高層建築、雨、空飛ぶ交通を備えた Three.js 都市を作ったと報告しています。録画は生成コードの実行を示すもので、ネイティブ動画生成ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-23"></a>
### 事例 23: [日の出から夜までの水上飛行機](https://x.com/LuminaBench/status/2120939312564842663) (作者 [@LuminaBench](https://x.com/LuminaBench))

**対話型3D場面の環境操作と照明の移り変わりを調べます。**

LuminaBench の元のデモは水上飛行機と時刻の変化を示し、後に Google が再共有しました。投稿は記録上の一般公開時点より前で、利用経路とモデル呼び出しは独立して確認されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

種類: Demo | 日付: 2026-11-12

---


<a id="comparisons-limits"></a>
## 🧪 比較と限界

<a id="case-24"></a>
### 事例 24: [ネオン棒人間アニメーション：Hydrogen と Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**実行環境が同じだと仮定せず、完成アニメーションと報告された時間・費用を比較します。**

作者は Hydrogen と Opus 5.5 の出力を示し、費用を $1.02 対 $7.43、時間を10分22秒対34分と報告しています。本コレクションでは請求、プロンプト、反復回数、実行設定の同等性を確認していません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-25"></a>
### 事例 25: [ロボットの作業と自ら認識したミス](https://x.com/ArtificialAnlys/status/2120995180891508833) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**ロボット評価に、作業の完了と小さなミスの認識を含めます。**

Artificial Analysis は注ぐ作業と積み木の片付けを示し、Hydrogen が少量のこぼれと閉じていないふたに気づいたとしています。動画と AA-Robotics v0.1 の順位は評価者によるもので、ここで独立再現したものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-26"></a>
### 事例 26: [自然言語で動く実験室ワークセル](https://x.com/danielmckinn0n/status/2120990834246173125) (作者 [@danielmckinn0n](https://x.com/danielmckinn0n))

**ツールの実行と失敗への対応を、ベンチマークの代表的な点数とは分けて評価します。**

出典は自然言語の依頼で動く実験室ワークセルを示し、実験室関連の4つのベンチマーク結果を報告しています。Hydrogen の RareBench の報告点は Opus 5.5 より低く、他の3つは高い結果です。ベンチマーク所有者のデモであり、医学的検証ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-27"></a>
### 事例 27: [氷山とタグボート：Hydrogen と Carbon](https://x.com/EnvolDev/status/2120989670582677930) (作者 [@EnvolDev](https://x.com/EnvolDev))

**長時間の3D構築を比べるときは、推論レベルと実行環境の制約を記録します。**

制作者は両モデルを OpenRouter 経由の High で動かし、Hydrogen は $4.27、1時間23分40秒、Carbon は $8.83、2時間39分10秒と報告しています。条件未統制の出典側の報告であり、普遍的な価格比や速度比ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-28"></a>
### 事例 28: [ゼリーの錦鯉池：Hydrogen と Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (作者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**ベンチマーク順位からモデルを選ぶ前に、具体的な場面を調べます。**

作者は3D錦鯉池の課題で Hydrogen と Sonnet 5.5 を比較しています。視聴者に成果の判断を求めていますが、同等の設定や客観的な品質点数は示していません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-29"></a>
### 事例 29: [同じプロンプトを使う創作コード集](https://x.com/kickingkeys/status/2120985358317875222) (作者 [@kickingkeys](https://x.com/kickingkeys))

**多様な視覚課題を使い、魅力的な一つの出力からの過度な一般化を避けます。**

制作者は Hydrogen、Carbon、Argon に同じプロンプトを渡し、返信に比較を載せたとしています。元投稿の素材はローポリの動物、ネオン街、水彩風の容器を示しており、完全な統制ベンチマークではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-30"></a>
### 事例 30: [Megamind のボクセル：費用と品質の反例](https://x.com/thehypedotnews/status/2120980737012670720) (作者 [@thehypedotnews](https://x.com/thehypedotnews))

**モデルが常に安いか、視覚的に優れるかを評価するときは失敗例も残します。**

出典は Hydrogen の Titan がまとまりに欠け、費用も $36.07 で、Sonnet 5.5 の $8.64 を上回ったとしています。投稿には商業的宣伝が含まれ、費用と品質判断は投稿者の主張です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

種類: Limit | 日付: 2026-11-12

---

<a id="case-31"></a>
### 事例 31: [四季を巡るジャグリングのライオン](https://x.com/SahilPanhotra/status/2120978349967458704) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**周辺画面の美しさだけでなく、指定された動きを確認します。**

作者は Carbon が交差するジャグリングの軌道を処理した一方、Hydrogen は季節の切り替えやクリッピングが整っていても球を浮かせたままにしたと報告しています。同じ課題の SVG 比較は特定の動作失敗を示すもので、総合順位ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

種類: Limit | 日付: 2026-11-12

---

<a id="case-32"></a>
### 事例 32: [3モデルの棒人間格闘：遅く高価な結果](https://x.com/DanielZambrini/status/2120963180461769183) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**宣伝される効率と実際の作業報告を比較するときは、反例も残します。**

制作者は Hydrogen、Carbon、Argon を比較し、このテストでは Hydrogen が Carbon より遅く高価だったと報告しています。設定、請求、反復回数は独立して確認されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

種類: Limit | 日付: 2026-11-12

---

<a id="case-33"></a>
### 事例 33: [農場の自転車風景：Hydrogen と Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**制作者の報告した完了時間とともに、動きや風景の品質を比較します。**

出典は農場の自転車風景で Hydrogen と Gemini 3.8 Flash を比較し、56秒対6分超と報告しています。一人の制作者によるテストであり、一般的な速度ベンチマークではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-34"></a>
### 事例 34: [タンデム自転車の少女と猫](https://x.com/marcthecreatorr/status/2120956699951628637) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**異なるコーディング環境を明示しながら、指示への忠実さと追加の細部を比較します。**

制作者は同じとする SVG 課題で、Opus 5.5 を Claude Code、Hydrogen を Cursor で動かしました。報告された時間と費用は大きく異なりますが、環境の違いと非公開の反復により、モデルだけを統制した比較にはなりません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-35"></a>
### 事例 35: [4モデルが作る Three.js マリオゲーム](https://x.com/StatsWire/status/2120955723396071548) (作者 [@StatsWire](https://x.com/StatsWire))

**同じプロンプトによるゲーム比較を解釈する前に、異なる推論設定を記録します。**

出典は High の Gemini 3.8 Flash、Argon、Carbon と XHigh の Hydrogen を比較し、外部3Dモデルやテクスチャなしの純粋な Three.js を使用しています。4つの出力を示すもので、推論条件を合わせたベンチマークではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-36"></a>
### 事例 36: [3つの Gemini モデルが描くコントローラー](https://x.com/notjazii/status/2120952314873987271) (作者 [@notjazii](https://x.com/notjazii))

**系列内の序列を決めつけず、課題ごとの退歩と改善を探します。**

制作者は Carbon、Argon、Hydrogen のコントローラー SVG を比較し、再実行したと報告しています。時間と費用は出典の主張であり、モデル品質の一般的な順序を確立するものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-37"></a>
### 事例 37: [アプリと Studio で異なる画像認識の回答](https://x.com/thegenioo/status/2120946497802174688) (作者 [@thegenioo](https://x.com/thegenioo))

**画像認識の結果を頼る前に、使う予定の製品画面で同じ画像を試します。**

出典は Gemini アプリと AI Studio の Hydrogen によるものとして、食べ物の識別に相反する回答を示しています。ルーティング、設定、会話全体の文脈が同一かは独立して検証されていません。

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

種類: Limit | 日付: 2026-11-12

---

<a id="case-38"></a>
### 事例 38: [ロケット打ち上げ：Hydrogen と Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (作者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**報告された構築時間に加え、実際の打ち上げアニメーションも比較します。**

制作者は Hydrogen と Gemini 3.8 Flash の成果を示し、1分未満対約3分と報告しています。一つの課題の視覚比較であり、独立して統制された実行環境はありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-39"></a>
### 事例 39: [4つの SVG アニメーション課題](https://x.com/Angaisb_/status/2120944947193127061) (作者 [@Angaisb_](https://x.com/Angaisb_))

**複数の操作・アニメーションの題材で、課題をまたいだ一貫性を確認します。**

出典は移動、昼夜の変化、開封、カメレオンの課題で Hydrogen と Carbon の出力を並べています。短い元投稿には完全なプロンプト、時間の証拠、客観的採点方法は公開されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-40"></a>
### 事例 40: [3モデルが動かすサバンナの馬](https://x.com/AI_Screening/status/2120944276586823689) (作者 [@AI_Screening](https://x.com/AI_Screening))

**広い範囲の費用や品質の主張を受け入れる前に、動きと視覚的細部を直接確認します。**

制作者は Hydrogen、Carbon、Argon によるサバンナの馬の場面を紹介しています。高速、低費用、高品質という主張は出典側の評価であり、ここで再現した統制比較ではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon の事例と比較

<a id="acknowledge"></a>
## 🙏 謝辞

Hydrogen を使った成果を公開した制作者、開発者、評価者の皆様に感謝します。

**出典の制作者:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening)

*帰属は引用した公開情報に基づき、最初の制作者を特定できているとは限りません。訂正や削除の依頼は、公開の出典を添えて issue を作成してください。*

貢献チェックリストに従い、issue または pull request で出典のある事例を提案してください。
