<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/ko/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=docs_link)

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

# Gemini 4 Hydrogen 활용 가이드와 엄선 사례

## 🍌 소개

출처가 있는 애플리케이션, 코딩 작업 흐름, 실용적인 비교를 통해 Gemini 4 Hydrogen을 살펴봅니다.

**엄선한 40개 사례는 무엇을 만들었고 어떻게 작업했으며 결과에 어떤 부족함이 있었는지 보여줍니다.**

각 사례에는 출처 링크와 작성자가 표시됩니다. 시연, 제공업체 사례, 제작자 비교는 설명에 구분하며, 공개되지 않은 프롬프트를 재구성하지 않습니다.

## 📊 개요

- 2026년 11월 13일 수집한 최대 500개의 X 게시물에서 시연 게시물 75개를 검토하고 사례 40개를 선정했습니다.
- 에이전트, 학습과 앱, 스프레드시트와 검색, 인터랙티브 3D, 비교와 한계의 다섯 분야를 다룹니다.
- 선정한 출처의 시각 자료 41개를 모두 보존했습니다. 포스터 이미지가 있는 재생 가능한 영상 38개와 이미지 3개입니다.
- Gemini 4 Hydrogen은 2026년 11월 12일 발표되었습니다. EvoLink에서 모델과 현재 이용 방법을 살펴보세요.

> [!NOTE]
> 별도 설명이 없다면 모델 귀속, 비용, 시간, 결과는 출처 측의 주장입니다. 영상 검토에는 추출한 프레임을 사용했으며 전체 기능 테스트는 하지 않았습니다. 코드로 만든 앱의 녹화는 네이티브 영상 생성의 증거가 아닙니다. 실행 환경, 추론 수준, 반복 횟수가 다르면 조건이 통제된 비교가 아닙니다.

**공식 참고 자료: [Google 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind 모델 카드](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**여기서 시작하기: [EvoLink에서 Hydrogen 살펴보기](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ 빠른 시작

먼저 EvoLink에서 시작하고, Hydrogen을 앱에 통합할 때 Gemini 네이티브 API를 사용하세요.

1. [브라우저에서 Gemini 4 Hydrogen 보기](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [EvoLink API 키 생성 또는 관리](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

최소 구성의 네이티브 API 요청

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

[Gemini 네이티브 API 빠른 시작 읽기](https://evolink.ai/docs/ko/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> 응답의 candidates[].content.parts[].text 필드에서 생성된 텍스트를 읽습니다.

> [!IMPORTANT]
> API 키를 환경 변수에 보관하고 절대로 커밋하지 마세요. 스트리밍, 추론 및 기타 요청 옵션은 API 문서를 참조하세요.

## 📑 목차

| 섹션 | 사례 |
|---|---|
| [⚡ 에이전트와 코딩 작업 흐름](#agents) | 5 |
| [💻 앱과 학습](#apps-learning) | 5 |
| [📊 스프레드시트와 검색](#data-search) | 4 |
| [🎮 인터랙티브 3D와 UI](#interactive-3d) | 9 |
| [🧪 비교와 한계](#comparisons-limits) | 17 |
| [관련 저장소](#related-repositories) |  |
| [빠른 시작](#quick-start) |  |
| [감사의 말](#acknowledge) |  |

| 사례 | 분류 | 시도할 사항 | 유형 |
|---|---|---|---|
| [Antigravity에서 코드베이스 유지보수](#case-1) | 에이전트와 코딩 작업 흐름 | 범위가 명확한 유지보수 작업으로 편집, 도구 사용, 검증을 함께 평가합니다. | Demo |
| [Canvas 앱 16개 병렬 구축](#case-2) | 에이전트와 코딩 작업 흐름 | 구축 작업을 독립 모듈로 나누고 계획, 구현, 품질 검증 역할을 명확히 합니다. | Demo |
| [여러 모델의 에이전트 군집으로 만든 진홍색 나방](#case-3) | 에이전트와 코딩 작업 흐름 | 인터랙티브 창작 코딩 프로젝트에서 조율과 구현 역할을 분리합니다. | Demo |
| [3D Medic 검사와 복구](#case-4) | 에이전트와 코딩 작업 흐름 | 3D 파일을 검사하고 오류를 찾아 내보내기 전에 복구를 제안하는 에이전트를 살펴봅니다. | Demo |
| [Devin에서 만든 범선 장면](#case-5) | 에이전트와 코딩 작업 흐름 | 실제로 사용할 코딩 에이전트 환경 안에서 모델을 평가합니다. | Demo |
| [Lingo City 언어 연습](#case-6) | 앱과 학습 | 학습 카드와 인터랙티브 거리 장면을 결합해 맥락 속에서 언어를 연습합니다. | Demo |
| [3D 종이 극장으로 배우는 로미오와 줄리엣](#case-7) | 앱과 학습 | 구체적인 수업을 명확한 학습 목표가 있는 인터랙티브 장면으로 바꿉니다. | Demo |
| [디자인 이미지에서 독서 웹사이트로](#case-8) | 앱과 학습 | 참고 디자인을 이용해 시각 이해와 작동하는 프런트엔드 구현을 평가합니다. | Demo |
| [20개 모듈로 만든 잉어 정원](#case-9) | 앱과 학습 | 한 번의 프롬프트로 완성을 기대하지 말고 작은 모듈로 큰 장면을 구축합니다. | Demo |
| [양성자 핵융합 학습 게임](#case-10) | 앱과 학습 | 과학적 과정을 설명하는 인터랙티브 시제품을 만든 뒤 과학적 내용을 확인합니다. | Demo |
| [Google Sheets의 움직이는 풍경](#case-11) | 스프레드시트와 검색 | 색다른 스프레드시트 애니메이션으로 생성 코드와 셀 단위 갱신을 살펴봅니다. | Demo |
| [Folio 인터랙티브 데이터 웹사이트](#case-12) | 스프레드시트와 검색 | 작은 웹 시제품에서 랜딩 페이지 구성과 인터랙티브 데이터 시각화를 결합합니다. | Demo |
| [여러 부분으로 된 검색 질문의 시각적 답변](#case-13) | 스프레드시트와 검색 | 섬세한 조건이 여러 개 있는 검색 요청에서 답변 구성과 인용 링크를 비교합니다. | Demo |
| [Sheets의 인터랙티브 재무 예측](#case-14) | 스프레드시트와 검색 | 가정을 명확히 표시하는 재무 모델 시제품을 만들고 생성된 수식과 차트를 확인합니다. | Demo |
| [인터랙티브 식당](#case-15) | 인터랙티브 3D와 UI | 정지 이미지만 보고 판단하지 말고 물체 상호작용, 조명, 상태 변화를 확인합니다. | Demo |
| [작은 세계를 담은 볼륨 슬라이더](#case-16) | 인터랙티브 3D와 UI | 익숙한 조작 요소 하나로 상호작용 설계와 움직이는 장면의 세부 묘사를 함께 시험합니다. | Demo |
| [Three.js로 만든 일본식 주택](#case-17) | 인터랙티브 3D와 UI | 정교한 3D 탐색 장면을 평가할 때 코드 생성 시간과 렌더링 시간을 구분합니다. | Demo |
| [자전거를 타는 3D 펠리컨](#case-18) | 인터랙티브 3D와 UI | 움직이는 캐릭터로 동작의 조화, 움직임, 장면 일관성을 확인합니다. | Demo |
| [계획을 먼저 주는 행성 시뮬레이터](#case-19) | 인터랙티브 3D와 UI | 복잡한 장면의 편집을 요청하기 전에 코딩 모델에 구체적인 계획을 제공합니다. | Demo |
| [Antigravity Swarm으로 만든 항구 섬](#case-20) | 인터랙티브 3D와 UI | 이동 가능한 작은 환경으로 여러 에이전트의 장면 구축 동작을 살펴봅니다. | Demo |
| [에펠탑 공중 섬](#case-21) | 인터랙티브 3D와 UI | 작은 랜드마크 장면으로 구도, 카메라 움직임, 모델 생성 코드를 평가합니다. | Demo |
| [비행 가능한 미래 도시](#case-22) | 인터랙티브 3D와 UI | 첫 출력을 완성본으로 가정하지 말고 절차적으로 생성한 세계에 후속 편집을 시험합니다. | Demo |
| [일출부터 밤까지의 수상 비행기](#case-23) | 인터랙티브 3D와 UI | 인터랙티브 3D 장면의 환경 조작과 조명 전환을 살펴봅니다. | Demo |
| [네온 스틱맨 애니메이션: Hydrogen과 Opus](#case-24) | 비교와 한계 | 실행 환경이 같다고 가정하지 말고 완성 애니메이션과 보고된 시간 및 비용을 비교합니다. | Evaluation |
| [로봇 작업과 스스로 알아챈 실수](#case-25) | 비교와 한계 | 로봇 평가에 작업 완료와 작은 실수의 인식을 포함합니다. | Evaluation |
| [자연어로 작동하는 실험실 작업 셀](#case-26) | 비교와 한계 | 도구 실행과 실패 처리를 벤치마크 대표 점수와 별도로 평가합니다. | Evaluation |
| [빙산과 예인선: Hydrogen과 Carbon](#case-27) | 비교와 한계 | 오래 걸리는 3D 구축을 비교할 때 추론 수준과 실행 환경 제한을 기록합니다. | Evaluation |
| [젤리 잉어 연못: Hydrogen과 Sonnet](#case-28) | 비교와 한계 | 벤치마크 순위로 모델을 선택하기 전에 구체적인 장면을 확인합니다. | Evaluation |
| [같은 프롬프트를 사용한 창작 코드 모음](#case-29) | 비교와 한계 | 다양한 시각 과제를 이용해 매력적인 출력 하나로 지나치게 일반화하지 않도록 합니다. | Evaluation |
| [Megamind 복셀: 비용과 품질의 반례](#case-30) | 비교와 한계 | 모델이 일관되게 저렴하거나 시각적으로 우수한지 평가할 때 실패 사례도 남깁니다. | Limit |
| [사계절을 지나는 저글링 사자](#case-31) | 비교와 한계 | 주변 인터페이스의 시각적 완성도뿐 아니라 요청한 움직임을 확인합니다. | Limit |
| [세 모델의 스틱맨 격투: 더 느리고 비싼 결과](#case-32) | 비교와 한계 | 모델이 광고하는 효율과 실제 작업 보고를 비교할 때 반례도 보존합니다. | Limit |
| [농장 자전거 장면: Hydrogen과 Flash](#case-33) | 비교와 한계 | 제작자가 보고한 완료 시간과 함께 움직임과 장면 품질을 비교합니다. | Evaluation |
| [탠덤 자전거를 타는 소녀와 고양이](#case-34) | 비교와 한계 | 서로 다른 코딩 실행 환경을 명시하면서 프롬프트 준수와 추가 세부 묘사를 비교합니다. | Evaluation |
| [네 모델이 만드는 Three.js 마리오 게임](#case-35) | 비교와 한계 | 같은 프롬프트의 게임 비교를 해석하기 전에 추론 설정의 차이를 기록합니다. | Evaluation |
| [세 Gemini 모델의 컨트롤러 그림](#case-36) | 비교와 한계 | 모델 계열의 서열을 가정하지 말고 과제별 퇴보와 개선을 찾습니다. | Evaluation |
| [앱과 Studio에서 달라지는 시각 답변](#case-37) | 비교와 한계 | 시각 결과에 의존하기 전에 사용할 제품 환경에서 같은 이미지를 시험합니다. | Limit |
| [로켓 발사 장면: Hydrogen과 Flash](#case-38) | 비교와 한계 | 보고된 구축 시간뿐 아니라 실제 발사 애니메이션도 비교합니다. | Evaluation |
| [네 가지 SVG 애니메이션 과제](#case-39) | 비교와 한계 | 여러 상호작용과 애니메이션 주제로 과제 간 일관성을 살펴봅니다. | Evaluation |
| [세 모델의 사바나 말 애니메이션](#case-40) | 비교와 한계 | 광범위한 비용 또는 품질 주장을 받아들이기 전에 움직임과 시각적 세부 묘사를 직접 확인합니다. | Evaluation |

<a id="agents"></a>
## ⚡ 에이전트와 코딩 작업 흐름

<a id="case-1"></a>
### 사례 1: [Antigravity에서 코드베이스 유지보수](https://x.com/antigravity/status/2120944334023389476) (작성자 [@antigravity](https://x.com/antigravity))

**범위가 명확한 유지보수 작업으로 편집, 도구 사용, 검증을 함께 평가합니다.**

Antigravity의 출시 시연은 Hydrogen이 코드베이스를 유지보수하는 모습을 보여줍니다. 플랫폼이 제작한 사례이며 독립적으로 재현한 엔지니어링 벤치마크가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-2"></a>
### 사례 2: [Canvas 앱 16개 병렬 구축](https://x.com/shengzheyao/status/2120944141559550409) (작성자 [@shengzheyao](https://x.com/shengzheyao))

**구축 작업을 독립 모듈로 나누고 계획, 구현, 품질 검증 역할을 명확히 합니다.**

Google DeepMind의 Antigravity CLI 제작자는 Carbon이 조정, 검증, 통합을 맡고 Hydrogen이 의존성 없는 canvas 미니 앱 16개를 구축했다고 설명합니다. 여러 모델을 사용하는 흐름이므로 결과를 Hydrogen만의 성과로 보아서는 안 됩니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-3"></a>
### 사례 3: [여러 모델의 에이전트 군집으로 만든 진홍색 나방](https://x.com/thtbee_/status/2120958666480513310) (작성자 [@thtbee_](https://x.com/thtbee_))

**인터랙티브 창작 코딩 프로젝트에서 조율과 구현 역할을 분리합니다.**

제작자는 Carbon이 Antigravity 군집을 조율하고 Hydrogen 작업 에이전트가 진홍색 나방 작품을 만들었다고 말합니다. 보고된 45분에는 여러 모델의 작업 흐름이 포함되며 독립적으로 시간을 측정하지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-4"></a>
### 사례 4: [3D Medic 검사와 복구](https://x.com/GoogleAI/status/2120940683233984862) (작성자 [@GoogleAI](https://x.com/GoogleAI))

**3D 파일을 검사하고 오류를 찾아 내보내기 전에 복구를 제안하는 에이전트를 살펴봅니다.**

Google AI의 3D Medic 시연은 AI Studio에서 만든 Managed Agent 앱을 사용합니다. 파일 복구 흐름을 보여주는 것이며 임의의 3D 자산을 올바르게 복구한다는 증거는 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-5"></a>
### 사례 5: [Devin에서 만든 범선 장면](https://x.com/Da7_Tech/status/2120967690722677144) (작성자 [@Da7_Tech](https://x.com/Da7_Tech))

**실제로 사용할 코딩 에이전트 환경 안에서 모델을 평가합니다.**

출처는 Devin 안에서 실행된 Hydrogen의 결과로 범선 장면을 소개합니다. 짧은 게시물에는 전체 프롬프트, 반복 이력, 재현 가능한 설정이 공개되지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

유형: Demo | 날짜: 2026-11-12

---


<a id="apps-learning"></a>
## 💻 앱과 학습

<a id="case-6"></a>
### 사례 6: [Lingo City 언어 연습](https://x.com/tulseedoshi/status/2121095754844713427) (작성자 [@tulseedoshi](https://x.com/tulseedoshi))

**학습 카드와 인터랙티브 거리 장면을 결합해 맥락 속에서 언어를 연습합니다.**

Tulsee Doshi는 맞춤형 2D·3D 학습 카드를 스트리밍하고 가상 도시에서 상점 주인과 대화를 연습하는 Google 사례를 공유합니다. 제공업체의 시연이며 독립적인 학습 성과 연구가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-7"></a>
### 사례 7: [3D 종이 극장으로 배우는 로미오와 줄리엣](https://x.com/techartist_/status/2120957446202253803) (작성자 [@techartist_](https://x.com/techartist_))

**구체적인 수업을 명확한 학습 목표가 있는 인터랙티브 장면으로 바꿉니다.**

제작자는 GCSE 영문학 수업을 위해 로미오와 줄리엣의 발코니 장면을 다룬 3D 종이 극장을 만들었습니다. 출처는 인터페이스를 시연하지만 학습 성과를 측정하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-8"></a>
### 사례 8: [디자인 이미지에서 독서 웹사이트로](https://x.com/thebuggeddev/status/2120952661046689992) (작성자 [@thebuggeddev](https://x.com/thebuggeddev))

**참고 디자인을 이용해 시각 이해와 작동하는 프런트엔드 구현을 평가합니다.**

제작자는 Hydrogen이 디자인 이미지를 작동하는 독서 관리 웹사이트로 바꾸는 데 5분 27초가 걸렸다고 말합니다. 시간과 완성도는 출처 측의 주장이며 이 모음에서는 독립적인 기능 테스트를 하지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-9"></a>
### 사례 9: [20개 모듈로 만든 잉어 정원](https://x.com/IamEmily2050/status/2120951069874532806) (작성자 [@IamEmily2050](https://x.com/IamEmily2050))

**한 번의 프롬프트로 완성을 기대하지 말고 작은 모듈로 큰 장면을 구축합니다.**

제작자는 Gemini 앱에서 프롬프트 20개로 모듈 20개를 만들었으며 각각 90–270초가 걸렸다고 보고합니다. 사전 이용 권한을 받았음을 밝혔으며 한 번에 생성한 결과가 아닌 반복형 사례입니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-10"></a>
### 사례 10: [양성자 핵융합 학습 게임](https://x.com/SidraMiconi/status/2120948703095820743) (작성자 [@SidraMiconi](https://x.com/SidraMiconi))

**과학적 과정을 설명하는 인터랙티브 시제품을 만든 뒤 과학적 내용을 확인합니다.**

제작자의 게임은 젊은 별 내부의 양성자–양성자 연쇄 반응을 따라갑니다. 프롬프트 1개, 실행 시간 78초, 약 $0.19라는 비용은 출처 측의 주장이며 독립적으로 재현한 결과가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

유형: Demo | 날짜: 2026-11-12

---


<a id="data-search"></a>
## 📊 스프레드시트와 검색

<a id="case-11"></a>
### 사례 11: [Google Sheets의 움직이는 풍경](https://x.com/Google/status/2121004369617485896) (작성자 [@Google](https://x.com/Google))

**색다른 스프레드시트 애니메이션으로 생성 코드와 셀 단위 갱신을 살펴봅니다.**

Google은 Antigravity에서 작성한 코드로 스프레드시트 셀에 해안 열차, 구름, 단풍을 그리는 모습을 보여줍니다. 공식 창작 시연이며 스프레드시트 성능 벤치마크가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-12"></a>
### 사례 12: [Folio 인터랙티브 데이터 웹사이트](https://x.com/vamsibatchuk/status/2120996342923436188) (작성자 [@vamsibatchuk](https://x.com/vamsibatchuk))

**작은 웹 시제품에서 랜딩 페이지 구성과 인터랙티브 데이터 시각화를 결합합니다.**

Google DeepMind 직원은 Google AI Studio로 만든 Folio 스타일 웹사이트와 인터랙티브 애니메이션을 소개합니다. 전체 생성 프롬프트나 독립적인 기능 테스트는 제공하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-13"></a>
### 사례 13: [여러 부분으로 된 검색 질문의 시각적 답변](https://x.com/Google/status/2120960715011883148) (작성자 [@Google](https://x.com/Google))

**섬세한 조건이 여러 개 있는 검색 요청에서 답변 구성과 인용 링크를 비교합니다.**

Google 검색 사례는 의도 이해, 시각적 배치, 비교표, 쿼리 확장을 결합합니다. 제공업체가 설명한 제품 동작이며 게시자의 검색 순위나 방문량에 미치는 영향을 입증하지는 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-14"></a>
### 사례 14: [Sheets의 인터랙티브 재무 예측](https://x.com/ChanduThota/status/2120942270627414079) (작성자 [@ChanduThota](https://x.com/ChanduThota))

**가정을 명확히 표시하는 재무 모델 시제품을 만들고 생성된 수식과 차트를 확인합니다.**

Chandu Thota는 Google Sheets 예측 시연을 소개합니다. canvas 생성이 30% 넘게 빨라졌다는 출처의 설명은 제공업체의 주장이지 이 저장소에서 수행한 통제된 시간 측정이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

유형: Demo | 날짜: 2026-11-12

---


<a id="interactive-3d"></a>
## 🎮 인터랙티브 3D와 UI

<a id="case-15"></a>
### 사례 15: [인터랙티브 식당](https://x.com/notjazii/status/2120979811569222137) (작성자 [@notjazii](https://x.com/notjazii))

**정지 이미지만 보고 판단하지 말고 물체 상호작용, 조명, 상태 변화를 확인합니다.**

제작자는 조명, 램프, 냉장고와 내부 물건을 조작할 수 있는 식당을 보여줍니다. 보고된 제작 시간 30분은 독립적으로 검증되지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-16"></a>
### 사례 16: [작은 세계를 담은 볼륨 슬라이더](https://x.com/vib3coded/status/2120973294090555890) (작성자 [@vib3coded](https://x.com/vib3coded))

**익숙한 조작 요소 하나로 상호작용 설계와 움직이는 장면의 세부 묘사를 함께 시험합니다.**

출처는 작은 일본풍 세계가 움직이는 볼륨 슬라이더를 보여줍니다. 제작자는 비용을 $0.19로 보고하지만 청구서나 전체 생성 흐름을 제공하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-17"></a>
### 사례 17: [Three.js로 만든 일본식 주택](https://x.com/SPAC89/status/2120972954146140409) (작성자 [@SPAC89](https://x.com/SPAC89))

**정교한 3D 탐색 장면을 평가할 때 코드 생성 시간과 렌더링 시간을 구분합니다.**

제작자는 에이전트 없이 Hydrogen이 Three.js로 주택과 정원을 만들었다고 설명합니다. 구독 사용량과 두 시간 미만이라는 설명은 해당 제작자의 환경에 한정되며 일반적인 가격이나 지연 시간 보장이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-18"></a>
### 사례 18: [자전거를 타는 3D 펠리컨](https://x.com/nehstrr3/status/2120953932692537722) (작성자 [@nehstrr3](https://x.com/nehstrr3))

**움직이는 캐릭터로 동작의 조화, 움직임, 장면 일관성을 확인합니다.**

제작자는 자전거를 타는 3D 애니메이션 펠리컨을 소개하며 모델을 Hydrogen XHigh로 표시합니다. 출력 시연이지 완전히 재현 가능한 프롬프트나 물리 검증이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-19"></a>
### 사례 19: [계획을 먼저 주는 행성 시뮬레이터](https://x.com/The_Alex/status/2120950301318582643) (작성자 [@The_Alex](https://x.com/The_Alex))

**복잡한 장면의 편집을 요청하기 전에 코딩 모델에 구체적인 계획을 제공합니다.**

사전 이용 제작자는 행성 시뮬레이터를 보여주며 더 상세한 계획을 주자 편집 결과가 나아졌다고 보고합니다. 아이디어 출처를 ForwardEditor로 밝히고 반복형 작업 흐름을 설명합니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-20"></a>
### 사례 20: [Antigravity Swarm으로 만든 항구 섬](https://x.com/ai_for_success/status/2120942147780464660) (작성자 [@ai_for_success](https://x.com/ai_for_success))

**이동 가능한 작은 환경으로 여러 에이전트의 장면 구축 동작을 살펴봅니다.**

제작자는 사전 이용 권한을 공개하고 Antigravity의 Swarm 기능에서 Hydrogen으로 만든 항구 섬을 보여줍니다. 공개 게시물에는 전체 조율 방식이나 프롬프트 이력이 명시되지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-21"></a>
### 사례 21: [에펠탑 공중 섬](https://x.com/RezAIT00/status/2120940988780736973) (작성자 [@RezAIT00](https://x.com/RezAIT00))

**작은 랜드마크 장면으로 구도, 카메라 움직임, 모델 생성 코드를 평가합니다.**

출처는 에펠탑 미니어처 섬을 보여주며 Hydrogen XHigh의 결과라고 설명합니다. 제작과 녹화가 6분이라는 설명은 작성자의 보고이지 독립적인 시간 측정이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-22"></a>
### 사례 22: [비행 가능한 미래 도시](https://x.com/kimmonismus/status/2120940617169826037) (작성자 [@kimmonismus](https://x.com/kimmonismus))

**첫 출력을 완성본으로 가정하지 말고 절차적으로 생성한 세계에 후속 편집을 시험합니다.**

사전 이용 제작자는 Antigravity에서 Hydrogen High를 사용해 후속 지시 한 번으로 절차적 고층 건물, 비, 비행 교통이 있는 Three.js 도시를 만들었다고 보고합니다. 녹화는 생성 코드의 실행을 보여주며 네이티브 영상 생성이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-23"></a>
### 사례 23: [일출부터 밤까지의 수상 비행기](https://x.com/LuminaBench/status/2120939312564842663) (작성자 [@LuminaBench](https://x.com/LuminaBench))

**인터랙티브 3D 장면의 환경 조작과 조명 전환을 살펴봅니다.**

LuminaBench의 원본 시연은 수상 비행기와 시간대 변화를 보여주며 이후 Google이 다시 공유했습니다. 게시물은 기록된 일반 공개 시점보다 앞서며 이용 경로와 모델 호출은 독립적으로 확인되지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

유형: Demo | 날짜: 2026-11-12

---


<a id="comparisons-limits"></a>
## 🧪 비교와 한계

<a id="case-24"></a>
### 사례 24: [네온 스틱맨 애니메이션: Hydrogen과 Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (작성자 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**실행 환경이 같다고 가정하지 말고 완성 애니메이션과 보고된 시간 및 비용을 비교합니다.**

작성자는 Hydrogen과 Opus 5.5 출력을 소개하며 비용을 $1.02 대 $7.43, 시간을 10분 22초 대 34분으로 보고합니다. 이 모음은 청구 내역, 프롬프트, 반복 횟수, 실행 설정의 동등성을 검증하지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-25"></a>
### 사례 25: [로봇 작업과 스스로 알아챈 실수](https://x.com/ArtificialAnlys/status/2120995180891508833) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**로봇 평가에 작업 완료와 작은 실수의 인식을 포함합니다.**

Artificial Analysis는 붓기와 블록 정리 작업을 보여주며 Hydrogen이 약간의 흘림과 닫히지 않은 뚜껑을 알아챘다고 말합니다. 영상과 AA-Robotics v0.1 순위는 평가자가 제공한 것으로 여기서 독립적으로 재현한 것이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-26"></a>
### 사례 26: [자연어로 작동하는 실험실 작업 셀](https://x.com/danielmckinn0n/status/2120990834246173125) (작성자 [@danielmckinn0n](https://x.com/danielmckinn0n))

**도구 실행과 실패 처리를 벤치마크 대표 점수와 별도로 평가합니다.**

출처는 자연어 요청으로 움직이는 실험실 작업 셀을 보여주고 실험실 관련 벤치마크 네 가지의 결과를 보고합니다. Hydrogen의 보고된 RareBench 점수는 Opus 5.5보다 낮고 나머지 세 점수는 높습니다. 벤치마크 소유자의 시연이며 의학적 검증이 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-27"></a>
### 사례 27: [빙산과 예인선: Hydrogen과 Carbon](https://x.com/EnvolDev/status/2120989670582677930) (작성자 [@EnvolDev](https://x.com/EnvolDev))

**오래 걸리는 3D 구축을 비교할 때 추론 수준과 실행 환경 제한을 기록합니다.**

제작자는 두 모델을 OpenRouter에서 High로 실행했다고 보고하며 Hydrogen은 $4.27과 1시간 23분 40초, Carbon은 $8.83과 2시간 39분 10초였다고 설명합니다. 통제되지 않은 출처 측 보고이며 보편적인 가격비나 속도비가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-28"></a>
### 사례 28: [젤리 잉어 연못: Hydrogen과 Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (작성자 [@Haleeeemahh](https://x.com/Haleeeemahh))

**벤치마크 순위로 모델을 선택하기 전에 구체적인 장면을 확인합니다.**

작성자는 3D 잉어 연못 과제에서 Hydrogen과 Sonnet 5.5를 비교합니다. 시청자에게 출력을 판단하도록 요청하지만 동일한 설정이나 객관적인 품질 점수를 확립하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-29"></a>
### 사례 29: [같은 프롬프트를 사용한 창작 코드 모음](https://x.com/kickingkeys/status/2120985358317875222) (작성자 [@kickingkeys](https://x.com/kickingkeys))

**다양한 시각 과제를 이용해 매력적인 출력 하나로 지나치게 일반화하지 않도록 합니다.**

제작자는 Hydrogen, Carbon, Argon에 동일한 프롬프트를 주고 답글에 비교를 게시했다고 말합니다. 원 게시물의 자료는 로우폴리 동물, 네온 거리, 수채화풍 용기를 보여주며 완전한 통제 벤치마크가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-30"></a>
### 사례 30: [Megamind 복셀: 비용과 품질의 반례](https://x.com/thehypedotnews/status/2120980737012670720) (작성자 [@thehypedotnews](https://x.com/thehypedotnews))

**모델이 일관되게 저렴하거나 시각적으로 우수한지 평가할 때 실패 사례도 남깁니다.**

출처는 Hydrogen이 덜 일관된 Titan 형상을 만들면서 $36.07을 사용했고 Sonnet 5.5는 $8.64였다고 설명합니다. 게시물에는 상업 홍보가 포함되며 비용과 품질 판단은 게시자의 주장입니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

유형: Limit | 날짜: 2026-11-12

---

<a id="case-31"></a>
### 사례 31: [사계절을 지나는 저글링 사자](https://x.com/SahilPanhotra/status/2120978349967458704) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**주변 인터페이스의 시각적 완성도뿐 아니라 요청한 움직임을 확인합니다.**

작성자는 Carbon이 교차하는 저글링 궤적을 처리한 반면 Hydrogen은 계절 전환과 클리핑이 더 깔끔했음에도 공을 공중에 띄운 채 두었다고 보고합니다. 동일 과제의 SVG 비교는 특정 움직임 실패를 보여주며 종합 모델 순위가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

유형: Limit | 날짜: 2026-11-12

---

<a id="case-32"></a>
### 사례 32: [세 모델의 스틱맨 격투: 더 느리고 비싼 결과](https://x.com/DanielZambrini/status/2120963180461769183) (작성자 [@DanielZambrini](https://x.com/DanielZambrini))

**모델이 광고하는 효율과 실제 작업 보고를 비교할 때 반례도 보존합니다.**

제작자는 Hydrogen, Carbon, Argon을 비교하며 이 테스트에서는 Hydrogen이 Carbon보다 오래 걸리고 비용도 높았다고 보고합니다. 설정, 청구, 반복 횟수는 독립적으로 검증되지 않았습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

유형: Limit | 날짜: 2026-11-12

---

<a id="case-33"></a>
### 사례 33: [농장 자전거 장면: Hydrogen과 Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (작성자 [@Bhavani_00007](https://x.com/Bhavani_00007))

**제작자가 보고한 완료 시간과 함께 움직임과 장면 품질을 비교합니다.**

출처는 농장 자전거 장면에서 Hydrogen과 Gemini 3.8 Flash를 비교하며 56초 대 6분 초과라고 보고합니다. 한 제작자의 테스트이며 일반적인 속도 벤치마크가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-34"></a>
### 사례 34: [탠덤 자전거를 타는 소녀와 고양이](https://x.com/marcthecreatorr/status/2120956699951628637) (작성자 [@marcthecreatorr](https://x.com/marcthecreatorr))

**서로 다른 코딩 실행 환경을 명시하면서 프롬프트 준수와 추가 세부 묘사를 비교합니다.**

제작자는 같다고 밝힌 SVG 과제를 사용했지만 Opus 5.5는 Claude Code에서, Hydrogen은 Cursor에서 실행했습니다. 보고된 시간과 비용은 크게 다르지만 실행 환경 차이와 공개되지 않은 반복 때문에 모델만을 통제한 비교는 불가능합니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-35"></a>
### 사례 35: [네 모델이 만드는 Three.js 마리오 게임](https://x.com/StatsWire/status/2120955723396071548) (작성자 [@StatsWire](https://x.com/StatsWire))

**같은 프롬프트의 게임 비교를 해석하기 전에 추론 설정의 차이를 기록합니다.**

출처는 High의 Gemini 3.8 Flash, Argon, Carbon과 XHigh의 Hydrogen을 비교하며 외부 3D 모델이나 텍스처 없이 순수 Three.js를 사용합니다. 네 출력을 보여주는 것이지 추론 조건을 맞춘 벤치마크는 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-36"></a>
### 사례 36: [세 Gemini 모델의 컨트롤러 그림](https://x.com/notjazii/status/2120952314873987271) (작성자 [@notjazii](https://x.com/notjazii))

**모델 계열의 서열을 가정하지 말고 과제별 퇴보와 개선을 찾습니다.**

제작자는 Carbon, Argon, Hydrogen의 컨트롤러 SVG 출력을 비교하고 테스트를 다시 실행했다고 보고합니다. 시간과 비용은 출처 측의 주장으로 모델 품질의 일반적인 순서를 확립하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-37"></a>
### 사례 37: [앱과 Studio에서 달라지는 시각 답변](https://x.com/thegenioo/status/2120946497802174688) (작성자 [@thegenioo](https://x.com/thegenioo))

**시각 결과에 의존하기 전에 사용할 제품 환경에서 같은 이미지를 시험합니다.**

출처는 Gemini 앱과 AI Studio의 Hydrogen이 내놓았다고 하는 서로 모순되는 음식 식별 답변을 보여줍니다. 동일한 라우팅, 설정, 전체 대화 맥락인지는 독립적으로 검증하지 않습니다.

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

유형: Limit | 날짜: 2026-11-12

---

<a id="case-38"></a>
### 사례 38: [로켓 발사 장면: Hydrogen과 Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (작성자 [@Bhavani_00007](https://x.com/Bhavani_00007))

**보고된 구축 시간뿐 아니라 실제 발사 애니메이션도 비교합니다.**

제작자는 Hydrogen과 Gemini 3.8 Flash 출력을 소개하며 1분 미만 대 약 3분이라고 보고합니다. 단일 과제의 시각 비교이며 독립적으로 통제된 실행 설정은 없습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-39"></a>
### 사례 39: [네 가지 SVG 애니메이션 과제](https://x.com/Angaisb_/status/2120944947193127061) (작성자 [@Angaisb_](https://x.com/Angaisb_))

**여러 상호작용과 애니메이션 주제로 과제 간 일관성을 살펴봅니다.**

출처는 전달, 낮과 밤의 변화, 개봉, 카멜레온 과제에서 Hydrogen과 Carbon 출력을 짝지어 보여줍니다. 짧은 원문은 전체 프롬프트, 시간 측정 증거, 객관적인 채점 방법을 공개하지 않습니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-40"></a>
### 사례 40: [세 모델의 사바나 말 애니메이션](https://x.com/AI_Screening/status/2120944276586823689) (작성자 [@AI_Screening](https://x.com/AI_Screening))

**광범위한 비용 또는 품질 주장을 받아들이기 전에 움직임과 시각적 세부 묘사를 직접 확인합니다.**

제작자는 Hydrogen, Carbon, Argon의 사바나 말 장면을 소개합니다. 더 빠른 속도, 더 낮은 비용, 높은 품질이라는 주장은 출처 측의 평가이며 여기서 재현한 통제 비교가 아닙니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="related-repositories"></a>
## 관련 저장소

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon 사례와 비교

<a id="acknowledge"></a>
## 🙏 감사의 말

Hydrogen 작업물을 공개한 제작자, 개발자, 평가자 여러분께 감사드립니다.

**출처 제작자:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening)

*귀속은 인용한 공개 출처를 따르며 최초 제작자를 식별하지 못할 수 있습니다. 수정 또는 삭제를 요청하려면 공개 출처를 첨부하여 issue를 작성하세요.*

기여 체크리스트에 따라 issue 또는 pull request로 출처가 있는 사례를 제안하세요.
