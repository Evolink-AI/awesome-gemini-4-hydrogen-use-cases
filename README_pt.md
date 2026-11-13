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

# Guia e casos de uso selecionados do Gemini 4 Hydrogen

## 🍌 Introdução

Explore o Gemini 4 Hydrogen por meio de aplicações com fontes, fluxos de programação e comparações práticas.

**40 exemplos selecionados mostram o que as pessoas criaram, como trabalharam e onde os resultados ficaram aquém do esperado.**

Cada caso inclui um link para a fonte e os créditos do autor. Demonstrações, exemplos do fornecedor e comparações de criadores são identificados nas notas; instruções ausentes não são reconstruídas.

## 📊 Visão geral

- 40 casos selecionados entre 75 publicações de demonstrações analisadas em uma coleta do X limitada a 500 publicações, realizada em 13 de novembro de 2026.
- Cinco categorias abrangem agentes, aprendizado e aplicativos, planilhas e Search, 3D interativo, e comparações e limitações.
- Todos os 41 recursos visuais selecionados foram preservados: 38 vídeos reproduzíveis com imagens de capa e 3 imagens.
- O Gemini 4 Hydrogen foi anunciado em 12 de novembro de 2026. Explore o modelo e suas opções atuais de acesso no EvoLink.

> [!NOTE]
> A atribuição do modelo, os custos, os tempos e os resultados permanecem alegações das fontes, salvo indicação contrária. A revisão dos vídeos usou quadros amostrados, não testes funcionais completos. Gravações de aplicativos programados não comprovam geração nativa de vídeo. Diferenças nos ambientes de execução, níveis de raciocínio ou números de iterações tornam as comparações não controladas.

**Referências oficiais: [Anúncio do Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Ficha do modelo do Google DeepMind](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**Comece aqui: [Explore o Hydrogen no EvoLink](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [Obtenha uma chave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ Início rápido

Comece no EvoLink e use a API nativa do Gemini quando quiser integrar o Hydrogen a um aplicativo.

1. [Ver o Gemini 4 Hydrogen no navegador](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [Crie ou gerencie uma chave de API do EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

Requisição mínima à API nativa

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

[Leia o guia de início rápido da API nativa do Gemini (em inglês)](https://evolink.ai/docs/en/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> Leia o texto gerado nos campos candidates[].content.parts[].text da resposta.

> [!IMPORTANT]
> Mantenha sua chave de API em uma variável de ambiente e nunca a inclua em um commit. Consulte a documentação da API para opções de transmissão, raciocínio e outras requisições.

## 📑 Menu

| Seção | Casos |
|---|---|
| [⚡ Agentes e fluxos de programação](#agents) | 5 |
| [💻 Aplicativos e aprendizagem](#apps-learning) | 5 |
| [📊 Planilhas e Search](#data-search) | 4 |
| [🎮 3D interativo e interfaces](#interactive-3d) | 9 |
| [🧪 Comparações e limitações](#comparisons-limits) | 17 |
| [Repositórios relacionados](#related-repositories) |  |
| [Início rápido](#quick-start) |  |
| [Agradecimentos](#acknowledge) |  |

| Caso | Categoria | O que experimentar | Tipo |
|---|---|---|---|
| [Manutenção de código no Antigravity](#case-1) | Agentes e fluxos de programação | Use uma tarefa de manutenção delimitada para avaliar conjuntamente edições, uso de ferramentas e verificação. | Demo |
| [Dezesseis aplicativos canvas em paralelo](#case-2) | Agentes e fluxos de programação | Divida o desenvolvimento em módulos independentes e deixe explícitos os papéis de planejamento, implementação e controle de qualidade. | Demo |
| [Mariposa carmesim com um enxame de vários modelos](#case-3) | Agentes e fluxos de programação | Separe os papéis de orquestração e implementação em um projeto interativo de programação criativa. | Demo |
| [Inspeção e reparo com 3D Medic](#case-4) | Agentes e fluxos de programação | Explore um agente que inspeciona um arquivo 3D, encontra erros e propõe reparos antes da exportação. | Demo |
| [Uma cena de veleiro criada no Devin](#case-5) | Agentes e fluxos de programação | Avalie um modelo no ambiente de agente de programação que você realmente pretende usar. | Demo |
| [Prática de idiomas no Lingo City](#case-6) | Aplicativos e aprendizagem | Combine cartões de estudo com uma cena de rua interativa para praticar idiomas em contexto. | Demo |
| [Romeu e Julieta como teatro de papel em 3D](#case-7) | Aplicativos e aprendizagem | Transforme uma aula específica em uma cena interativa com um objetivo de aprendizagem claro. | Demo |
| [Da imagem de design a um site de leitura](#case-8) | Aplicativos e aprendizagem | Use um design de referência para avaliar a compreensão visual e uma implementação funcional da interface. | Demo |
| [Um jardim de carpas koi criado em vinte módulos](#case-9) | Aplicativos e aprendizagem | Construa uma cena maior em módulos pequenos, em vez de esperar um resultado completo com uma única instrução. | Demo |
| [Um jogo educativo de fusão de prótons](#case-10) | Aplicativos e aprendizagem | Crie um protótipo de explicação interativa de um processo científico e depois confira a ciência subjacente. | Demo |
| [Uma paisagem animada no Google Sheets](#case-11) | Planilhas e Search | Use uma animação incomum em planilha para inspecionar o código gerado e as atualizações das células. | Demo |
| [Site de dados interativos Folio](#case-12) | Planilhas e Search | Combine o layout de uma página de apresentação com visualizações interativas de dados em um pequeno protótipo web. | Demo |
| [Respostas visuais a buscas com várias partes](#case-13) | Planilhas e Search | Compare a disposição das respostas e os links citados ao testar uma busca detalhada com várias restrições. | Demo |
| [Previsões financeiras interativas no Sheets](#case-14) | Planilhas e Search | Crie um protótipo de modelo financeiro com premissas visíveis e inspecione as fórmulas e os gráficos gerados. | Demo |
| [Uma sala de jantar interativa](#case-15) | 3D interativo e interfaces | Confira as interações dos objetos, a iluminação e as mudanças de estado em vez de julgar uma cena por uma imagem estática. | Demo |
| [Um controle de volume com um mundo em miniatura](#case-16) | 3D interativo e interfaces | Use um controle conhecido para testar tanto o design de interação quanto os detalhes da cena animada. | Demo |
| [Uma casa japonesa em Three.js](#case-17) | 3D interativo e interfaces | Separe a geração de código do tempo de renderização ao avaliar um passeio 3D detalhado. | Demo |
| [Um pelicano andando de bicicleta em 3D](#case-18) | 3D interativo e interfaces | Use um personagem em movimento para inspecionar coordenação, movimento e consistência da cena. | Demo |
| [Um simulador planetário que começa pelo planejamento](#case-19) | 3D interativo e interfaces | Dê ao modelo de programação um plano concreto antes de pedir que edite uma cena complexa. | Demo |
| [Uma ilha portuária com Antigravity Swarm](#case-20) | 3D interativo e interfaces | Use um pequeno ambiente navegável para inspecionar como vários agentes constroem cenas. | Demo |
| [Uma ilha flutuante com a Torre Eiffel](#case-21) | 3D interativo e interfaces | Avalie composição, movimento de câmera e código gerado em uma cena compacta de um monumento. | Demo |
| [Uma cidade futurista sobrevoável](#case-22) | 3D interativo e interfaces | Teste edições posteriores em um mundo procedural em vez de assumir que o primeiro resultado é final. | Demo |
| [Um hidroavião do amanhecer à noite](#case-23) | 3D interativo e interfaces | Inspecione os controles ambientais e as transições de iluminação em uma cena 3D interativa. | Demo |
| [Animação de bonecos de neon: Hydrogen e Opus](#case-24) | Comparações e limitações | Compare a animação pronta com o tempo e o custo informados, sem pressupor ambientes de execução idênticos. | Evaluation |
| [Tarefas robóticas e erros reconhecidos](#case-25) | Comparações e limitações | Inclua a conclusão de tarefas e o reconhecimento de pequenos erros em uma avaliação de robótica. | Evaluation |
| [Uma célula de trabalho de laboratório em linguagem natural](#case-26) | Comparações e limitações | Avalie a execução de ferramentas e o tratamento de falhas separadamente das principais pontuações das avaliações. | Evaluation |
| [Iceberg e rebocador: Hydrogen e Carbon](#case-27) | Comparações e limitações | Registre o nível de raciocínio e as restrições do ambiente ao comparar uma construção 3D longa. | Evaluation |
| [Um lago gelatinoso de carpas koi: Hydrogen e Sonnet](#case-28) | Comparações e limitações | Inspecione uma cena concreta antes de transformar uma classificação de avaliação em uma escolha de modelo. | Evaluation |
| [Uma coleção de programação criativa com instruções compartilhadas](#case-29) | Comparações e limitações | Use um conjunto variado de tarefas visuais para evitar generalizar a partir de um único resultado atraente. | Evaluation |
| [Vóxeis de Megamind: um contraexemplo de custo e qualidade](#case-30) | Comparações e limitações | Mantenha os casos de falha ao avaliar se um modelo é consistentemente mais barato ou visualmente melhor. | Limit |
| [Um leão malabarista nas quatro estações](#case-31) | Comparações e limitações | Confira o movimento solicitado, não apenas o acabamento visual da interface ao redor. | Limit |
| [Luta de bonecos com três modelos: resultado mais lento e caro](#case-32) | Comparações e limitações | Preserve contraexemplos ao comparar a eficiência anunciada de um modelo com relatos de tarefas reais. | Limit |
| [Uma cena de bicicleta na fazenda: Hydrogen e Flash](#case-33) | Comparações e limitações | Compare o movimento e a qualidade da cena com o tempo de conclusão informado pelo criador. | Evaluation |
| [Uma menina e um gato em bicicletas tandem](#case-34) | Comparações e limitações | Compare a fidelidade à instrução e os detalhes adicionais, deixando visíveis as diferenças entre os ambientes de programação. | Evaluation |
| [Quatro modelos constroem um jogo de Mario em Three.js](#case-35) | Comparações e limitações | Registre as diferenças de raciocínio antes de interpretar uma comparação de jogos com a mesma instrução. | Evaluation |
| [Três modelos Gemini desenham um controle](#case-36) | Comparações e limitações | Procure regressões e melhorias específicas da tarefa em vez de pressupor uma hierarquia entre modelos da família. | Evaluation |
| [Respostas visuais diferentes entre o aplicativo e o Studio](#case-37) | Comparações e limitações | Teste a mesma imagem no produto que pretende usar antes de confiar em um resultado visual. | Limit |
| [Uma cena de lançamento de foguete: Hydrogen e Flash](#case-38) | Comparações e limitações | Compare a animação real do lançamento e também a duração de construção informada. | Evaluation |
| [Quatro tarefas de animação SVG](#case-39) | Comparações e limitações | Use vários temas de interação e animação para inspecionar a consistência entre tarefas. | Evaluation |
| [Três modelos animam um cavalo na savana](#case-40) | Comparações e limitações | Inspecione diretamente o movimento e os detalhes visuais antes de aceitar alegações amplas sobre custo ou qualidade. | Evaluation |

<a id="agents"></a>
## ⚡ Agentes e fluxos de programação

<a id="case-1"></a>
### Caso 1: [Manutenção de código no Antigravity](https://x.com/antigravity/status/2120944334023389476) (por [@antigravity](https://x.com/antigravity))

**Use uma tarefa de manutenção delimitada para avaliar conjuntamente edições, uso de ferramentas e verificação.**

A demonstração de lançamento do Antigravity mostra o Hydrogen mantendo uma base de código. É um exemplo produzido pela plataforma, não uma avaliação de engenharia reproduzida independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-2"></a>
### Caso 2: [Dezesseis aplicativos canvas em paralelo](https://x.com/shengzheyao/status/2120944141559550409) (por [@shengzheyao](https://x.com/shengzheyao))

**Divida o desenvolvimento em módulos independentes e deixe explícitos os papéis de planejamento, implementação e controle de qualidade.**

Um criador do Antigravity CLI no Google DeepMind descreve o Carbon coordenando, verificando e integrando enquanto o Hydrogen cria 16 miniaplicativos canvas sem dependências. Esse fluxo combina modelos, portanto seu resultado não deve ser atribuído apenas ao Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-3"></a>
### Caso 3: [Mariposa carmesim com um enxame de vários modelos](https://x.com/thtbee_/status/2120958666480513310) (por [@thtbee_](https://x.com/thtbee_))

**Separe os papéis de orquestração e implementação em um projeto interativo de programação criativa.**

O criador diz que o Carbon orquestrou um enxame do Antigravity enquanto agentes Hydrogen construíram a obra da mariposa carmesim. Os 45 minutos informados incluem esse fluxo com vários modelos e não foram cronometrados independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-4"></a>
### Caso 4: [Inspeção e reparo com 3D Medic](https://x.com/GoogleAI/status/2120940683233984862) (por [@GoogleAI](https://x.com/GoogleAI))

**Explore um agente que inspeciona um arquivo 3D, encontra erros e propõe reparos antes da exportação.**

A demonstração 3D Medic do Google AI usa um aplicativo Managed Agent criado no AI Studio. Ela mostra um fluxo de reparo de arquivos, não evidências de que quaisquer recursos 3D serão reparados corretamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-5"></a>
### Caso 5: [Uma cena de veleiro criada no Devin](https://x.com/Da7_Tech/status/2120967690722677144) (por [@Da7_Tech](https://x.com/Da7_Tech))

**Avalie um modelo no ambiente de agente de programação que você realmente pretende usar.**

A fonte apresenta uma cena de veleiro atribuída ao Hydrogen executado no Devin. A publicação curta não divulga a instrução completa, o histórico de iterações ou uma configuração reproduzível.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

Tipo: Demo | Data: 2026-11-12

---


<a id="apps-learning"></a>
## 💻 Aplicativos e aprendizagem

<a id="case-6"></a>
### Caso 6: [Prática de idiomas no Lingo City](https://x.com/tulseedoshi/status/2121095754844713427) (por [@tulseedoshi](https://x.com/tulseedoshi))

**Combine cartões de estudo com uma cena de rua interativa para praticar idiomas em contexto.**

Tulsee Doshi compartilha um exemplo do Google que transmite cartões personalizados em 2D e 3D e permite praticar conversas com comerciantes em uma cidade virtual. É uma demonstração do fornecedor, não um estudo independente de resultados de aprendizagem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-7"></a>
### Caso 7: [Romeu e Julieta como teatro de papel em 3D](https://x.com/techartist_/status/2120957446202253803) (por [@techartist_](https://x.com/techartist_))

**Transforme uma aula específica em uma cena interativa com um objetivo de aprendizagem claro.**

O criador construiu uma aula de teatro de papel em 3D sobre a cena da sacada de Romeu e Julieta para Literatura Inglesa do GCSE. A fonte demonstra a interface, mas não mede resultados de aprendizagem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-8"></a>
### Caso 8: [Da imagem de design a um site de leitura](https://x.com/thebuggeddev/status/2120952661046689992) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Use um design de referência para avaliar a compreensão visual e uma implementação funcional da interface.**

O criador afirma que o Hydrogen transformou uma imagem de design em um site funcional de gestão de leituras em 5 minutos e 27 segundos. A duração e a completude são alegações da fonte; esta coleção não inclui teste funcional independente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-9"></a>
### Caso 9: [Um jardim de carpas koi criado em vinte módulos](https://x.com/IamEmily2050/status/2120951069874532806) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Construa uma cena maior em módulos pequenos, em vez de esperar um resultado completo com uma única instrução.**

O criador relata 20 instruções para 20 módulos no aplicativo Gemini, cada um levando 90–270 segundos. O autor declarou acesso antecipado e o exemplo é explicitamente iterativo, não um resultado obtido de uma só vez.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-10"></a>
### Caso 10: [Um jogo educativo de fusão de prótons](https://x.com/SidraMiconi/status/2120948703095820743) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Crie um protótipo de explicação interativa de um processo científico e depois confira a ciência subjacente.**

O jogo do criador percorre a cadeia próton–próton dentro de uma estrela jovem. A única instrução, os 78 segundos de execução e o custo aproximado de $0.19 relatados são alegações da fonte, não resultados reproduzidos independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

Tipo: Demo | Data: 2026-11-12

---


<a id="data-search"></a>
## 📊 Planilhas e Search

<a id="case-11"></a>
### Caso 11: [Uma paisagem animada no Google Sheets](https://x.com/Google/status/2121004369617485896) (por [@Google](https://x.com/Google))

**Use uma animação incomum em planilha para inspecionar o código gerado e as atualizações das células.**

O Google demonstra trens costeiros, nuvens e folhas de outono pintados nas células com código escrito no Antigravity. É uma demonstração criativa oficial, não uma avaliação de desempenho de planilhas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-12"></a>
### Caso 12: [Site de dados interativos Folio](https://x.com/vamsibatchuk/status/2120996342923436188) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Combine o layout de uma página de apresentação com visualizações interativas de dados em um pequeno protótipo web.**

Um funcionário do Google DeepMind apresenta um site no estilo Folio e uma animação interativa criados no Google AI Studio. A publicação não fornece a instrução completa de geração nem um teste funcional independente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-13"></a>
### Caso 13: [Respostas visuais a buscas com várias partes](https://x.com/Google/status/2120960715011883148) (por [@Google](https://x.com/Google))

**Compare a disposição das respostas e os links citados ao testar uma busca detalhada com várias restrições.**

O exemplo do Search do Google combina compreensão da intenção, layouts visuais, tabelas comparativas e expansão de consultas. São comportamentos do produto descritos pelo fornecedor; a demonstração não estabelece efeitos sobre posicionamento ou tráfego para editores.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-14"></a>
### Caso 14: [Previsões financeiras interativas no Sheets](https://x.com/ChanduThota/status/2120942270627414079) (por [@ChanduThota](https://x.com/ChanduThota))

**Crie um protótipo de modelo financeiro com premissas visíveis e inspecione as fórmulas e os gráficos gerados.**

Chandu Thota apresenta uma demonstração de previsões no Google Sheets. A alegação de geração de canvas mais de 30% mais rápida vem do fornecedor, não de uma medição controlada de tempo realizada para este repositório.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

Tipo: Demo | Data: 2026-11-12

---


<a id="interactive-3d"></a>
## 🎮 3D interativo e interfaces

<a id="case-15"></a>
### Caso 15: [Uma sala de jantar interativa](https://x.com/notjazii/status/2120979811569222137) (por [@notjazii](https://x.com/notjazii))

**Confira as interações dos objetos, a iluminação e as mudanças de estado em vez de julgar uma cena por uma imagem estática.**

O criador mostra uma sala de jantar com luzes, luminárias, geladeira e itens internos interativos. Os 30 minutos de construção informados não foram verificados independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-16"></a>
### Caso 16: [Um controle de volume com um mundo em miniatura](https://x.com/vib3coded/status/2120973294090555890) (por [@vib3coded](https://x.com/vib3coded))

**Use um controle conhecido para testar tanto o design de interação quanto os detalhes da cena animada.**

A fonte mostra um controle de volume que anima um pequeno mundo de estilo japonês. O criador informa um custo de $0.19, mas não apresenta uma fatura nem o fluxo completo de geração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-17"></a>
### Caso 17: [Uma casa japonesa em Three.js](https://x.com/SPAC89/status/2120972954146140409) (por [@SPAC89](https://x.com/SPAC89))

**Separe a geração de código do tempo de renderização ao avaliar um passeio 3D detalhado.**

O criador atribui essa casa e jardim ao Hydrogen em Three.js sem agentes. As alegações sobre consumo da assinatura e duração inferior a duas horas são específicas da configuração do autor, não garantias gerais de preço ou latência.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-18"></a>
### Caso 18: [Um pelicano andando de bicicleta em 3D](https://x.com/nehstrr3/status/2120953932692537722) (por [@nehstrr3](https://x.com/nehstrr3))

**Use um personagem em movimento para inspecionar coordenação, movimento e consistência da cena.**

O criador apresenta um pelicano animado em 3D andando de bicicleta e identifica o modelo como Hydrogen em XHigh. A publicação demonstra um resultado, não uma instrução completa reproduzível nem uma validação física.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-19"></a>
### Caso 19: [Um simulador planetário que começa pelo planejamento](https://x.com/The_Alex/status/2120950301318582643) (por [@The_Alex](https://x.com/The_Alex))

**Dê ao modelo de programação um plano concreto antes de pedir que edite uma cena complexa.**

O criador com acesso antecipado mostra um simulador planetário e relata melhores resultados de edição após fornecer planos mais detalhados. A fonte credita a ideia ao ForwardEditor e descreve um fluxo iterativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-20"></a>
### Caso 20: [Uma ilha portuária com Antigravity Swarm](https://x.com/ai_for_success/status/2120942147780464660) (por [@ai_for_success](https://x.com/ai_for_success))

**Use um pequeno ambiente navegável para inspecionar como vários agentes constroem cenas.**

O criador declarou acesso antecipado e mostra uma ilha portuária construída com Hydrogen no recurso Swarm do Antigravity. A publicação pública não especifica toda a orquestração nem o histórico de instruções.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-21"></a>
### Caso 21: [Uma ilha flutuante com a Torre Eiffel](https://x.com/RezAIT00/status/2120940988780736973) (por [@RezAIT00](https://x.com/RezAIT00))

**Avalie composição, movimento de câmera e código gerado em uma cena compacta de um monumento.**

A fonte mostra uma ilha em miniatura com a Torre Eiffel e a atribui ao Hydrogen XHigh. Os seis minutos de construção e gravação são um relato do autor, não um teste independente de tempo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-22"></a>
### Caso 22: [Uma cidade futurista sobrevoável](https://x.com/kimmonismus/status/2120940617169826037) (por [@kimmonismus](https://x.com/kimmonismus))

**Teste edições posteriores em um mundo procedural em vez de assumir que o primeiro resultado é final.**

O criador com acesso antecipado usou Hydrogen High no Antigravity e relata uma instrução adicional para produzir uma cidade Three.js com torres procedurais, chuva e tráfego aéreo. A gravação mostra código gerado em execução, não geração nativa de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-23"></a>
### Caso 23: [Um hidroavião do amanhecer à noite](https://x.com/LuminaBench/status/2120939312564842663) (por [@LuminaBench](https://x.com/LuminaBench))

**Inspecione os controles ambientais e as transições de iluminação em uma cena 3D interativa.**

A demonstração original do LuminaBench mostra um hidroavião e mudanças na hora do dia, sendo depois compartilhada pelo Google. A publicação é anterior ao limite registrado do lançamento público; a via de acesso e a invocação do modelo não foram verificadas independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

Tipo: Demo | Data: 2026-11-12

---


<a id="comparisons-limits"></a>
## 🧪 Comparações e limitações

<a id="case-24"></a>
### Caso 24: [Animação de bonecos de neon: Hydrogen e Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (por [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Compare a animação pronta com o tempo e o custo informados, sem pressupor ambientes de execução idênticos.**

O autor apresenta resultados do Hydrogen e do Opus 5.5 e informa $1.02 contra $7.43 e 10m 22s contra 34m. A coleção não verificou cobrança, instruções, número de iterações nem configurações de execução comparáveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-25"></a>
### Caso 25: [Tarefas robóticas e erros reconhecidos](https://x.com/ArtificialAnlys/status/2120995180891508833) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Inclua a conclusão de tarefas e o reconhecimento de pequenos erros em uma avaliação de robótica.**

A Artificial Analysis mostra tarefas de despejar líquido e arrumar blocos e diz que o Hydrogen percebeu um pequeno derramamento e uma tampa aberta. O vídeo e a classificação AA-Robotics v0.1 vêm do avaliador; aqui não são reproduzidos independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-26"></a>
### Caso 26: [Uma célula de trabalho de laboratório em linguagem natural](https://x.com/danielmckinn0n/status/2120990834246173125) (por [@danielmckinn0n](https://x.com/danielmckinn0n))

**Avalie a execução de ferramentas e o tratamento de falhas separadamente das principais pontuações das avaliações.**

A fonte mostra uma célula de trabalho de laboratório acionada por um pedido em linguagem natural e relata resultados em quatro avaliações ligadas a laboratórios. A pontuação informada do Hydrogen no RareBench é menor que a do Opus 5.5, enquanto as outras três são maiores; é uma demonstração do responsável pelas avaliações, não uma validação médica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-27"></a>
### Caso 27: [Iceberg e rebocador: Hydrogen e Carbon](https://x.com/EnvolDev/status/2120989670582677930) (por [@EnvolDev](https://x.com/EnvolDev))

**Registre o nível de raciocínio e as restrições do ambiente ao comparar uma construção 3D longa.**

O criador relata ambos os modelos em High via OpenRouter, com Hydrogen a $4.27 e 1h 23m 40s contra Carbon a $8.83 e 2h 39m 10s. São resultados não controlados relatados pela fonte, não proporções universais de preço ou velocidade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-28"></a>
### Caso 28: [Um lago gelatinoso de carpas koi: Hydrogen e Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (por [@Haleeeemahh](https://x.com/Haleeeemahh))

**Inspecione uma cena concreta antes de transformar uma classificação de avaliação em uma escolha de modelo.**

O autor compara Hydrogen e Sonnet 5.5 em uma tarefa de lago de carpas koi em 3D. A fonte pede que o público julgue os resultados, mas não estabelece configurações equivalentes nem uma pontuação objetiva de qualidade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-29"></a>
### Caso 29: [Uma coleção de programação criativa com instruções compartilhadas](https://x.com/kickingkeys/status/2120985358317875222) (por [@kickingkeys](https://x.com/kickingkeys))

**Use um conjunto variado de tarefas visuais para evitar generalizar a partir de um único resultado atraente.**

O criador relata ter dado as mesmas instruções ao Hydrogen, Carbon e Argon e coloca comparações nas respostas. A mídia da publicação principal mostra animais com poucos polígonos, uma rua de neon e um recipiente em estilo aquarela; não é uma avaliação controlada completa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-30"></a>
### Caso 30: [Vóxeis de Megamind: um contraexemplo de custo e qualidade](https://x.com/thehypedotnews/status/2120980737012670720) (por [@thehypedotnews](https://x.com/thehypedotnews))

**Mantenha os casos de falha ao avaliar se um modelo é consistentemente mais barato ou visualmente melhor.**

A fonte diz que o Hydrogen produziu uma figura de Titan menos coerente ao custo de $36.07, contra $8.64 do Sonnet 5.5. A publicação inclui promoção comercial, e os custos e o julgamento de qualidade são alegações do publicador.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

Tipo: Limit | Data: 2026-11-12

---

<a id="case-31"></a>
### Caso 31: [Um leão malabarista nas quatro estações](https://x.com/SahilPanhotra/status/2120978349967458704) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Confira o movimento solicitado, não apenas o acabamento visual da interface ao redor.**

O autor relata que o Carbon executou os arcos cruzados dos malabares enquanto o Hydrogen deixou as bolas flutuando, apesar de transições de estações e recortes mais limpos. Essa comparação SVG da mesma tarefa revela uma falha específica de movimento, não uma classificação geral dos modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

Tipo: Limit | Data: 2026-11-12

---

<a id="case-32"></a>
### Caso 32: [Luta de bonecos com três modelos: resultado mais lento e caro](https://x.com/DanielZambrini/status/2120963180461769183) (por [@DanielZambrini](https://x.com/DanielZambrini))

**Preserve contraexemplos ao comparar a eficiência anunciada de um modelo com relatos de tarefas reais.**

O criador compara Hydrogen, Carbon e Argon e relata que o Hydrogen levou mais tempo e custou mais que o Carbon nesse teste. Configurações, cobrança e número de iterações não foram verificados independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

Tipo: Limit | Data: 2026-11-12

---

<a id="case-33"></a>
### Caso 33: [Uma cena de bicicleta na fazenda: Hydrogen e Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (por [@Bhavani_00007](https://x.com/Bhavani_00007))

**Compare o movimento e a qualidade da cena com o tempo de conclusão informado pelo criador.**

A fonte compara Hydrogen e Gemini 3.8 Flash em uma cena de bicicleta na fazenda e relata 56 segundos contra mais de seis minutos. É um teste de um único criador, não uma avaliação geral de velocidade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-34"></a>
### Caso 34: [Uma menina e um gato em bicicletas tandem](https://x.com/marcthecreatorr/status/2120956699951628637) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Compare a fidelidade à instrução e os detalhes adicionais, deixando visíveis as diferenças entre os ambientes de programação.**

O criador usou a mesma tarefa SVG declarada, mas executou Opus 5.5 no Claude Code e Hydrogen no Cursor. Tempo e custo informados diferem bastante, mas ambientes diferentes e iterações não divulgadas impedem uma comparação controlada apenas dos modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-35"></a>
### Caso 35: [Quatro modelos constroem um jogo de Mario em Three.js](https://x.com/StatsWire/status/2120955723396071548) (por [@StatsWire](https://x.com/StatsWire))

**Registre as diferenças de raciocínio antes de interpretar uma comparação de jogos com a mesma instrução.**

A fonte compara Gemini 3.8 Flash, Argon e Carbon em High com Hydrogen em XHigh, usando apenas Three.js sem modelos 3D ou texturas externos. Ela mostra quatro resultados, não uma avaliação com raciocínio equivalente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-36"></a>
### Caso 36: [Três modelos Gemini desenham um controle](https://x.com/notjazii/status/2120952314873987271) (por [@notjazii](https://x.com/notjazii))

**Procure regressões e melhorias específicas da tarefa em vez de pressupor uma hierarquia entre modelos da família.**

O criador compara controles SVG do Carbon, Argon e Hydrogen e relata ter repetido o teste. Durações e custos informados são alegações da fonte e não estabelecem uma ordem geral de qualidade dos modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-37"></a>
### Caso 37: [Respostas visuais diferentes entre o aplicativo e o Studio](https://x.com/thegenioo/status/2120946497802174688) (por [@thegenioo](https://x.com/thegenioo))

**Teste a mesma imagem no produto que pretende usar antes de confiar em um resultado visual.**

A fonte mostra respostas conflitantes de identificação de alimentos atribuídas ao Hydrogen no aplicativo Gemini e no AI Studio. A comparação não verifica independentemente se o roteamento, as configurações ou o contexto completo da conversa são idênticos.

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

Tipo: Limit | Data: 2026-11-12

---

<a id="case-38"></a>
### Caso 38: [Uma cena de lançamento de foguete: Hydrogen e Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (por [@Bhavani_00007](https://x.com/Bhavani_00007))

**Compare a animação real do lançamento e também a duração de construção informada.**

O criador apresenta resultados do Hydrogen e do Gemini 3.8 Flash e relata menos de um minuto contra aproximadamente três minutos. A comparação visual é de uma tarefa sem configuração de execução controlada independentemente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-39"></a>
### Caso 39: [Quatro tarefas de animação SVG](https://x.com/Angaisb_/status/2120944947193127061) (por [@Angaisb_](https://x.com/Angaisb_))

**Use vários temas de interação e animação para inspecionar a consistência entre tarefas.**

A fonte apresenta pares de resultados do Hydrogen e do Carbon para transferências, mudanças de dia e noite, abertura de caixa e um camaleão. Seu breve texto principal não revela instruções completas, evidências de tempo nem um método objetivo de pontuação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-40"></a>
### Caso 40: [Três modelos animam um cavalo na savana](https://x.com/AI_Screening/status/2120944276586823689) (por [@AI_Screening](https://x.com/AI_Screening))

**Inspecione diretamente o movimento e os detalhes visuais antes de aceitar alegações amplas sobre custo ou qualidade.**

O criador apresenta Hydrogen, Carbon e Argon em uma cena de cavalo na savana. As alegações de maior velocidade, menor custo e alta qualidade continuam sendo a avaliação da fonte, não uma comparação controlada reproduzida aqui.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="related-repositories"></a>
## Repositórios relacionados

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Exemplos e comparações do Gemini 4 Carbon

<a id="acknowledge"></a>
## 🙏 Agradecimentos

Obrigado aos criadores, desenvolvedores e avaliadores que compartilharam publicamente seu trabalho com o Hydrogen.

**Criadores das fontes:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening)

*A atribuição segue as fontes públicas citadas e pode não identificar o criador original. Para correções ou solicitações de remoção, abra uma questão com uma fonte pública.*

Sugira um exemplo respaldado por fontes por meio de uma questão ou solicitação de integração, seguindo a lista de contribuição.
