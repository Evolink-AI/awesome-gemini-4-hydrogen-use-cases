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

**225개 사례에서 Hydrogen 활용 방법과 결과의 한계를 확인할 수 있습니다.**

각 사례에는 출처 링크와 작성자가 표시됩니다. 시연, 제공업체 사례, 제작자 비교는 설명에 구분하며, 공개되지 않은 프롬프트를 재구성하지 않습니다.

## 📊 개요

- 전체 225개 중 185개는 X 게시물 1,304개를 검토한 11월 17일 업데이트에서 추가했습니다. 새 글은 수집 당시 좋아요가 30개를 넘었습니다.
- 에이전트, 학습과 앱, 스프레드시트와 검색, 인터랙티브 3D, 비교와 한계의 다섯 분야를 다룹니다.
- 원본 시각 자료 264개를 제공합니다. 미리보기 이미지가 있는 재생 가능한 동영상 168개와 이미지 96개입니다.
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
| [⚡ 에이전트와 코딩 작업 흐름](#agents) | 30 |
| [💻 앱과 학습](#apps-learning) | 37 |
| [📊 스프레드시트와 검색](#data-search) | 9 |
| [🎮 인터랙티브 3D와 UI](#interactive-3d) | 48 |
| [🧪 비교와 한계](#comparisons-limits) | 101 |
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
| [우주 참고 이미지를 HTML 장면으로](#case-41) | 인터랙티브 3D와 UI | 소수의 참고 이미지로 특징적인 화풍을 재현하는지 확인한다. | Demo |
| [Gemini Canvas에서 만든 F1 차량 시제품](#case-42) | 인터랙티브 3D와 UI | 차량 뷰어에 여러 카메라를 두고 다양한 각도에서 모델을 확인한다. | Demo |
| [Hydrogen API와 Antigravity의 Carbon 비교](#case-43) | 비교와 한계 | 같은 프롬프트로 만든 결과를 비교할 때 각 실행 환경을 기록한다. | Evaluation |
| [Hydrogen과 Astra의 그림자 표현](#case-44) | 비교와 한계 | 두 실행의 비용과 시간을 비교하면서 세부 묘사도 살펴본다. | Evaluation |
| [절차적 3D 모션 비교](#case-45) | 비교와 한계 | 장면의 움직임과 구도를 비교하면서 생성 시간을 기록한다. | Evaluation |
| [PokéBench 비전 테스트 89분](#case-46) | 비교와 한계 | 장시간 비전 에이전트를 테스트할 때 과제 완료 여부, 턴 수, API 실패 횟수를 기록한다. | Benchmark |
| [Hydrogen과 DeepSeek로 같은 3D 장면 제작](#case-47) | 비교와 한계 | 시각적 결과를 비교하고 실행 시간과 API 비용은 따로 기록한다. | Evaluation |
| [SVG로 그린 BMW 옆모습](#case-48) | 인터랙티브 3D와 UI | 차량의 SVG 측면도에서 비율, 윤곽, 작은 디테일을 살핀다. | Demo |
| [천문학자의 공중 섬](#case-49) | 인터랙티브 3D와 UI | 작은 장면에 뚜렷한 주제를 정해 소품과 조명이 이를 뒷받침하는지 확인한다. | Demo |
| [참고 이미지로 걸어 다닐 수 있는 3D 풍경 제작](#case-50) | 인터랙티브 3D와 UI | 이미지를 바탕으로 만든 장면에서 외관의 재현과 이동 기능을 확인한다. | Demo |
| [3D 블록으로 만든 미니어처 풍경](#case-51) | 인터랙티브 3D와 UI | 블록으로 소형 풍경을 만들게 하고 각 모양이 하나의 장면으로 읽히는지 살핀다. | Demo |
| [조작 가능한 벚나무](#case-52) | 인터랙티브 3D와 UI | 움직이는 물체와 몇 가지 조작 요소로 실시간 변화를 살펴본다. | Demo |
| [Agent Arena의 과제당 시간과 비용](#case-53) | 비교와 한계 | 전체 성공률과 함께 과제별 지연, 비용, 출력 토큰을 확인한다. | Benchmark |
| [시각 문서와 터미널 벤치마크](#case-54) | 비교와 한계 | 추론 예산을 고를 때 문서와 터미널 결과를 따로 본다. | Benchmark |
| [Vals Index와 Tax Agent 결과](#case-55) | 비교와 한계 | 종합 평가와 함께 전문 과제 점수를 확인한다. | Benchmark |
| [CursorBench의 기본 추론 설정](#case-56) | 비교와 한계 | 기본 설정 점수를 출발점으로 삼아 자신의 저장소에서 시험한다. | Benchmark |
| [네 모델의 궁수 전투 애니메이션](#case-57) | 비교와 한계 | 각 애니메이션에서 인물의 전투 행동이 얼마나 분명한지 비교한다. | Evaluation |
| [15분 만에 만든 Minecraft풍 시제품](#case-58) | 앱과 학습 | 복셀 샌드박스에서 채굴과 인벤토리 등 여러 기능이 맞물리는지 확인한다. | Demo |
| [n8n에서 Hydrogen으로 도구 호출하기](#case-59) | 에이전트와 코딩 작업 흐름 | 반복적인 도구 사용을 Hydrogen에 맡기고 계획은 별도 단계로 둔다. | Integration |
| [Box Agent로 복잡한 기업 문서 처리](#case-60) | 스프레드시트와 검색 | 실제와 비슷한 문서 작업에서 정확도, 시간, 토큰 사용량을 확인한다. | Benchmark |
| [Devin FrontierCode의 Hydrogen](#case-61) | 비교와 한계 | 후보 패치를 병합할 수 있는지 살피고 에이전트 실행 환경을 기록한다. | Benchmark |
| [작은 인터랙티브 애니메이션의 굴절](#case-62) | 인터랙티브 3D와 UI | 짧은 미리 보기로 굴절 효과를 조정한 뒤 장면을 확장한다. | Demo |
| [위쪽으로 흐르는 강](#case-63) | 인터랙티브 3D와 UI | 흐름 방향을 바꾼 작은 장면으로 시각 효과를 확인한다. | Demo |
| [검색을 금지해도 실행된 웹 검색](#case-64) | 비교와 한계 | 검색 없이 답해야 하는 작업에서는 도구 호출 기록을 확인한다. | Limit |
| [Antigravity Swarm의 사용량 기록](#case-65) | 비교와 한계 | 멀티에이전트 실행의 토큰 수와 소진한 한도를 기록한다. | Evaluation |
| [전문 업무 평가의 도구 호출](#case-66) | 비교와 한계 | 에이전트가 전문 과제를 수행하기 전에 정보를 어떻게 모으는지 살핀다. | Benchmark |
| [Hydrogen으로 만든 3D 초상](#case-67) | 인터랙티브 3D와 UI | 인지 가능한 인물 특징이 3D에 드러나는지 작은 초상 과제로 확인한다. | Demo |
| [네 모델의 마법사와 용 전투](#case-68) | 비교와 한계 | 같은 판타지 장면에서 연출, 동작의 명료함, 효과를 비교한다. | Evaluation |
| [멀티에이전트 환경의 인증 경로](#case-69) | 에이전트와 코딩 작업 흐름 | 다른 제공업체에 과제를 위임할 때 실제로 어느 클라이언트가 인증하는지 확인한다. | Limit |
| [Antigravity Goal Mode 실행](#case-70) | 에이전트와 코딩 작업 흐름 | 장시간 코딩 세션의 계획, 코드 변경, 테스트 결과를 추적한다. | Demo |
| [MazeBench에서 나타난 낮은 성공률](#case-71) | 비교와 한계 | 공간 추론을 활용하기 전에 미로 과제로 시험한다. | Benchmark |
| [Gemini 모델 세 종류의 범선 장면](#case-72) | 비교와 한계 | 같은 Three.js 주제에서 움직임과 환경의 세부 표현을 비교한다. | Evaluation |
| [Antigravity Orchestrator의 Carbon과 Hydrogen](#case-73) | 에이전트와 코딩 작업 흐름 | 빠른 구현 모델이 막히면 계획 모델에서 문제를 다시 검토한다. | Integration |
| [Workspace 데이터에서 차트와 보고서 생성](#case-74) | 스프레드시트와 검색 | 후속 요청으로 누락된 분석, 차트, 보고서를 보완할 수 있는지 확인한다. | Demo |
| [등번호를 읽다가 추론 예산 소진](#case-75) | 비교와 한계 | 이미지 속 작은 세부 정보를 읽을 때 추론 한도와 대체 수단을 설정한다. | Limit |
| [모델 계열별 ClutterBench 성능](#case-76) | 비교와 한계 | 복잡하게 섞인 장면의 전용 평가에서 모델 계열의 강점이 이어지는지 확인한다. | Benchmark |
| [뉴스 브리핑을 내레이션 영상으로](#case-77) | 앱과 학습 | 조사한 브리핑을 짧은 영상으로 바꾸고 제시된 사실을 확인한다. | Demo |
| [Minecraft풍 인체 단면 흉상](#case-78) | 비교와 한계 | 생성한 단면에 요청한 내부 구조가 들어 있는지 확인한다. | Evaluation |
| [세 모델이 같은 소품을 렌더링](#case-79) | 비교와 한계 | 단가가 낮은 모델이 과제에서 사용하는 토큰을 품질과 별도로 기록한다. | Evaluation |
| [귀납 추론 벤치마크와 토큰 사용량](#case-80) | 비교와 한계 | 어려운 추론 과제에서는 점수와 청구 입력·출력 토큰을 함께 기록한다. | Benchmark |
| [Gemini 모드별 스프레드시트 픽셀 아트](#case-81) | 스프레드시트와 검색 | 같은 Google 스프레드시트 그림 과제로 여러 모델 설정을 비교한다. | Evaluation |
| [참고 이미지 속 아파트를 3D 프린트](#case-82) | 인터랙티브 3D와 UI | 이미지에서 3D를 생성하는 시험을 실제 출력까지 진행한다. | Demo |
| [세 모델이 3D 동물을 애니메이션으로 제작](#case-83) | 비교와 한계 | 같은 3D 동물 모델링 과제에서 몸 구조와 동작을 살핀다. | Evaluation |
| [ts-bench의 Hydrogen과 Qwen](#case-84) | 비교와 한계 | 종합 결과와 함께 도구 호출 오류를 확인한다. | Benchmark |
| [Vending-Bench 사업 시뮬레이션](#case-85) | 비교와 한계 | 모의 매출과 에이전트 운영 비용을 함께 비교한다. | Benchmark |
| [고잉 메리호의 바다 장면](#case-86) | 인터랙티브 3D와 UI | 잘 알려진 가상 선박을 소재로 바다 장면의 구도를 확인한다. | Demo |
| [OpenClaw에서 Hydrogen 사용](#case-87) | 에이전트와 코딩 작업 흐름 | 사용할 에이전트 프레임워크에서 모델을 선택할 수 있는지 확인한다. | Integration |
| [구름 바다를 헤엄치는 고래](#case-88) | 인터랙티브 3D와 UI | 코드로 만든 생물 장면에서 유체의 움직임과 눈 디자인을 따로 본다. | Demo |
| [네 모델이 만든 미니어처 섬](#case-89) | 비교와 한계 | 섬의 디자인과 각 환경에서의 시간 및 비용을 비교한다. | Evaluation |
| [웹캠으로 공중에 그리는 도구](#case-90) | 앱과 학습 | 공중에서 선을 그려 인터페이스가 입력을 따라가는지 시험한다. | Demo |
| [코드로 표현한 천 찢김 비교](#case-91) | 비교와 한계 | 같은 애니메이션 과제에서 천의 늘어남, 찢어짐, 털과의 상호 작용을 확인한다. | Evaluation |
| [Gemini Canvas의 해저 도시](#case-92) | 인터랙티브 3D와 UI | 작은 3D 장면에서 시작해 돌아다닐 공간과 움직이는 생물을 여러 차례에 걸쳐 추가한다. | Demo |
| [한 번에 생성한 웹 포털](#case-93) | 앱과 학습 | 개별 동작을 테스트하기 전에 첫 번째 포털 화면의 레이아웃을 확인한다. | Demo |
| [출처를 확인할 수 없는 사실 검증](#case-94) | 비교와 한계 | 스크린샷의 진위를 판단하기 전에 확인할 수 있는 인용 출처를 요청한다. | Limit |
| [Cities: Skylines풍 도시 건설 도구](#case-95) | 앱과 학습 | 도시 건설 시제품을 만들어 조작 방식과 시뮬레이션이 어떻게 맞물리는지 본다. | Demo |
| [Hydrogen과 Sol의 2D 펠리컨](#case-96) | 비교와 한계 | 같은 간단한 2D 과제로 제작 시간과 움직임을 비교한다. | Evaluation |
| [Blender MCP로 만든 왕좌의 방](#case-97) | 에이전트와 코딩 작업 흐름 | Blender MCP를 사용해 편집기 안에서 생성한 장면의 구도를 확인한다. | Integration |
| [네 모델의 거미줄 이동 게임](#case-98) | 비교와 한계 | 같은 단일 파일 제약을 두고 이동과 조작을 비교한다. | Evaluation |
| [Three.js로 만든 회색조 해적선](#case-99) | 인터랙티브 3D와 UI | 색을 회색조로 제한하고도 조명이 입체 형태를 드러내는지 확인한다. | Demo |
| [네 모델의 건물 디오라마](#case-100) | 비교와 한계 | 같은 건축 프롬프트를 쓰고 모델마다 조명을 어떻게 표현하는지 살핀다. | Evaluation |
| [CadXStudio의 파라메트릭 탁상 조명](#case-101) | 인터랙티브 3D와 UI | 생성한 CAD 모델에서 부품 치수와 편집 가능 여부를 확인한다. | Integration |
| [C++로 만든 신사 참배로 애니메이션](#case-102) | 인터랙티브 3D와 UI | 작은 네이티브 코드 장면으로 웹 기술 없이 작동하는 애니메이션을 작성할 수 있는지 테스트한다. | Demo |
| [세 모델의 기차 장면](#case-103) | 비교와 한계 | 같은 기차 장면 과제로 각 설정에서의 완성 시간을 비교한다. | Evaluation |
| [Extra로 애니메이션화한 비 오는 차이나타운](#case-104) | 비교와 한계 | 대형 애니메이션의 추론 모드를 고르기 전에 시간과 최종 장면을 확인한다. | Evaluation |
| [30개 모듈로 만든 마을](#case-105) | 인터랙티브 3D와 UI | 프롬프트를 모듈별로 나눠 장면을 만든 다음 조립 결과를 검토한다. | Demo |
| [세 모델의 행성 시각화](#case-106) | 비교와 한계 | 같은 프롬프트로 과학 시각화 인터페이스를 만들고 모델별 출력을 비교한다. | Evaluation |
| [네 모델이 재현한 Chrome 공룡 게임](#case-107) | 비교와 한계 | 익숙한 게임을 재현하는 시간을 측정하고 직접 플레이하는 결과를 비교한다. | Evaluation |
| [공중 섬의 우체국](#case-108) | 인터랙티브 3D와 UI | 미니어처 건물을 지정하고 재질과 조명이 장면을 어떻게 만드는지 살핀다. | Demo |
| [두 코딩 에이전트가 만든 배](#case-109) | 비교와 한계 | 실제 사용할 환경에서 첫 번째 사용 가능한 출력과 수정 부담을 비교한다. | Evaluation |
| [잉어가 헤엄치는 안뜰](#case-110) | 인터랙티브 3D와 UI | 물고기가 움직일 때 수면 반사와 조명이 자연스럽게 유지되는지 본다. | Demo |
| [네 모델의 강체 투석기 공성 장면](#case-111) | 비교와 한계 | 같은 과제로 조작 가능한 물리 시제품을 비교하고 추론 설정을 기록한다. | Evaluation |
| [Gemini 앱에서 실행되는 3D 장면](#case-112) | 인터랙티브 3D와 UI | 웹 Gemini에서 상호 작용할 수 있는 조명과 입자 효과를 만들어 본다. | Demo |
| [브라우저 CAD의 콘크리트 믹서 조립체](#case-113) | 에이전트와 코딩 작업 흐름 | 생성한 조립체를 CAD 작업에 쓰기 전에 부품 트리와 맞물림을 점검한다. | Integration |
| [Blender에서 절차적으로 도끼 만들기](#case-114) | 에이전트와 코딩 작업 흐름 | 윤곽 참고 이미지와 뷰포트 점검으로 절차적으로 만든 Blender 에셋을 확인한다. | Integration |
| [한 HTML 파일에 담은 분홍색 3D 장면](#case-115) | 인터랙티브 3D와 UI | 외부 에셋 없이 Three.js만 사용해 구도가 명확한지 확인한다. | Demo |
| [FrontierMemory의 장기 기억 평가](#case-116) | 비교와 한계 | 오래 작동하는 에이전트의 기억 모델을 고를 때 점수와 실행당 비용을 함께 본다. | Benchmark |
| [고장 낸 LiveKit 음성 에이전트의 Hydrogen](#case-117) | 비교와 한계 | 도구에 통제된 실패를 일으켜 음성 에이전트가 근거 없는 결과를 보고하는지 확인한다. | Evaluation |
| [28개 모듈로 만든 Ember Isle](#case-118) | 에이전트와 코딩 작업 흐름 | 큰 장면을 모듈로 나누고 각 생성에 걸린 시간을 기록한다. | Demo |
| [코드만으로 만든 빅뱅 시뮬레이션](#case-119) | 인터랙티브 3D와 UI | 짧은 애니메이션으로 설명 시제품을 만들고 과학적 표현을 확인한다. | Demo |
| [조립 및 분해 보기가 있는 헬리콥터](#case-120) | 인터랙티브 3D와 UI | 비행 조작과 부품 검사 보기가 3D 시제품에서 연결되는지 확인한다. | Demo |
| [X선 및 와이어프레임을 갖춘 Hydrogen Express](#case-121) | 인터랙티브 3D와 UI | 조작할 수 있는 3D 시제품에 여러 검사 모드를 추가한다. | Demo |
| [하늘에 떠 있는 주유소](#case-122) | 인터랙티브 3D와 UI | 서로 다른 움직이는 요소와 조명 상태로 시연에서 변화가 보이게 한다. | Demo |
| [Gemini 세 모델의 자전거 동작](#case-123) | 비교와 한계 | 같은 지시로 만든 짧은 움직임을 비교하고 각 실행 시간을 기록한다. | Evaluation |
| [화학 교과서를 인터랙티브 학습 자료로](#case-124) | 앱과 학습 | 힌트, 음성, 선택적으로 표시하는 텍스트를 조합해 자습 자료를 만든다. | Demo |
| [Vocaloid 노래 시제품](#case-125) | 앱과 학습 | 한 번에 만든 곡이 캐릭터와 스타일 요구를 충족하는지 살핀다. | Demo |
| [두 모델이 만든 LEGO 세계](#case-126) | 비교와 한계 | 걸린 시간과 그 시간에 완성한 범위를 함께 비교한다. | Evaluation |
| [두 저장소에 심은 버그 다시 수정하기](#case-127) | 비교와 한계 | 이미 알려진 결함을 심어 에이전트가 찾아 고칠 수 있는 범위를 측정한다. | Benchmark |
| [두 모델의 막대 인간 대 커서](#case-128) | 비교와 한계 | 각 애니메이션이 포인터의 움직임에 어떻게 반응하는지 비교한다. | Evaluation |
| [단일 HTML 파일의 물레방아](#case-129) | 인터랙티브 3D와 UI | 움직이는 요소를 쉽게 알아볼 수 있는 작은 풍경으로 3D 빠른 시제품을 확인한다. | Demo |
| [두 모델의 산악 풍경 렌더링](#case-130) | 비교와 한계 | 풍경 애니메이션에서 구도, 생성 시간, 비용을 따로 비교한다. | Evaluation |
| [맞춤 환경의 영어·페르시아어 번역](#case-131) | 비교와 한계 | 어려운 문단의 번역을 사람이 만든 기준 번역과 비교한다. | Evaluation |
| [Hydrogen Extra로 만든 Blender 장면](#case-132) | 인터랙티브 3D와 UI | 시각적 디테일을 늘리기 전에 Blender에서 형상과 재질을 확인한다. | Demo |
| [네 모델이 만든 침몰하는 배](#case-133) | 비교와 한계 | 같은 장면에서 묘사의 정확도, 제작 시간, 비용을 따로 기록한다. | Evaluation |
| [이미지 속 복잡한 적분 읽기](#case-134) | 앱과 학습 | 긴 식을 간단히 하기 전에 모델이 적분 구간의 두 경계가 같음을 알아보는지 확인한다. | Evaluation |
| [네 모델의 블라인드 문안 비교](#case-135) | 비교와 한계 | 모델 이름을 가리고 사용할 문안을 선택한다. | Evaluation |
| [추론 단계별 시각 검출과 읽기](#case-136) | 비교와 한계 | 추론 단계마다 검출 정확도, 문자 정확도, 비용, 지연을 따로 측정한다. | Benchmark |
| [네 모델이 재현한 업의 집](#case-137) | 비교와 한계 | 같은 참고 이미지와 요구 사항으로 3D 결과의 장단점을 살핀다. | Evaluation |
| [WebGL2 인체 세포 백과](#case-138) | 앱과 학습 | 조작할 수 있는 단면으로 세포 내부의 공간 관계를 설명한다. | Demo |
| [Hydrogen의 두 가지 입자 애니메이션](#case-139) | 인터랙티브 3D와 UI | 다른 입자 장면에서 간단한 효과의 모양과 움직임을 살핀다. | Demo |
| [Parking Bench의 이미지 전용 상대](#case-140) | 앱과 학습 | 보드 이미지만 상태 입력으로 사용해 퍼즐 상대를 시험한다. | Integration |
| [Google 문서 조작 방법 영상](#case-141) | 앱과 학습 | 스크린샷과 번호가 있는 설명으로 모바일 편집 과정을 안내한다. | Demo |
| [미니어처 세계의 낮과 밤 스위치](#case-142) | 인터랙티브 3D와 UI | 작은 스위치를 두고 화면 상태가 바뀔 때 움직임이 이어지는지 확인한다. | Demo |
| [65개 모듈로 만든 환경](#case-143) | 인터랙티브 3D와 UI | 생성 장면이 커질 때 제작 시간과 통합에 필요한 작업을 기록한다. | Demo |
| [카메라를 고정한 춤 영상](#case-144) | 비교와 한계 | 참고 이미지 기반 애니메이션에서 캐릭터, 구도, 카메라 위치가 유지되는지 확인한다. | Evaluation |
| [기준 테스트에서 멈춘 코딩 에이전트](#case-145) | 비교와 한계 | 기준 테스트에 시간 제한을 두고 수정안을 기다리기 전에 진행 상황을 확인한다. | Limit |
| [MZ-1500용 BASIC 환경](#case-146) | 앱과 학습 | 레트로 BASIC 환경을 시제품으로 만들고 주변 기기 지원을 구체적으로 확인한다. | Demo |
| [두 모델의 인터랙티브 로봇 팔](#case-147) | 비교와 한계 | Three.js 로봇 팔을 조작할 때 관절이 자연스럽게 연동되는지 본다. | Evaluation |
| [조작 가능한 FAA 지상 대기 지도](#case-148) | 스프레드시트와 검색 | 운항 제한이 끝난 뒤 대기열이 남는 이유를 지도와 시간축으로 설명한다. | Demo |
| [미니어처 탑과 정원](#case-149) | 인터랙티브 3D와 UI | 생성된 미니어처에서 건축물과 주변 조경의 균형을 살핀다. | Demo |
| [계획, 실행, 검토를 다른 모델에 맡기기](#case-150) | 에이전트와 코딩 작업 흐름 | 별도의 계획, 실행, 검토 역할을 두고 모델별 과제 수를 비교한다. | Demo |
| [Hydrogen과 Sol이 만든 눈 덮인 마을](#case-151) | 비교와 한계 | 코딩 비교에서 시간, 비용, 장면 품질을 각각 기록한다. | Evaluation |
| [High와 Ultra로 만든 Three.js 섬](#case-152) | 비교와 한계 | 외관과 작업 시간을 비교하며 추론 단계를 기록하고 제품별 할당량은 구분한다. | Evaluation |
| [제2차 세계대전 비행장 디오라마](#case-153) | 인터랙티브 3D와 UI | 3D 시제품에 참고 자료와 기계의 움직임 요구 사항을 주어 외관과 동작을 모두 살핀다. | Demo |
| [코딩 클라이언트에서 Hydrogen 설정](#case-154) | 에이전트와 코딩 작업 흐름 | Google API 키를 설정할 때 정확한 모델 ID를 선택한다. | Tutorial |
| [SuperARIS 연구팀의 Hydrogen](#case-155) | 에이전트와 코딩 작업 흐름 | 여러 모델이 참여하는 팀에서 Hydrogen에 조사와 원고 역할을 배정한다. | Integration |
| [네 모델의 클린룸 모듈 재작성](#case-156) | 에이전트와 코딩 작업 흐름 | 재작성을 맡길 에이전트를 평가할 때 코드 이해, 설계, 구현을 따로 비교한다. | Evaluation |
| [3D PS5 컨트롤러 세부 비교](#case-157) | 비교와 한계 | 컨트롤러를 비교할 때 버튼 그림자와 뒷면 하드웨어를 점검한다. | Evaluation |
| [Muse에서 Antigravity CLI로 과제 위임](#case-158) | 에이전트와 코딩 작업 흐름 | 원격 비서를 로컬 코딩 환경과 연결해 기본 글쓰기 모델을 지정한다. | Integration |
| [CursorBench의 추론 예산 비교](#case-159) | 비교와 한계 | 더 빠른 기본 설정을 정하기 전에 추론 예산별 성공률을 비교한다. | Benchmark |
| [세 모델의 별빛 사원 장면](#case-160) | 비교와 한계 | 3D 장면에서 렌더링 안정성과 시각적 디테일을 따로 살핀다. | Evaluation |
| [1분 안에 만든 HTML 슈팅 게임](#case-161) | 앱과 학습 | 단일 HTML 파일로 슈팅 게임의 조작과 반응을 점검한다. | Demo |
| [기존 마이그레이션 설계 재검토](#case-162) | 비교와 한계 | 마이그레이션에서 기존 구조를 대체할지 코딩 에이전트에 검토시킨다. | Limit |
| [AITuber OnAir에서 Hydrogen과 대화](#case-163) | 앱과 학습 | Live2D 아바타 뒤의 대화 모델로 Hydrogen을 사용해 본다. | Integration |
| [코드로 만든 홍보 영상](#case-164) | 앱과 학습 | 코딩 모델에 짧은 홍보 지시를 주고 동작 표현을 확인한다. | Demo |
| [두 모델이 만든 사원 탈출 게임](#case-165) | 비교와 한계 | 같은 게임에서 조명과 분위기가 장면의 가독성을 돕는지 비교한다. | Evaluation |
| [Gemini 세 모델의 랠리 버기 애니메이션](#case-166) | 비교와 한계 | 경사진 코너에서 서스펜션과 타이어 접지가 자연스러운지 확인한다. | Evaluation |
| [절차적으로 만든 울새 비행](#case-167) | 인터랙티브 3D와 UI | 생성한 비행에서 날개와 몸통이 움직이는 모습을 살핀다. | Demo |
| [Antigravity에서 Orchestrator 또는 Swarm 선택](#case-168) | 에이전트와 코딩 작업 흐름 | 순차 작업은 모델 간 인계로 처리하고 병렬 작업은 독립 작업자와 검증자에 나눠 맡긴다. | Tutorial |
| [두 모델의 Chasing Views 애니메이션](#case-169) | 비교와 한계 | 각 추론 단계를 기록하면서 출력과 소요 시간을 비교한다. | Evaluation |
| [Design Creativity Bench의 시간과 비용](#case-170) | 비교와 한계 | 창의성 점수와 함께 디자인 한 건의 생성 시간과 비용을 본다. | Benchmark |
| [참고 이미지로 SolidWorks 부품 만들기](#case-171) | 에이전트와 코딩 작업 흐름 | 3D 참고 이미지를 이용해 에이전트의 SolidWorks 모델링 작업을 평가한다. | Integration |
| [네 모델이 만든 사막 질주 장면](#case-172) | 비교와 한계 | 조명과 메시를 보기 전에 발의 접지와 체중 이동을 비교한다. | Evaluation |
| [융의 동시성을 설명하는 슬라이드](#case-173) | 앱과 학습 | 관련 개념을 구분해서 설명해야 하는 주제로 슬라이드 생성 절차를 시험한다. | Demo |
| [FrontierCS 2 컴퓨터 과학 연구 문제](#case-174) | 비교와 한계 | 일반 코딩 평가에 연구 벤치마크를 더하고 실행 환경을 기록한다. | Benchmark |
| [네 모델의 Rio Above the Clouds](#case-175) | 비교와 한계 | 같은 창작 과제에서 비용, 시간, 주관적 품질을 비교한다. | Evaluation |
| [GBENCH 기술 과제의 Hydrogen](#case-176) | 비교와 한계 | 기술 작업은 검증할 수 있는 코딩 및 비코딩 결과와 가격, 시간을 함께 평가한다. | Benchmark |
| [차량에 평행 주차를 가르치는 시뮬레이션](#case-177) | 비교와 한계 | 생성한 시뮬레이션의 학습 과정과 최종 성공률을 비교한다. | Evaluation |
| [조작 가능한 미토콘드리아 분자 모터](#case-178) | 앱과 학습 | 인터랙티브 도식으로 분자 운동과 ATP 생성을 연결한다. | Demo |
| [Qix 스타일의 땅따먹기 게임](#case-179) | 앱과 학습 | 짧은 아케이드 게임 지시로 첫 출력에 조작과 반응이 구현되는지 시험한다. | Demo |
| [Hydrogen으로 HTML 슬라이드 생성](#case-180) | 앱과 학습 | HTML 생성 속도와 함께 슬라이드의 정보 위계와 배치를 살핀다. | Demo |
| [Terminal-Bench 4.0의 Hydrogen](#case-181) | 비교와 한계 | 명령줄 코딩 모델을 고를 때 과제 성공률과 비용을 함께 살펴본다. | Benchmark |
| [단일 HTML 파일로 만든 일러스트](#case-182) | 인터랙티브 3D와 UI | 외부 자산 없이 코드로 참고 이미지를 재현할 수 있는지 확인한다. | Demo |
| [문어를 움직이는 세 가지 Gemini 모델](#case-183) | 비교와 한계 | 바위를 잡는 동작이 몸을 앞으로 끌어당기는 장면으로 이어지는지 살펴본다. | Evaluation |
| [Chrome에서 구조화된 YouTube 요약 받기](#case-184) | 스프레드시트와 검색 | Chrome의 Gemini 패널에 타임스탬프가 포함된 요약을 요청하고 외부 배경 정보의 출처를 구분한다. | Tutorial |
| [수업 내용을 짧은 영상으로 변환](#case-185) | 앱과 학습 | 수업을 영상으로 바꿀 때 설명의 정확성과 전달 속도를 살펴본다. | Demo |
| [정지 장면에서 퍼핀 애니메이션 만들기](#case-186) | 인터랙티브 3D와 UI | 기존 HTML 장면을 절차적 애니메이션의 첫 프레임으로 사용한다. | Demo |
| [3D 성 모델링 테스트](#case-187) | 비교와 한계 | 여러 모델을 반복 실행해 성의 외형과 자원 사용량을 비교한다. | Evaluation |
| [Antigravity Swarm에서 브라우저 사용](#case-188) | 에이전트와 코딩 작업 흐름 | 스웜을 평가할 때 각 에이전트의 작업과 브라우저 활동을 함께 확인한다. | Demo |
| [Google Drive를 통해 Muse에 작업 넘기기](#case-189) | 에이전트와 코딩 작업 흐름 | 다른 에이전트가 다음 단계를 맡을 때 감시 중인 Drive 폴더로 조사 결과를 넘긴다. | Integration |
| [Gemini Canvas에서 만든 리코더 연습 안내](#case-190) | 앱과 학습 | 빠른 모드로 악보와 악기 연주 안내를 연결한 연습 도구를 만들어 본다. | Demo |
| [범위가 늘자 크게 바뀐 프로젝트 일정](#case-191) | 비교와 한계 | 일정 추정치가 크게 바뀌면 범위와 가정을 설명하도록 요청한다. | Limit |
| [Antigravity Swarm으로 만든 펠리컨 애니메이션](#case-192) | 에이전트와 코딩 작업 흐름 | 애니메이션과 소리 제작을 코딩 에이전트에 나누고 합쳐진 장면을 확인한다. | Demo |
| [윤년이 포함된 달력 계산](#case-193) | 비교와 한계 | 간단한 단위 환산에서도 달력의 예외를 고려하는지 확인한다. | Evaluation |
| [한 개의 HTML 파일로 만든 TAJ VICE](#case-194) | 앱과 학습 | 파일 하나로 탐색할 수 있는 지도를 구현하고 남은 버그를 확인한다. | Demo |
| [Google Cloud 프로젝트에서 Antigravity 사용](#case-195) | 에이전트와 코딩 작업 흐름 | 관리형 자격 증명으로 Hydrogen을 연결할 때 인증 경로와 프로젝트 청구를 확인한다. | Tutorial |
| [답변에 남은 오래된 구독 한도](#case-196) | 비교와 한계 | 조사 에이전트를 평가할 때 최신 구독 조건과 모델 이름을 원출처와 대조한다. | Limit |
| [WebGL 애니메이션의 이야기 다듬기](#case-197) | 비교와 한계 | 기술적으로 복잡한 초안에 흐름이 부족하면 이야기의 전개가 드러나도록 수정한다. | Limit |
| [Carbon으로 기획하고 Hydrogen으로 모바일 앱 구현](#case-198) | 에이전트와 코딩 작업 흐름 | 기획 모델에 인터랙션 설계를 맡기고 실행 모델에 구현을 맡긴다. | Demo |
| [산 위 용 전투를 코드로 만든 두 모델](#case-199) | 비교와 한계 | 같은 장면에서 두 등장인물의 상호작용을 애니메이션이 어떻게 처리하는지 비교한다. | Evaluation |
| [프롬프트 한 번으로 만든 3D 미니어처 섬](#case-200) | 인터랙티브 3D와 UI | 한 번에 생성한 장면에서 건물, 지형과 물이 알아보기 쉽게 배치됐는지 확인한다. | Demo |
| [재현 가능한 Three.js 펠리컨 프롬프트](#case-201) | 비교와 한계 | 자전거 애니메이션에서 다리, 바퀴와 조향이 서로 맞물리는지 확인한다. | Evaluation |
| [T3 Code에서 Hydrogen 사용](#case-202) | 에이전트와 코딩 작업 흐름 | 전용 코딩 클라이언트에서 실제 세션을 진행하며 시간 구간별 한도와 주간 한도를 기록한다. | Integration |
| [손그림 풍의 공익 영상](#case-203) | 앱과 학습 | 짧은 공익 메시지에 손그림 스타일이 어울리는지 살펴본다. | Demo |
| [열 가지 화풍을 오가는 공작 자전거 애니메이션](#case-204) | 에이전트와 코딩 작업 흐름 | 여러 모델로 구성된 스웜에 화면 전환과 소리 동기화를 코드로 구현하도록 맡긴다. | Demo |
| [세 실행 환경에서 같은 오두막 프롬프트 사용](#case-205) | 비교와 한계 | 시각 작업을 다른 설정과 플랫폼에서 수행할 때 출력 형식을 확인한다. | Evaluation |
| [같은 프롬프트로 만든 대시보드 비교](#case-206) | 비교와 한계 | 공통 프런트엔드 프롬프트로 나온 레이아웃과 정보 배치를 비교한다. | Evaluation |
| [이미지로 React.gg 사이트 재현](#case-207) | 앱과 학습 | 참고 이미지를 출발점으로 삼고 어떤 세부 요소를 손봐야 하는지 확인한다. | Demo |
| [특이점을 주제로 한 인터랙티브 패널](#case-208) | 인터랙티브 3D와 UI | 시각 개념 하나를 중심으로 짧은 인터랙티브 장면을 만들어 본다. | Demo |
| [두 모델로 만든 횡스크롤 애니메이션](#case-209) | 비교와 한계 | 액션 장면을 비교할 때 움직임의 연속성과 제작 비용을 함께 확인한다. | Evaluation |
| [Gemini를 달리기 코치로 활용](#case-210) | 앱과 학습 | 운동 기록을 코칭 제안과 비교하고 현재 수준에 맞게 목표를 조정한다. | Demo |
| [온체인 점수를 기록하는 브라우저 게임](#case-211) | 앱과 학습 | 데스크톱에서 게임을 실행하고 플레이와 별도로 점수 기록을 확인한다. | Demo |
| [일본어 답변에서 수식 렌더링 실패](#case-212) | 비교와 한계 | TeX 명령이 들어 있는 답변은 정확도와 함께 화면에 표시되는지도 확인한다. | Limit |
| [프롬프트를 MIDI로 바꾸는 작곡 앱](#case-213) | 앱과 학습 | 일본어 요청을 MIDI, WAV와 피아노 롤 화면으로 바꾸는 도구를 시도한다. | Demo |
| [응답하지 말라는 지시 테스트](#case-214) | 비교와 한계 | 응답을 보내지 않아야 하는 워크플로에서 모델이 실제로 침묵할 수 있는지 확인한다. | Evaluation |
| [콘서트 정보를 한 페이지 요약으로](#case-215) | 앱과 학습 | 행사 정보를 훑어보기 쉬운 한 페이지의 시각 요약으로 구성한다. | Demo |
| [전기 모터를 설명하는 세 모델](#case-216) | 비교와 한계 | 같은 시뮬레이션 프롬프트로 시각적 명확성과 학습용 제어 기능을 비교한다. | Evaluation |
| [책상 장면을 움직이는 두 모델 워크플로](#case-217) | 비교와 한계 | 원래 요청에 비춰 장면의 세부 표현, 음량과 마지막 정지 구간을 확인한다. | Evaluation |
| [아바타로 만든 일상 몽타주](#case-218) | 앱과 학습 | 하나의 아바타와 네 가지 일상 장면으로 짧은 스토리보드 적응을 평가한다. | Demo |
| [Hydrogen으로 ComfyUI 캐릭터 클립 기획](#case-219) | 앱과 학습 | 의상과 배경은 유지하고 영상의 표정과 동작을 바꿔 본다. | Integration |
| [Almance Vale을 100개 모듈로 확장](#case-220) | 에이전트와 코딩 작업 흐름 | 기존 앱을 코딩 에이전트로 옮기고 스타일을 유지하면서 모듈을 추가하도록 요청한다. | Demo |
| [절차적 사운드를 넣은 2D 마을](#case-221) | 비교와 한계 | 제작 시간과 함께 화면의 사건에 따라 샌드박스 사운드가 바뀌는지 확인한다. | Evaluation |
| [노래를 와이드 화면으로 시각화](#case-222) | 앱과 학습 | 곡과 화면 구성 요청을 주고 움직임이 음악의 에너지를 얼마나 전달하는지 확인한다. | Demo |
| [Hydrogen 하위 에이전트 일곱 개로 나이아가라 폭포 구현](#case-223) | 에이전트와 코딩 작업 흐름 | 장면을 여러 요소로 나눠 조정 에이전트가 실행 담당자에게 분배하도록 한다. | Demo |
| [두 시대극 로맨스 클립의 연속성](#case-224) | 앱과 학습 | 두 번째 클립에서 앞 장면의 어떤 요소를 유지해야 하는지 명시한다. | Demo |
| [Gemini 앱에서 만든 물 구체](#case-225) | 인터랙티브 3D와 UI | 간단한 광학 장면에서 하이라이트와 굴절의 관계를 살펴본다. | Demo |

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

<a id="case-59"></a>
### 사례 59: [n8n에서 Hydrogen으로 도구 호출하기](https://x.com/n8n_io/status/2120947273534197886) (작성자 [@n8n_io](https://x.com/n8n_io))

**반복적인 도구 사용을 Hydrogen에 맡기고 계획은 별도 단계로 둔다.**

n8n은 Hydrogen 지원과 함께 Carbon 또는 Argon이 계획하고 Hydrogen이 실행하는 방식을 소개했다. 원문에 통합 설정이 연결돼 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-12

---

<a id="case-69"></a>
### 사례 69: [멀티에이전트 환경의 인증 경로](https://x.com/studio_yebisu/status/2120969033260646551) (작성자 [@studio_yebisu](https://x.com/studio_yebisu))

**다른 제공업체에 과제를 위임할 때 실제로 어느 클라이언트가 인증하는지 확인한다.**

게시자는 Claude에 Antigravity CLI를 통해 Hydrogen을 쓰도록 요청했다고 밝혔다. Claude Code가 직접 인증을 시도한 뒤 Antigravity 사용이 정지됐다는 보고다. 화면은 정지 통지를 보여 주며 원인은 게시자의 설명이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-12

---

<a id="case-70"></a>
### 사례 70: [Antigravity Goal Mode 실행](https://x.com/Inmerson/status/2120973427788124345) (작성자 [@Inmerson](https://x.com/Inmerson))

**장시간 코딩 세션의 계획, 코드 변경, 테스트 결과를 추적한다.**

게시자는 Hydrogen Extra의 Goal Mode에서 105분간 계획, 구현, 테스트를 진행했다고 밝혔다. 테스트 결과는 게시자의 보고다.

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

유형: Demo | 날짜: 2026-11-12

---

<a id="case-73"></a>
### 사례 73: [Antigravity Orchestrator의 Carbon과 Hydrogen](https://x.com/Google/status/2120982566891356279) (작성자 [@Google](https://x.com/Google))

**빠른 구현 모델이 막히면 계획 모델에서 문제를 다시 검토한다.**

Google은 Carbon이 계획과 문제 해결을 맡고 Hydrogen이 수정과 테스트를 맡는 방식을 설명했다. Terminal-Bench 4.0 성공률은 Carbon에 가까웠고 시간과 한도 사용량은 줄었다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

유형: Integration | 날짜: 2026-11-12

---

<a id="case-87"></a>
### 사례 87: [OpenClaw에서 Hydrogen 사용](https://x.com/openclaw/status/2121098531205501401) (작성자 [@openclaw](https://x.com/openclaw))

**사용할 에이전트 프레임워크에서 모델을 선택할 수 있는지 확인한다.**

OpenClaw는 화면 이미지와 함께 Hydrogen 지원을 발표했다. 벤치마크나 전체 설정 기록은 포함되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-13

---

<a id="case-97"></a>
### 사례 97: [Blender MCP로 만든 왕좌의 방](https://x.com/ashen_one/status/2121165467821936651) (작성자 [@ashen_one](https://x.com/ashen_one))

**Blender MCP를 사용해 편집기 안에서 생성한 장면의 구도를 확인한다.**

제작자는 Hydrogen과 Blender MCP로 왕좌의 게임 속 철왕좌의 방을 재현했다고 밝혔으며 장면의 녹화를 공개했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

유형: Integration | 날짜: 2026-11-13

---

<a id="case-113"></a>
### 사례 113: [브라우저 CAD의 콘크리트 믹서 조립체](https://x.com/johnsanthosh01/status/2121243197901041869) (작성자 [@johnsanthosh01](https://x.com/johnsanthosh01))

**생성한 조립체를 CAD 작업에 쓰기 전에 부품 트리와 맞물림을 점검한다.**

제작자는 Hydrogen에 프롬프트를 한 번 주어 CadX Studio에서 부품 265개로 된 믹서를 40분 만에 만들었다고 밝혔다. 부품을 하나씩 수작업으로 모델링하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

유형: Integration | 날짜: 2026-11-13

---

<a id="case-114"></a>
### 사례 114: [Blender에서 절차적으로 도끼 만들기](https://x.com/camperaigg/status/2121252572115951897) (작성자 [@camperaigg](https://x.com/camperaigg))

**윤곽 참고 이미지와 뷰포트 점검으로 절차적으로 만든 Blender 에셋을 확인한다.**

제작자는 Antigravity CLI의 Hydrogen, Python 모듈, 반복 확인을 통해 도끼를 만들었다고 보고했다. 촬영을 포함한 시간은 51분, API 비용은 5.01달러였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-13

---

<a id="case-118"></a>
### 사례 118: [28개 모듈로 만든 Ember Isle](https://x.com/IamEmily2050/status/2121258646759952644) (작성자 [@IamEmily2050](https://x.com/IamEmily2050))

**큰 장면을 모듈로 나누고 각 생성에 걸린 시간을 기록한다.**

제작자는 Gemini 앱의 Hydrogen High로 Ember Isle을 만들었다. 28모듈에 프롬프트를 하나씩 사용했고 한 번에 82~290초가 걸렸다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-150"></a>
### 사례 150: [계획, 실행, 검토를 다른 모델에 맡기기](https://x.com/naufaldi/status/2121499487999013081) (작성자 [@naufaldi](https://x.com/naufaldi))

**별도의 계획, 실행, 검토 역할을 두고 모델별 과제 수를 비교한다.**

게시자는 Opus 5.5가 계획하고 Hydrogen이 실행하며 Sol이 예비 역할을 하고 Sol 6.1이 검토한다고 설명했다. 개인 Antigravity 사용량과 별도 공개 평가를 함께 소개했다.

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

유형: Demo | 날짜: 2026-11-14

---

<a id="case-154"></a>
### 사례 154: [코딩 클라이언트에서 Hydrogen 설정](https://x.com/k2sbhai/status/2121509825658147041) (작성자 [@k2sbhai](https://x.com/k2sbhai))

**Google API 키를 설정할 때 정확한 모델 ID를 선택한다.**

게시자는 Google AI Studio에서 키를 받고 OpenCode 또는 Cline에서 gemini-4-hydrogen을 고르는 과정을 소개했다. 이용 자격과 요청 한도는 제공업체에 따라 다르다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

유형: Tutorial | 날짜: 2026-11-14

---

<a id="case-155"></a>
### 사례 155: [SuperARIS 연구팀의 Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (작성자 [@NFT_Chen](https://x.com/NFT_Chen))

**여러 모델이 참여하는 팀에서 Hydrogen에 조사와 원고 역할을 배정한다.**

게시물은 SuperARIS 설치와 팀 설정을 안내한다. Hydrogen 또는 Carbon이 논의와 집필을 맡고 조정과 구현 역할을 별도로 두는 방식이다. 연구 품질은 측정되지 않았다.

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

유형: Integration | 날짜: 2026-11-14

---

<a id="case-156"></a>
### 사례 156: [네 모델의 클린룸 모듈 재작성](https://x.com/oasisfeng/status/2121523934831276203) (작성자 [@oasisfeng](https://x.com/oasisfeng))

**재작성을 맡길 에이전트를 평가할 때 코드 이해, 설계, 구현을 따로 비교한다.**

제작자는 핵심 소프트웨어 모듈을 Hydrogen, Argon, GPT-6 Astra, Claude Opus 5.5로 다시 작성했다. Hydrogen의 실행력을 높이 평가하며 다른 결과의 설계 장점도 구분해 설명했다.

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

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-158"></a>
### 사례 158: [Muse에서 Antigravity CLI로 과제 위임](https://x.com/tetumemo/status/2121528823061852166) (작성자 [@tetumemo](https://x.com/tetumemo))

**원격 비서를 로컬 코딩 환경과 연결해 기본 글쓰기 모델을 지정한다.**

게시자는 Muse가 집 PC의 Antigravity CLI로 작업을 보내 결과를 받는다고 설명했다. 기본 모델은 Hydrogen이며 Argon도 선택할 수 있다. 일본어 글쓰기와 시각 자료가 예로 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-14

---

<a id="case-168"></a>
### 사례 168: [Antigravity에서 Orchestrator 또는 Swarm 선택](https://x.com/ohayou792/status/2121624258984153452) (작성자 [@ohayou792](https://x.com/ohayou792))

**순차 작업은 모델 간 인계로 처리하고 병렬 작업은 독립 작업자와 검증자에 나눠 맡긴다.**

게시자는 상위 모델이 계획하고 Hydrogen이 구현하는 Orchestrator 흐름을 설명하고 별도의 /swarm 조정 방식과 비교했다. 작업 간 의존성에 따른 선택법을 제시했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

유형: Tutorial | 날짜: 2026-11-14

---

<a id="case-171"></a>
### 사례 171: [참고 이미지로 SolidWorks 부품 만들기](https://x.com/GoGoFly23/status/2121636952479080713) (작성자 [@GoGoFly23](https://x.com/GoGoFly23))

**3D 참고 이미지를 이용해 에이전트의 SolidWorks 모델링 작업을 평가한다.**

제작자는 Antigravity의 Hydrogen에 이미지 한 장을 주어 SolidWorks 부품을 만들었다고 보고했다. 후속 게시물은 SolidWorks MCP를 사용했다고 밝혔다. 공차와 공학적 적합성은 검증되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-14

---

<a id="case-188"></a>
### 사례 188: [Antigravity Swarm에서 브라우저 사용](https://x.com/Saboo_Shubham_/status/2121852445756477924) (작성자 [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**스웜을 평가할 때 각 에이전트의 작업과 브라우저 활동을 함께 확인한다.**

Google 직원이 Hydrogen과 Antigravity Swarm으로 브라우저를 사용하는 화면을 공유했다. 전체 작업 로그는 게시하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-15

---

<a id="case-189"></a>
### 사례 189: [Google Drive를 통해 Muse에 작업 넘기기](https://x.com/nasuvit_z/status/2121857992702525734) (작성자 [@nasuvit_z](https://x.com/nasuvit_z))

**다른 에이전트가 다음 단계를 맡을 때 감시 중인 Drive 폴더로 조사 결과를 넘긴다.**

작성자는 Hydrogen으로 정보를 수집해 Drive 파일에 정리하고, 파일이 생기면 Muse가 이어받도록 했다고 설명했다. 다이어그램에 인계 흐름이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-15

---

<a id="case-192"></a>
### 사례 192: [Antigravity Swarm으로 만든 펠리컨 애니메이션](https://x.com/chetaslua/status/2121885449509851415) (작성자 [@chetaslua](https://x.com/chetaslua))

**애니메이션과 소리 제작을 코딩 에이전트에 나누고 합쳐진 장면을 확인한다.**

제작자는 Carbon과 Hydrogen이 여러 화풍을 오가는 JavaScript 펠리컨 장면을 만들었다고 밝혔다. 음악과 효과음도 코드로 생성했다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-195"></a>
### 사례 195: [Google Cloud 프로젝트에서 Antigravity 사용](https://x.com/loganlu51268/status/2121911409042719023) (작성자 [@loganlu51268](https://x.com/loganlu51268))

**관리형 자격 증명으로 Hydrogen을 연결할 때 인증 경로와 프로젝트 청구를 확인한다.**

작성자는 개인 요금제 대신 Application Default Credentials로 Google Cloud Agent Platform 프로젝트에 연결하는 과정을 설명했다. 선택 목록에 Hydrogen이 포함되며 SKU별 프로젝트 요금을 확인할 수 있다고 밝혔다.

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

유형: Tutorial | 날짜: 2026-11-15

---

<a id="case-198"></a>
### 사례 198: [Carbon으로 기획하고 Hydrogen으로 모바일 앱 구현](https://x.com/thebuggeddev/status/2121945961555718334) (작성자 [@thebuggeddev](https://x.com/thebuggeddev))

**기획 모델에 인터랙션 설계를 맡기고 실행 모델에 구현을 맡긴다.**

제작자는 Carbon이 모바일 앱을 기획하고 Hydrogen이 Reanimated 물리 동작을 포함해 구현했다고 밝혔다. 움직임이 부드럽다고 평가하며 결과 영상을 공개했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-202"></a>
### 사례 202: [T3 Code에서 Hydrogen 사용](https://x.com/bei351009016/status/2121964293906206916) (작성자 [@bei351009016](https://x.com/bei351009016))

**전용 코딩 클라이언트에서 실제 세션을 진행하며 시간 구간별 한도와 주간 한도를 기록한다.**

작성자는 Gemini Pro에 연결한 T3 Code로 Hydrogen을 약 반나절 사용했다고 밝혔다. 화면과 본문에서 한도 사용 경험을 기록하고 체감 속도와 정확도를 구분했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

유형: Integration | 날짜: 2026-11-15

---

<a id="case-204"></a>
### 사례 204: [열 가지 화풍을 오가는 공작 자전거 애니메이션](https://x.com/SahilPanhotra/status/2121995488425849064) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**여러 모델로 구성된 스웜에 화면 전환과 소리 동기화를 코드로 구현하도록 맡긴다.**

제작자는 Carbon과 Hydrogen 스웜으로 공작이 자전거를 타며 열 가지 화풍을 오가는 영상을 만들었다고 밝혔다. 이미지, 음악, 효과음을 코드로 제작했다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-220"></a>
### 사례 220: [Almance Vale을 100개 모듈로 확장](https://x.com/IamEmily2050/status/2122257581175410858) (작성자 [@IamEmily2050](https://x.com/IamEmily2050))

**기존 앱을 코딩 에이전트로 옮기고 스타일을 유지하면서 모듈을 추가하도록 요청한다.**

제작자는 Almance Vale을 Gemini 앱에서 Antigravity로 옮겼다. Swarm 모드의 Hydrogen Extra가 몇 시간에 걸쳐 기존 코드 관례를 따르며 장면을 100개 모듈로 늘렸다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

유형: Demo | 날짜: 2026-11-16

---

<a id="case-223"></a>
### 사례 223: [Hydrogen 하위 에이전트 일곱 개로 나이아가라 폭포 구현](https://x.com/SahilPanhotra/status/2122311637684424737) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**장면을 여러 요소로 나눠 조정 에이전트가 실행 담당자에게 분배하도록 한다.**

제작자는 Carbon과 Hydrogen 하위 에이전트 일곱 개가 프롬프트 하나로 한 시간 안에 나이아가라 폭포 체험을 만들었다고 밝혔다. 녹화에는 물, 배, 다양한 시점과 바뀌는 환경이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

유형: Demo | 날짜: 2026-11-16

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

<a id="case-58"></a>
### 사례 58: [15분 만에 만든 Minecraft풍 시제품](https://x.com/RezAIT00/status/2120947124418293876) (작성자 [@RezAIT00](https://x.com/RezAIT00))

**복셀 샌드박스에서 채굴과 인벤토리 등 여러 기능이 맞물리는지 확인한다.**

제작자는 Hydrogen Extra High로 15분 만에 시제품을 만들었다고 보고했다. 배치, 채굴, 인벤토리를 소개했으며 녹화에는 일부 기능이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-77"></a>
### 사례 77: [뉴스 브리핑을 내레이션 영상으로](https://x.com/gigabit_million/status/2121011957042163722) (작성자 [@gigabit_million](https://x.com/gigabit_million))

**조사한 브리핑을 짧은 영상으로 바꾸고 제시된 사실을 확인한다.**

녹화에서 Gemini 모바일 앱의 Hydrogen은 최근 뉴스를 검색해 개요를 만든다. 이어진 영상 요청의 결과가 앱에서 10초 재생된다. 제작 시간과 내레이션은 작성자의 보고이며 렌더링 백엔드는 밝혀지지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-90"></a>
### 사례 90: [웹캠으로 공중에 그리는 도구](https://x.com/CodeByPoonam/status/2121121804483969102) (작성자 [@CodeByPoonam](https://x.com/CodeByPoonam))

**공중에서 선을 그려 인터페이스가 입력을 따라가는지 시험한다.**

제작자는 사전 사용 기간에 Hydrogen으로 웹캠 공중 그리기 도구를 만들었다고 보고하고 녹화를 공개했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-93"></a>
### 사례 93: [한 번에 생성한 웹 포털](https://x.com/kimura_0314/status/2121130305532878979) (작성자 [@kimura_0314](https://x.com/kimura_0314))

**개별 동작을 테스트하기 전에 첫 번째 포털 화면의 레이아웃을 확인한다.**

게시자는 Antigravity에서 Hydrogen으로 한 번에 만들었다는 웹 포털 화면을 공개했다. 이미지는 외관을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-13

---

<a id="case-95"></a>
### 사례 95: [Cities: Skylines풍 도시 건설 도구](https://x.com/yohakujpn/status/2121146464466604147) (작성자 [@yohakujpn](https://x.com/yohakujpn))

**도시 건설 시제품을 만들어 조작 방식과 시뮬레이션이 어떻게 맞물리는지 본다.**

제작자는 Cities: Skylines풍 시제품을 Hydrogen으로 만들었고 생성 세션은 30분이 채 걸리지 않았다고 밝혔다. 영상에 시제품이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-124"></a>
### 사례 124: [화학 교과서를 인터랙티브 학습 자료로](https://x.com/smalkalbani/status/2121282231759155617) (작성자 [@smalkalbani](https://x.com/smalkalbani))

**힌트, 음성, 선택적으로 표시하는 텍스트를 조합해 자습 자료를 만든다.**

게시자는 음성 안내와 힌트를 제공하는 9학년 화학 수업을 시연했다. 학습 효과 측정은 포함되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-125"></a>
### 사례 125: [Vocaloid 노래 시제품](https://x.com/peach2k2/status/2121284159565902188) (작성자 [@peach2k2](https://x.com/peach2k2))

**한 번에 만든 곡이 캐릭터와 스타일 요구를 충족하는지 살핀다.**

게시자는 노래 클립을 공개하고 Hydrogen이 작곡했다고 밝혔다. 오디오 렌더링 도구는 알려지지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-134"></a>
### 사례 134: [이미지 속 복잡한 적분 읽기](https://x.com/HarshithLucky3/status/2121303778548908228) (작성자 [@HarshithLucky3](https://x.com/HarshithLucky3))

**긴 식을 간단히 하기 전에 모델이 적분 구간의 두 경계가 같음을 알아보는지 확인한다.**

제작자는 Gemini 앱의 Hydrogen High가 복잡한 적분 스크린샷에 답하는 과정을 녹화했다. 바깥 적분의 상한과 하한이 같음을 찾는 것이 시험의 초점이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-138"></a>
### 사례 138: [WebGL2 인체 세포 백과](https://x.com/soumyadesign/status/2121354542344466565) (작성자 [@soumyadesign](https://x.com/soumyadesign))

**조작할 수 있는 단면으로 세포 내부의 공간 관계를 설명한다.**

제작자는 Antigravity의 Hydrogen을 이용해 WebGL2로 외부 라이브러리 없이 3D 세포 백과를 만들었다고 보고했다. 단면 보기를 주요 결과로 꼽았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-140"></a>
### 사례 140: [Parking Bench의 이미지 전용 상대](https://x.com/agenticjay/status/2121391300822081713) (작성자 [@agenticjay](https://x.com/agenticjay))

**보드 이미지만 상태 입력으로 사용해 퍼즐 상대를 시험한다.**

제작자는 Carbon이 게임을 만들었고, 플레이어는 5단계에서 API를 통해 Hydrogen 또는 Gemini Decision 1과 겨룬다고 밝혔다. 두 모델은 격자 상태 데이터 없이 보드 PNG만 받는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

유형: Integration | 날짜: 2026-11-13

---

<a id="case-141"></a>
### 사례 141: [Google 문서 조작 방법 영상](https://x.com/nin222/status/2121395008863621390) (작성자 [@nin222](https://x.com/nin222))

**스크린샷과 번호가 있는 설명으로 모바일 편집 과정을 안내한다.**

제작자는 Hydrogen으로 편집한 Google 문서 사용 영상을 공개했다. 표본 프레임에서 글자 선택, 스타일, 색, 글꼴과 저장 단계의 안내를 확인할 수 있다. 편집 방법은 밝히지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-146"></a>
### 사례 146: [MZ-1500용 BASIC 환경](https://x.com/hiromsa/status/2121465784715338065) (작성자 [@hiromsa](https://x.com/hiromsa))

**레트로 BASIC 환경을 시제품으로 만들고 주변 기기 지원을 구체적으로 확인한다.**

게시자는 Hydrogen으로 약 15분 만에 만들었다고 보고했다. PCG, PSG, QuickDisk를 지원하며 QuickDisk는 LOAD만 지원한다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-14

---

<a id="case-161"></a>
### 사례 161: [1분 안에 만든 HTML 슈팅 게임](https://x.com/SahilPanhotra/status/2121561371951399133) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**단일 HTML 파일로 슈팅 게임의 조작과 반응을 점검한다.**

제작자는 Hydrogen이 프롬프트 한 번으로 1분이 채 되기 전에 플레이 가능한 게임을 만들었다고 보고했다. 프레임워크나 추가 설정 없이 단일 HTML을 사용했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-163"></a>
### 사례 163: [AITuber OnAir에서 Hydrogen과 대화](https://x.com/shinshin86/status/2121571590442017094) (작성자 [@shinshin86](https://x.com/shinshin86))

**Live2D 아바타 뒤의 대화 모델로 Hydrogen을 사용해 본다.**

프로젝트 관리자는 AITuber OnAir의 Hydrogen 지원을 발표하고 Live2D를 포함한 여러 대화용 아바타를 제공했다. 녹화에 통합 동작이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

유형: Integration | 날짜: 2026-11-14

---

<a id="case-164"></a>
### 사례 164: [코드로 만든 홍보 영상](https://x.com/xiangning0/status/2121594643540480293) (작성자 [@xiangning0](https://x.com/xiangning0))

**코딩 모델에 짧은 홍보 지시를 주고 동작 표현을 확인한다.**

게시자는 GPT-6.2 Astra 주제의 홍보 영상을 공개하며 Hydrogen에서 순수 코드로 제작했다고 밝혔다. 영상은 해당 출력의 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-173"></a>
### 사례 173: [융의 동시성을 설명하는 슬라이드](https://x.com/soumyadesign/status/2121676345835241916) (작성자 [@soumyadesign](https://x.com/soumyadesign))

**관련 개념을 구분해서 설명해야 하는 주제로 슬라이드 생성 절차를 시험한다.**

게시자는 Hydrogen과 맞춤 도구로 칼 융의 동시성 및 비인과적 질서를 다룬 발표 자료를 만들었다고 밝혔다. 도구는 Antigravity에서 개발했으며 일부 슬라이드를 공유했다.

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

유형: Demo | 날짜: 2026-11-14

---

<a id="case-178"></a>
### 사례 178: [조작 가능한 미토콘드리아 분자 모터](https://x.com/SidraMiconi/status/2121745863827697687) (작성자 [@SidraMiconi](https://x.com/SidraMiconi))

**인터랙티브 도식으로 분자 운동과 ATP 생성을 연결한다.**

게시자는 Hydrogen High가 프롬프트 하나로 ATP 합성효소 앱을 만든 뒤 카메라를 수정했다고 밝혔다. 구조는 극저온 전자현미경 좌표를 사용했고 움직임은 단순화했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-179"></a>
### 사례 179: [Qix 스타일의 땅따먹기 게임](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (작성자 [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**짧은 아케이드 게임 지시로 첫 출력에 조작과 반응이 구현되는지 시험한다.**

제작자는 무료 Gemini에 Qix풍 게임을 한 번 요청하고 데모를 공유했다. 게시물에는 Hydrogen이 명시돼 있다.

**프롬프트:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-180"></a>
### 사례 180: [Hydrogen으로 HTML 슬라이드 생성](https://x.com/yamachan_ai_log/status/2121772023710118043) (작성자 [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**HTML 생성 속도와 함께 슬라이드의 정보 위계와 배치를 살핀다.**

게시자는 Hydrogen의 HTML 슬라이드 생성을 보여 주고 결과가 빠르고 세부 묘사가 좋았다고 평가했다. 영상에 발표 자료가 나오며 비교를 위한 시간 데이터는 없다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-185"></a>
### 사례 185: [수업 내용을 짧은 영상으로 변환](https://x.com/smalkalbani/status/2121844887033458954) (작성자 [@smalkalbani](https://x.com/smalkalbani))

**수업을 영상으로 바꿀 때 설명의 정확성과 전달 속도를 살펴본다.**

제작자는 수업 영상 작업에 Hydrogen을 사용했다고 밝혔고 클립 두 개를 공개했다. 영상을 렌더링한 시스템은 게시물로 확인할 수 없다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-190"></a>
### 사례 190: [Gemini Canvas에서 만든 리코더 연습 안내](https://x.com/nin222/status/2121877676042682538) (작성자 [@nin222](https://x.com/nin222))

**빠른 모드로 악보와 악기 연주 안내를 연결한 연습 도구를 만들어 본다.**

영상은 Hydrogen 빠른 모드로 제작한 Canvas 리코더 안내 앱을 보여준다. 제작자는 가져온 악보로도 앱을 만들 수 있다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-194"></a>
### 사례 194: [한 개의 HTML 파일로 만든 TAJ VICE](https://x.com/SahilPanhotra/status/2121909681514074328) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**파일 하나로 탐색할 수 있는 지도를 구현하고 남은 버그를 확인한다.**

제작자는 Hydrogen을 사용해 가상의 아그라를 배경으로 한 GTA풍 게임을 12시간 이내 세션에서 만들었다고 밝혔다. 외부 자산 없는 단일 HTML과 순수 JavaScript를 사용했고 게임에 버그가 남아 있다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-203"></a>
### 사례 203: [손그림 풍의 공익 영상](https://x.com/shengtang135754/status/2121965385356612020) (작성자 [@shengtang135754](https://x.com/shengtang135754))

**짧은 공익 메시지에 손그림 스타일이 어울리는지 살펴본다.**

제작자는 Gemini 4 Hydrogen으로 만들었다는 손그림풍 공익 영상을 공개했다. 한 번에 완성했다고 밝혔으며 렌더링 모델과 제작 과정은 공개하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-207"></a>
### 사례 207: [이미지로 React.gg 사이트 재현](https://x.com/thebuggeddev/status/2122019549117911473) (작성자 [@thebuggeddev](https://x.com/thebuggeddev))

**참고 이미지를 출발점으로 삼고 어떤 세부 요소를 손봐야 하는지 확인한다.**

제작자는 참고 이미지를 주고 몇 번의 프롬프트로 Hydrogen에 React.gg를 재현시켰다고 밝혔다. 데모를 연결했으며 완전히 같지는 않다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-210"></a>
### 사례 210: [Gemini를 달리기 코치로 활용](https://x.com/ivanleomk/status/2122036783307469199) (작성자 [@ivanleomk](https://x.com/ivanleomk))

**운동 기록을 코칭 제안과 비교하고 현재 수준에 맞게 목표를 조정한다.**

작성자는 Gemini Hydrogen으로 달리기 코칭을 받았으며 약 일 년 만에 가장 긴 거리를 달렸다고 밝히고 운동 화면을 공유했다. 개인 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-15

---

<a id="case-211"></a>
### 사례 211: [온체인 점수를 기록하는 브라우저 게임](https://x.com/itshoseyn/status/2122063851143246140) (작성자 [@itshoseyn](https://x.com/itshoseyn))

**데스크톱에서 게임을 실행하고 플레이와 별도로 점수 기록을 확인한다.**

제작자는 Hydrogen의 도움으로 점수를 Base에 기록하는 Sheytonak을 만들었다고 밝혔다. 데스크톱에 최적화했으며 모바일 문제와 남은 버그를 공개했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-213"></a>
### 사례 213: [프롬프트를 MIDI로 바꾸는 작곡 앱](https://x.com/Awed_Urshy/status/2122161392828727738) (작성자 [@Awed_Urshy](https://x.com/Awed_Urshy))

**일본어 요청을 MIDI, WAV와 피아노 롤 화면으로 바꾸는 도구를 시도한다.**

제작자는 Hydrogen으로 일본어 입력을 영어 음악 프롬프트로 바꾸고 MIDI, WAV 음원과 피아노 롤 영상을 만드는 앱을 보여줬다. 해당 기능은 데모 앱에서 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

유형: Demo | 날짜: 2026-11-16

---

<a id="case-215"></a>
### 사례 215: [콘서트 정보를 한 페이지 요약으로](https://x.com/fukubaya/status/2122215495474794640) (작성자 [@fukubaya](https://x.com/fukubaya))

**행사 정보를 훑어보기 쉬운 한 페이지의 시각 요약으로 구성한다.**

작성자는 Batten Girls 공연의 일본어 요약을 공유하고 Hydrogen을 활용했다고 밝혔다. 전체 입력 자료와 프롬프트는 공개하지 않았다.

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

유형: Demo | 날짜: 2026-11-16

---

<a id="case-218"></a>
### 사례 218: [아바타로 만든 일상 몽타주](https://x.com/antiAIvo/status/2122251181112353276) (작성자 [@antiAIvo](https://x.com/antiAIvo))

**하나의 아바타와 네 가지 일상 장면으로 짧은 스토리보드 적응을 평가한다.**

제작자는 X 아바타와 공부, 식사, 휴대전화 확인, 운동 장면을 입력했다. Hydrogen으로 만든 약 10초 결과라고 밝혔지만 영상 렌더링 시스템은 명시하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

유형: Demo | 날짜: 2026-11-16

---

<a id="case-219"></a>
### 사례 219: [Hydrogen으로 ComfyUI 캐릭터 클립 기획](https://x.com/nyapan_mohy/status/2122253350808744004) (작성자 [@nyapan_mohy](https://x.com/nyapan_mohy))

**의상과 배경은 유지하고 영상의 표정과 동작을 바꿔 본다.**

제작자는 참고 디자인을 바탕으로 Hydrogen이 기획했고 별도의 ComfyUI MiniMax 이미지 투 비디오 과정으로 렌더링했다고 밝혔다. 새 첫 프레임과 30개 샷의 프롬프트를 준비했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

유형: Integration | 날짜: 2026-11-16

---

<a id="case-222"></a>
### 사례 222: [노래를 와이드 화면으로 시각화](https://x.com/ivy432hz/status/2122283590180589791) (작성자 [@ivy432hz](https://x.com/ivy432hz))

**곡과 화면 구성 요청을 주고 움직임이 음악의 에너지를 얼마나 전달하는지 확인한다.**

제작자는 Hydrogen XHigh에 노래, 21:9 비율과 속도감만 요청했다고 밝혔다. 클립은 빠르게 달리는 도로 장면을 보여주며 렌더링 방법은 설명하지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

유형: Demo | 날짜: 2026-11-16

---

<a id="case-224"></a>
### 사례 224: [두 시대극 로맨스 클립의 연속성](https://x.com/AvaSinclairAi_/status/2122315627113107670) (작성자 [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**두 번째 클립에서 앞 장면의 어떤 요소를 유지해야 하는지 명시한다.**

제작자는 Hydrogen을 사용하는 Gemini 작업 흐름으로 원양 여객선 로맨스 장면을 만들었다고 밝혔다. 인물과 의상을 일관되게 유지하는 두 부분의 요청을 공개했으며 영상 렌더링 모델은 명시하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

유형: Demo | 날짜: 2026-11-16

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

<a id="case-60"></a>
### 사례 60: [Box Agent로 복잡한 기업 문서 처리](https://x.com/levie/status/2120947988143198302) (작성자 [@levie](https://x.com/levie))

**실제와 비슷한 문서 작업에서 정확도, 시간, 토큰 사용량을 확인한다.**

Box의 사전 사용 평가에서 Hydrogen은 일반 과제 기준 Gemini 3.8 Flash보다 정확도가 5%포인트 높았고, 시간은 절반 미만, 토큰은 약 12% 적었다고 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-74"></a>
### 사례 74: [Workspace 데이터에서 차트와 보고서 생성](https://x.com/nin222/status/2120989168247652674) (작성자 [@nin222](https://x.com/nin222))

**후속 요청으로 누락된 분석, 차트, 보고서를 보완할 수 있는지 확인한다.**

제작자는 Google Workspace for Education Fundamentals 데모 환경에서 Hydrogen으로 데이터를 분석하고 차트와 보고서 파일을 만들었다. 두 번의 대화가 필요했다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-12

---

<a id="case-81"></a>
### 사례 81: [Gemini 모드별 스프레드시트 픽셀 아트](https://x.com/kkitase/status/2121041283640926401) (작성자 [@kkitase](https://x.com/kkitase))

**같은 Google 스프레드시트 그림 과제로 여러 모델 설정을 비교한다.**

제작자는 Hydrogen으로 픽셀 아트를 그리는 장면을 녹화하고 Antigravity Orchestrator, Carbon, Argon 실행을 연결했다. 정식 채점 기준은 사용하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-148"></a>
### 사례 148: [조작 가능한 FAA 지상 대기 지도](https://x.com/SidraMiconi/status/2121486870341370204) (작성자 [@SidraMiconi](https://x.com/SidraMiconi))

**운항 제한이 끝난 뒤 대기열이 남는 이유를 지도와 시간축으로 설명한다.**

제작자는 Hydrogen으로 222초 만에 FAA 운항 차질 지도를 만들고 라벨 하나를 고쳤다고 보고했다. 시간축은 공식 보고를 따르고 교통량은 일반적인 운항 일정을 이용해 모의했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-184"></a>
### 사례 184: [Chrome에서 구조화된 YouTube 요약 받기](https://x.com/studio_yebisu/status/2121835594674561098) (작성자 [@studio_yebisu](https://x.com/studio_yebisu))

**Chrome의 Gemini 패널에 타임스탬프가 포함된 요약을 요청하고 외부 배경 정보의 출처를 구분한다.**

일본어 게시물은 열려 있는 YouTube 영상을 Chrome의 Gemini로 요약하는 과정을 보여준다. 공개 프롬프트에는 한줄 요약, 핵심 내용, 챕터별 흐름, 별도 출처, 주의점과 추가 자료가 포함된다.

**프롬프트:**

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

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

유형: Tutorial | 날짜: 2026-11-15

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

<a id="case-41"></a>
### 사례 41: [우주 참고 이미지를 HTML 장면으로](https://x.com/Inmerson/status/2120482539907559651) (작성자 [@Inmerson](https://x.com/Inmerson))

**소수의 참고 이미지로 특징적인 화풍을 재현하는지 확인한다.**

제작자는 우주 시각화를 Hydrogen으로 만들었다고 밝혔다. 원문에는 입력한 행성 이미지와 고리가 있는 행성의 HTML 장면이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-11

---

<a id="case-42"></a>
### 사례 42: [Gemini Canvas에서 만든 F1 차량 시제품](https://x.com/auricxofficial/status/2120843585914605830) (작성자 [@auricxofficial](https://x.com/auricxofficial))

**차량 뷰어에 여러 카메라를 두고 다양한 각도에서 모델을 확인한다.**

제작자는 Gemini Canvas에서 Hydrogen을 처음 사용해 F1 스타일 뷰어를 만들었다고 밝혔다. 녹화에는 여러 카메라 프리셋과 서스펜션 보기가 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-48"></a>
### 사례 48: [SVG로 그린 BMW 옆모습](https://x.com/HarshithLucky3/status/2120932649938382894) (작성자 [@HarshithLucky3](https://x.com/HarshithLucky3))

**차량의 SVG 측면도에서 비율, 윤곽, 작은 디테일을 살핀다.**

게시자는 Gemini 앱의 Hydrogen High로 만들었다는 BMW M4 CS 측면 SVG를 공개했고 30초가 채 걸리지 않았다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-12

---

<a id="case-49"></a>
### 사례 49: [천문학자의 공중 섬](https://x.com/pankajkumar_dev/status/2120933196221333791) (작성자 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**작은 장면에 뚜렷한 주제를 정해 소품과 조명이 이를 뒷받침하는지 확인한다.**

제작자는 Arena의 Hydrogen 체크포인트로 천문학자의 공중 섬을 만들었으며 4분 걸렸다고 밝혔다. 모델 표기는 해당 Arena 실행에 대한 설명이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-50"></a>
### 사례 50: [참고 이미지로 걸어 다닐 수 있는 3D 풍경 제작](https://x.com/HarshithLucky3/status/2120935535422374055) (작성자 [@HarshithLucky3](https://x.com/HarshithLucky3))

**이미지를 바탕으로 만든 장면에서 외관의 재현과 이동 기능을 확인한다.**

제작자는 Gemini 앱에서 Hydrogen으로 만들었다는 조작 가능한 3D 풍경을 보여 주고 GLSL 반사, 절차적 지오메트리, 수영 물리를 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-51"></a>
### 사례 51: [3D 블록으로 만든 미니어처 풍경](https://x.com/abhinavflac/status/2120936501961969990) (작성자 [@abhinavflac](https://x.com/abhinavflac))

**블록으로 소형 풍경을 만들게 하고 각 모양이 하나의 장면으로 읽히는지 살핀다.**

제작자는 Hydrogen으로 만든 3D 블록 풍경 녹화를 공유했다. 제작 시간과 정확한 실행 환경은 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-52"></a>
### 사례 52: [조작 가능한 벚나무](https://x.com/hakmgpt/status/2120936640436642231) (작성자 [@hakmgpt](https://x.com/hakmgpt))

**움직이는 물체와 몇 가지 조작 요소로 실시간 변화를 살펴본다.**

제작자는 화면의 벚나무를 Hydrogen으로 만들었다고 밝혔다. 이미지에서 장면 설정을 볼 수 있으며 구현 세부 사항은 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-12

---

<a id="case-62"></a>
### 사례 62: [작은 인터랙티브 애니메이션의 굴절](https://x.com/chanelluuh/status/2120951519470399710) (작성자 [@chanelluuh](https://x.com/chanelluuh))

**짧은 미리 보기로 굴절 효과를 조정한 뒤 장면을 확장한다.**

제작자는 Small Delights 시리즈의 작품을 Hydrogen으로 만들었으며 굴절 효과를 눈여겨보라고 설명했다. 원문에는 여러 번 조정하는 제작 과정이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-63"></a>
### 사례 63: [위쪽으로 흐르는 강](https://x.com/xKaka1456/status/2120952404225265983) (작성자 [@xKaka1456](https://x.com/xKaka1456))

**흐름 방향을 바꾼 작은 장면으로 시각 효과를 확인한다.**

제작자는 웹 버전 Hydrogen으로 역류하는 강을 만들었다고 보고하고 녹화를 공유했다. 소요 시간과 구독 한도 사용량은 본인의 관찰이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

유형: Demo | 날짜: 2026-11-12

---

<a id="case-67"></a>
### 사례 67: [Hydrogen으로 만든 3D 초상](https://x.com/soyamiruku/status/2120959893943251322) (작성자 [@soyamiruku](https://x.com/soyamiruku))

**인지 가능한 인물 특징이 3D에 드러나는지 작은 초상 과제로 확인한다.**

게시자는 포스트에서 지목한 사람의 3D 초상을 Hydrogen으로 만들었다며 이미지를 공유했다. 세부 설정은 제한적으로 공개됐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

유형: Demo | 날짜: 2026-11-12

---

<a id="case-82"></a>
### 사례 82: [참고 이미지 속 아파트를 3D 프린트](https://x.com/bijanbowen/status/2121042010928709932) (작성자 [@bijanbowen](https://x.com/bijanbowen))

**이미지에서 3D를 생성하는 시험을 실제 출력까지 진행한다.**

게시자는 Hydrogen으로 만들었다는 사인펠드 아파트의 참고 이미지와 3D 프린트 결과를 공유했다.

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

유형: Demo | 날짜: 2026-11-13

---

<a id="case-86"></a>
### 사례 86: [고잉 메리호의 바다 장면](https://x.com/xKaka1456/status/2121063351136739388) (작성자 [@xKaka1456](https://x.com/xKaka1456))

**잘 알려진 가상 선박을 소재로 바다 장면의 구도를 확인한다.**

제작자는 푸른 바다에 있는 고잉 메리호 영상을 공개하고 Hydrogen으로 만들었다고 밝혔다. 프롬프트, 설정, 반복 횟수는 기재되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-88"></a>
### 사례 88: [구름 바다를 헤엄치는 고래](https://x.com/xKaka1456/status/2121100318150898144) (작성자 [@xKaka1456](https://x.com/xKaka1456))

**코드로 만든 생물 장면에서 유체의 움직임과 눈 디자인을 따로 본다.**

출처는 구름 바다를 움직이는 코드 기반 고래를 보여 주며 Hydrogen 실행에 약 2분이 걸렸다고 보고한다. 시간과 사용 한도는 작성자의 관찰이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-92"></a>
### 사례 92: [Gemini Canvas의 해저 도시](https://x.com/ayyh_18/status/2121128385690693821) (작성자 [@ayyh_18](https://x.com/ayyh_18))

**작은 3D 장면에서 시작해 돌아다닐 공간과 움직이는 생물을 여러 차례에 걸쳐 추가한다.**

제작자는 Gemini 앱에서 프롬프트를 여러 번 보내 물고기, 해파리, 산호, 들어갈 수 있는 유리 돔이 있는 해저 도시를 만들었다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-99"></a>
### 사례 99: [Three.js로 만든 회색조 해적선](https://x.com/parves075/status/2121172856889618528) (작성자 [@parves075](https://x.com/parves075))

**색을 회색조로 제한하고도 조명이 입체 형태를 드러내는지 확인한다.**

게시자는 Antigravity의 Hydrogen으로 회색조 해적선을 Three.js에서 제작했다. 영상은 빛과 세부 입체 표현을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-101"></a>
### 사례 101: [CadXStudio의 파라메트릭 탁상 조명](https://x.com/CadX_Studio/status/2121175785356853312) (작성자 [@CadX_Studio](https://x.com/CadX_Studio))

**생성한 CAD 모델에서 부품 치수와 편집 가능 여부를 확인한다.**

도구 제공업체 CadXStudio는 브라우저에서 작동하는 탁상 조명을 공개했다. 편집 가능한 부품이 35개라고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

유형: Integration | 날짜: 2026-11-13

---

<a id="case-102"></a>
### 사례 102: [C++로 만든 신사 참배로 애니메이션](https://x.com/nehstrr3/status/2121184399245128137) (작성자 [@nehstrr3](https://x.com/nehstrr3))

**작은 네이티브 코드 장면으로 웹 기술 없이 작동하는 애니메이션을 작성할 수 있는지 테스트한다.**

제작자는 신사 문을 통과하는 길을 Hydrogen Extra High로 애니메이션화했다고 밝혔다. 직접 작성한 C++로 구현한 결과를 녹화했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-105"></a>
### 사례 105: [30개 모듈로 만든 마을](https://x.com/IamEmily2050/status/2121200010574598655) (작성자 [@IamEmily2050](https://x.com/IamEmily2050))

**프롬프트를 모듈별로 나눠 장면을 만든 다음 조립 결과를 검토한다.**

게시자는 Gemini 앱의 Hydrogen High를 사용해 30개 모듈을 각각 프롬프트 한 번으로 만들었다고 말했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-108"></a>
### 사례 108: [공중 섬의 우체국](https://x.com/pankajkumar_dev/status/2121220537984954448) (작성자 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**미니어처 건물을 지정하고 재질과 조명이 장면을 어떻게 만드는지 살핀다.**

제작자는 Hydrogen에 공중 섬의 3D 미니어처 우체국을 요청하고 녹화를 올렸다. 질감과 색, 조명을 눈여겨볼 부분으로 꼽았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-110"></a>
### 사례 110: [잉어가 헤엄치는 안뜰](https://x.com/SahilPanhotra/status/2121225566779023432) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**물고기가 움직일 때 수면 반사와 조명이 자연스럽게 유지되는지 본다.**

제작자는 Hydrogen으로 만든 잉어 안뜰을 보여 주고 물속 집광, 반사, 물고기 움직임을 언급했다. 참고할 수 있도록 Carbon 버전도 연결했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-112"></a>
### 사례 112: [Gemini 앱에서 실행되는 3D 장면](https://x.com/YxzRainy/status/2121232725185339869) (작성자 [@YxzRainy](https://x.com/YxzRainy))

**웹 Gemini에서 상호 작용할 수 있는 조명과 입자 효과를 만들어 본다.**

제작자는 입자, 움직이는 조명, 실시간 조작 요소를 갖춘 3D 장면을 공개했다. Hydrogen 결과가 Gemini 브라우저 인터페이스에서 동작하는 모습이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-115"></a>
### 사례 115: [한 HTML 파일에 담은 분홍색 3D 장면](https://x.com/SahilPanhotra/status/2121254256288137484) (작성자 [@SahilPanhotra](https://x.com/SahilPanhotra))

**외부 에셋 없이 Three.js만 사용해 구도가 명확한지 확인한다.**

제작자는 Hydrogen이 단일 HTML 파일에서 외부 에셋 없이 Three.js만 사용해 분홍색 장면을 만들었다고 밝혔다. 링크된 잉어 안뜰은 별도의 프로젝트다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-119"></a>
### 사례 119: [코드만으로 만든 빅뱅 시뮬레이션](https://x.com/ash_twtz/status/2121268140630000020) (작성자 [@ash_twtz](https://x.com/ash_twtz))

**짧은 애니메이션으로 설명 시제품을 만들고 과학적 표현을 확인한다.**

제작자는 Gemini 앱의 Hydrogen을 이용해 웹 접근, 텍스처, 외부 에셋, 3D 모델 없이 코드만으로 15초 빅뱅 장면을 만들었다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-120"></a>
### 사례 120: [조립 및 분해 보기가 있는 헬리콥터](https://x.com/LuminaBench/status/2121273297715277930) (작성자 [@LuminaBench](https://x.com/LuminaBench))

**비행 조작과 부품 검사 보기가 3D 시제품에서 연결되는지 확인한다.**

제작자는 조종할 수 있는 헬리콥터와 조립 및 분해 보기를 공개했다. Hydrogen Extra High로 만들었다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-121"></a>
### 사례 121: [X선 및 와이어프레임을 갖춘 Hydrogen Express](https://x.com/LuminaBench/status/2121277060983234788) (작성자 [@LuminaBench](https://x.com/LuminaBench))

**조작할 수 있는 3D 시제품에 여러 검사 모드를 추가한다.**

제작자는 속도 조절, 분해도, 와이어프레임, X선 모드를 갖춘 기차를 보여 주고 생성에 약 5분이 걸렸다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-122"></a>
### 사례 122: [하늘에 떠 있는 주유소](https://x.com/doe_naps/status/2121279837512106168) (작성자 [@doe_naps](https://x.com/doe_naps))

**서로 다른 움직이는 요소와 조명 상태로 시연에서 변화가 보이게 한다.**

제작자는 복고풍 비행 자동차, 돌아가는 터빈, 낮과 밤이 바뀌는 하늘을 갖춘 Hydrogen 주유소를 공개했다. 생성을 한 번 했다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-129"></a>
### 사례 129: [단일 HTML 파일의 물레방아](https://x.com/NovaXCode/status/2121294356875509851) (작성자 [@NovaXCode](https://x.com/NovaXCode))

**움직이는 요소를 쉽게 알아볼 수 있는 작은 풍경으로 3D 빠른 시제품을 확인한다.**

제작자는 Hydrogen이 한 HTML에서 물레방아를 약 30초 만에 만들었다고 보고하고 녹화를 공유했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-132"></a>
### 사례 132: [Hydrogen Extra로 만든 Blender 장면](https://x.com/SPAC89/status/2121302218347270625) (작성자 [@SPAC89](https://x.com/SPAC89))

**시각적 디테일을 늘리기 전에 Blender에서 형상과 재질을 확인한다.**

게시자는 Hydrogen Extra로 만들었다는 Blender 결과를 공개하고 해당 세션에서 사용한 구독 한도를 추정했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-139"></a>
### 사례 139: [Hydrogen의 두 가지 입자 애니메이션](https://x.com/gwammyy/status/2121355401392189746) (작성자 [@gwammyy](https://x.com/gwammyy))

**다른 입자 장면에서 간단한 효과의 모양과 움직임을 살핀다.**

제작자는 두 편의 짧은 입자 효과를 Hydrogen으로 만들었다고 설명했다. 원문에는 결과 영상만 나오고 실행 환경은 명시되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

유형: Demo | 날짜: 2026-11-13

---

<a id="case-142"></a>
### 사례 142: [미니어처 세계의 낮과 밤 스위치](https://x.com/vib3coded/status/2121398359395283027) (작성자 [@vib3coded](https://x.com/vib3coded))

**작은 스위치를 두고 화면 상태가 바뀔 때 움직임이 이어지는지 확인한다.**

제작자는 스위치로 낮과 밤을 바꾸는 장면을 공개했으며 제작비는 0.21달러였다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-143"></a>
### 사례 143: [65개 모듈로 만든 환경](https://x.com/IamEmily2050/status/2121400396002492781) (작성자 [@IamEmily2050](https://x.com/IamEmily2050))

**생성 장면이 커질 때 제작 시간과 통합에 필요한 작업을 기록한다.**

제작자는 Gemini 앱에서 모듈마다 프롬프트를 하나씩 보내 65개 모듈을 만들었다고 보고하고 결과를 녹화했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-149"></a>
### 사례 149: [미니어처 탑과 정원](https://x.com/auricxofficial/status/2121498286926540970) (작성자 [@auricxofficial](https://x.com/auricxofficial))

**생성된 미니어처에서 건축물과 주변 조경의 균형을 살핀다.**

제작자는 블록풍 탑과 정원 영상이 Hydrogen으로 만든 결과라고 밝혔다. 구현 세부 사항은 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-153"></a>
### 사례 153: [제2차 세계대전 비행장 디오라마](https://x.com/doe_naps/status/2121508105947320688) (작성자 [@doe_naps](https://x.com/doe_naps))

**3D 시제품에 참고 자료와 기계의 움직임 요구 사항을 주어 외관과 동작을 모두 살핀다.**

제작자는 Hydrogen에 자료와 짧은 지시를 줘 단일 HTML로 비행장 디오라마를 만들었다고 밝혔다. 과제에는 움직이는 비행기와 전차가 포함됐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-167"></a>
### 사례 167: [절차적으로 만든 울새 비행](https://x.com/LuminaBench/status/2121620820791562291) (작성자 [@LuminaBench](https://x.com/LuminaBench))

**생성한 비행에서 날개와 몸통이 움직이는 모습을 살핀다.**

제작자는 Hydrogen이 울새 비행 애니메이션 코드를 작성했다고 밝혔다. 후속 게시물에는 같은 작업의 Antigravity swarm 그래프가 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

유형: Demo | 날짜: 2026-11-14

---

<a id="case-182"></a>
### 사례 182: [단일 HTML 파일로 만든 일러스트](https://x.com/vamsibatchuk/status/2121788887823778297) (작성자 [@vamsibatchuk](https://x.com/vamsibatchuk))

**외부 자산 없이 코드로 참고 이미지를 재현할 수 있는지 확인한다.**

DeepMind 직원은 HTML 파일 하나로 만든 일러스트를 공개했다. 라이브러리, 이미지 생성기, 스킬, 삽입 자산을 사용하지 않았다고 밝혔다.

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

유형: Demo | 날짜: 2026-11-15

---

<a id="case-186"></a>
### 사례 186: [정지 장면에서 퍼핀 애니메이션 만들기](https://x.com/vamsibatchuk/status/2121846407950639541) (작성자 [@vamsibatchuk](https://x.com/vamsibatchuk))

**기존 HTML 장면을 절차적 애니메이션의 첫 프레임으로 사용한다.**

제작자는 Hydrogen에 이어지는 50프레임을 HTML 파일 하나로 만들도록 요청했다. 클립에는 퍼핀이 등장인물의 모자를 가져가는 장면이 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-200"></a>
### 사례 200: [프롬프트 한 번으로 만든 3D 미니어처 섬](https://x.com/CodeByPoonam/status/2121952483132289270) (작성자 [@CodeByPoonam](https://x.com/CodeByPoonam))

**한 번에 생성한 장면에서 건물, 지형과 물이 알아보기 쉽게 배치됐는지 확인한다.**

제작자는 한 번의 요청으로 Hydrogen이 미니어처 섬을 만들었다고 밝혔다. 이미지에 건물과 여러 지형물이 보인다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-208"></a>
### 사례 208: [특이점을 주제로 한 인터랙티브 패널](https://x.com/Moleh1ll/status/2122032596263776351) (작성자 [@Moleh1ll](https://x.com/Moleh1ll))

**시각 개념 하나를 중심으로 짧은 인터랙티브 장면을 만들어 본다.**

제작자는 Hydrogen으로 만든 특이점 테마 패널을 공유했다. 영상은 결과를 보여주지만 구현 상세는 제한적이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

유형: Demo | 날짜: 2026-11-15

---

<a id="case-225"></a>
### 사례 225: [Gemini 앱에서 만든 물 구체](https://x.com/Google/status/2122366286659289502) (작성자 [@Google](https://x.com/Google))

**간단한 광학 장면에서 하이라이트와 굴절의 관계를 살펴본다.**

Google은 Gemini 앱의 Hydrogen으로 만들었다는 물 같은 구체를 공개했다. 구체에는 Hydrogen 글자가 들어 있다. 실제 렌더링 설정은 설명하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

유형: Demo | 날짜: 2026-11-16

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

<a id="case-43"></a>
### 사례 43: [Hydrogen API와 Antigravity의 Carbon 비교](https://x.com/huang18825/status/2120876396264444314) (작성자 [@huang18825](https://x.com/huang18825))

**같은 프롬프트로 만든 결과를 비교할 때 각 실행 환경을 기록한다.**

제작자는 Hydrogen은 API로, Carbon은 Antigravity에서 실행해 결과를 나란히 놓았다. 보고한 4분 47초는 이 환경에서 Hydrogen을 실행한 시간이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-44"></a>
### 사례 44: [Hydrogen과 Astra의 그림자 표현](https://x.com/SPAC89/status/2120911537296515321) (작성자 [@SPAC89](https://x.com/SPAC89))

**두 실행의 비용과 시간을 비교하면서 세부 묘사도 살펴본다.**

제작자는 그림자가 있는 Hydrogen 결과를 선호했으며, 자신의 환경에서 더 빨리 완성됐다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-45"></a>
### 사례 45: [절차적 3D 모션 비교](https://x.com/SPAC89/status/2120923185981915156) (작성자 [@SPAC89](https://x.com/SPAC89))

**장면의 움직임과 구도를 비교하면서 생성 시간을 기록한다.**

제작자는 Hydrogen High로 만든 줄무늬 3D 형상을 공개했다. 제작에 5분이 채 걸리지 않았다고 보고하며, 자신의 테스트에 사용한 더 비싼 모델과 비교했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-46"></a>
### 사례 46: [PokéBench 비전 테스트 89분](https://x.com/StatsWire/status/2120923685296988296) (작성자 [@StatsWire](https://x.com/StatsWire))

**장시간 비전 에이전트를 테스트할 때 과제 완료 여부, 턴 수, API 실패 횟수를 기록한다.**

출처에 따르면 발표 전 Vertex High 설정에서 Hydrogen이 89분 동안 365턴 만에 웅이를 이겼고 API 호출은 모두 성공했다. 이 결과는 해당 실행 환경에 한정된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-47"></a>
### 사례 47: [Hydrogen과 DeepSeek로 같은 3D 장면 제작](https://x.com/AiHubMix/status/2120928687537418581) (작성자 [@AiHubMix](https://x.com/AiHubMix))

**시각적 결과를 비교하고 실행 시간과 API 비용은 따로 기록한다.**

AIHubMix는 두 모델에서 각각 사용 가능한 최고 추론 설정으로 같은 프롬프트를 실행했다. 업체는 Hydrogen이 3분에 1.30달러, DeepSeek V4.1 Flash가 100분에 0.90달러였다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-53"></a>
### 사례 53: [Agent Arena의 과제당 시간과 비용](https://x.com/arena/status/2120940869889175840) (작성자 [@arena](https://x.com/arena))

**전체 성공률과 함께 과제별 지연, 비용, 출력 토큰을 확인한다.**

Agent Arena에 따르면 Hydrogen High의 과제당 중간값은 5.3분과 1.60달러다. 출력 토큰은 Carbon과 Argon보다 많았다고 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-54"></a>
### 사례 54: [시각 문서와 터미널 벤치마크](https://x.com/ArtificialAnlys/status/2120941511223185722) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**추론 예산을 고를 때 문서와 터미널 결과를 따로 본다.**

Artificial Analysis는 시각 문서에서 좋은 결과를 보고했다. Extra 추론에서 과학 터미널 점수는 올랐으며 일반 Terminal-Bench는 54%로 유지됐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-55"></a>
### 사례 55: [Vals Index와 Tax Agent 결과](https://x.com/ValsAI/status/2120943893894303808) (작성자 [@ValsAI](https://x.com/ValsAI))

**종합 평가와 함께 전문 과제 점수를 확인한다.**

Vals AI에 따르면 Hydrogen은 평가 당시 Vals Index에서 68.5%를 기록했고 Tax Agent에서 1위였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-56"></a>
### 사례 56: [CursorBench의 기본 추론 설정](https://x.com/cursor_ai/status/2120944639633211619) (작성자 [@cursor_ai](https://x.com/cursor_ai))

**기본 설정 점수를 출발점으로 삼아 자신의 저장소에서 시험한다.**

Cursor의 자체 평가에서 기본 설정 Hydrogen은 54.3%, Gemini 3.8 Flash는 39.6%였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-57"></a>
### 사례 57: [네 모델의 궁수 전투 애니메이션](https://x.com/IndependentEco/status/2120945011277590733) (작성자 [@IndependentEco](https://x.com/IndependentEco))

**각 애니메이션에서 인물의 전투 행동이 얼마나 분명한지 비교한다.**

제작자는 Hydrogen, Fable 5.2, GPT-6.1 Sol, Carbon으로 만든 궁수 전투를 한 영상에 나란히 담았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-61"></a>
### 사례 61: [Devin FrontierCode의 Hydrogen](https://x.com/cognition/status/2120950876248641588) (작성자 [@cognition](https://x.com/cognition))

**후보 패치를 병합할 수 있는지 살피고 에이전트 실행 환경을 기록한다.**

Cognition은 FrontierCode 2.0에서 Hydrogen이 38.2%를 기록했다고 보고했다. 비교 모델의 Devin CLI 설정과 Hydrogen의 평가 설정이 다르다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-64"></a>
### 사례 64: [검색을 금지해도 실행된 웹 검색](https://x.com/amanunreal/status/2120954045615768054) (작성자 [@amanunreal](https://x.com/amanunreal))

**검색 없이 답해야 하는 작업에서는 도구 호출 기록을 확인한다.**

게시자는 검색과 도구 호출을 하지 말라고 요청했는데도 Hydrogen이 웹을 검색했다고 보고했다. 원문은 한 차례의 사례를 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-12

---

<a id="case-65"></a>
### 사례 65: [Antigravity Swarm의 사용량 기록](https://x.com/HarshithLucky3/status/2120954399971487774) (작성자 [@HarshithLucky3](https://x.com/HarshithLucky3))

**멀티에이전트 실행의 토큰 수와 소진한 한도를 기록한다.**

제작자는 자신의 구독에서 Swarm을 사용해 토큰 1,700만 개와 5시간 사용 한도의 21%를 소비했다고 밝혔다. 해당 세션의 수치다.

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

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-66"></a>
### 사례 66: [전문 업무 평가의 도구 호출](https://x.com/mercor/status/2120957582139642095) (작성자 [@mercor](https://x.com/mercor))

**에이전트가 전문 과제를 수행하기 전에 정보를 어떻게 모으는지 살핀다.**

Mercor는 APEX-Agents에서 Pass@1 78.0%와 과제당 평균 93회 도구 호출을 보고했다. 법률, 컨설팅, 은행 업무를 다룬 평가다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-68"></a>
### 사례 68: [네 모델의 마법사와 용 전투](https://x.com/IndependentEco/status/2120964690906161461) (작성자 [@IndependentEco](https://x.com/IndependentEco))

**같은 판타지 장면에서 연출, 동작의 명료함, 효과를 비교한다.**

비교 영상에는 Hydrogen과 Claude 모델 세 종류가 만든 마법사와 용의 전투가 나온다. 제작자는 이 경우 Claude 결과를 선호했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-71"></a>
### 사례 71: [MazeBench에서 나타난 낮은 성공률](https://x.com/patience_cave/status/2120973681937809766) (작성자 [@patience_cave](https://x.com/patience_cave))

**공간 추론을 활용하기 전에 미로 과제로 시험한다.**

공개된 MazeBench 비교에서 해당 설정의 성공률은 Hydrogen 1%, Sonnet 5.5 4%, GPT-6.1 Terra 8%였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-72"></a>
### 사례 72: [Gemini 모델 세 종류의 범선 장면](https://x.com/Octoberry/status/2120974412144902376) (작성자 [@Octoberry](https://x.com/Octoberry))

**같은 Three.js 주제에서 움직임과 환경의 세부 표현을 비교한다.**

제작자는 Hydrogen, Argon, Carbon의 범선을 공유했다. Carbon의 세부 묘사를 선호했고 Hydrogen은 Argon에 가까웠다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-75"></a>
### 사례 75: [등번호를 읽다가 추론 예산 소진](https://x.com/skalskip92/status/2120994631072776235) (작성자 [@skalskip92](https://x.com/skalskip92))

**이미지 속 작은 세부 정보를 읽을 때 추론 한도와 대체 수단을 설정한다.**

평가자는 Hydrogen XHigh가 9분 55초 동안 추론 토큰 131,069개를 사용하고도 등번호를 반환하지 않았다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-12

---

<a id="case-76"></a>
### 사례 76: [모델 계열별 ClutterBench 성능](https://x.com/AdamHoltererer/status/2121000759118459138) (작성자 [@AdamHoltererer](https://x.com/AdamHoltererer))

**복잡하게 섞인 장면의 전용 평가에서 모델 계열의 강점이 이어지는지 확인한다.**

게시된 ClutterBench 결과에서 Hydrogen은 포함된 Gemini 가운데 선두였고 비교 대상인 OpenAI 모델보다 낮았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-12

---

<a id="case-78"></a>
### 사례 78: [Minecraft풍 인체 단면 흉상](https://x.com/jan_volad/status/2121026531472339340) (작성자 [@jan_volad](https://x.com/jan_volad))

**생성한 단면에 요청한 내부 구조가 들어 있는지 확인한다.**

제작자는 Hydrogen과 Argon에 같은 일회성 지시로 Minecraft풍 흉상을 만들게 했다. Hydrogen 결과에서 두개골, 갈비뼈, 척추를 확인했다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-79"></a>
### 사례 79: [세 모델이 같은 소품을 렌더링](https://x.com/luckeyfaraday/status/2121030005899825504) (작성자 [@luckeyfaraday](https://x.com/luckeyfaraday))

**단가가 낮은 모델이 과제에서 사용하는 토큰을 품질과 별도로 기록한다.**

Hydrogen, Carbon, Fable 5.2가 같은 소총 모양 소품을 렌더링했다. 제작자는 Hydrogen에 토큰 369만 개와 1.62달러, Carbon에 39만 8,000개와 0.77달러가 들었다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

유형: Evaluation | 날짜: 2026-11-12

---

<a id="case-80"></a>
### 사례 80: [귀납 추론 벤치마크와 토큰 사용량](https://x.com/s_batzoglou/status/2121037853258129811) (작성자 [@s_batzoglou](https://x.com/s_batzoglou))

**어려운 추론 과제에서는 점수와 청구 입력·출력 토큰을 함께 기록한다.**

평가자는 100문제 귀납 시험에서 Hydrogen이 4위로 Opus 5.5에 가까웠다고 밝혔다. 출력 5,500만 토큰과 과금된 입력 3억 700만 토큰을 보고했으며 과금 방식은 확인되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-83"></a>
### 사례 83: [세 모델이 3D 동물을 애니메이션으로 제작](https://x.com/leo114119/status/2121054098753785915) (작성자 [@leo114119](https://x.com/leo114119))

**같은 3D 동물 모델링 과제에서 몸 구조와 동작을 살핀다.**

출처는 Hydrogen, GPT-6.1 Terra, Claude Haiku 5.5를 비교한다. 제작자가 지적한 Hydrogen의 약점은 이 과제에서 관찰됐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-84"></a>
### 사례 84: [ts-bench의 Hydrogen과 Qwen](https://x.com/gosrum/status/2121058334552060102) (작성자 [@gosrum](https://x.com/gosrum))

**종합 결과와 함께 도구 호출 오류를 확인한다.**

출처는 ts-bench에서 Hydrogen과 Qwen4 Max Preview를 비교하고 도구 호출 신뢰성을 언급한다. 이미지에는 평가 당시 결과가 담겨 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-85"></a>
### 사례 85: [Vending-Bench 사업 시뮬레이션](https://x.com/andonlabs/status/2121061429889642497) (작성자 [@andonlabs](https://x.com/andonlabs))

**모의 매출과 에이전트 운영 비용을 함께 비교한다.**

Andon Labs는 Hydrogen이 Vending-Bench 2에서 3위를 차지했고 비슷한 가격의 모델보다 높은 매출을 올렸다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-89"></a>
### 사례 89: [네 모델이 만든 미니어처 섬](https://x.com/xKaka1456/status/2121111495358697924) (작성자 [@xKaka1456](https://x.com/xKaka1456))

**섬의 디자인과 각 환경에서의 시간 및 비용을 비교한다.**

출처에 따르면 Hydrogen 4분, GPT-6.1 Terra 20분, Sol 40분, DeepSeek 60분이다. Hydrogen에 추가 요금이 없었다는 보고는 제작자의 설정에 따른 것이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-91"></a>
### 사례 91: [코드로 표현한 천 찢김 비교](https://x.com/MichaelLee009/status/2121126779276402904) (작성자 [@MichaelLee009](https://x.com/MichaelLee009))

**같은 애니메이션 과제에서 천의 늘어남, 찢어짐, 털과의 상호 작용을 확인한다.**

제작자는 Hydrogen과 Claude Fable 5.2의 코드 애니메이션을 비교해 후자의 시각 표현이 더 좋다고 평가했다. 동일 설정이나 물리 동작의 독립 검증은 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-94"></a>
### 사례 94: [출처를 확인할 수 없는 사실 검증](https://x.com/cagrimbakirci/status/2121130756684886279) (작성자 [@cagrimbakirci](https://x.com/cagrimbakirci))

**스크린샷의 진위를 판단하기 전에 확인할 수 있는 인용 출처를 요청한다.**

게시자가 Hydrogen에 화면 속 게시물이 정확한지 물었다. 모델은 사실이라고 답하고 검증 도구를 여러 번 열었으나 근거 출처를 제공하지 않았다고 한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-13

---

<a id="case-96"></a>
### 사례 96: [Hydrogen과 Sol의 2D 펠리컨](https://x.com/YxzRainy/status/2121148582166491164) (작성자 [@YxzRainy](https://x.com/YxzRainy))

**같은 간단한 2D 과제로 제작 시간과 움직임을 비교한다.**

제작자는 자전거를 타는 2D 펠리컨을 Hydrogen과 GPT-6.1 Sol로 제작했다. 각각 28초와 6분 51초가 걸렸다고 보고했다. 실행 설정이 동일한지는 확인되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-98"></a>
### 사례 98: [네 모델의 거미줄 이동 게임](https://x.com/StatsWire/status/2121172215182065807) (작성자 [@StatsWire](https://x.com/StatsWire))

**같은 단일 파일 제약을 두고 이동과 조작을 비교한다.**

출처는 외부 에셋 없이 단일 HTML 파일로 만든 3D 거미줄 이동 과제를 Gemini 네 모델로 비교한다. Hydrogen은 Extra High, Gemini 3.8 Flash, Argon, Carbon은 High였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-100"></a>
### 사례 100: [네 모델의 건물 디오라마](https://x.com/Jackson77li/status/2121172890838352306) (작성자 [@Jackson77li](https://x.com/Jackson77li))

**같은 건축 프롬프트를 쓰고 모델마다 조명을 어떻게 표현하는지 살핀다.**

제작자는 같은 프롬프트로 Hydrogen, GPT-6.2, Claude Fable 5.2, DeepSeek에서 나온 건물 디오라마를 나란히 보여 준다. 순위와 속도 평가는 주관적이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-103"></a>
### 사례 103: [세 모델의 기차 장면](https://x.com/xKaka1456/status/2121193705810104515) (작성자 [@xKaka1456](https://x.com/xKaka1456))

**같은 기차 장면 과제로 각 설정에서의 완성 시간을 비교한다.**

제작자는 Hydrogen 약 3분, GPT-6.1 Terra 20분, Qwen4 Max Preview 68분으로 보고했다. 영상에 출력이 나오며 설정과 반복 횟수는 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-104"></a>
### 사례 104: [Extra로 애니메이션화한 비 오는 차이나타운](https://x.com/qingzhoucloud/status/2121198911515967952) (작성자 [@qingzhoucloud](https://x.com/qingzhoucloud))

**대형 애니메이션의 추론 모드를 고르기 전에 시간과 최종 장면을 확인한다.**

제작자는 다른 제작자의 프롬프트를 Hydrogen Extra로 실행해 차이나타운 MP4에 약 4시간이 걸렸다고 밝혔다. 별도의 Claude Fable 5.2 실행과 비교했으나 조건을 서로 맞추기는 어렵다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-106"></a>
### 사례 106: [세 모델의 행성 시각화](https://x.com/Stargridcompass/status/2121208957276713181) (작성자 [@Stargridcompass](https://x.com/Stargridcompass))

**같은 프롬프트로 과학 시각화 인터페이스를 만들고 모델별 출력을 비교한다.**

녹화는 Claude Fable 5.2, GPT-6.2 Sol, Hydrogen이 만든 행성 주제 출력을 비교한다. 순서는 게시자의 시각 평가이며 통일된 설정이나 객관 점수는 공개되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-107"></a>
### 사례 107: [네 모델이 재현한 Chrome 공룡 게임](https://x.com/noclipepe/status/2121219775170761044) (작성자 [@noclipepe](https://x.com/noclipepe))

**익숙한 게임을 재현하는 시간을 측정하고 직접 플레이하는 결과를 비교한다.**

제작자는 AI Studio의 Hydrogen이 18분 41초, Fable 5.2가 45분 30초였다고 보고했다. 녹화에 Qwen4-Max-Preview, Carbon과 외관 평가도 나온다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-109"></a>
### 사례 109: [두 코딩 에이전트가 만든 배](https://x.com/marcthecreatorr/status/2121221667619852660) (작성자 [@marcthecreatorr](https://x.com/marcthecreatorr))

**실제 사용할 환경에서 첫 번째 사용 가능한 출력과 수정 부담을 비교한다.**

게시자는 같은 프롬프트를 Claude Code의 Sonnet과 Cursor의 Hydrogen에 각각 입력했다. Hydrogen 실행은 짧았으나 두 번째 버전이 필요했다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-111"></a>
### 사례 111: [네 모델의 강체 투석기 공성 장면](https://x.com/StatsWire/status/2121226579141386285) (작성자 [@StatsWire](https://x.com/StatsWire))

**같은 과제로 조작 가능한 물리 시제품을 비교하고 추론 설정을 기록한다.**

제작자는 돌 블록 수백 개가 있는 투석기 장면을 Gemini 네 모델에 시켰다. Hydrogen Extra High는 10분 3초, Carbon High는 23분 33초였으며 Gemini 3.8 Flash High가 가장 빨랐다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-116"></a>
### 사례 116: [FrontierMemory의 장기 기억 평가](https://x.com/Letta_AI/status/2121255895745351874) (작성자 [@Letta_AI](https://x.com/Letta_AI))

**오래 작동하는 에이전트의 기억 모델을 고를 때 점수와 실행당 비용을 함께 본다.**

Letta는 Hydrogen이 64.4%로 Argon과 같고 기억 실행당 약 100달러였다고 보고했다. 같은 평가 설정에서 Carbon은 71.1%와 약 94달러였다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-117"></a>
### 사례 117: [고장 낸 LiveKit 음성 에이전트의 Hydrogen](https://x.com/livekit/status/2121256982023672076) (작성자 [@livekit](https://x.com/livekit))

**도구에 통제된 실패를 일으켜 음성 에이전트가 근거 없는 결과를 보고하는지 확인한다.**

LiveKit은 일부러 고장 낸 음성 에이전트에서 Hydrogen을 사용해 허위 보고가 없었다고 밝혔다. Gemini 3.8 Flash와 비교하고 보고서를 연결했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-123"></a>
### 사례 123: [Gemini 세 모델의 자전거 동작](https://x.com/AI_Screening/status/2121281026916057443) (작성자 [@AI_Screening](https://x.com/AI_Screening))

**같은 지시로 만든 짧은 움직임을 비교하고 각 실행 시간을 기록한다.**

제작자는 Carbon, Argon, Hydrogen의 자전거 애니메이션을 공유했다. Hydrogen은 약 90초, Argon은 5분 넘게 걸렸다고 밝혔으며 Carbon의 렌더링을 선호했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-126"></a>
### 사례 126: [두 모델이 만든 LEGO 세계](https://x.com/kepochnik/status/2121286219669836027) (작성자 [@kepochnik](https://x.com/kepochnik))

**걸린 시간과 그 시간에 완성한 범위를 함께 비교한다.**

제작자는 Fable 5.2와 Hydrogen으로 만든 LEGO 세계를 보여 주며 각각 44분과 28분 걸렸다고 밝혔다. 결과는 제작자의 실행에 한정된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-127"></a>
### 사례 127: [두 저장소에 심은 버그 다시 수정하기](https://x.com/PawelHuryn/status/2121286545223086302) (작성자 [@PawelHuryn](https://x.com/PawelHuryn))

**이미 알려진 결함을 심어 에이전트가 찾아 고칠 수 있는 범위를 측정한다.**

평가자는 두 저장소에 버그 105개를 심었다. 이 설정에서 Extra High Hydrogen이 같은 Extra High의 Sonnet 5.5보다 조금 낮았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-128"></a>
### 사례 128: [두 모델의 막대 인간 대 커서](https://x.com/DanielZambrini/status/2121289822677483740) (작성자 [@DanielZambrini](https://x.com/DanielZambrini))

**각 애니메이션이 포인터의 움직임에 어떻게 반응하는지 비교한다.**

제작자는 막대 인간이 커서와 싸우는 장면에서 Fable 결과를 선호했으며, 비용을 줄일 경우 Hydrogen도 충분하다고 보았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-130"></a>
### 사례 130: [두 모델의 산악 풍경 렌더링](https://x.com/ZryMiller/status/2121295750122594440) (작성자 [@ZryMiller](https://x.com/ZryMiller))

**풍경 애니메이션에서 구도, 생성 시간, 비용을 따로 비교한다.**

제작자는 Hydrogen과 Opus 5.5의 산악 영상을 공개했다. 보고된 값은 Hydrogen 20분 30초에 0.50달러, Opus 11분 23초에 2.50달러다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-131"></a>
### 사례 131: [맞춤 환경의 영어·페르시아어 번역](https://x.com/MatinSenPai/status/2121296733258887365) (작성자 [@MatinSenPai](https://x.com/MatinSenPai))

**어려운 문단의 번역을 사람이 만든 기준 번역과 비교한다.**

게시자는 맞춤 실행 도구로 개인 번역 과제를 평가해 Hydrogen에 100점 만점 중 94점을 주었다. 해당 설정에 따른 주관 점수다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-133"></a>
### 사례 133: [네 모델이 만든 침몰하는 배](https://x.com/remoteugur/status/2121302956741902451) (작성자 [@remoteugur](https://x.com/remoteugur))

**같은 장면에서 묘사의 정확도, 제작 시간, 비용을 따로 기록한다.**

제작자는 Hydrogen 8.6분과 1.16달러, Gemini 3.8 Flash 10.8분과 1.06달러를 보고했다. Carbon과 Opus 5.5도 테스트했으며 사실성은 Opus를 선호했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-135"></a>
### 사례 135: [네 모델의 블라인드 문안 비교](https://x.com/quintanilha/status/2121315967447757299) (작성자 [@quintanilha](https://x.com/quintanilha))

**모델 이름을 가리고 사용할 문안을 선택한다.**

제작자는 네 모델의 문안 블라인드 비교에서 Hydrogen 결과를 선호했다. 테스트에서 Carbon보다 빠르고 저렴했다고도 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-136"></a>
### 사례 136: [추론 단계별 시각 검출과 읽기](https://x.com/skalskip92/status/2121322414453694489) (작성자 [@skalskip92](https://x.com/skalskip92))

**추론 단계마다 검출 정확도, 문자 정확도, 비용, 지연을 따로 측정한다.**

평가자는 Hydrogen, Argon, Carbon의 검출 및 문자 점수를 따로 보고했다. Hydrogen High는 이미지당 평균 29.3초, 검출 64.6점, 문자 87.2점이었다. Carbon High는 두 점수가 높았고 비용과 대기 시간도 더 컸다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-13

---

<a id="case-137"></a>
### 사례 137: [네 모델이 재현한 업의 집](https://x.com/noclipepe/status/2121326233044537688) (작성자 [@noclipepe](https://x.com/noclipepe))

**같은 참고 이미지와 요구 사항으로 3D 결과의 장단점을 살핀다.**

게시자는 네 실행 중 Hydrogen이 가장 빠르고 저렴했으며 Fable의 외관을 선호했다고 밝혔다. 설정과 청구 정보는 원문의 보고다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

유형: Evaluation | 날짜: 2026-11-13

---

<a id="case-144"></a>
### 사례 144: [카메라를 고정한 춤 영상](https://x.com/notoro_ai/status/2121427503952834562) (작성자 [@notoro_ai](https://x.com/notoro_ai))

**참고 이미지 기반 애니메이션에서 캐릭터, 구도, 카메라 위치가 유지되는지 확인한다.**

게시자는 Google Gemini의 Hydrogen과 연관된 춤 영상과 일본어 프롬프트를 공유했다. 카메라 고정과 원본 화풍 유지는 프롬프트의 요구 사항이다. 실제 영상 생성 모델은 확인되지 않았다.

**프롬프트:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-145"></a>
### 사례 145: [기준 테스트에서 멈춘 코딩 에이전트](https://x.com/Its_lakshya_ai/status/2121431788266659919) (작성자 [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**기준 테스트에 시간 제한을 두고 수정안을 기다리기 전에 진행 상황을 확인한다.**

제작자는 오래 기다린 뒤에도 Hydrogen이 기준 테스트를 실행 중인 Antigravity 세션을 보여 줬다. 다시 시작하기 전에 멈추고 조사해 달라는 요청이 남아 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-14

---

<a id="case-147"></a>
### 사례 147: [두 모델의 인터랙티브 로봇 팔](https://x.com/gmi_cloud/status/2121467337119588834) (작성자 [@gmi_cloud](https://x.com/gmi_cloud))

**Three.js 로봇 팔을 조작할 때 관절이 자연스럽게 연동되는지 본다.**

GMI Cloud는 Hydrogen과 Sonnet 5.5로 구현한 Three.js 로봇 팔의 녹화를 선보였다. 이 비교에서 업체는 Sonnet을 선호했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-151"></a>
### 사례 151: [Hydrogen과 Sol이 만든 눈 덮인 마을](https://x.com/badboyfoxy/status/2121501015442669866) (작성자 [@badboyfoxy](https://x.com/badboyfoxy))

**코딩 비교에서 시간, 비용, 장면 품질을 각각 기록한다.**

제작자는 Hydrogen High가 3분에 1.37달러, Sol High가 15분에 4.03달러였다고 보고했다. 겨울 마을의 창의적 표현은 Sol을 선호했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-152"></a>
### 사례 152: [High와 Ultra로 만든 Three.js 섬](https://x.com/laopai1990/status/2121502334866096160) (작성자 [@laopai1990](https://x.com/laopai1990))

**외관과 작업 시간을 비교하며 추론 단계를 기록하고 제품별 할당량은 구분한다.**

게시자는 섬 장면을 Hydrogen High와 GPT-6.1 Sol Ultra로 비교해 약 90초와 30분을 보고했다. 비용은 추정치이며 추론 단계가 달랐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-157"></a>
### 사례 157: [3D PS5 컨트롤러 세부 비교](https://x.com/Stargridcompass/status/2121528563254043015) (작성자 [@Stargridcompass](https://x.com/Stargridcompass))

**컨트롤러를 비교할 때 버튼 그림자와 뒷면 하드웨어를 점검한다.**

제작자는 Hydrogen High와 GPT-6.2 Sol을 비교했다. 각각 약 3분과 11분이 걸렸으며 Sol의 뒷면과 측면 버튼이 더 완전하다고 평가했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-159"></a>
### 사례 159: [CursorBench의 추론 예산 비교](https://x.com/Beamsters1/status/2121538515909628111) (작성자 [@Beamsters1](https://x.com/Beamsters1))

**더 빠른 기본 설정을 정하기 전에 추론 예산별 성공률을 비교한다.**

게시자는 Hydrogen의 추론 예산을 늘리자 CursorBench 4.0 성공률이 크게 상승했다고 보고했다. 결과는 시험한 설정에 해당한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-14

---

<a id="case-160"></a>
### 사례 160: [세 모델의 별빛 사원 장면](https://x.com/YxzRainy/status/2121551796766376081) (작성자 [@YxzRainy](https://x.com/YxzRainy))

**3D 장면에서 렌더링 안정성과 시각적 디테일을 따로 살핀다.**

제작자는 별을 주제로 Hydrogen, DeepSeek V4.1 1017, Qwen4 Max Preview를 비교했다. 이 시험에서 Hydrogen은 빠르고 화면이 꺼지거나 깜박이지 않았으나 세부 표현은 적었다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-162"></a>
### 사례 162: [기존 마이그레이션 설계 재검토](https://x.com/is_llll/status/2121565725072490559) (작성자 [@is_llll](https://x.com/is_llll))

**마이그레이션에서 기존 구조를 대체할지 코딩 에이전트에 검토시킨다.**

게시자의 비교에서 Hydrogen과 Argon은 기존 접근법을 지지했고 Claude Opus는 구조를 교체해 더 일찍 이전하자고 제안했다. 한 프로젝트에서 나온 판단이다.

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

유형: Limit | 날짜: 2026-11-14

---

<a id="case-165"></a>
### 사례 165: [두 모델이 만든 사원 탈출 게임](https://x.com/runable_hq/status/2121596515474964556) (작성자 [@runable_hq](https://x.com/runable_hq))

**같은 게임에서 조명과 분위기가 장면의 가독성을 돕는지 비교한다.**

Runable은 사원 탈출 게임을 Hydrogen과 Argon으로 구현했다. 제공업체는 Hydrogen 조명에 분위기가 더 있고 Argon 장면은 더 밝다고 설명했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-166"></a>
### 사례 166: [Gemini 세 모델의 랠리 버기 애니메이션](https://x.com/teddyaisi/status/2121604816380010719) (작성자 [@teddyaisi](https://x.com/teddyaisi))

**경사진 코너에서 서스펜션과 타이어 접지가 자연스러운지 확인한다.**

제작자는 채석장의 Three.js 버기 장면으로 Carbon, Argon, Hydrogen을 비교했다. 과제는 서스펜션 압축과 경사 흙길에서 미끄러지는 동작을 요구했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-169"></a>
### 사례 169: [두 모델의 Chasing Views 애니메이션](https://x.com/VulKan42069/status/2121625271493382166) (작성자 [@VulKan42069](https://x.com/VulKan42069))

**각 추론 단계를 기록하면서 출력과 소요 시간을 비교한다.**

제작자는 Hydrogen Extra High와 Opus 5.5 High로 만든 Chasing Views 애니메이션을 공개했다. 이번 실행 시간은 각각 22분과 18분이었다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-170"></a>
### 사례 170: [Design Creativity Bench의 시간과 비용](https://x.com/Kombaico/status/2121635837180031129) (작성자 [@Kombaico](https://x.com/Kombaico))

**창의성 점수와 함께 디자인 한 건의 생성 시간과 비용을 본다.**

평가 운영자는 Hydrogen의 창의성 점수 49.4, 디자인당 중앙값 3.4분과 0.39달러를 보고했다. 이 시험에서 Argon은 느리고 저렴했으며 Carbon은 느리고 비쌌다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

유형: Benchmark | 날짜: 2026-11-14

---

<a id="case-172"></a>
### 사례 172: [네 모델이 만든 사막 질주 장면](https://x.com/Marlenuii/status/2121664345818235177) (작성자 [@Marlenuii](https://x.com/Marlenuii))

**조명과 메시를 보기 전에 발의 접지와 체중 이동을 비교한다.**

제작자는 Astra, Carbon, Fable 5.2, Hydrogen으로 사막을 달리는 말을 비교했다. Astra의 보행을 선호했고 Hydrogen 결과의 말 모양에 문제를 지적했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-174"></a>
### 사례 174: [FrontierCS 2 컴퓨터 과학 연구 문제](https://x.com/wenhaocha1/status/2121679887400403308) (작성자 [@wenhaocha1](https://x.com/wenhaocha1))

**일반 코딩 평가에 연구 벤치마크를 더하고 실행 환경을 기록한다.**

출처는 Antigravity의 Hydrogen이 FrontierCS 2 통과율에서 7위라고 보고했다. 벤치마크는 컴퓨터 과학 연구에서 가져온 기술 문제를 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

유형: Benchmark | 날짜: 2026-11-14

---

<a id="case-175"></a>
### 사례 175: [네 모델의 Rio Above the Clouds](https://x.com/EnvolDev/status/2121701704139956250) (작성자 [@EnvolDev](https://x.com/EnvolDev))

**같은 창작 과제에서 비용, 시간, 주관적 품질을 비교한다.**

평가자는 Hydrogen Extra High가 6.21달러였고 결과가 가장 마음에 들지 않았다고 밝혔다. 이번 실행에서 Astra는 더 빨랐고 네이티브 영상 생성 여부는 확인되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-176"></a>
### 사례 176: [GBENCH 기술 과제의 Hydrogen](https://x.com/leo_linsky/status/2121710421891780864) (작성자 [@leo_linsky](https://x.com/leo_linsky))

**기술 작업은 검증할 수 있는 코딩 및 비코딩 결과와 가격, 시간을 함께 평가한다.**

운영자는 회로 설계와 추상 추론을 포함한 GBENCH의 Hydrogen 결과를 공개했다. 비슷한 가격과 속도에서 Sol의 경쟁력이 높았다고 설명했다.

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

유형: Benchmark | 날짜: 2026-11-14

---

<a id="case-177"></a>
### 사례 177: [차량에 평행 주차를 가르치는 시뮬레이션](https://x.com/noclipepe/status/2121734795738652934) (작성자 [@noclipepe](https://x.com/noclipepe))

**생성한 시뮬레이션의 학습 과정과 최종 성공률을 비교한다.**

제작자는 같은 과제에서 Hydrogen은 차량 44대 중 5대, Fable 5.2는 40대 중 26대가 주차했다고 보고했다. 제작 시간은 각각 5.6분과 24분이었다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

유형: Evaluation | 날짜: 2026-11-14

---

<a id="case-181"></a>
### 사례 181: [Terminal-Bench 4.0의 Hydrogen](https://x.com/gosrum/status/2121785156273160558) (작성자 [@gosrum](https://x.com/gosrum))

**명령줄 코딩 모델을 고를 때 과제 성공률과 비용을 함께 살펴본다.**

독립 평가에서 Hydrogen, Claude Opus 5.5, GPT-6.1 Sol을 비교했다. 평가자는 점수가 비슷하고 Hydrogen의 비용은 두 모델 사이였다고 보고했으며, 실제 도입에는 실행 환경의 성숙도도 영향을 준다고 설명했다.

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

유형: Benchmark | 날짜: 2026-11-15

---

<a id="case-183"></a>
### 사례 183: [문어를 움직이는 세 가지 Gemini 모델](https://x.com/teddyaisi/status/2121800606406885880) (작성자 [@teddyaisi](https://x.com/teddyaisi))

**바위를 잡는 동작이 몸을 앞으로 끌어당기는 장면으로 이어지는지 살펴본다.**

제작자는 문어가 암초를 움켜쥐고 몸을 당기는 Three.js 장면을 Carbon, Argon, Hydrogen으로 비교했다. 팔의 움직임과 몸의 이동이 자연스럽게 연결되는지 비교하도록 했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-187"></a>
### 사례 187: [3D 성 모델링 테스트](https://x.com/nemumusitocha/status/2121848375998063012) (작성자 [@nemumusitocha](https://x.com/nemumusitocha))

**여러 모델을 반복 실행해 성의 외형과 자원 사용량을 비교한다.**

제작자는 Hydrogen으로 만든 3D 성을 보여주고 다른 모델의 이전 결과를 연결했다. Google AI Pro 주간 한도의 3%를 썼다는 수치는 이번 실행에 해당한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-191"></a>
### 사례 191: [범위가 늘자 크게 바뀐 프로젝트 일정](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (작성자 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**일정 추정치가 크게 바뀌면 범위와 가정을 설명하도록 요청한다.**

공개된 대화에서는 필요한 기능을 반영해 현실적으로 추정해 달라는 요청 뒤 일정이 한 달에서 일 년으로 바뀌었다. 실제 소요 기간은 확인할 수 없다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-15

---

<a id="case-193"></a>
### 사례 193: [윤년이 포함된 달력 계산](https://x.com/itsvishaltwt/status/2121891117050589249) (작성자 [@itsvishaltwt](https://x.com/itsvishaltwt))

**간단한 단위 환산에서도 달력의 예외를 고려하는지 확인한다.**

제작자는 Hydrogen High와 GPT에 1년이 몇 초인지 물었다. 두 화면 모두 평년과 윤년의 값을 제시했고, Hydrogen은 그레고리력의 평균 연도 값도 계산했다.

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

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-196"></a>
### 사례 196: [답변에 남은 오래된 구독 한도](https://x.com/take14262/status/2121934737539514533) (작성자 [@take14262](https://x.com/take14262))

**조사 에이전트를 평가할 때 최신 구독 조건과 모델 이름을 원출처와 대조한다.**

작성자는 Hydrogen이 비슷한 모델 이름을 혼동하고 Qwen 요금제의 오래된 시간 한도를 답한 화면을 공유했다. 이는 캡처에 나온 개별 오류 사례다.

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

유형: Limit | 날짜: 2026-11-15

---

<a id="case-197"></a>
### 사례 197: [WebGL 애니메이션의 이야기 다듬기](https://x.com/snakajima/status/2121939899242996058) (작성자 [@snakajima](https://x.com/snakajima))

**기술적으로 복잡한 초안에 흐름이 부족하면 이야기의 전개가 드러나도록 수정한다.**

제작자는 산만하고 이야기가 약하다는 피드백을 반영한 두 번째 WebGL 버전을 보여줬다. 수정본을 더 선호했지만 비교에 사용한 Claude Code 결과를 가장 높게 평가했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

유형: Limit | 날짜: 2026-11-15

---

<a id="case-199"></a>
### 사례 199: [산 위 용 전투를 코드로 만든 두 모델](https://x.com/DrstaOne/status/2121947540509831302) (작성자 [@DrstaOne](https://x.com/DrstaOne))

**같은 장면에서 두 등장인물의 상호작용을 애니메이션이 어떻게 처리하는지 비교한다.**

제작자는 Qwen-4 Max와 Hydrogen으로 만든 산사 위의 용 전투를 비교했다. 프롬프트는 다른 제작자의 것이라고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-201"></a>
### 사례 201: [재현 가능한 Three.js 펠리컨 프롬프트](https://x.com/Aki_LIG/status/2121960943361896596) (작성자 [@Aki_LIG](https://x.com/Aki_LIG))

**자전거 애니메이션에서 다리, 바퀴와 조향이 서로 맞물리는지 확인한다.**

제작자는 완전한 일본어 Three.js 프롬프트와 Hydrogen이 만든 해안 도로 장면을 공개했다. 앞서 GPT-6.1 Terra에도 같은 프롬프트를 줬다고 했고, 이 녹화는 Hydrogen 결과를 보여준다.

**프롬프트:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-205"></a>
### 사례 205: [세 실행 환경에서 같은 오두막 프롬프트 사용](https://x.com/doe_naps/status/2121999317628330476) (작성자 [@doe_naps](https://x.com/doe_naps))

**시각 작업을 다른 설정과 플랫폼에서 수행할 때 출력 형식을 확인한다.**

제작자는 Antigravity의 Hydrogen High와 Carbon High, AI Studio의 Hydrogen Extra High에서 정지 결과를 얻었다고 밝혔다. Arena에서 Hydrogen으로 표시된 실행은 SVG 애니메이션을 만들었으나 실제 체크포인트는 확인되지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-206"></a>
### 사례 206: [같은 프롬프트로 만든 대시보드 비교](https://x.com/fiapp_pro/status/2122014257667846338) (작성자 [@fiapp_pro](https://x.com/fiapp_pro))

**공통 프런트엔드 프롬프트로 나온 레이아웃과 정보 배치를 비교한다.**

작성자는 GPT-6.1 Sol과 Hydrogen으로 만들었다는 웹 인터페이스 화면을 나란히 공개했다. 두 화면을 시각적으로 비교할 수 있으며 구현, 설정, 기능 동작은 공개되지 않았다.

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

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-209"></a>
### 사례 209: [두 모델로 만든 횡스크롤 애니메이션](https://x.com/rubenssoto_ai/status/2122035198728814753) (작성자 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**액션 장면을 비교할 때 움직임의 연속성과 제작 비용을 함께 확인한다.**

제작자는 Hydrogen과 GPT-6 Astra의 횡스크롤 장면을 비교했다. 두 번의 실행에서 Hydrogen의 동작이 더 자연스럽고 비용이 낮았다고 평가했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

유형: Evaluation | 날짜: 2026-11-15

---

<a id="case-212"></a>
### 사례 212: [일본어 답변에서 수식 렌더링 실패](https://x.com/ToraMutton/status/2122131489718759930) (작성자 [@ToraMutton](https://x.com/ToraMutton))

**TeX 명령이 들어 있는 답변은 정확도와 함께 화면에 표시되는지도 확인한다.**

작성자는 Hydrogen으로 바뀐 뒤 Gemini 일본어 답변에 조판된 수식 대신 원시 표기가 나온 화면을 보여줬다. 해당 인터페이스에서 포착된 형식 오류 한 건이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

유형: Limit | 날짜: 2026-11-16

---

<a id="case-214"></a>
### 사례 214: [응답하지 말라는 지시 테스트](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (작성자 [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**응답을 보내지 않아야 하는 워크플로에서 모델이 실제로 침묵할 수 있는지 확인한다.**

작성자는 무응답 테스트 화면을 공유하고 Carbon·Argon과 동작이 달랐다고 밝혔다. 게시물은 한 묶음의 실험만 보여준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

유형: Evaluation | 날짜: 2026-11-16

---

<a id="case-216"></a>
### 사례 216: [전기 모터를 설명하는 세 모델](https://x.com/analogalok/status/2122221106304352257) (작성자 [@analogalok](https://x.com/analogalok))

**같은 시뮬레이션 프롬프트로 시각적 명확성과 학습용 제어 기능을 비교한다.**

제작자는 두 Qwen 모델과 Hydrogen을 비교했고 Hydrogen의 3D 모터와 물리 설명을 선호했다. 단일 비교에 대한 평가다.

**프롬프트:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

유형: Evaluation | 날짜: 2026-11-16

---

<a id="case-217"></a>
### 사례 217: [책상 장면을 움직이는 두 모델 워크플로](https://x.com/GeroXBT/status/2122234332102435128) (작성자 [@GeroXBT](https://x.com/GeroXBT))

**원래 요청에 비춰 장면의 세부 표현, 음량과 마지막 정지 구간을 확인한다.**

제작자는 API 환경에서 같은 프롬프트를 쓴 Hydrogen·Astra 보조 애니메이션을 비교했다. Gemini 결과는 더 매끄럽지만 마지막에 계속 움직였고 음량이 낮았다고 평가했다. 렌더링 과정은 명시하지 않았다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

유형: Evaluation | 날짜: 2026-11-16

---

<a id="case-221"></a>
### 사례 221: [절차적 사운드를 넣은 2D 마을](https://x.com/marcthecreatorr/status/2122266495216459841) (작성자 [@marcthecreatorr](https://x.com/marcthecreatorr))

**제작 시간과 함께 화면의 사건에 따라 샌드박스 사운드가 바뀌는지 확인한다.**

제작자는 Qwen 4 Max와 Hydrogen을 Extra High로 비교했다. Qwen은 약 75분과 0.90달러, Hydrogen은 12분과 1.70달러가 들었다고 밝히고, Hydrogen의 음악이 사건에 더 잘 맞는다고 평가했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[출처 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

유형: Evaluation | 날짜: 2026-11-16

---

<a id="related-repositories"></a>
## 관련 저장소

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon 사례와 비교

<a id="acknowledge"></a>
## 🙏 감사의 말

Hydrogen 작업물을 공개한 제작자, 개발자, 평가자 여러분께 감사드립니다.

**출처 제작자:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*귀속은 인용한 공개 출처를 따르며 최초 제작자를 식별하지 못할 수 있습니다. 수정 또는 삭제를 요청하려면 공개 출처를 첨부하여 issue를 작성하세요.*

기여 체크리스트에 따라 issue 또는 pull request로 출처가 있는 사례를 제안하세요.
