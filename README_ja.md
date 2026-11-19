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

# Gemini 4 Hydrogen 活用ガイドと厳選事例

## 🍌 はじめに

出典に基づくアプリケーション、コーディングのワークフロー、実践的な比較を通じて Gemini 4 Hydrogen を探ります。

**225 件の事例から、Hydrogen の使い方と出力の限界を確認できます。**

各事例に出典リンクと作者を記載しています。デモ、提供元の事例、制作者による比較は注記で区別し、未公開のプロンプトは再構成していません。

## 📊 概要

- 全 225 件のうち、185 件は X の投稿 1,304 件を確認した 11 月 17 日の更新で追加しました。追加した投稿は収集時に 30 件を超える「いいね」がありました。
- エージェント、学習とアプリ、スプレッドシートと検索、インタラクティブ3D、比較と限界の5分野を扱います。
- 元の投稿にある 264 点のビジュアルを掲載しています。内訳はサムネイル付きの再生可能な動画 168 本と画像 96 枚です。
- Gemini 4 Hydrogen は2026年11月12日に発表されました。モデルと現在の利用方法は EvoLink で確認できます。

> [!NOTE]
> 特に断りがない限り、モデルの帰属、費用、所要時間、結果は出典側の主張です。動画は抽出フレームで確認しており、完全な機能テストは行っていません。コードで作られたアプリの録画は、ネイティブ動画生成の証拠ではありません。実行環境、推論レベル、反復回数が異なる比較は、条件を統制した比較ではありません。

**公式資料: [Google の発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind のモデルカード](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**ここから始める: [EvoLink で Hydrogen を探る](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [API キーを取得 (モデルページから)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)**

<a id="quick-start"></a>
## ⚡ クイックスタート

まず EvoLink から始め、Hydrogen をアプリに組み込む際は Gemini ネイティブ API を利用してください。

1. [ブラウザで Gemini 4 Hydrogen を見る](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [EvoLink API キーを作成・管理 (モデルページから)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)

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

[Gemini ネイティブ API クイックスタートを読む (モデルページから)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

> [!TIP]
> レスポンスの candidates[].content.parts[].text フィールドから生成テキストを読み取ります。

> [!IMPORTANT]
> API キーは環境変数に保存し、決してコミットしないでください。ストリーミング、推論、その他のリクエストオプションは API ドキュメントを参照してください。

## 📑 目次

| セクション | 事例 |
|---|---|
| [⚡ エージェントとコーディングのワークフロー](#agents) | 30 |
| [💻 アプリと学習](#apps-learning) | 37 |
| [📊 スプレッドシートと検索](#data-search) | 9 |
| [🎮 インタラクティブ3DとUI](#interactive-3d) | 48 |
| [🧪 比較と限界](#comparisons-limits) | 101 |
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
| [宇宙の参考画像から HTML シーンを作る](#case-41) | インタラクティブ3DとUI | 少数の参考画像から、見分けのつく画風を再現できるか確認する。 | Demo |
| [Gemini Canvas で作る F1 車両の試作](#case-42) | インタラクティブ3DとUI | 車両ビューアーに複数のカメラを設け、違う角度からモデルを確認する。 | Demo |
| [Hydrogen API と Antigravity の Carbon を比較](#case-43) | 比較と限界 | 同じプロンプトによる描画を比較するときは、それぞれの実行環境を記録する。 | Evaluation |
| [Hydrogen と Astra の影の描写](#case-44) | 比較と限界 | 実行時間と費用を比べながら、細かな描写も確認する。 | Evaluation |
| [プロシージャルな3Dモーションを比較](#case-45) | 比較と限界 | 動きのつながりと構図を見比べながら、生成時間を記録する。 | Evaluation |
| [PokéBench の画像入力テストを89分実行](#case-46) | 比較と限界 | 長時間動く視覚エージェントは、達成結果と併せてターン数と API 失敗件数を記録する。 | Benchmark |
| [Hydrogen と DeepSeek が同じ3Dシーンを制作](#case-47) | 比較と限界 | 描画を比較し、実行時間と API 料金は別々に記録する。 | Evaluation |
| [BMW の側面を SVG で描く](#case-48) | インタラクティブ3DとUI | 車両の側面図で比率、輪郭、細部を確認する。 | Demo |
| [天文学者の浮遊島](#case-49) | インタラクティブ3DとUI | 小さなシーンに明確な主題を設定し、小物と光がその主題を伝えるかを見る。 | Demo |
| [参考画像から歩き回れる3D風景へ](#case-50) | インタラクティブ3DとUI | 画像からできたシーンで、見た目の再現と移動の両方を確かめる。 | Demo |
| [3Dブロックで作るミニチュア風景](#case-51) | インタラクティブ3DとUI | 積み木で小さな風景を作らせ、形がまとまった場面に見えるか確認する。 | Demo |
| [操作できる桜の木](#case-52) | インタラクティブ3DとUI | 動くオブジェクトと少数の操作項目で、シーンがリアルタイムに変わる様子を見る。 | Demo |
| [Agent Arena のタスク別所要時間と費用](#case-53) | 比較と限界 | 全体の成功率に加え、1タスクあたりの所要時間、費用、出力トークンを確認する。 | Benchmark |
| [画像文書とターミナルのベンチマーク](#case-54) | 比較と限界 | 推論予算を決めるときに文書とターミナルの結果を個別に見る。 | Benchmark |
| [Vals Index と Tax Agent の結果](#case-55) | 比較と限界 | 全体評価と併せて、専門タスクのスコアを確認する。 | Benchmark |
| [CursorBench のデフォルト推論レベル](#case-56) | 比較と限界 | デフォルトのスコアを出発点に、自分のリポジトリでテストする。 | Benchmark |
| [4モデルで弓兵の対戦をアニメ化](#case-57) | 比較と限界 | 戦う人物の行動が各アニメーションでどれくらい伝わるか比較する。 | Evaluation |
| [15分で作る Minecraft 風プロトタイプ](#case-58) | アプリと学習 | ボクセルの試作品で、採掘と所持品など複数の機能が連携するか確認する。 | Demo |
| [n8n で Hydrogen にツールを使わせる](#case-59) | エージェントとコーディングのワークフロー | ツールを繰り返し使う処理を Hydrogen に、計画を別ステップに割り当てる。 | Integration |
| [Box Agent で複雑な業務文書を処理](#case-60) | スプレッドシートと検索 | 現実的な文書タスクで正確さ、処理時間、トークン量を測る。 | Benchmark |
| [Devin FrontierCode での Hydrogen](#case-61) | 比較と限界 | 修正をマージできるか確認し、エージェントの実行環境も記録する。 | Benchmark |
| [小さなインタラクティブ作品の屈折表現](#case-62) | インタラクティブ3DとUI | 短いプレビューで光学効果を調整してからシーンを作り込む。 | Demo |
| [上に向かって流れる川](#case-63) | インタラクティブ3DとUI | 普段と逆の動きを指定し、視覚効果を見て確かめる。 | Demo |
| [検索禁止の指示があっても検索を実行](#case-64) | 比較と限界 | 外部検索を使わない回答が必要なときは、実際のツール履歴を確認する。 | Limit |
| [Antigravity Swarm の利用枠を測る](#case-65) | 比較と限界 | 複数エージェントによる処理のトークン量と消費枠を記録する。 | Evaluation |
| [専門職タスクでのツール呼び出し](#case-66) | 比較と限界 | 専門業務の判断前にエージェントがどのように情報を集めるか調べる。 | Benchmark |
| [Hydrogen で作る3D肖像](#case-67) | インタラクティブ3DとUI | 小さな肖像課題で3D表現が人物の特徴を伝えられるか見る。 | Demo |
| [4モデルで魔法使いとドラゴンの戦いを描く](#case-68) | 比較と限界 | 同じファンタジー場面の演出、動きの読みやすさ、効果を比較する。 | Evaluation |
| [マルチエージェント環境の認証経路](#case-69) | エージェントとコーディングのワークフロー | 他社のサービスへタスクを任せるとき、どのクライアントが認証を行うか確かめる。 | Limit |
| [Antigravity の Goal Mode を実行](#case-70) | エージェントとコーディングのワークフロー | 長時間の実装で計画、コード変更、テスト結果を記録する。 | Demo |
| [MazeBench で見えた低い成功率](#case-71) | 比較と限界 | 迷路で空間推論を試し、実務で頼れる範囲を判断する。 | Benchmark |
| [Geminiの3モデルで帆船を描く](#case-72) | 比較と限界 | 同じ Three.js の題材で動きと背景の細部を比較する。 | Evaluation |
| [Antigravity Orchestrator の Carbon と Hydrogen](#case-73) | エージェントとコーディングのワークフロー | 高速な実装モデルが行き詰まったときに、計画モデルで再検討する。 | Integration |
| [Workspace のデータからグラフと報告書を作成](#case-74) | スプレッドシートと検索 | 追加のやり取りで、足りない分析、グラフ、報告書を補えるか確認する。 | Demo |
| [背番号を読めずに推論予算を使い切る](#case-75) | 比較と限界 | 画像の細部を読む処理に上限と代替手段を設ける。 | Limit |
| [モデル系列ごとの ClutterBench の成績](#case-76) | 比較と限界 | 散らかった場面に特化したベンチマークで、得意分野がその課題にも当てはまるか確かめる。 | Benchmark |
| [ニュース要約からナレーション付き動画へ](#case-77) | アプリと学習 | 取材した情報を短い動画にまとめ、事実関係を確認する。 | Demo |
| [Minecraft 風の人体断面像](#case-78) | 比較と限界 | 指定した内部構造が生成された断面に含まれるか見る。 | Evaluation |
| [3モデルで同じ小道具を描画](#case-79) | 比較と限界 | 価格が低いモデルがどれだけトークンを使うか、品質とは別に記録する。 | Evaluation |
| [帰納推論ベンチマークとトークン消費](#case-80) | 比較と限界 | 難しい推論タスクでは、スコアと入力・出力の請求量を併せて記録する。 | Benchmark |
| [Gemini の各モードで表にドット絵を描く](#case-81) | スプレッドシートと検索 | 同じスプレッドシート描画課題で、いくつかのモデル選択肢を比較する。 | Evaluation |
| [参考画像からアパートを3Dプリント](#case-82) | インタラクティブ3DとUI | 画像から3Dを生成するテストを実物の出力まで進める。 | Demo |
| [3モデルで3Dの動物を動かす](#case-83) | 比較と限界 | 同じ3D動物課題で体の構造と動きを見る。 | Evaluation |
| [ts-bench で Hydrogen と Qwen を比較](#case-84) | 比較と限界 | 総合結果と一緒にツール呼び出しの失敗を確認する。 | Benchmark |
| [Vending-Bench の事業シミュレーション](#case-85) | 比較と限界 | シミュレーションで得た売上とエージェント運用費を合わせて見る。 | Benchmark |
| [ゴーイングメリー号の海上シーン](#case-86) | インタラクティブ3DとUI | よく知られた架空の船を題材に、海上シーンの構図を確かめる。 | Demo |
| [OpenClaw で Hydrogen を使う](#case-87) | エージェントとコーディングのワークフロー | 利用するエージェント基盤でモデルが選べるか確かめる。 | Integration |
| [雲海を泳ぐクジラ](#case-88) | インタラクティブ3DとUI | コードで作った生物シーンで流体の動きと目の造形を分けて確認する。 | Demo |
| [4モデルでミニチュアの島を作る](#case-89) | 比較と限界 | 島のデザインを比べるときに、その環境での時間と費用を記録する。 | Evaluation |
| [ウェブカメラで空中に絵を描く](#case-90) | アプリと学習 | 空中で線を描き、カメラ入力で画面が動きを追う様子を確認する。 | Demo |
| [布が裂ける動きをコードで比較](#case-91) | 比較と限界 | 同じアニメーション課題で生地の伸び、裂け方、毛との相互作用を見る。 | Evaluation |
| [Gemini Canvas の海底都市](#case-92) | インタラクティブ3DとUI | 小さな3Dシーンから始め、何回かのやり取りで探索エリアと動く生き物を加える。 | Demo |
| [一度の生成で作るウェブポータル](#case-93) | アプリと学習 | 個々の操作を試す前に、最初の画面構成を確認する。 | Demo |
| [出典をたどれない事実確認](#case-94) | 比較と限界 | スクリーンショットの真偽を判断するときは、検証可能な引用元を求める。 | Limit |
| [『Cities: Skylines』風の都市建設ツール](#case-95) | アプリと学習 | 都市建設の試作品を作り、操作とシミュレーションのつながりを調べる。 | Demo |
| [Hydrogen と Sol が描く2Dペリカン](#case-96) | 比較と限界 | 同じ短い2Dアニメーションで所要時間と動きを比較する。 | Evaluation |
| [Blender MCP で王座の間を作る](#case-97) | エージェントとコーディングのワークフロー | Blender MCP を使い、エディターで生成シーンの構図を確かめる。 | Integration |
| [4モデルのウェブスイングゲーム](#case-98) | 比較と限界 | 単一ファイルの条件をそろえて、移動と操作を比較する。 | Evaluation |
| [Three.js のグレースケール海賊船](#case-99) | インタラクティブ3DとUI | 色をグレーに限定し、光だけで形状が伝わるか確かめる。 | Demo |
| [4モデルの建築ジオラマ](#case-100) | 比較と限界 | 同じ建築の指示で生成し、モデルごとの照明表現を見比べる。 | Evaluation |
| [CadXStudio のパラメトリックな卓上照明](#case-101) | インタラクティブ3DとUI | 生成した CAD で部品の寸法と編集のしやすさを確認する。 | Integration |
| [C++ で作る神社の参道アニメーション](#case-102) | インタラクティブ3DとUI | 小さなネイティブコードの場面で、ウェブ基盤を使わずに動くアニメーションを書けるか試す。 | Demo |
| [3モデルで列車を描画](#case-103) | 比較と限界 | 同じ列車の題材で、各設定の完成時間を確認する。 | Evaluation |
| [Extra で作る雨のチャイナタウン](#case-104) | 比較と限界 | 大きなアニメーションの推論レベルを選ぶ前に、時間を測り、完成画を確認する。 | Evaluation |
| [30モジュールから作る町並み](#case-105) | インタラクティブ3DとUI | モジュールごとの指示で場面を組み立て、完成した全景を確認する。 | Demo |
| [3モデルで惑星の可視化を制作](#case-106) | 比較と限界 | 科学の可視化画面で同じプロンプトを使い、出力を比較する。 | Evaluation |
| [4モデルで Chrome の恐竜ゲームを再現](#case-107) | 比較と限界 | おなじみのゲームを再現するときに、所要時間とプレイ結果を比べる。 | Evaluation |
| [浮遊島の郵便局](#case-108) | インタラクティブ3DとUI | ミニチュアの建物を指定し、素材と光が場面をどう見せるか確認する。 | Demo |
| [2つのコーディングエージェントで船を作る](#case-109) | 比較と限界 | 使う実行環境で、最初に使える出力と修正の負担を確認する。 | Evaluation |
| [錦鯉の庭園で水と魚を描く](#case-110) | インタラクティブ3DとUI | 魚が動くシーンで、水面の反射と照明が破綻しないか確認する。 | Demo |
| [4モデルで剛体の投石機を作る](#case-111) | 比較と限界 | 同じ課題で遊べる物理プロトタイプを比べ、推論設定を記録する。 | Evaluation |
| [Gemini アプリで動く3Dシーン](#case-112) | インタラクティブ3DとUI | ウェブ版 Gemini で操作できる照明と粒子効果を試作する。 | Demo |
| [ブラウザー CAD のコンクリートミキサー](#case-113) | エージェントとコーディングのワークフロー | 生成したアセンブリを CAD 作業で使う前に部品ツリーと嵌合を確認する。 | Integration |
| [Blender で斧をプロシージャルに作る](#case-114) | エージェントとコーディングのワークフロー | 参考シルエットと複数回のビューポート確認で生成物を評価する。 | Integration |
| [一つの HTML に収めたピンクの3Dシーン](#case-115) | インタラクティブ3DとUI | 外部素材なしの Three.js で、見やすい構図になるか試す。 | Demo |
| [FrontierMemory で長期の記憶を評価](#case-116) | 比較と限界 | 長く動くエージェントの記憶モデルを選ぶとき、得点と実行ごとの費用を比べる。 | Benchmark |
| [故障させた LiveKit 音声エージェント](#case-117) | 比較と限界 | 意図的にツールを失敗させ、裏付けなしの結果を報告するか確認する。 | Evaluation |
| [28モジュールの Ember Isle](#case-118) | エージェントとコーディングのワークフロー | 大きなシーンをモジュールに分けて、毎回の生成時間を記録する。 | Demo |
| [コードだけのビッグバン・シミュレーション](#case-119) | インタラクティブ3DとUI | 短い動画で説明の試作品を作り、科学的な表現を確かめる。 | Demo |
| [分解表示ができるヘリコプター](#case-120) | インタラクティブ3DとUI | 飛行操作と部品を調べるビューが3D試作で両立するか試す。 | Demo |
| [X線とワイヤーフレーム付き Hydrogen Express](#case-121) | インタラクティブ3DとUI | 操作可能な3D試作に複数の確認モードを組み込む。 | Demo |
| [空に浮かぶ給油所](#case-122) | インタラクティブ3DとUI | 複数の動く物体と照明状態を使い、デモでシーンの変化が見えるようにする。 | Demo |
| [Gemini の3モデルが自転車をアニメ化](#case-123) | 比較と限界 | 同じ指示の短いアニメーションを比較し、それぞれの実行時間を記録する。 | Evaluation |
| [化学の教科書を対話型教材にする](#case-124) | アプリと学習 | ヒント、音声案内、任意表示のテキストで自習教材を組み立てる。 | Demo |
| [Vocaloid 楽曲の試作](#case-125) | アプリと学習 | 一度に生成した曲がキャラクターや曲調の指定を満たすか聴く。 | Demo |
| [2モデルで LEGO の世界を作る](#case-126) | 比較と限界 | 完成時間と、時間内に作り込めた範囲を合わせて比較する。 | Evaluation |
| [2リポジトリに埋め戻したバグを修正](#case-127) | 比較と限界 | 既知の欠陥を仕込み、エージェントが発見・修正できた数を測る。 | Benchmark |
| [2モデルの棒人間対カーソル](#case-128) | 比較と限界 | 両方のアニメーションがポインターの動きにどう反応するか確認する。 | Evaluation |
| [一つの HTML に収めた水車小屋](#case-129) | インタラクティブ3DとUI | 動きが見分けやすい小さな風景で3Dの短時間試作を確認する。 | Demo |
| [2モデルで山岳風景を描く](#case-130) | 比較と限界 | 風景アニメーションの構図、生成時間、費用を分けて比較する。 | Evaluation |
| [独自の評価環境で英語からペルシャ語に翻訳](#case-131) | 比較と限界 | 難しい段落の翻訳を人間の参照訳と突き合わせて採点する。 | Evaluation |
| [Hydrogen Extra で作る Blender シーン](#case-132) | インタラクティブ3DとUI | 作り込みを増やす前に Blender で形状と素材を確かめる。 | Demo |
| [4モデルで沈没船を作る](#case-133) | 比較と限界 | 同じシーンで見た目、時間、費用を個別に記録する。 | Evaluation |
| [複雑な積分を画像から読む](#case-134) | アプリと学習 | 長い式の簡約に進む前に、積分の上下限が等しいことに気づくか確認する。 | Evaluation |
| [4モデルのコピーライティングをブラインド比較](#case-135) | 比較と限界 | モデル名を隠し、利用する文章を選ぶ。 | Evaluation |
| [推論レベル別の物体検出と読み取り](#case-136) | 比較と限界 | 推論レベルごとに検出精度、文字認識、料金、待ち時間を測る。 | Benchmark |
| [4モデルで『カールじいさんの空飛ぶ家』を再現](#case-137) | 比較と限界 | 同じ参考画像と指示で3D作品を作り、違いを調べる。 | Evaluation |
| [WebGL2 で作る人体の細胞図鑑](#case-138) | アプリと学習 | 操作できる断面図で細胞内部の位置関係を説明する。 | Demo |
| [Hydrogen で作る2種類の粒子アニメーション](#case-139) | インタラクティブ3DとUI | 異なるパーティクルの場面で、簡単な効果の形と動きを見る。 | Demo |
| [Parking Bench の画像だけで動く対戦相手](#case-140) | アプリと学習 | 盤面画像だけを入力として、パズルの対戦相手を試す。 | Integration |
| [Google ドキュメントの操作解説動画](#case-141) | アプリと学習 | スクリーンショットと番号付き注釈で、モバイルの編集操作を教える。 | Demo |
| [ミニチュア世界の昼夜スイッチ](#case-142) | インタラクティブ3DとUI | 小さなスイッチを使い、画面の状態が変わるときの動きのつながりを調べる。 | Demo |
| [65モジュールで環境を作る](#case-143) | インタラクティブ3DとUI | 生成シーンを拡張するとき、制作時間と統合作業を記録する。 | Demo |
| [固定カメラのダンス動画](#case-144) | 比較と限界 | 参照画像を使ったアニメーションで、キャラクター、構図、カメラ位置が保たれるか確認する。 | Evaluation |
| [基準テストで止まるコーディングエージェント](#case-145) | 比較と限界 | 基準テストには時間制限を設け、修正を待つ前に進捗を確認する。 | Limit |
| [MZ-1500 用の BASIC 環境](#case-146) | アプリと学習 | レトロな BASIC 環境を試作し、周辺機器への対応を個別に確認する。 | Demo |
| [2モデルで対話型ロボットアームを作る](#case-147) | 比較と限界 | Three.js のアームを操作し、関節が自然に連動するか確認する。 | Evaluation |
| [操作できる FAA 地上待機マップ](#case-148) | スプレッドシートと検索 | 運航停止が終わった後も待ち行列が残る理由を、地図とタイムラインで示す。 | Demo |
| [ミニチュアの塔と庭園](#case-149) | インタラクティブ3DとUI | 生成したミニチュアで建築と周辺の植栽のバランスを見る。 | Demo |
| [計画・実行・レビューにモデルを分ける](#case-150) | エージェントとコーディングのワークフロー | 計画、実行、レビューに別の役割を割り当て、モデルごとのタスク数を比較する。 | Demo |
| [Hydrogen と Sol が雪の村を作る](#case-151) | 比較と限界 | コーディングの比較では、所要時間、費用、見た目を個別に評価する。 | Evaluation |
| [High と Ultra で作る Three.js の島](#case-152) | 比較と限界 | 見た目と所要時間を比較するときは推論レベルを記録し、製品間の利用枠は区別する。 | Evaluation |
| [第二次大戦の飛行場をジオラマにする](#case-153) | インタラクティブ3DとUI | 資料に加えて機械の動作を指定し、見た目と動きの両方を確かめる。 | Demo |
| [コーディング用クライアントに Hydrogen を設定](#case-154) | エージェントとコーディングのワークフロー | Google の API キーを設定するとき、正確なモデル ID を選ぶ。 | Tutorial |
| [SuperARIS の研究チームに Hydrogen を組み込む](#case-155) | エージェントとコーディングのワークフロー | 複数モデルのチームで、Hydrogen に研究や原稿の担当を割り当てる。 | Integration |
| [4モデルでコアモジュールをクリーンルーム再実装](#case-156) | エージェントとコーディングのワークフロー | 書き直しを任せるとき、コードの理解、設計、実装を個別に比較する。 | Evaluation |
| [3Dの PS5 コントローラーの細部を比較](#case-157) | 比較と限界 | ボタンの影と背面部品を確認してモデリングを評価する。 | Evaluation |
| [Muse から Antigravity CLI に仕事を渡す](#case-158) | エージェントとコーディングのワークフロー | 遠隔のアシスタントを自宅の実行環境につなぎ、文章作成に使うモデルを選ぶ。 | Integration |
| [CursorBench の推論予算比較](#case-159) | 比較と限界 | 高速な設定をデフォルトにする前に、推論予算ごとの成功率を比較する。 | Benchmark |
| [3モデルで星をモチーフにした聖堂を描く](#case-160) | 比較と限界 | 3Dで映像の細かさと描画の安定性を別々に見る。 | Evaluation |
| [1分以内で HTML のシューティングを試作](#case-161) | アプリと学習 | 単一 HTML で操作と反応の基本ループを確かめる。 | Demo |
| [既存の移行設計を見直す](#case-162) | 比較と限界 | 移行にあたって現在の設計を置き換えるべきか、エージェントに検討させる。 | Limit |
| [AITuber OnAir で Hydrogen と会話](#case-163) | アプリと学習 | Live2D アバターの会話モデルとして Hydrogen を試す。 | Integration |
| [コードで作ったプロモーション動画](#case-164) | アプリと学習 | 短い宣伝内容をコーディングモデルに渡し、動きの表現を確認する。 | Demo |
| [2モデルが作る神殿脱出ゲーム](#case-165) | 比較と限界 | 同じゲームの照明と雰囲気が、遊ぶときの見やすさを支えるか比較する。 | Evaluation |
| [Gemini の3モデルでラリーバギーを動かす](#case-166) | 比較と限界 | 傾斜したコーナーでサスペンションとタイヤの接地が自然か確かめる。 | Evaluation |
| [プロシージャルに描いたコマドリの飛行](#case-167) | インタラクティブ3DとUI | 生成された飛行で翼と胴体の動きを確認する。 | Demo |
| [Antigravity の Orchestrator と Swarm を選ぶ](#case-168) | エージェントとコーディングのワークフロー | 依存がある作業はモデル間で順番に渡し、分けられる作業は独立した実装と検証に割り振る。 | Tutorial |
| [2モデルで Chasing Views をアニメ化](#case-169) | 比較と限界 | 各モデルの推論レベルを記録し、出力と実行時間を比べる。 | Evaluation |
| [Design Creativity Bench の速度と費用](#case-170) | 比較と限界 | 創造性スコアと併せて、デザイン1件あたりの時間と費用を比較する。 | Benchmark |
| [参考画像から SolidWorks の部品を作る](#case-171) | エージェントとコーディングのワークフロー | 3D参考画像でエージェントを使った SolidWorks の作業を評価する。 | Integration |
| [4モデルで砂漠を疾走する馬を描く](#case-172) | 比較と限界 | 光やメッシュを見る前に足の接地と重心移動を比べる。 | Evaluation |
| [ユングの共時性を説明するスライド](#case-173) | アプリと学習 | 関連概念の区別が必要な題材でスライド作成工程を試す。 | Demo |
| [FrontierCS 2 で計算機科学の研究課題を解く](#case-174) | 比較と限界 | 通常のコーディングと併せて研究ベンチマークを実行し、環境を記録する。 | Benchmark |
| [4モデルの『Rio Above the Clouds』](#case-175) | 比較と限界 | 同じ制作指示で、費用、実行時間、主観的な品質を比較する。 | Evaluation |
| [GBENCH の技術問題に取り組む Hydrogen](#case-176) | 比較と限界 | 価格や時間に加え、検証可能なコーディングと非コーディングの成果で判断する。 | Benchmark |
| [車に縦列駐車を学ばせる](#case-177) | 比較と限界 | 生成したシミュレーションの学習経過と最終成功率を比較する。 | Evaluation |
| [操作できるミトコンドリアの分子モーター](#case-178) | アプリと学習 | 操作可能な図で、分子の動きと ATP 生成を結びつける。 | Demo |
| [Qix 風の陣取りゲーム](#case-179) | アプリと学習 | 短いアーケードゲームの指示で、最初の生成が操作と反応の流れを実装するか確認する。 | Demo |
| [Hydrogen で HTML スライドを生成](#case-180) | アプリと学習 | HTML の生成時間と併せ、スライドの情報の階層とレイアウトを確認する。 | Demo |
| [Terminal-Bench 4.0 の Hydrogen](#case-181) | 比較と限界 | コマンドライン向けのモデルを選ぶときは、成功率とタスク費用を合わせて見る。 | Benchmark |
| [単一の HTML だけで描くイラスト](#case-182) | インタラクティブ3DとUI | 参考イメージを外部素材なしのコードで再現できるか試す。 | Demo |
| [Gemini の3モデルでタコを動かす](#case-183) | 比較と限界 | 岩をつかんだときにその動きが体を前に進めるか確認する。 | Evaluation |
| [Chrome で構造化した YouTube 要約を作る](#case-184) | スプレッドシートと検索 | Chrome の Gemini パネルに、タイムスタンプ付き要約と出典付きの背景説明を求める。 | Tutorial |
| [授業を短い解説動画にする](#case-185) | アプリと学習 | 授業を動画にするとき、説明の正確さとテンポを確認する。 | Demo |
| [静止画からパフィンを動かす](#case-186) | インタラクティブ3DとUI | 既存 HTML の場面を、プログラムで動かすアニメーションの最初のフレームに使う。 | Demo |
| [城のモデリングテスト](#case-187) | 比較と限界 | モデルごとの城と、作業に使った資源を比べる。 | Evaluation |
| [Antigravity Swarm でのブラウザー操作](#case-188) | エージェントとコーディングのワークフロー | スウォームを評価するときに、エージェントの作業とブラウザーの動きを合わせて確認する。 | Demo |
| [Google ドライブ経由で Muse に引き継ぐ](#case-189) | エージェントとコーディングのワークフロー | 調査の次工程を別のエージェントが担当するときは、監視するドライブフォルダーで渡す。 | Integration |
| [Gemini Canvas のリコーダー練習ガイド](#case-190) | アプリと学習 | 高速モードで楽譜と演奏案内を組み合わせる。 | Demo |
| [スコープ追加で大きく変わる工期見積もり](#case-191) | 比較と限界 | 納期が大きく変わったときは、範囲と前提条件を説明させる。 | Limit |
| [Antigravity Swarm でペリカンを動かす](#case-192) | エージェントとコーディングのワークフロー | アニメーションと音をコーディングエージェントに分け、完成したシーンを確認する。 | Demo |
| [うるう年を含めて暦を換算](#case-193) | 比較と限界 | 簡単な換算問題でも、暦の例外を考慮するかを確認する。 | Evaluation |
| [単一の HTML に収めた TAJ VICE](#case-194) | アプリと学習 | 単一ファイルで探索マップを試作し、残る不具合をテストする。 | Demo |
| [Google Cloud プロジェクトから Antigravity を使う](#case-195) | エージェントとコーディングのワークフロー | 管理された認証情報で Hydrogen を有効にするときに、認証と請求先を確認する。 | Tutorial |
| [回答に古い契約条件が混じる](#case-196) | 比較と限界 | 調査アシスタントを評価するときは、契約条件やモデル名を一次情報で確認する。 | Limit |
| [WebGL アニメーションの物語を修正](#case-197) | 比較と限界 | 技巧的な初稿の流れが分かりにくい場合は、筋立てに焦点を当てて修正を頼む。 | Limit |
| [Carbon が計画し Hydrogen がモバイル実装](#case-198) | エージェントとコーディングのワークフロー | インタラクション設計を計画モデルに任せ、実行モデルに実装を渡す。 | Demo |
| [2モデルが山寺の上でドラゴンを戦わせる](#case-199) | 比較と限界 | 同じシーンで絡み合う二者のアニメーションを比べる。 | Evaluation |
| [一つのプロンプトで3Dのミニチュア島](#case-200) | インタラクティブ3DとUI | 一度の生成で目印、地形、水が分かりやすく並ぶか調べる。 | Demo |
| [再現に使える Three.js ペリカンのプロンプト](#case-201) | 比較と限界 | 自転車の脚、車輪、ハンドルの動きが連動するか見る。 | Evaluation |
| [T3 Code で Hydrogen を使う](#case-202) | エージェントとコーディングのワークフロー | コーディング用クライアントに接続し、通常の作業で時間枠と週間枠を測る。 | Integration |
| [手描き風の公共広告動画](#case-203) | アプリと学習 | 短い公共広告を題材に、手描きの表現が伝わるかを見る。 | Demo |
| [10種類の画風を走る自転車のクジャク](#case-204) | エージェントとコーディングのワークフロー | 複数モデルのスウォームに、画風の変化と音の同期をコードで作らせる。 | Demo |
| [同じ小屋を3つの環境で作る](#case-205) | 比較と限界 | 設定や実行先を変えて画像タスクを試し、出力形式を確認する。 | Evaluation |
| [同じ指示でダッシュボードを比較](#case-206) | 比較と限界 | 共通のフロントエンドの指示で、レイアウトと情報の優先順位を見比べる。 | Evaluation |
| [画像から React.gg のウェブサイトを再現](#case-207) | アプリと学習 | 参考画像で作り始め、どの細部に修正が必要か確かめる。 | Demo |
| [特異点を題材にした操作パネル](#case-208) | インタラクティブ3DとUI | 単一の視覚コンセプトで、短い対話型のシーケンスを試作する。 | Demo |
| [2モデルがコードで横スクロールを作る](#case-209) | 比較と限界 | 生成されたアクションシーンでは、動きのつながりと制作費を見る。 | Evaluation |
| [Gemini をランニングコーチに使う](#case-210) | アプリと学習 | 練習記録と助言を突き合わせ、自分の基準に合わせて目標を調整する。 | Demo |
| [スコアをオンチェーンに記録するゲーム](#case-211) | アプリと学習 | デスクトップブラウザーで遊び、ゲーム本体と分けてスコアの記録方法を確認する。 | Demo |
| [日本語の回答で数式がレンダリングされない](#case-212) | 比較と限界 | TeX を含む回答では、内容の正しさと表示の両方を確認する。 | Limit |
| [プロンプトから MIDI を書く作曲アプリ](#case-213) | アプリと学習 | 日本語の指示を MIDI、WAV、ピアノロールに変換する試作を作る。 | Demo |
| [回答しないという指示をテスト](#case-214) | 比較と限界 | 無応答が必要な作業で、モデルが実際に返信を出さないか試す。 | Evaluation |
| [コンサートの振り返りを1ページに](#case-215) | アプリと学習 | イベント情報を一目で追える視覚資料にまとめる。 | Demo |
| [3モデルが電動機の仕組みを説明](#case-216) | 比較と限界 | 同じシミュレーションで見やすさと学習者向けの操作を比較する。 | Evaluation |
| [2つのモデルの作業で机のシーンを動かす](#case-217) | 比較と限界 | 元の指示に照らして、細部、音量、最後の静止を確認する。 | Evaluation |
| [アバター画像から日常の短い動画へ](#case-218) | アプリと学習 | 参照画像1枚と日常の4シーンで、短い絵コンテへの展開を評価する。 | Demo |
| [Hydrogen が ComfyUI 用のキャラクター動画を計画](#case-219) | アプリと学習 | 衣装と背景を固定し、表情と動きに変化を付ける。 | Integration |
| [Almance Vale を100モジュールに拡張](#case-220) | エージェントとコーディングのワークフロー | 既存のアプリをコーディングエージェントに渡し、画風を保ったままモジュールを増やす。 | Demo |
| [プログラムで音が変わる2Dの村](#case-221) | 比較と限界 | 制作時間を測り、画面上の出来事に合わせて音が変化するかを見る。 | Evaluation |
| [曲をワイド画面の映像にする](#case-222) | アプリと学習 | 曲と画角の指定から、動きで曲の勢いを表現できるか試す。 | Demo |
| [7つの Hydrogen サブエージェントでナイアガラの滝を作る](#case-223) | エージェントとコーディングのワークフロー | シーンを分割し、調整役が実装を各エージェントに配る。 | Demo |
| [時代物の恋愛動画2本で連続性を保つ](#case-224) | アプリと学習 | 次の動画で場面を続けるときに、引き継ぐ細部を具体的に指定する。 | Demo |
| [Gemini アプリの水の球体](#case-225) | インタラクティブ3DとUI | 簡単な光学シーンで反射光と屈折の関係を確かめる。 | Demo |

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

<a id="case-59"></a>
### 事例 59: [n8n で Hydrogen にツールを使わせる](https://x.com/n8n_io/status/2120947273534197886) (作者 [@n8n_io](https://x.com/n8n_io))

**ツールを繰り返し使う処理を Hydrogen に、計画を別ステップに割り当てる。**

n8n は Hydrogen 対応を紹介し、Carbon または Argon で計画して Hydrogen で実行する運用を提案する。出典に設定方法へのリンクがある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-12

---

<a id="case-69"></a>
### 事例 69: [マルチエージェント環境の認証経路](https://x.com/studio_yebisu/status/2120969033260646551) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**他社のサービスへタスクを任せるとき、どのクライアントが認証を行うか確かめる。**

投稿者は Claude に Antigravity CLI 経由で Hydrogen を使うよう頼み、Claude Code が直接認証を試して Antigravity の利用が停止されたと報告する。停止通知の画像があり、原因は投稿者の見立て。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-12

---

<a id="case-70"></a>
### 事例 70: [Antigravity の Goal Mode を実行](https://x.com/Inmerson/status/2120973427788124345) (作者 [@Inmerson](https://x.com/Inmerson))

**長時間の実装で計画、コード変更、テスト結果を記録する。**

投稿者は Hydrogen Extra の Goal Mode で計画、実装、テストを含む105分のセッションを報告した。テスト結果は本人の報告。

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

種類: Demo | 日付: 2026-11-12

---

<a id="case-73"></a>
### 事例 73: [Antigravity Orchestrator の Carbon と Hydrogen](https://x.com/Google/status/2120982566891356279) (作者 [@Google](https://x.com/Google))

**高速な実装モデルが行き詰まったときに、計画モデルで再検討する。**

Google は Carbon に計画と問題解決、Hydrogen に編集とテストを分担させた。Terminal-Bench 4.0 は Carbon に近い成功率で、利用枠の消費と時間が減ったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

種類: Integration | 日付: 2026-11-12

---

<a id="case-87"></a>
### 事例 87: [OpenClaw で Hydrogen を使う](https://x.com/openclaw/status/2121098531205501401) (作者 [@openclaw](https://x.com/openclaw))

**利用するエージェント基盤でモデルが選べるか確かめる。**

OpenClaw は Hydrogen に対応したとスクリーンショット付きで発表した。投稿にはベンチマークや完全な設定ログはない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-13

---

<a id="case-97"></a>
### 事例 97: [Blender MCP で王座の間を作る](https://x.com/ashen_one/status/2121165467821936651) (作者 [@ashen_one](https://x.com/ashen_one))

**Blender MCP を使い、エディターで生成シーンの構図を確かめる。**

制作者は Hydrogen と Blender MCP で『ゲーム・オブ・スローンズ』の鉄の玉座の間を再現したとし、録画を公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

種類: Integration | 日付: 2026-11-13

---

<a id="case-113"></a>
### 事例 113: [ブラウザー CAD のコンクリートミキサー](https://x.com/johnsanthosh01/status/2121243197901041869) (作者 [@johnsanthosh01](https://x.com/johnsanthosh01))

**生成したアセンブリを CAD 作業で使う前に部品ツリーと嵌合を確認する。**

制作者によると、Hydrogen は CadX Studio で一つのプロンプトから265部品のミキサーを40分かけて生成した。部品ごとの手作業は行っていないという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

種類: Integration | 日付: 2026-11-13

---

<a id="case-114"></a>
### 事例 114: [Blender で斧をプロシージャルに作る](https://x.com/camperaigg/status/2121252572115951897) (作者 [@camperaigg](https://x.com/camperaigg))

**参考シルエットと複数回のビューポート確認で生成物を評価する。**

制作者は Antigravity CLI の Hydrogen、Python モジュール、ビューポート確認を使って斧を作ったと報告した。録画込みで51分、API 費用は5.01ドルだったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-13

---

<a id="case-118"></a>
### 事例 118: [28モジュールの Ember Isle](https://x.com/IamEmily2050/status/2121258646759952644) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**大きなシーンをモジュールに分けて、毎回の生成時間を記録する。**

制作者は Gemini アプリの Hydrogen High を使用したという。28モジュールに各1プロンプトを使い、1回の生成は82〜290秒だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-150"></a>
### 事例 150: [計画・実行・レビューにモデルを分ける](https://x.com/naufaldi/status/2121499487999013081) (作者 [@naufaldi](https://x.com/naufaldi))

**計画、実行、レビューに別の役割を割り当て、モデルごとのタスク数を比較する。**

投稿者は Opus 5.5 で計画し、Hydrogen で実行して Sol を予備にし、Sol 6.1 でレビューしたと説明する。Antigravity の個人利用量と、別の公開評価を併記している。

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

種類: Demo | 日付: 2026-11-14

---

<a id="case-154"></a>
### 事例 154: [コーディング用クライアントに Hydrogen を設定](https://x.com/k2sbhai/status/2121509825658147041) (作者 [@k2sbhai](https://x.com/k2sbhai))

**Google の API キーを設定するとき、正確なモデル ID を選ぶ。**

投稿者は Google AI Studio でキーを取得し、OpenCode または Cline で gemini-4-hydrogen を選ぶ手順を紹介した。利用資格とレート制限は提供元に依存する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

種類: Tutorial | 日付: 2026-11-14

---

<a id="case-155"></a>
### 事例 155: [SuperARIS の研究チームに Hydrogen を組み込む](https://x.com/NFT_Chen/status/2121520579304206443) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**複数モデルのチームで、Hydrogen に研究や原稿の担当を割り当てる。**

投稿では SuperARIS の導入とチーム選択を紹介する。調査の議論や執筆に Hydrogen または Carbon を割り当て、調整と実装を分ける案で、研究品質の測定は行っていない。

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

種類: Integration | 日付: 2026-11-14

---

<a id="case-156"></a>
### 事例 156: [4モデルでコアモジュールをクリーンルーム再実装](https://x.com/oasisfeng/status/2121523934831276203) (作者 [@oasisfeng](https://x.com/oasisfeng))

**書き直しを任せるとき、コードの理解、設計、実装を個別に比較する。**

制作者は同じソフトウェアの再実装で Hydrogen、Argon、GPT-6 Astra、Claude Opus 5.5 を比較した。Hydrogen は実行力が強く、他の結果には設計上の強みがあったという。

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

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-158"></a>
### 事例 158: [Muse から Antigravity CLI に仕事を渡す](https://x.com/tetumemo/status/2121528823061852166) (作者 [@tetumemo](https://x.com/tetumemo))

**遠隔のアシスタントを自宅の実行環境につなぎ、文章作成に使うモデルを選ぶ。**

投稿者は Muse が自宅 PC の Antigravity CLI に処理を送り、成果を受け取る構成を説明する。通常は Hydrogen を使い、Argon も選択できる。例には日本語執筆や図解の作成がある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-14

---

<a id="case-168"></a>
### 事例 168: [Antigravity の Orchestrator と Swarm を選ぶ](https://x.com/ohayou792/status/2121624258984153452) (作者 [@ohayou792](https://x.com/ohayou792))

**依存がある作業はモデル間で順番に渡し、分けられる作業は独立した実装と検証に割り振る。**

投稿者は上位モデルの計画後に Hydrogen が実装する Orchestrator を図示し、別の /swarm の調整方法と比較する。依存関係に基づく使い分けを提案した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

種類: Tutorial | 日付: 2026-11-14

---

<a id="case-171"></a>
### 事例 171: [参考画像から SolidWorks の部品を作る](https://x.com/GoGoFly23/status/2121636952479080713) (作者 [@GoGoFly23](https://x.com/GoGoFly23))

**3D参考画像でエージェントを使った SolidWorks の作業を評価する。**

制作者は Antigravity の Hydrogen に画像を1枚渡して SolidWorks 部品を作ったと報告した。追加投稿によると SolidWorks MCP を使用。公差や実務での適合性は未検証。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-14

---

<a id="case-188"></a>
### 事例 188: [Antigravity Swarm でのブラウザー操作](https://x.com/Saboo_Shubham_/status/2121852445756477924) (作者 [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**スウォームを評価するときに、エージェントの作業とブラウザーの動きを合わせて確認する。**

Google のスタッフは Hydrogen と Antigravity swarm でブラウザーを使うスクリーンショットを投稿した。完全なタスクログは掲載されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-15

---

<a id="case-189"></a>
### 事例 189: [Google ドライブ経由で Muse に引き継ぐ](https://x.com/nasuvit_z/status/2121857992702525734) (作者 [@nasuvit_z](https://x.com/nasuvit_z))

**調査の次工程を別のエージェントが担当するときは、監視するドライブフォルダーで渡す。**

投稿者は Hydrogen で情報を集めてドライブ上のファイルに整理し、それを Muse が検知して次の作業を引き継ぐ構成を説明した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-15

---

<a id="case-192"></a>
### 事例 192: [Antigravity Swarm でペリカンを動かす](https://x.com/chetaslua/status/2121885449509851415) (作者 [@chetaslua](https://x.com/chetaslua))

**アニメーションと音をコーディングエージェントに分け、完成したシーンを確認する。**

制作者は Carbon と Hydrogen で、画風が移り変わるペリカンを JavaScript で作ったと説明する。音楽と効果音もコードで生成したという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-195"></a>
### 事例 195: [Google Cloud プロジェクトから Antigravity を使う](https://x.com/loganlu51268/status/2121911409042719023) (作者 [@loganlu51268](https://x.com/loganlu51268))

**管理された認証情報で Hydrogen を有効にするときに、認証と請求先を確認する。**

投稿者はアプリケーションのデフォルト認証情報を使い、個人契約から Google Cloud Agent Platform プロジェクトに切り替えた。選択画面に Hydrogen があり、SKU ごとの請求確認も説明する。

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

種類: Tutorial | 日付: 2026-11-15

---

<a id="case-198"></a>
### 事例 198: [Carbon が計画し Hydrogen がモバイル実装](https://x.com/thebuggeddev/status/2121945961555718334) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**インタラクション設計を計画モデルに任せ、実行モデルに実装を渡す。**

制作者はモバイルアプリの計画を Carbon、Reanimated の物理挙動を含む実装を Hydrogen に頼んだ。動きが滑らかだったと述べ、録画を公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-202"></a>
### 事例 202: [T3 Code で Hydrogen を使う](https://x.com/bei351009016/status/2121964293906206916) (作者 [@bei351009016](https://x.com/bei351009016))

**コーディング用クライアントに接続し、通常の作業で時間枠と週間枠を測る。**

投稿者は T3 Code を Gemini Pro に接続して Hydrogen を約半日使ったと述べる。スクリーンショットと本文で利用枠を示し、速度と精度の印象を別々に記した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

種類: Integration | 日付: 2026-11-15

---

<a id="case-204"></a>
### 事例 204: [10種類の画風を走る自転車のクジャク](https://x.com/SahilPanhotra/status/2121995488425849064) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**複数モデルのスウォームに、画風の変化と音の同期をコードで作らせる。**

制作者は Carbon と Hydrogen で10種類の画風を切り替えるクジャクの自転車動画を制作したと説明する。画面、音楽、効果音をコードで作ったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-220"></a>
### 事例 220: [Almance Vale を100モジュールに拡張](https://x.com/IamEmily2050/status/2122257581175410858) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**既存のアプリをコーディングエージェントに渡し、画風を保ったままモジュールを増やす。**

制作者は Gemini アプリから Antigravity へ移し、swarm モードの Hydrogen Extra で既存コードに従い、数時間で計100モジュールまで拡張したという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

種類: Demo | 日付: 2026-11-16

---

<a id="case-223"></a>
### 事例 223: [7つの Hydrogen サブエージェントでナイアガラの滝を作る](https://x.com/SahilPanhotra/status/2122311637684424737) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**シーンを分割し、調整役が実装を各エージェントに配る。**

投稿者は一つの指示から Carbon と7つの Hydrogen サブエージェントで1時間未満に滝の体験を作ったと述べる。録画には水、船、複数の視点と環境の変化が映る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

種類: Demo | 日付: 2026-11-16

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

<a id="case-58"></a>
### 事例 58: [15分で作る Minecraft 風プロトタイプ](https://x.com/RezAIT00/status/2120947124418293876) (作者 [@RezAIT00](https://x.com/RezAIT00))

**ボクセルの試作品で、採掘と所持品など複数の機能が連携するか確認する。**

制作者は Hydrogen Extra High で15分かけて作ったと報告する。設置、採掘、所持品を挙げているが、録画で確認できる機能は一部。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-77"></a>
### 事例 77: [ニュース要約からナレーション付き動画へ](https://x.com/gigabit_million/status/2121011957042163722) (作者 [@gigabit_million](https://x.com/gigabit_million))

**取材した情報を短い動画にまとめ、事実関係を確認する。**

録画では Gemini のモバイル版で Hydrogen がニュースを検索して構成案を作り、制作者が動画化を頼む。アプリ内で10秒の再生を確認できる。制作時間とナレーションは本人の報告で、描画基盤は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-90"></a>
### 事例 90: [ウェブカメラで空中に絵を描く](https://x.com/CodeByPoonam/status/2121121804483969102) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**空中で線を描き、カメラ入力で画面が動きを追う様子を確認する。**

制作者は早期アクセスの Hydrogen で空中描画ツールを作ったと報告し、録画を公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-93"></a>
### 事例 93: [一度の生成で作るウェブポータル](https://x.com/kimura_0314/status/2121130305532878979) (作者 [@kimura_0314](https://x.com/kimura_0314))

**個々の操作を試す前に、最初の画面構成を確認する。**

投稿者は Antigravity の Hydrogen で一度に作ったというポータルの画像を公開した。スクリーンショットで確認できるのは見た目。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-13

---

<a id="case-95"></a>
### 事例 95: [『Cities: Skylines』風の都市建設ツール](https://x.com/yohakujpn/status/2121146464466604147) (作者 [@yohakujpn](https://x.com/yohakujpn))

**都市建設の試作品を作り、操作とシミュレーションのつながりを調べる。**

制作者は動画の都市建設プロトタイプを Hydrogen で作ったと説明し、生成に30分かからなかったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-124"></a>
### 事例 124: [化学の教科書を対話型教材にする](https://x.com/smalkalbani/status/2121282231759155617) (作者 [@smalkalbani](https://x.com/smalkalbani))

**ヒント、音声案内、任意表示のテキストで自習教材を組み立てる。**

投稿者は音声案内とヒントのある中学3年向け化学教材を実演した。学習効果の測定は行われていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-125"></a>
### 事例 125: [Vocaloid 楽曲の試作](https://x.com/peach2k2/status/2121284159565902188) (作者 [@peach2k2](https://x.com/peach2k2))

**一度に生成した曲がキャラクターや曲調の指定を満たすか聴く。**

投稿者は楽曲クリップを共有し、作曲を Hydrogen によるものと説明する。音声を作るために使用したツールは不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-134"></a>
### 事例 134: [複雑な積分を画像から読む](https://x.com/HarshithLucky3/status/2121303778548908228) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**長い式の簡約に進む前に、積分の上下限が等しいことに気づくか確認する。**

制作者は Gemini アプリの Hydrogen High が複雑な積分の画像に回答する様子を録画した。外側の積分の上下限が同じだと見抜けるかが焦点。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-138"></a>
### 事例 138: [WebGL2 で作る人体の細胞図鑑](https://x.com/soumyadesign/status/2121354542344466565) (作者 [@soumyadesign](https://x.com/soumyadesign))

**操作できる断面図で細胞内部の位置関係を説明する。**

制作者は Antigravity の Hydrogen を使い、WebGL2 で外部ライブラリーなしの3D細胞図鑑を作ったと報告した。断面表示を見どころに挙げている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-140"></a>
### 事例 140: [Parking Bench の画像だけで動く対戦相手](https://x.com/agenticjay/status/2121391300822081713) (作者 [@agenticjay](https://x.com/agenticjay))

**盤面画像だけを入力として、パズルの対戦相手を試す。**

制作者によると Carbon がゲームを作り、プレイヤーは5レベルで API 経由の Hydrogen または Gemini Decision 1 と対戦する。両モデルが受け取る状態は盤面の PNG 画像のみ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

種類: Integration | 日付: 2026-11-13

---

<a id="case-141"></a>
### 事例 141: [Google ドキュメントの操作解説動画](https://x.com/nin222/status/2121395008863621390) (作者 [@nin222](https://x.com/nin222))

**スクリーンショットと番号付き注釈で、モバイルの編集操作を教える。**

制作者は Hydrogen で編集した Google ドキュメントの操作動画を公開した。抜粋した画面では、文字選択、スタイル、色、フォント、保存の手順と注釈を確認できる。編集方法の詳細は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-146"></a>
### 事例 146: [MZ-1500 用の BASIC 環境](https://x.com/hiromsa/status/2121465784715338065) (作者 [@hiromsa](https://x.com/hiromsa))

**レトロな BASIC 環境を試作し、周辺機器への対応を個別に確認する。**

投稿者は Hydrogen で約15分かけて制作したと説明した。PCG、PSG、QuickDisk に対応し、QuickDisk は LOAD のみと記載する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-14

---

<a id="case-161"></a>
### 事例 161: [1分以内で HTML のシューティングを試作](https://x.com/SahilPanhotra/status/2121561371951399133) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**単一 HTML で操作と反応の基本ループを確かめる。**

制作者は一つの指示で Hydrogen が1分未満で遊べるゲームを作ったと報告した。フレームワークや事前設定のない単一の HTML で構成した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-163"></a>
### 事例 163: [AITuber OnAir で Hydrogen と会話](https://x.com/shinshin86/status/2121571590442017094) (作者 [@shinshin86](https://x.com/shinshin86))

**Live2D アバターの会話モデルとして Hydrogen を試す。**

メンテナーは AITuber OnAir の Hydrogen 対応を告知した。Live2D などのサンプルアバターがあり、録画で連携を確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

種類: Integration | 日付: 2026-11-14

---

<a id="case-164"></a>
### 事例 164: [コードで作ったプロモーション動画](https://x.com/xiangning0/status/2121594643540480293) (作者 [@xiangning0](https://x.com/xiangning0))

**短い宣伝内容をコーディングモデルに渡し、動きの表現を確認する。**

投稿者は GPT-6.2 Astra を題材にした動画を公開し、Hydrogen がコードだけで制作したと説明する。動画にはその出力が映る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-173"></a>
### 事例 173: [ユングの共時性を説明するスライド](https://x.com/soumyadesign/status/2121676345835241916) (作者 [@soumyadesign](https://x.com/soumyadesign))

**関連概念の区別が必要な題材でスライド作成工程を試す。**

投稿者はカール・ユングの共時性と非因果的秩序のスライドを Hydrogen と自作ツールで作ったと説明する。ツールは Antigravity で開発し、出力の一部を公開した。

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

種類: Demo | 日付: 2026-11-14

---

<a id="case-178"></a>
### 事例 178: [操作できるミトコンドリアの分子モーター](https://x.com/SidraMiconi/status/2121745863827697687) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**操作可能な図で、分子の動きと ATP 生成を結びつける。**

投稿者によると Hydrogen High は一つの指示で ATP 合成酵素のアプリを作り、後でカメラを修正した。形状はクライオ電子顕微鏡の座標に基づき、動きは単純化している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-179"></a>
### 事例 179: [Qix 風の陣取りゲーム](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (作者 [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**短いアーケードゲームの指示で、最初の生成が操作と反応の流れを実装するか確認する。**

制作者は無料の Gemini で Qix 風の陣取りを一度の依頼で作ったとし、Hydrogen と明記したデモを共有した。

**プロンプト:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-180"></a>
### 事例 180: [Hydrogen で HTML スライドを生成](https://x.com/yamachan_ai_log/status/2121772023710118043) (作者 [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**HTML の生成時間と併せ、スライドの情報の階層とレイアウトを確認する。**

投稿者は Hydrogen で HTML スライドを作る様子を公開し、速く丁寧に仕上がったと評した。録画に成果物があり、比較時間は記載されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-185"></a>
### 事例 185: [授業を短い解説動画にする](https://x.com/smalkalbani/status/2121844887033458954) (作者 [@smalkalbani](https://x.com/smalkalbani))

**授業を動画にするとき、説明の正確さとテンポを確認する。**

制作者は授業を動画にする流れに Hydrogen を使い、2本を投稿した。どのシステムが映像を作ったかは不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-190"></a>
### 事例 190: [Gemini Canvas のリコーダー練習ガイド](https://x.com/nin222/status/2121877676042682538) (作者 [@nin222](https://x.com/nin222))

**高速モードで楽譜と演奏案内を組み合わせる。**

録画は Hydrogen の高速モードで作った Canvas のリコーダーガイドを示す。制作者は楽譜の読み込みからも作れたと述べる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-194"></a>
### 事例 194: [単一の HTML に収めた TAJ VICE](https://x.com/SahilPanhotra/status/2121909681514074328) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**単一ファイルで探索マップを試作し、残る不具合をテストする。**

制作者は Hydrogen と12時間未満のセッションで、架空のアグラを舞台に GTA 風ゲームを作ったと述べる。構成は純粋な JavaScript と単一 HTML、外部素材なし。遊び方には不具合が残る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-203"></a>
### 事例 203: [手描き風の公共広告動画](https://x.com/shengtang135754/status/2121965385356612020) (作者 [@shengtang135754](https://x.com/shengtang135754))

**短い公共広告を題材に、手描きの表現が伝わるかを見る。**

制作者は手描き風の公共広告を Gemini 4 Hydrogen で一度に作ったと報告した。映像の描画方式や制作工程は記載されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-207"></a>
### 事例 207: [画像から React.gg のウェブサイトを再現](https://x.com/thebuggeddev/status/2122019549117911473) (作者 [@thebuggeddev](https://x.com/thebuggeddev))

**参考画像で作り始め、どの細部に修正が必要か確かめる。**

制作者は Hydrogen に参照画像を渡し、少数の指示で React.gg を再現したと報告する。デモへのリンクがあり、一致しない部分もあるという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-210"></a>
### 事例 210: [Gemini をランニングコーチに使う](https://x.com/ivanleomk/status/2122036783307469199) (作者 [@ivanleomk](https://x.com/ivanleomk))

**練習記録と助言を突き合わせ、自分の基準に合わせて目標を調整する。**

制作者は Gemini Hydrogen の指導を受け、約1年で最長のランニングを終えたと報告した。練習のスクリーンショット付きの個人事例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-15

---

<a id="case-211"></a>
### 事例 211: [スコアをオンチェーンに記録するゲーム](https://x.com/itshoseyn/status/2122063851143246140) (作者 [@itshoseyn](https://x.com/itshoseyn))

**デスクトップブラウザーで遊び、ゲーム本体と分けてスコアの記録方法を確認する。**

制作者は Hydrogen が Base に連携した Sheytonak の制作を支援し、スコアをオンチェーンに保存すると説明する。デスクトップ向けで、モバイルの問題や不具合が残る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-213"></a>
### 事例 213: [プロンプトから MIDI を書く作曲アプリ](https://x.com/Awed_Urshy/status/2122161392828727738) (作者 [@Awed_Urshy](https://x.com/Awed_Urshy))

**日本語の指示を MIDI、WAV、ピアノロールに変換する試作を作る。**

制作者は Hydrogen で作ったアプリを公開した。アプリは日本語入力から英語の作曲指示を作り、MIDI を書いて WAV 音声とピアノロール動画を出力する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

種類: Demo | 日付: 2026-11-16

---

<a id="case-215"></a>
### 事例 215: [コンサートの振り返りを1ページに](https://x.com/fukubaya/status/2122215495474794640) (作者 [@fukubaya](https://x.com/fukubaya))

**イベント情報を一目で追える視覚資料にまとめる。**

投稿者はばってん少女隊のコンサートを Hydrogen でまとめた日本語資料を公開した。元の情報一式やプロンプトは掲載していない。

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

種類: Demo | 日付: 2026-11-16

---

<a id="case-218"></a>
### 事例 218: [アバター画像から日常の短い動画へ](https://x.com/antiAIvo/status/2122251181112353276) (作者 [@antiAIvo](https://x.com/antiAIvo))

**参照画像1枚と日常の4シーンで、短い絵コンテへの展開を評価する。**

制作者は X のプロフィール画像と、勉強、食事、スマートフォン、運動を指定し、Hydrogen による約10秒の出力を公開した。映像生成の基盤は記載されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

種類: Demo | 日付: 2026-11-16

---

<a id="case-219"></a>
### 事例 219: [Hydrogen が ComfyUI 用のキャラクター動画を計画](https://x.com/nyapan_mohy/status/2122253350808744004) (作者 [@nyapan_mohy](https://x.com/nyapan_mohy))

**衣装と背景を固定し、表情と動きに変化を付ける。**

制作者によると Hydrogen が設定画に沿って動画を企画し、別の ComfyUI MiniMax の画像から動画を作る工程で描画した。変化を付けるため、新しい開始フレームと30ショットの指示を用意した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

種類: Integration | 日付: 2026-11-16

---

<a id="case-222"></a>
### 事例 222: [曲をワイド画面の映像にする](https://x.com/ivy432hz/status/2122283590180589791) (作者 [@ivy432hz](https://x.com/ivy432hz))

**曲と画角の指定から、動きで曲の勢いを表現できるか試す。**

制作者は Hydrogen XHigh に曲だけを渡し、21:9と疾走感を指定したと説明する。動画は道路を高速で移動する映像で、描画方法は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

種類: Demo | 日付: 2026-11-16

---

<a id="case-224"></a>
### 事例 224: [時代物の恋愛動画2本で連続性を保つ](https://x.com/AvaSinclairAi_/status/2122315627113107670) (作者 [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**次の動画で場面を続けるときに、引き継ぐ細部を具体的に指定する。**

制作者は客船での恋愛シーンを Hydrogen を使う Gemini の作業で作り、人物や衣装をそろえる二部構成の指示を公開した。元の動画生成モデルは不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

種類: Demo | 日付: 2026-11-16

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

<a id="case-60"></a>
### 事例 60: [Box Agent で複雑な業務文書を処理](https://x.com/levie/status/2120947988143198302) (作者 [@levie](https://x.com/levie))

**現実的な文書タスクで正確さ、処理時間、トークン量を測る。**

Box の早期アクセス評価では、典型的なタスクで Gemini 3.8 Flash より正確さが5ポイント上がり、時間は半分未満、トークンは約12%減ったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-74"></a>
### 事例 74: [Workspace のデータからグラフと報告書を作成](https://x.com/nin222/status/2120989168247652674) (作者 [@nin222](https://x.com/nin222))

**追加のやり取りで、足りない分析、グラフ、報告書を補えるか確認する。**

制作者は Google Workspace for Education Fundamentals のデモ環境で Hydrogen を使い、データ分析、グラフ作成、報告書出力を2回のやり取りで完了したと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-12

---

<a id="case-81"></a>
### 事例 81: [Gemini の各モードで表にドット絵を描く](https://x.com/kkitase/status/2121041283640926401) (作者 [@kkitase](https://x.com/kkitase))

**同じスプレッドシート描画課題で、いくつかのモデル選択肢を比較する。**

制作者は Hydrogen で Google スプレッドシートにドット絵を描く様子を録画し、Antigravity Orchestrator、Carbon、Argon の各実行にもリンクした。正式な採点は行っていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-148"></a>
### 事例 148: [操作できる FAA 地上待機マップ](https://x.com/SidraMiconi/status/2121486870341370204) (作者 [@SidraMiconi](https://x.com/SidraMiconi))

**運航停止が終わった後も待ち行列が残る理由を、地図とタイムラインで示す。**

制作者は Hydrogen で FAA の運航混乱を扱うマップを222秒で作り、ラベルを一つ直したと報告した。時系列は公式情報に基づき、交通量は通常の時刻表で模擬している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-184"></a>
### 事例 184: [Chrome で構造化した YouTube 要約を作る](https://x.com/studio_yebisu/status/2121835594674561098) (作者 [@studio_yebisu](https://x.com/studio_yebisu))

**Chrome の Gemini パネルに、タイムスタンプ付き要約と出典付きの背景説明を求める。**

出典は Chrome で開いている YouTube を要約する手順を示す。公開プロンプトは概要、要点、各章の流れ、出典を分けた背景、事実関係の注意点、参考資料を求めている。

**プロンプト:**

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

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

種類: Tutorial | 日付: 2026-11-15

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

<a id="case-41"></a>
### 事例 41: [宇宙の参考画像から HTML シーンを作る](https://x.com/Inmerson/status/2120482539907559651) (作者 [@Inmerson](https://x.com/Inmerson))

**少数の参考画像から、見分けのつく画風を再現できるか確認する。**

制作者は宇宙の可視化を Hydrogen で作ったと説明する。出典では入力の惑星画像と、環を持つ惑星を描いた HTML シーンが確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-11

---

<a id="case-42"></a>
### 事例 42: [Gemini Canvas で作る F1 車両の試作](https://x.com/auricxofficial/status/2120843585914605830) (作者 [@auricxofficial](https://x.com/auricxofficial))

**車両ビューアーに複数のカメラを設け、違う角度からモデルを確認する。**

制作者は Gemini Canvas で初めて Hydrogen を使い、F1 風の車両ビューアーを作ったと説明する。録画では複数のカメラとサスペンションの表示が確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-48"></a>
### 事例 48: [BMW の側面を SVG で描く](https://x.com/HarshithLucky3/status/2120932649938382894) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**車両の側面図で比率、輪郭、細部を確認する。**

投稿者は Gemini アプリの Hydrogen High で生成したという BMW M4 CS の SVG 側面図を示し、所要時間は30秒未満だったと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-12

---

<a id="case-49"></a>
### 事例 49: [天文学者の浮遊島](https://x.com/pankajkumar_dev/status/2120933196221333791) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**小さなシーンに明確な主題を設定し、小物と光がその主題を伝えるかを見る。**

制作者は天文学者の浮遊島を Arena 上の Hydrogen チェックポイントで作り、生成に4分かかったと報告している。モデルの帰属はその Arena 実行についての説明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-50"></a>
### 事例 50: [参考画像から歩き回れる3D風景へ](https://x.com/HarshithLucky3/status/2120935535422374055) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**画像からできたシーンで、見た目の再現と移動の両方を確かめる。**

制作者は Gemini アプリの Hydrogen による操作可能な3D風景を示し、GLSL の反射、プロシージャルな形状、水泳時の物理挙動を紹介している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-51"></a>
### 事例 51: [3Dブロックで作るミニチュア風景](https://x.com/abhinavflac/status/2120936501961969990) (作者 [@abhinavflac](https://x.com/abhinavflac))

**積み木で小さな風景を作らせ、形がまとまった場面に見えるか確認する。**

制作者は3Dブロックのミニチュアを録画し、Hydrogen で作ったと説明する。制作時間や正確な設定は公表されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-52"></a>
### 事例 52: [操作できる桜の木](https://x.com/hakmgpt/status/2120936640436642231) (作者 [@hakmgpt](https://x.com/hakmgpt))

**動くオブジェクトと少数の操作項目で、シーンがリアルタイムに変わる様子を見る。**

制作者はスクリーンショットの桜の木の画面を Hydrogen で作ったと説明する。画面には設定項目が見えるが、実装の詳細は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-12

---

<a id="case-62"></a>
### 事例 62: [小さなインタラクティブ作品の屈折表現](https://x.com/chanelluuh/status/2120951519470399710) (作者 [@chanelluuh](https://x.com/chanelluuh))

**短いプレビューで光学効果を調整してからシーンを作り込む。**

制作者は Small Delights のミニ作品を Hydrogen によるものとし、屈折効果を見どころに挙げる。投稿には反復して作る流れも記述されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-63"></a>
### 事例 63: [上に向かって流れる川](https://x.com/xKaka1456/status/2120952404225265983) (作者 [@xKaka1456](https://x.com/xKaka1456))

**普段と逆の動きを指定し、視覚効果を見て確かめる。**

投稿者はウェブ版 Hydrogen で逆流する川を作ったと説明し、録画を公開した。時間と契約枠の使用量は本人の観測値。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

種類: Demo | 日付: 2026-11-12

---

<a id="case-67"></a>
### 事例 67: [Hydrogen で作る3D肖像](https://x.com/soyamiruku/status/2120959893943251322) (作者 [@soyamiruku](https://x.com/soyamiruku))

**小さな肖像課題で3D表現が人物の特徴を伝えられるか見る。**

投稿者は投稿先の人物を題材にした3D肖像を Hydrogen で制作したと説明し、画像を公開した。設定の説明は限られる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

種類: Demo | 日付: 2026-11-12

---

<a id="case-82"></a>
### 事例 82: [参考画像からアパートを3Dプリント](https://x.com/bijanbowen/status/2121042010928709932) (作者 [@bijanbowen](https://x.com/bijanbowen))

**画像から3Dを生成するテストを実物の出力まで進める。**

投稿者は Hydrogen で作成したという『となりのサインフェルド』のアパートの参考画像と3Dプリントを公開した。

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

種類: Demo | 日付: 2026-11-13

---

<a id="case-86"></a>
### 事例 86: [ゴーイングメリー号の海上シーン](https://x.com/xKaka1456/status/2121063351136739388) (作者 [@xKaka1456](https://x.com/xKaka1456))

**よく知られた架空の船を題材に、海上シーンの構図を確かめる。**

制作者は青い海に浮かぶゴーイングメリー号の動画を公開し、Hydrogen で作ったと説明する。プロンプトや設定、反復回数は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-88"></a>
### 事例 88: [雲海を泳ぐクジラ](https://x.com/xKaka1456/status/2121100318150898144) (作者 [@xKaka1456](https://x.com/xKaka1456))

**コードで作った生物シーンで流体の動きと目の造形を分けて確認する。**

出典は雲海を泳ぐクジラを示し、Hydrogen の実行に約2分かかったと報告する。時間と枠の消費量は投稿者の観測。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-92"></a>
### 事例 92: [Gemini Canvas の海底都市](https://x.com/ayyh_18/status/2121128385690693821) (作者 [@ayyh_18](https://x.com/ayyh_18))

**小さな3Dシーンから始め、何回かのやり取りで探索エリアと動く生き物を加える。**

制作者は Gemini アプリで指示を繰り返し、魚、クラゲ、サンゴ、内部を歩けるガラスドームのある海底都市を作った。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-99"></a>
### 事例 99: [Three.js のグレースケール海賊船](https://x.com/parves075/status/2121172856889618528) (作者 [@parves075](https://x.com/parves075))

**色をグレーに限定し、光だけで形状が伝わるか確かめる。**

投稿者は Antigravity の Hydrogen を使い、Three.js でグレースケールの海賊船を作成した。録画で光の当たり方と3Dの細部を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-101"></a>
### 事例 101: [CadXStudio のパラメトリックな卓上照明](https://x.com/CadX_Studio/status/2121175785356853312) (作者 [@CadX_Studio](https://x.com/CadX_Studio))

**生成した CAD で部品の寸法と編集のしやすさを確認する。**

ツール提供元の CadXStudio はブラウザー内の卓上照明を示し、編集できる部品が35個あると報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

種類: Integration | 日付: 2026-11-13

---

<a id="case-102"></a>
### 事例 102: [C++ で作る神社の参道アニメーション](https://x.com/nehstrr3/status/2121184399245128137) (作者 [@nehstrr3](https://x.com/nehstrr3))

**小さなネイティブコードの場面で、ウェブ基盤を使わずに動くアニメーションを書けるか試す。**

制作者は鳥居の下を通る参道の動画を Hydrogen Extra High の出力とし、独自の C++ で実装したと説明する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-105"></a>
### 事例 105: [30モジュールから作る町並み](https://x.com/IamEmily2050/status/2121200010574598655) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**モジュールごとの指示で場面を組み立て、完成した全景を確認する。**

投稿者は Gemini アプリの Hydrogen High を使い、30モジュールを各1回のプロンプトで作ったと述べる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-108"></a>
### 事例 108: [浮遊島の郵便局](https://x.com/pankajkumar_dev/status/2121220537984954448) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**ミニチュアの建物を指定し、素材と光が場面をどう見せるか確認する。**

投稿者は Hydrogen に浮遊島の小さな3D郵便局を作らせ、録画を公開した。質感、色、照明を見どころとして挙げる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-110"></a>
### 事例 110: [錦鯉の庭園で水と魚を描く](https://x.com/SahilPanhotra/status/2121225566779023432) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**魚が動くシーンで、水面の反射と照明が破綻しないか確認する。**

制作者は Hydrogen による錦鯉の庭園を公開し、集光、反射、魚の動きに触れている。比較用に Carbon 版へリンクした。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-112"></a>
### 事例 112: [Gemini アプリで動く3Dシーン](https://x.com/YxzRainy/status/2121232725185339869) (作者 [@YxzRainy](https://x.com/YxzRainy))

**ウェブ版 Gemini で操作できる照明と粒子効果を試作する。**

制作者は粒子、動く照明、リアルタイムの操作を備えた3Dシーンを公開した。Hydrogen で作った場面がブラウザー版 Gemini で動く様子が見える。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-115"></a>
### 事例 115: [一つの HTML に収めたピンクの3Dシーン](https://x.com/SahilPanhotra/status/2121254256288137484) (作者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**外部素材なしの Three.js で、見やすい構図になるか試す。**

制作者によると、Hydrogen が作ったピンクの場面は単一 HTML の純粋な Three.js で実装した。リンク先の錦鯉の庭園は別プロジェクト。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-119"></a>
### 事例 119: [コードだけのビッグバン・シミュレーション](https://x.com/ash_twtz/status/2121268140630000020) (作者 [@ash_twtz](https://x.com/ash_twtz))

**短い動画で説明の試作品を作り、科学的な表現を確かめる。**

制作者は Gemini アプリの Hydrogen を使い、ウェブアクセス、テクスチャ、外部素材、3Dモデルなしで15秒のビッグバンをコードだけで表現したと説明する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-120"></a>
### 事例 120: [分解表示ができるヘリコプター](https://x.com/LuminaBench/status/2121273297715277930) (作者 [@LuminaBench](https://x.com/LuminaBench))

**飛行操作と部品を調べるビューが3D試作で両立するか試す。**

制作者は飛行できるヘリコプターと組み立て・分解ビューを示し、Hydrogen Extra High で作ったと説明する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-121"></a>
### 事例 121: [X線とワイヤーフレーム付き Hydrogen Express](https://x.com/LuminaBench/status/2121277060983234788) (作者 [@LuminaBench](https://x.com/LuminaBench))

**操作可能な3D試作に複数の確認モードを組み込む。**

制作者は速度操作、分解、ワイヤーフレーム、X線表示がある列車を公開し、約5分の実行だったと報告する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-122"></a>
### 事例 122: [空に浮かぶ給油所](https://x.com/doe_naps/status/2121279837512106168) (作者 [@doe_naps](https://x.com/doe_naps))

**複数の動く物体と照明状態を使い、デモでシーンの変化が見えるようにする。**

制作者はレトロな飛行車、回るタービン、昼夜の移り変わりを含む給油所を Hydrogen で作った。一度の生成でできたと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-129"></a>
### 事例 129: [一つの HTML に収めた水車小屋](https://x.com/NovaXCode/status/2121294356875509851) (作者 [@NovaXCode](https://x.com/NovaXCode))

**動きが見分けやすい小さな風景で3Dの短時間試作を確認する。**

制作者は一つの HTML で Hydrogen が水車小屋を約30秒で作ったと述べ、録画を公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-132"></a>
### 事例 132: [Hydrogen Extra で作る Blender シーン](https://x.com/SPAC89/status/2121302218347270625) (作者 [@SPAC89](https://x.com/SPAC89))

**作り込みを増やす前に Blender で形状と素材を確かめる。**

投稿者は Hydrogen Extra によるものとする Blender の作例を見せ、その実行での契約枠の消費量を見積もった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-139"></a>
### 事例 139: [Hydrogen で作る2種類の粒子アニメーション](https://x.com/gwammyy/status/2121355401392189746) (作者 [@gwammyy](https://x.com/gwammyy))

**異なるパーティクルの場面で、簡単な効果の形と動きを見る。**

制作者は2本の短いパーティクル効果を Hydrogen で作ったと説明する。投稿は出力だけを掲載し、実行設定は記載していない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

種類: Demo | 日付: 2026-11-13

---

<a id="case-142"></a>
### 事例 142: [ミニチュア世界の昼夜スイッチ](https://x.com/vib3coded/status/2121398359395283027) (作者 [@vib3coded](https://x.com/vib3coded))

**小さなスイッチを使い、画面の状態が変わるときの動きのつながりを調べる。**

制作者はスイッチに連動する昼夜の変化を公開し、制作費は0.21ドルだったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-143"></a>
### 事例 143: [65モジュールで環境を作る](https://x.com/IamEmily2050/status/2121400396002492781) (作者 [@IamEmily2050](https://x.com/IamEmily2050))

**生成シーンを拡張するとき、制作時間と統合作業を記録する。**

制作者は Gemini アプリでモジュールごとに一つの指示を使い、65個のモジュールを作ったと報告し、結果を録画した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-149"></a>
### 事例 149: [ミニチュアの塔と庭園](https://x.com/auricxofficial/status/2121498286926540970) (作者 [@auricxofficial](https://x.com/auricxofficial))

**生成したミニチュアで建築と周辺の植栽のバランスを見る。**

制作者はブロック風の塔と庭園の動画を Hydrogen による作品とし、実装の詳細は記載していない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-153"></a>
### 事例 153: [第二次大戦の飛行場をジオラマにする](https://x.com/doe_naps/status/2121508105947320688) (作者 [@doe_naps](https://x.com/doe_naps))

**資料に加えて機械の動作を指定し、見た目と動きの両方を確かめる。**

制作者は資料と短い指示を Hydrogen に与え、一つの HTML で飛行場を作ったと説明する。指示には動く飛行機と戦車が含まれていた。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-167"></a>
### 事例 167: [プロシージャルに描いたコマドリの飛行](https://x.com/LuminaBench/status/2121620820791562291) (作者 [@LuminaBench](https://x.com/LuminaBench))

**生成された飛行で翼と胴体の動きを確認する。**

制作者はコマドリが飛ぶアニメーションを Hydrogen がコードで作ったと説明し、後続の投稿で同じ作業の Antigravity swarm のグラフを公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

種類: Demo | 日付: 2026-11-14

---

<a id="case-182"></a>
### 事例 182: [単一の HTML だけで描くイラスト](https://x.com/vamsibatchuk/status/2121788887823778297) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**参考イメージを外部素材なしのコードで再現できるか試す。**

DeepMind のスタッフは単一ファイルのイラストを公開し、ライブラリー、画像生成ツール、スキル、埋め込み素材を使わなかったと説明した。

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

種類: Demo | 日付: 2026-11-15

---

<a id="case-186"></a>
### 事例 186: [静止画からパフィンを動かす](https://x.com/vamsibatchuk/status/2121846407950639541) (作者 [@vamsibatchuk](https://x.com/vamsibatchuk))

**既存 HTML の場面を、プログラムで動かすアニメーションの最初のフレームに使う。**

制作者は一つの HTML で続きの50フレームを Hydrogen に作らせた。動画ではパフィンが登場人物の帽子を取る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-200"></a>
### 事例 200: [一つのプロンプトで3Dのミニチュア島](https://x.com/CodeByPoonam/status/2121952483132289270) (作者 [@CodeByPoonam](https://x.com/CodeByPoonam))

**一度の生成で目印、地形、水が分かりやすく並ぶか調べる。**

制作者は掲載した島を Hydrogen で一回の指示から作ったと説明する。画像で建物などの目印を確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-208"></a>
### 事例 208: [特異点を題材にした操作パネル](https://x.com/Moleh1ll/status/2122032596263776351) (作者 [@Moleh1ll](https://x.com/Moleh1ll))

**単一の視覚コンセプトで、短い対話型のシーケンスを試作する。**

制作者は特異点を題材にした操作パネルを Hydrogen で作ったと説明している。録画は出力を示し、実装の背景は限られる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

種類: Demo | 日付: 2026-11-15

---

<a id="case-225"></a>
### 事例 225: [Gemini アプリの水の球体](https://x.com/Google/status/2122366286659289502) (作者 [@Google](https://x.com/Google))

**簡単な光学シーンで反射光と屈折の関係を確かめる。**

Google は Hydrogen の文字を含む水のような球を Gemini アプリの作例として公開し、Hydrogen による成果と説明した。描画環境の詳細は記載されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

種類: Demo | 日付: 2026-11-16

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

<a id="case-43"></a>
### 事例 43: [Hydrogen API と Antigravity の Carbon を比較](https://x.com/huang18825/status/2120876396264444314) (作者 [@huang18825](https://x.com/huang18825))

**同じプロンプトによる描画を比較するときは、それぞれの実行環境を記録する。**

制作者は Hydrogen を API、Carbon を Antigravity で実行し、結果を並べた。報告された4分47秒は、この環境での Hydrogen の実行時間。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-44"></a>
### 事例 44: [Hydrogen と Astra の影の描写](https://x.com/SPAC89/status/2120911537296515321) (作者 [@SPAC89](https://x.com/SPAC89))

**実行時間と費用を比べながら、細かな描写も確認する。**

制作者は影を描いた Hydrogen の出力を好み、この環境では処理も速かったと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-45"></a>
### 事例 45: [プロシージャルな3Dモーションを比較](https://x.com/SPAC89/status/2120923185981915156) (作者 [@SPAC89](https://x.com/SPAC89))

**動きのつながりと構図を見比べながら、生成時間を記録する。**

制作者は Hydrogen High による縞模様の3D形状を示し、5分未満で作れたと報告する。自身のテストで使った、より高価なモデルの結果とも比較している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-46"></a>
### 事例 46: [PokéBench の画像入力テストを89分実行](https://x.com/StatsWire/status/2120923685296988296) (作者 [@StatsWire](https://x.com/StatsWire))

**長時間動く視覚エージェントは、達成結果と併せてターン数と API 失敗件数を記録する。**

出典によると、発表前に Vertex の High で実行した Hydrogen は、89分・365ターンでタケシを倒し、API 呼び出しはすべて成功した。この結果は出典の実行環境に限られる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-47"></a>
### 事例 47: [Hydrogen と DeepSeek が同じ3Dシーンを制作](https://x.com/AiHubMix/status/2120928687537418581) (作者 [@AiHubMix](https://x.com/AiHubMix))

**描画を比較し、実行時間と API 料金は別々に記録する。**

AIHubMix は両モデルの利用可能な最高推論レベルで、同じ3Dシーンのプロンプトを試した。事業者の報告では、Hydrogen が3分・1.30ドル、DeepSeek V4.1 Flash が100分・0.90ドル。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-53"></a>
### 事例 53: [Agent Arena のタスク別所要時間と費用](https://x.com/arena/status/2120940869889175840) (作者 [@arena](https://x.com/arena))

**全体の成功率に加え、1タスクあたりの所要時間、費用、出力トークンを確認する。**

Agent Arena の評価によると、Hydrogen High のタスクあたりの中央値は5.3分、1.60ドル。出力トークンは Carbon や Argon より多かったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-54"></a>
### 事例 54: [画像文書とターミナルのベンチマーク](https://x.com/ArtificialAnlys/status/2120941511223185722) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**推論予算を決めるときに文書とターミナルの結果を個別に見る。**

Artificial Analysis は画像文書で良い結果を報告した。Extra 推論で科学向けターミナルのスコアは上がり、一般向け Terminal-Bench は54%のままだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-55"></a>
### 事例 55: [Vals Index と Tax Agent の結果](https://x.com/ValsAI/status/2120943893894303808) (作者 [@ValsAI](https://x.com/ValsAI))

**全体評価と併せて、専門タスクのスコアを確認する。**

Vals AI によると、評価時の Hydrogen は Vals Index で68.5%を獲得し、Tax Agent で首位だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-56"></a>
### 事例 56: [CursorBench のデフォルト推論レベル](https://x.com/cursor_ai/status/2120944639633211619) (作者 [@cursor_ai](https://x.com/cursor_ai))

**デフォルトのスコアを出発点に、自分のリポジトリでテストする。**

Cursor の自社評価では、デフォルトの Hydrogen が54.3%、Gemini 3.8 Flash が39.6%だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-57"></a>
### 事例 57: [4モデルで弓兵の対戦をアニメ化](https://x.com/IndependentEco/status/2120945011277590733) (作者 [@IndependentEco](https://x.com/IndependentEco))

**戦う人物の行動が各アニメーションでどれくらい伝わるか比較する。**

制作者は Hydrogen、Fable 5.2、GPT-6.1 Sol、Carbon による弓兵の対戦を一つの動画に並べた。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-61"></a>
### 事例 61: [Devin FrontierCode での Hydrogen](https://x.com/cognition/status/2120950876248641588) (作者 [@cognition](https://x.com/cognition))

**修正をマージできるか確認し、エージェントの実行環境も記録する。**

Cognition は FrontierCode 2.0 で38.2%を報告した。Hydrogen と比較モデルでは Devin CLI のテスト環境が異なる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-64"></a>
### 事例 64: [検索禁止の指示があっても検索を実行](https://x.com/amanunreal/status/2120954045615768054) (作者 [@amanunreal](https://x.com/amanunreal))

**外部検索を使わない回答が必要なときは、実際のツール履歴を確認する。**

投稿者によると、検索とツール呼び出しを避けるよう求めても Hydrogen がウェブ検索を行った。出典は個別の実例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-12

---

<a id="case-65"></a>
### 事例 65: [Antigravity Swarm の利用枠を測る](https://x.com/HarshithLucky3/status/2120954399971487774) (作者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**複数エージェントによる処理のトークン量と消費枠を記録する。**

制作者は自身の契約で Swarm を使い、1,700万トークンと5時間枠の21%を消費したと報告した。数値はこのセッションのもの。

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

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-66"></a>
### 事例 66: [専門職タスクでのツール呼び出し](https://x.com/mercor/status/2120957582139642095) (作者 [@mercor](https://x.com/mercor))

**専門業務の判断前にエージェントがどのように情報を集めるか調べる。**

Mercor は APEX-Agents で Pass@1 78.0%、タスクあたり平均93回のツール呼び出しを報告した。対象分野は法律、コンサルティング、銀行業務。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-68"></a>
### 事例 68: [4モデルで魔法使いとドラゴンの戦いを描く](https://x.com/IndependentEco/status/2120964690906161461) (作者 [@IndependentEco](https://x.com/IndependentEco))

**同じファンタジー場面の演出、動きの読みやすさ、効果を比較する。**

比較動画は Hydrogen と3種類の Claude の戦闘場面を示す。制作者はこの例では Claude の出力を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-71"></a>
### 事例 71: [MazeBench で見えた低い成功率](https://x.com/patience_cave/status/2120973681937809766) (作者 [@patience_cave](https://x.com/patience_cave))

**迷路で空間推論を試し、実務で頼れる範囲を判断する。**

投稿された MazeBench の比較では、その設定で Hydrogen が1%、Sonnet 5.5 が4%、GPT-6.1 Terra が8%だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-72"></a>
### 事例 72: [Geminiの3モデルで帆船を描く](https://x.com/Octoberry/status/2120974412144902376) (作者 [@Octoberry](https://x.com/Octoberry))

**同じ Three.js の題材で動きと背景の細部を比較する。**

制作者は Hydrogen、Argon、Carbon の帆船を公開した。Carbon の細部を好み、Hydrogen は Argon に近かったと述べる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-75"></a>
### 事例 75: [背番号を読めずに推論予算を使い切る](https://x.com/skalskip92/status/2120994631072776235) (作者 [@skalskip92](https://x.com/skalskip92))

**画像の細部を読む処理に上限と代替手段を設ける。**

評価者によると Hydrogen XHigh は9分55秒で131,069推論トークンを使い、背番号を回答しなかった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-12

---

<a id="case-76"></a>
### 事例 76: [モデル系列ごとの ClutterBench の成績](https://x.com/AdamHoltererer/status/2121000759118459138) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**散らかった場面に特化したベンチマークで、得意分野がその課題にも当てはまるか確かめる。**

投稿された ClutterBench では、Hydrogen は掲載された Gemini の中で首位、比較の OpenAI モデルより下位だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-12

---

<a id="case-78"></a>
### 事例 78: [Minecraft 風の人体断面像](https://x.com/jan_volad/status/2121026531472339340) (作者 [@jan_volad](https://x.com/jan_volad))

**指定した内部構造が生成された断面に含まれるか見る。**

制作者は同じ一回の指示を Hydrogen と Argon に与え、Minecraft 風の胸像を作らせた。Hydrogen の出力に頭蓋骨、肋骨、脊椎があったと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-79"></a>
### 事例 79: [3モデルで同じ小道具を描画](https://x.com/luckeyfaraday/status/2121030005899825504) (作者 [@luckeyfaraday](https://x.com/luckeyfaraday))

**価格が低いモデルがどれだけトークンを使うか、品質とは別に記録する。**

Hydrogen、Carbon、Fable 5.2 でライフル形の小道具を描いた比較。制作者によると、Hydrogen は369万トークンで1.62ドル、Carbon は39万8,000トークンで0.77ドルだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

種類: Evaluation | 日付: 2026-11-12

---

<a id="case-80"></a>
### 事例 80: [帰納推論ベンチマークとトークン消費](https://x.com/s_batzoglou/status/2121037853258129811) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**難しい推論タスクでは、スコアと入力・出力の請求量を併せて記録する。**

評価者の100問ベンチマークで Hydrogen は4位、Opus 5.5 に近かった。5,500万出力トークンと3億700万の請求対象入力トークンが報告され、課金の内訳は未解明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-83"></a>
### 事例 83: [3モデルで3Dの動物を動かす](https://x.com/leo114119/status/2121054098753785915) (作者 [@leo114119](https://x.com/leo114119))

**同じ3D動物課題で体の構造と動きを見る。**

出典は Hydrogen、GPT-6.1 Terra、Claude Haiku 5.5 を比較している。制作者が Hydrogen の弱点を指摘したのは、この課題での結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-84"></a>
### 事例 84: [ts-bench で Hydrogen と Qwen を比較](https://x.com/gosrum/status/2121058334552060102) (作者 [@gosrum](https://x.com/gosrum))

**総合結果と一緒にツール呼び出しの失敗を確認する。**

出典は Hydrogen と Qwen4 Max Preview を ts-bench で比較し、ツール呼び出しの信頼性に触れている。画像はその評価時点の結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-85"></a>
### 事例 85: [Vending-Bench の事業シミュレーション](https://x.com/andonlabs/status/2121061429889642497) (作者 [@andonlabs](https://x.com/andonlabs))

**シミュレーションで得た売上とエージェント運用費を合わせて見る。**

Andon Labs によると Hydrogen は Vending-Bench 2 で3位。同程度の価格のモデルを上回る売上を得たという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-89"></a>
### 事例 89: [4モデルでミニチュアの島を作る](https://x.com/xKaka1456/status/2121111495358697924) (作者 [@xKaka1456](https://x.com/xKaka1456))

**島のデザインを比べるときに、その環境での時間と費用を記録する。**

出典によると Hydrogen は4分、GPT-6.1 Terra は20分、Sol は40分、DeepSeek は60分。Hydrogen が追加料金なしだったのは投稿者の環境での観測。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-91"></a>
### 事例 91: [布が裂ける動きをコードで比較](https://x.com/MichaelLee009/status/2121126779276402904) (作者 [@MichaelLee009](https://x.com/MichaelLee009))

**同じアニメーション課題で生地の伸び、裂け方、毛との相互作用を見る。**

制作者は Hydrogen と Claude Fable 5.2 によるコードアニメーションを比較し、後者の見た目を高く評価した。同じ設定での実行や、物理の独立検証は確認されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-94"></a>
### 事例 94: [出典をたどれない事実確認](https://x.com/cagrimbakirci/status/2121130756684886279) (作者 [@cagrimbakirci](https://x.com/cagrimbakirci))

**スクリーンショットの真偽を判断するときは、検証可能な引用元を求める。**

投稿者が Hydrogen に投稿画像の事実確認を頼むと、モデルは正しいと回答し、検証ツールを繰り返し開いたが、元の出典は示さなかったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-13

---

<a id="case-96"></a>
### 事例 96: [Hydrogen と Sol が描く2Dペリカン](https://x.com/YxzRainy/status/2121148582166491164) (作者 [@YxzRainy](https://x.com/YxzRainy))

**同じ短い2Dアニメーションで所要時間と動きを比較する。**

投稿者は自転車に乗る2Dペリカンを Hydrogen と GPT-6.1 Sol で出力した。報告された時間は28秒と6分51秒。実行設定が同じかは確認できない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-98"></a>
### 事例 98: [4モデルのウェブスイングゲーム](https://x.com/StatsWire/status/2121172215182065807) (作者 [@StatsWire](https://x.com/StatsWire))

**単一ファイルの条件をそろえて、移動と操作を比較する。**

出典は外部素材を使わず、単独の HTML に収めた3Dウェブスイングの比較を示す。Hydrogen は Extra High、Gemini 3.8 Flash、Argon、Carbon は High。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-100"></a>
### 事例 100: [4モデルの建築ジオラマ](https://x.com/Jackson77li/status/2121172890838352306) (作者 [@Jackson77li](https://x.com/Jackson77li))

**同じ建築の指示で生成し、モデルごとの照明表現を見比べる。**

制作者は同じプロンプトで作った Hydrogen、GPT-6.2、Claude Fable 5.2、DeepSeek の建築ジオラマを公開した。順位と速さは本人の評価。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-103"></a>
### 事例 103: [3モデルで列車を描画](https://x.com/xKaka1456/status/2121193705810104515) (作者 [@xKaka1456](https://x.com/xKaka1456))

**同じ列車の題材で、各設定の完成時間を確認する。**

制作者によると Hydrogen は約3分、GPT-6.1 Terra は20分、Qwen4 Max Preview は68分。動画で結果を確認できる。設定と修正回数は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-104"></a>
### 事例 104: [Extra で作る雨のチャイナタウン](https://x.com/qingzhoucloud/status/2121198911515967952) (作者 [@qingzhoucloud](https://x.com/qingzhoucloud))

**大きなアニメーションの推論レベルを選ぶ前に、時間を測り、完成画を確認する。**

制作者は別の人のプロンプトを Hydrogen Extra で実行し、雨のチャイナタウンの MP4 に約4時間かかったと報告する。比較先の Claude Fable 5.2 とは実行条件が十分にそろっていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-106"></a>
### 事例 106: [3モデルで惑星の可視化を制作](https://x.com/Stargridcompass/status/2121208957276713181) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**科学の可視化画面で同じプロンプトを使い、出力を比較する。**

録画は Claude Fable 5.2、GPT-6.2 Sol、Hydrogen の惑星を題材にした結果を比較する。順位は投稿者の目視評価で、統一設定や客観スコアは示されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-107"></a>
### 事例 107: [4モデルで Chrome の恐竜ゲームを再現](https://x.com/noclipepe/status/2121219775170761044) (作者 [@noclipepe](https://x.com/noclipepe))

**おなじみのゲームを再現するときに、所要時間とプレイ結果を比べる。**

制作者によると、AI Studio の Hydrogen は18分41秒、Fable 5.2 は45分30秒。録画には Qwen4-Max-Preview と Carbon の結果や見た目の採点もある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-109"></a>
### 事例 109: [2つのコーディングエージェントで船を作る](https://x.com/marcthecreatorr/status/2121221667619852660) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**使う実行環境で、最初に使える出力と修正の負担を確認する。**

投稿者は同じ指示を Claude Code の Sonnet と Cursor の Hydrogen に与えた。Hydrogen の実行は短かったが、2回目の出力が必要だったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-111"></a>
### 事例 111: [4モデルで剛体の投石機を作る](https://x.com/StatsWire/status/2121226579141386285) (作者 [@StatsWire](https://x.com/StatsWire))

**同じ課題で遊べる物理プロトタイプを比べ、推論設定を記録する。**

制作者は数百の石材を含む投石機シーンを4つの Gemini に試した。Hydrogen Extra High は10分3秒、Carbon High は23分33秒。Gemini 3.8 Flash High が最速だったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-116"></a>
### 事例 116: [FrontierMemory で長期の記憶を評価](https://x.com/Letta_AI/status/2121255895745351874) (作者 [@Letta_AI](https://x.com/Letta_AI))

**長く動くエージェントの記憶モデルを選ぶとき、得点と実行ごとの費用を比べる。**

Letta は Hydrogen が64.4%で Argon と同率、1回あたり約100ドルと報告した。同設定の Carbon は71.1%、約94ドル。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-117"></a>
### 事例 117: [故障させた LiveKit 音声エージェント](https://x.com/livekit/status/2121256982023672076) (作者 [@livekit](https://x.com/livekit))

**意図的にツールを失敗させ、裏付けなしの結果を報告するか確認する。**

LiveKit は意図的に不具合を入れた音声エージェントで Hydrogen を実行し、誤報告はゼロだったと伝える。Gemini 3.8 Flash とも比較し、記事にリンクした。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-123"></a>
### 事例 123: [Gemini の3モデルが自転車をアニメ化](https://x.com/AI_Screening/status/2121281026916057443) (作者 [@AI_Screening](https://x.com/AI_Screening))

**同じ指示の短いアニメーションを比較し、それぞれの実行時間を記録する。**

制作者は Carbon、Argon、Hydrogen の自転車アニメーションを公開した。Hydrogen は約90秒、Argon は5分超と報告し、描画は Carbon を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-126"></a>
### 事例 126: [2モデルで LEGO の世界を作る](https://x.com/kepochnik/status/2121286219669836027) (作者 [@kepochnik](https://x.com/kepochnik))

**完成時間と、時間内に作り込めた範囲を合わせて比較する。**

制作者は Fable 5.2 と Hydrogen の LEGO 世界を見せ、それぞれ44分と28分を報告した。比較は本人の実行に基づく。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-127"></a>
### 事例 127: [2リポジトリに埋め戻したバグを修正](https://x.com/PawelHuryn/status/2121286545223086302) (作者 [@PawelHuryn](https://x.com/PawelHuryn))

**既知の欠陥を仕込み、エージェントが発見・修正できた数を測る。**

評価者は2リポジトリに105件のバグを仕込み、実行した。この設定では Extra High の Hydrogen が、同じ Extra High の Sonnet 5.5 に僅差で及ばなかった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-128"></a>
### 事例 128: [2モデルの棒人間対カーソル](https://x.com/DanielZambrini/status/2121289822677483740) (作者 [@DanielZambrini](https://x.com/DanielZambrini))

**両方のアニメーションがポインターの動きにどう反応するか確認する。**

制作者は棒人間がカーソルと戦う比較で Fable の出力を好み、低コストの作業なら Hydrogen で十分と評価した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-130"></a>
### 事例 130: [2モデルで山岳風景を描く](https://x.com/ZryMiller/status/2121295750122594440) (作者 [@ZryMiller](https://x.com/ZryMiller))

**風景アニメーションの構図、生成時間、費用を分けて比較する。**

制作者の報告では、山のアニメーションに Hydrogen は20分30秒・0.50ドル、Opus 5.5 は11分23秒・2.50ドルを要した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-131"></a>
### 事例 131: [独自の評価環境で英語からペルシャ語に翻訳](https://x.com/MatinSenPai/status/2121296733258887365) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**難しい段落の翻訳を人間の参照訳と突き合わせて採点する。**

投稿者は自作の環境で Hydrogen の英語からペルシャ語への訳に100点中94点を付けた。採点はその設定に依存した主観評価。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-133"></a>
### 事例 133: [4モデルで沈没船を作る](https://x.com/remoteugur/status/2121302956741902451) (作者 [@remoteugur](https://x.com/remoteugur))

**同じシーンで見た目、時間、費用を個別に記録する。**

制作者によると Hydrogen は8.6分・1.16ドル、Gemini 3.8 Flash は10.8分・1.06ドル。Carbon と Opus 5.5 も試し、リアリティでは Opus を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-135"></a>
### 事例 135: [4モデルのコピーライティングをブラインド比較](https://x.com/quintanilha/status/2121315967447757299) (作者 [@quintanilha](https://x.com/quintanilha))

**モデル名を隠し、利用する文章を選ぶ。**

制作者は4モデルを匿名比較し、Hydrogen の文章を最も好んだ。自身の試行で Carbon より速く、安かったと報告する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-136"></a>
### 事例 136: [推論レベル別の物体検出と読み取り](https://x.com/skalskip92/status/2121322414453694489) (作者 [@skalskip92](https://x.com/skalskip92))

**推論レベルごとに検出精度、文字認識、料金、待ち時間を測る。**

評価者は Hydrogen、Argon、Carbon の検出と認識の点数を個別に報告した。Hydrogen High は1画像平均29.3秒で、検出64.6、認識87.2。Carbon High は両方で上回り、費用と待ち時間も増えた。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-13

---

<a id="case-137"></a>
### 事例 137: [4モデルで『カールじいさんの空飛ぶ家』を再現](https://x.com/noclipepe/status/2121326233044537688) (作者 [@noclipepe](https://x.com/noclipepe))

**同じ参考画像と指示で3D作品を作り、違いを調べる。**

投稿者は Hydrogen が4モデル中で最速・最安だったと報告し、見た目では Fable を好んだ。設定と料金は出典による。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

種類: Evaluation | 日付: 2026-11-13

---

<a id="case-144"></a>
### 事例 144: [固定カメラのダンス動画](https://x.com/notoro_ai/status/2121427503952834562) (作者 [@notoro_ai](https://x.com/notoro_ai))

**参照画像を使ったアニメーションで、キャラクター、構図、カメラ位置が保たれるか確認する。**

投稿者は Hydrogen に関連づけたダンス動画と日本語プロンプトを共有した。カメラの固定と元画像の画風維持は指示の要件で、動画を生成した基盤モデルは不明。

**プロンプト:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-145"></a>
### 事例 145: [基準テストで止まるコーディングエージェント](https://x.com/Its_lakshya_ai/status/2121431788266659919) (作者 [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**基準テストには時間制限を設け、修正を待つ前に進捗を確認する。**

制作者は、長く待っても Hydrogen が基準テストを実行し続けていた Antigravity の画面を示した。再開前に停止して調べるように求めた記録がある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-14

---

<a id="case-147"></a>
### 事例 147: [2モデルで対話型ロボットアームを作る](https://x.com/gmi_cloud/status/2121467337119588834) (作者 [@gmi_cloud](https://x.com/gmi_cloud))

**Three.js のアームを操作し、関節が自然に連動するか確認する。**

GMI Cloud は Hydrogen と Sonnet 5.5 を使ったロボットアームの動画を公開した。提供者はこの比較では Sonnet を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-151"></a>
### 事例 151: [Hydrogen と Sol が雪の村を作る](https://x.com/badboyfoxy/status/2121501015442669866) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**コーディングの比較では、所要時間、費用、見た目を個別に評価する。**

制作者の報告では Hydrogen High が3分・1.37ドル、Sol High が15分・4.03ドル。冬の村の見た目は Sol を好んだという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-152"></a>
### 事例 152: [High と Ultra で作る Three.js の島](https://x.com/laopai1990/status/2121502334866096160) (作者 [@laopai1990](https://x.com/laopai1990))

**見た目と所要時間を比較するときは推論レベルを記録し、製品間の利用枠は区別する。**

投稿者は Three.js の島で Hydrogen High と GPT-6.1 Sol Ultra を比較し、約90秒と30分を報告した。費用は推定で、推論レベルも異なる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-157"></a>
### 事例 157: [3Dの PS5 コントローラーの細部を比較](https://x.com/Stargridcompass/status/2121528563254043015) (作者 [@Stargridcompass](https://x.com/Stargridcompass))

**ボタンの影と背面部品を確認してモデリングを評価する。**

制作者は Hydrogen High と GPT-6.2 Sol を比較。約3分と11分だったとし、Sol が背面と側面の操作部をより詳しく再現したと評した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-159"></a>
### 事例 159: [CursorBench の推論予算比較](https://x.com/Beamsters1/status/2121538515909628111) (作者 [@Beamsters1](https://x.com/Beamsters1))

**高速な設定をデフォルトにする前に、推論予算ごとの成功率を比較する。**

投稿者は Hydrogen の推論予算を増やすと CursorBench 4.0 の成功率が大きく上がったと報告した。結果は当該設定に基づく。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-14

---

<a id="case-160"></a>
### 事例 160: [3モデルで星をモチーフにした聖堂を描く](https://x.com/YxzRainy/status/2121551796766376081) (作者 [@YxzRainy](https://x.com/YxzRainy))

**3Dで映像の細かさと描画の安定性を別々に見る。**

制作者は Hydrogen、DeepSeek V4.1 1017、Qwen4 Max Preview を比較した。Hydrogen はこの試行で速く、暗転やちらつきがなかったが、細部は少なかったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-162"></a>
### 事例 162: [既存の移行設計を見直す](https://x.com/is_llll/status/2121565725072490559) (作者 [@is_llll](https://x.com/is_llll))

**移行にあたって現在の設計を置き換えるべきか、エージェントに検討させる。**

投稿者の設計レビュー比較では Hydrogen と Argon が既存案を支持し、Claude Opus は設計を置き換えて早めに移行するよう提案した。個別のプロジェクトの判断。

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

種類: Limit | 日付: 2026-11-14

---

<a id="case-165"></a>
### 事例 165: [2モデルが作る神殿脱出ゲーム](https://x.com/runable_hq/status/2121596515474964556) (作者 [@runable_hq](https://x.com/runable_hq))

**同じゲームの照明と雰囲気が、遊ぶときの見やすさを支えるか比較する。**

Runable は同じ神殿脱出ゲームで Hydrogen と Argon の実装を公開した。提供者は Hydrogen の照明に雰囲気があり、Argon は明るいと説明する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-166"></a>
### 事例 166: [Gemini の3モデルでラリーバギーを動かす](https://x.com/teddyaisi/status/2121604816380010719) (作者 [@teddyaisi](https://x.com/teddyaisi))

**傾斜したコーナーでサスペンションとタイヤの接地が自然か確かめる。**

制作者は Carbon、Argon、Hydrogen を使い、採石場の Three.js バギーを比較した。指示にはサスペンションの縮みと傾いた未舗装路での滑りがあった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-169"></a>
### 事例 169: [2モデルで Chasing Views をアニメ化](https://x.com/VulKan42069/status/2121625271493382166) (作者 [@VulKan42069](https://x.com/VulKan42069))

**各モデルの推論レベルを記録し、出力と実行時間を比べる。**

制作者は Hydrogen Extra High と Opus 5.5 High のアニメーションを公開した。今回の所要時間はそれぞれ22分と18分と報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-170"></a>
### 事例 170: [Design Creativity Bench の速度と費用](https://x.com/Kombaico/status/2121635837180031129) (作者 [@Kombaico](https://x.com/Kombaico))

**創造性スコアと併せて、デザイン1件あたりの時間と費用を比較する。**

評価元は Hydrogen の創造性を49.4、デザインごとの中央値を3.4分と0.39ドルと報告した。Argon は時間が長く低価格、Carbon は時間も費用も増えた。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

種類: Benchmark | 日付: 2026-11-14

---

<a id="case-172"></a>
### 事例 172: [4モデルで砂漠を疾走する馬を描く](https://x.com/Marlenuii/status/2121664345818235177) (作者 [@Marlenuii](https://x.com/Marlenuii))

**光やメッシュを見る前に足の接地と重心移動を比べる。**

制作者は Astra、Carbon、Fable 5.2、Hydrogen で砂漠を走る馬を比較した。Astra の歩様を高く評価し、Hydrogen の馬の構造に問題があると指摘した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-174"></a>
### 事例 174: [FrontierCS 2 で計算機科学の研究課題を解く](https://x.com/wenhaocha1/status/2121679887400403308) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**通常のコーディングと併せて研究ベンチマークを実行し、環境を記録する。**

出典は Antigravity 上の Hydrogen が FrontierCS 2 で合格率7位だったと報告した。この評価は計算機科学の研究に由来する技術課題を扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

種類: Benchmark | 日付: 2026-11-14

---

<a id="case-175"></a>
### 事例 175: [4モデルの『Rio Above the Clouds』](https://x.com/EnvolDev/status/2121701704139956250) (作者 [@EnvolDev](https://x.com/EnvolDev))

**同じ制作指示で、費用、実行時間、主観的な品質を比較する。**

評価者は Hydrogen Extra High が6.21ドルで、出力は最も好みに合わなかったと報告した。この試行では Astra のほうが速く、ネイティブ動画生成の有無は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-176"></a>
### 事例 176: [GBENCH の技術問題に取り組む Hydrogen](https://x.com/leo_linsky/status/2121710421891780864) (作者 [@leo_linsky](https://x.com/leo_linsky))

**価格や時間に加え、検証可能なコーディングと非コーディングの成果で判断する。**

GBENCH の運営元は回路設計や抽象推論も含む評価結果を公開した。同程度の価格と速度で Sol のほうが有力だったと説明する。

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

種類: Benchmark | 日付: 2026-11-14

---

<a id="case-177"></a>
### 事例 177: [車に縦列駐車を学ばせる](https://x.com/noclipepe/status/2121734795738652934) (作者 [@noclipepe](https://x.com/noclipepe))

**生成したシミュレーションの学習経過と最終成功率を比較する。**

同じ課題で Hydrogen は44台中5台、Fable 5.2 は40台中26台が駐車できたと制作者は報告した。制作時間は5.6分と24分。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

種類: Evaluation | 日付: 2026-11-14

---

<a id="case-181"></a>
### 事例 181: [Terminal-Bench 4.0 の Hydrogen](https://x.com/gosrum/status/2121785156273160558) (作者 [@gosrum](https://x.com/gosrum))

**コマンドライン向けのモデルを選ぶときは、成功率とタスク費用を合わせて見る。**

独立評価の Terminal-Bench 4.0 で、Hydrogen は Claude Opus 5.5 と GPT-6.1 Sol に近い点数で、費用は両者の間だったという。評価者は実行環境の成熟度にも言及した。

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

種類: Benchmark | 日付: 2026-11-15

---

<a id="case-183"></a>
### 事例 183: [Gemini の3モデルでタコを動かす](https://x.com/teddyaisi/status/2121800606406885880) (作者 [@teddyaisi](https://x.com/teddyaisi))

**岩をつかんだときにその動きが体を前に進めるか確認する。**

制作者は Carbon、Argon、Hydrogen で、タコが岩棚をつかんで前進する Three.js の課題を比較した。腕と胴体の動きのつながりに注目するよう促している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-187"></a>
### 事例 187: [城のモデリングテスト](https://x.com/nemumusitocha/status/2121848375998063012) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**モデルごとの城と、作業に使った資源を比べる。**

制作者は Hydrogen で作った3Dの城を公開し、以前のモデルと比較する投稿にリンクした。Google AI Pro の週間枠3%という消費は、その実行の値。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-191"></a>
### 事例 191: [スコープ追加で大きく変わる工期見積もり](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**納期が大きく変わったときは、範囲と前提条件を説明させる。**

制作者が共有した対話で、必要な機能を含む現実的な工程を求めると、1か月が1年に変わった。実際の所要期間は記録されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-15

---

<a id="case-193"></a>
### 事例 193: [うるう年を含めて暦を換算](https://x.com/itsvishaltwt/status/2121891117050589249) (作者 [@itsvishaltwt](https://x.com/itsvishaltwt))

**簡単な換算問題でも、暦の例外を考慮するかを確認する。**

制作者は1年の秒数を Hydrogen High と GPT に尋ねた。両方の回答は平年と閏年の秒数を示し、Hydrogen はグレゴリオ暦の平均年も計算した。

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

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-196"></a>
### 事例 196: [回答に古い契約条件が混じる](https://x.com/take14262/status/2121934737539514533) (作者 [@take14262](https://x.com/take14262))

**調査アシスタントを評価するときは、契約条件やモデル名を一次情報で確認する。**

投稿者は Hydrogen が似たモデル名を混同し、Qwen プランの利用期間について古い情報を出した例を示した。スクリーンショットで具体的な箇所を確認できる。

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

種類: Limit | 日付: 2026-11-15

---

<a id="case-197"></a>
### 事例 197: [WebGL アニメーションの物語を修正](https://x.com/snakajima/status/2121939899242996058) (作者 [@snakajima](https://x.com/snakajima))

**技巧的な初稿の流れが分かりにくい場合は、筋立てに焦点を当てて修正を頼む。**

制作者は音や動きが騒がしく物語が見えにくいと指摘し、最初の WebGL 版と修正版を公開した。修正版を評価しつつ、比較した Claude Code 版をより好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

種類: Limit | 日付: 2026-11-15

---

<a id="case-199"></a>
### 事例 199: [2モデルが山寺の上でドラゴンを戦わせる](https://x.com/DrstaOne/status/2121947540509831302) (作者 [@DrstaOne](https://x.com/DrstaOne))

**同じシーンで絡み合う二者のアニメーションを比べる。**

制作者は山寺の上空でドラゴンが戦う場面を Qwen-4 Max と Hydrogen でコード化して比較した。指示を書いた別の制作者も明記した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-201"></a>
### 事例 201: [再現に使える Three.js ペリカンのプロンプト](https://x.com/Aki_LIG/status/2121960943361896596) (作者 [@Aki_LIG](https://x.com/Aki_LIG))

**自転車の脚、車輪、ハンドルの動きが連動するか見る。**

制作者は完全な日本語の指示を公開し、海岸道路の Hydrogen の出力を録画した。同じ指示は以前に GPT-6.1 Terra へも渡したという。掲載動画は Hydrogen の実行。

**プロンプト:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-205"></a>
### 事例 205: [同じ小屋を3つの環境で作る](https://x.com/doe_naps/status/2121999317628330476) (作者 [@doe_naps](https://x.com/doe_naps))

**設定や実行先を変えて画像タスクを試し、出力形式を確認する。**

制作者によると Antigravity の Hydrogen High と Carbon High、AI Studio の Hydrogen Extra High は静止画だった。Arena で Hydrogen と表示された実行は SVG が動いたが、チェックポイントの独立確認はない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-206"></a>
### 事例 206: [同じ指示でダッシュボードを比較](https://x.com/fiapp_pro/status/2122014257667846338) (作者 [@fiapp_pro](https://x.com/fiapp_pro))

**共通のフロントエンドの指示で、レイアウトと情報の優先順位を見比べる。**

投稿者は GPT-6.1 Sol と Hydrogen のウェブ画面を並べた。画像で外観は比較できるが、実装、設定、動作は記載されていない。

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

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-209"></a>
### 事例 209: [2モデルがコードで横スクロールを作る](https://x.com/rubenssoto_ai/status/2122035198728814753) (作者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**生成されたアクションシーンでは、動きのつながりと制作費を見る。**

制作者は Hydrogen と GPT-6 Astra の横スクロールを比較した。Hydrogen の動きが自然だと評価し、その実行の費用は低かったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

種類: Evaluation | 日付: 2026-11-15

---

<a id="case-212"></a>
### 事例 212: [日本語の回答で数式がレンダリングされない](https://x.com/ToraMutton/status/2122131489718759930) (作者 [@ToraMutton](https://x.com/ToraMutton))

**TeX を含む回答では、内容の正しさと表示の両方を確認する。**

投稿者は Hydrogen への切り替え後に日本語の回答で生の数式記法が表示された例を示した。スクリーンショットはその環境での一つの表示不具合。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

種類: Limit | 日付: 2026-11-16

---

<a id="case-214"></a>
### 事例 214: [回答しないという指示をテスト](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (作者 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**無応答が必要な作業で、モデルが実際に返信を出さないか試す。**

投稿者は無応答テストのスクリーンショットを公開し、Carbon、Argon との振る舞いの違いを報告した。出典は一組の試行。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

種類: Evaluation | 日付: 2026-11-16

---

<a id="case-216"></a>
### 事例 216: [3モデルが電動機の仕組みを説明](https://x.com/analogalok/status/2122221106304352257) (作者 [@analogalok](https://x.com/analogalok))

**同じシミュレーションで見やすさと学習者向けの操作を比較する。**

制作者は Hydrogen と2種類の Qwen を比べ、Hydrogen の3Dモーターと物理の説明を好んだ。一回の比較での評価。

**プロンプト:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

種類: Evaluation | 日付: 2026-11-16

---

<a id="case-217"></a>
### 事例 217: [2つのモデルの作業で机のシーンを動かす](https://x.com/GeroXBT/status/2122234332102435128) (作者 [@GeroXBT](https://x.com/GeroXBT))

**元の指示に照らして、細部、音量、最後の静止を確認する。**

制作者は同じ指示を API から渡し、Hydrogen と Astra を使った机上のアニメーションを比較した。Gemini の動きは滑らかだったが、最後も止まらず音は小さかったという。描画方法は不明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

種類: Evaluation | 日付: 2026-11-16

---

<a id="case-221"></a>
### 事例 221: [プログラムで音が変わる2Dの村](https://x.com/marcthecreatorr/status/2122266495216459841) (作者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**制作時間を測り、画面上の出来事に合わせて音が変化するかを見る。**

制作者は Qwen 4 Max と Hydrogen Extra High を比較した。Qwen は約75分・0.90ドル、Hydrogen は約12分・1.70ドルで、後者の音楽と出来事の連動を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[出典動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

種類: Evaluation | 日付: 2026-11-16

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon の事例と比較

<a id="acknowledge"></a>
## 🙏 謝辞

Hydrogen を使った成果を公開した制作者、開発者、評価者の皆様に感謝します。

**出典の制作者:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*帰属は引用した公開情報に基づき、最初の制作者を特定できているとは限りません。訂正や削除の依頼は、公開の出典を添えて issue を作成してください。*

貢献チェックリストに従い、issue または pull request で出典のある事例を提案してください。
