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

**225 exemplos mostram como o Hydrogen é usado e em que pontos os resultados ficaram aquém.**

Cada caso inclui um link para a fonte e os créditos do autor. Demonstrações, exemplos do fornecedor e comparações de criadores são identificados nas notas; instruções ausentes não são reconstruídas.

## 📊 Visão geral

- 225 casos no total. Em 17 de novembro, foram adicionados 185 após a análise de 1.304 publicações do X. As novas fontes tinham mais de 30 curtidas na coleta.
- Cinco categorias abrangem agentes, aprendizado e aplicativos, planilhas e Search, 3D interativo, e comparações e limitações.
- 264 materiais visuais originais, incluindo 168 vídeos reproduzíveis com imagem de capa e 96 imagens.
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
| [⚡ Agentes e fluxos de programação](#agents) | 30 |
| [💻 Aplicativos e aprendizagem](#apps-learning) | 37 |
| [📊 Planilhas e Search](#data-search) | 9 |
| [🎮 3D interativo e interfaces](#interactive-3d) | 48 |
| [🧪 Comparações e limitações](#comparisons-limits) | 101 |
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
| [De referências espaciais a uma cena HTML](#case-41) | 3D interativo e interfaces | Use algumas referências para testar se uma cena gerada conserva um estilo reconhecível. | Demo |
| [Um protótipo de Fórmula 1 no Gemini Canvas](#case-42) | 3D interativo e interfaces | Inclua vários ângulos de câmera para examinar um veículo gerado. | Demo |
| [Hydrogen pela API e Carbon no Antigravity](#case-43) | Comparações e limitações | Registre o ambiente de cada execução ao comparar imagens geradas com a mesma instrução. | Evaluation |
| [Sombras na comparação entre Hydrogen e Astra](#case-44) | Comparações e limitações | Avalie detalhes de renderização junto com o custo e o tempo de ambas as execuções. | Evaluation |
| [Comparação de movimento 3D procedural](#case-45) | Comparações e limitações | Registre o tempo de geração ao comparar a continuidade e a composição das animações. | Evaluation |
| [Um teste visual de 89 minutos no PokéBench](#case-46) | Comparações e limitações | Registre turnos e falhas de API junto com o resultado de um teste prolongado de agente visual. | Benchmark |
| [Hydrogen e DeepSeek criam a mesma cena 3D](#case-47) | Comparações e limitações | Registre tempo e custo de API separadamente ao comparar os resultados visuais. | Evaluation |
| [Vista lateral de um BMW em SVG](#case-48) | 3D interativo e interfaces | Use uma vista lateral em SVG para avaliar as proporções, a silhueta e os detalhes do veículo. | Demo |
| [A ilha flutuante de um astrônomo](#case-49) | 3D interativo e interfaces | Dê um tema claro a uma cena pequena e verifique se objetos e iluminação o reforçam. | Demo |
| [De uma imagem a uma paisagem 3D explorável](#case-50) | 3D interativo e interfaces | Verifique se uma cena baseada em imagem mantém a aparência e permite deslocamento. | Demo |
| [Um diorama em miniatura com blocos 3D](#case-51) | 3D interativo e interfaces | Peça uma miniatura de blocos e confira se as formas compõem uma cena coerente. | Demo |
| [Uma cerejeira florida interativa](#case-52) | 3D interativo e interfaces | Use um objeto animado e alguns controles para explorar mudanças em tempo real. | Demo |
| [Tempo e custo por tarefa no Agent Arena](#case-53) | Comparações e limitações | Compare latência, custo e tokens de saída por tarefa com a taxa de sucesso geral. | Benchmark |
| [Testes de documentos visuais e de terminal](#case-54) | Comparações e limitações | Considere separadamente os resultados em documentos e terminal ao escolher o orçamento de raciocínio. | Benchmark |
| [Resultados no Vals Index e no Tax Agent](#case-55) | Comparações e limitações | Consulte o resultado em uma tarefa especializada junto com a avaliação agregada. | Benchmark |
| [Hydrogen no CursorBench com raciocínio padrão](#case-56) | Comparações e limitações | Use a pontuação padrão como referência para testar seu próprio repositório. | Benchmark |
| [Quatro modelos animam uma batalha de arqueiros](#case-57) | Comparações e limitações | Compare a clareza das ações em cada animação. | Evaluation |
| [Um protótipo estilo Minecraft em quinze minutos](#case-58) | Aplicativos e aprendizagem | Use um ambiente de voxels para verificar como mineração e inventário funcionam juntos. | Demo |
| [Um fluxo com ferramentas do Hydrogen no n8n](#case-59) | Agentes e fluxos de programação | Delegue ao Hydrogen as chamadas de ferramentas no n8n e mantenha o planejamento à parte. | Integration |
| [Um agente da Box para documentos empresariais complexos](#case-60) | Planilhas e Search | Meça precisão, tempo e tokens em uma carga realista de documentos. | Benchmark |
| [Hydrogen no FrontierCode da Devin](#case-61) | Comparações e limitações | Avalie se os patches podem ser integrados e registre o ambiente de cada agente. | Benchmark |
| [Refração em uma animação interativa pequena](#case-62) | 3D interativo e interfaces | Use prévias rápidas para refinar um efeito óptico antes de ampliar a cena. | Demo |
| [Um rio que corre para cima](#case-63) | 3D interativo e interfaces | Teste um sentido de movimento incomum e avalie o efeito visualmente. | Demo |
| [Busca na web apesar de uma restrição explícita](#case-64) | Comparações e limitações | Confira se o modelo evitou ferramentas quando o fluxo exige uma resposta sem navegação. | Limit |
| [Consumo de cota num Swarm do Antigravity](#case-65) | Comparações e limitações | Registre o volume de tokens e a cota consumida em uma execução multiagente. | Evaluation |
| [Chamadas de ferramentas em tarefas profissionais](#case-66) | Comparações e limitações | Observe como um agente reúne contexto antes de agir em tarefas profissionais. | Benchmark |
| [Um retrato em 3D com Hydrogen](#case-67) | 3D interativo e interfaces | Use um retrato para verificar se a representação 3D é reconhecível. | Demo |
| [Quatro modelos animam um mago e um dragão](#case-68) | Comparações e limitações | Compare encenação, clareza da ação e efeitos em versões da mesma cena. | Evaluation |
| [Rota de autenticação num fluxo multiagente](#case-69) | Agentes e fluxos de programação | Verifique qual cliente se autentica quando um agente delega a tarefa a outro provedor. | Limit |
| [Uma execução de Goal Mode no Antigravity](#case-70) | Agentes e fluxos de programação | Acompanhe planejamento, mudanças no código e resultados dos testes em sessões longas. | Demo |
| [MazeBench mostra taxas de sucesso baixas](#case-71) | Comparações e limitações | Teste labirintos antes de depender do raciocínio espacial. | Benchmark |
| [Três modelos Gemini criam cenas de veleiros](#case-72) | Comparações e limitações | Compare movimento e detalhes do ambiente em uma cena temática no Three.js. | Evaluation |
| [Carbon e Hydrogen no Antigravity Orchestrator](#case-73) | Agentes e fluxos de programação | Recorra ao planejador quando o modelo de implementação mais rápido encontra um bloqueio. | Integration |
| [Gráfico e relatório a partir de dados do Workspace](#case-74) | Planilhas e Search | Veja se uma nova interação corrige lacunas da análise, do gráfico ou do relatório. | Demo |
| [A leitura de um número de camisa esgota o orçamento](#case-75) | Comparações e limitações | Defina um limite de raciocínio e uma alternativa ao ler um detalhe pequeno em uma imagem. | Limit |
| [Comparação de famílias de modelos no ClutterBench](#case-76) | Comparações e limitações | Use um teste com elementos sobrepostos para verificar se os pontos fortes gerais do modelo se aplicam à tarefa. | Benchmark |
| [De um resumo de notícias a um vídeo narrado](#case-77) | Aplicativos e aprendizagem | Transforme notícias pesquisadas em um vídeo curto e confira os fatos mencionados. | Demo |
| [Um busto anatômico em corte no estilo Minecraft](#case-78) | Comparações e limitações | Verifique se um corte gerado contém as estruturas internas solicitadas. | Evaluation |
| [Três modelos renderizam o mesmo objeto](#case-79) | Comparações e limitações | Acompanhe tokens e qualidade separadamente quando um modelo mais barato puder consumir mais tokens. | Evaluation |
| [Raciocínio indutivo e consumo de tokens](#case-80) | Comparações e limitações | Acompanhe os tokens de entrada e saída faturados junto com a nota de raciocínio. | Benchmark |
| [Arte em pixels em diferentes modos do Gemini](#case-81) | Planilhas e Search | Use a mesma tarefa de desenho no Google Sheets para comparar opções de modelo. | Evaluation |
| [Um apartamento impresso em 3D a partir de imagem](#case-82) | 3D interativo e interfaces | Leve um teste de imagem para 3D até a impressão física. | Demo |
| [Três modelos animam um animal em 3D](#case-83) | Comparações e limitações | Observe anatomia e movimento no mesmo teste de modelagem. | Evaluation |
| [Hydrogen e Qwen no ts-bench](#case-84) | Comparações e limitações | Analise falhas de chamadas a ferramentas junto com a avaliação geral. | Benchmark |
| [Simulação de negócios no Vending-Bench](#case-85) | Comparações e limitações | Compare a receita simulada com o custo de operar o agente. | Benchmark |
| [Uma cena náutica com o Golden Merry](#case-86) | 3D interativo e interfaces | Use um navio fictício conhecido para testar a composição náutica estilizada. | Demo |
| [Hydrogen no OpenClaw](#case-87) | Agentes e fluxos de programação | Confira a seleção de modelo no sistema de agentes que você vai usar. | Integration |
| [Uma baleia entre nuvens](#case-88) | 3D interativo e interfaces | Analise separadamente o movimento da criatura e o desenho dos olhos. | Demo |
| [Quatro modelos constroem uma ilha em miniatura](#case-89) | Comparações e limitações | Compare os projetos junto com o tempo e o preço do ambiente de cada execução. | Evaluation |
| [Desenho no ar com uma webcam](#case-90) | Aplicativos e aprendizagem | Trace linhas e observe se a interface de desenho acompanha seus movimentos. | Demo |
| [Rasgamento de tecidos em animações feitas com código](#case-91) | Comparações e limitações | Teste elasticidade, rasgos e interação com pelos na mesma instrução. | Evaluation |
| [Uma cidade submarina no Gemini Canvas](#case-92) | 3D interativo e interfaces | Comece com uma cena 3D pequena e acrescente áreas exploráveis e animais em várias etapas. | Demo |
| [Um portal web em uma tentativa](#case-93) | Aplicativos e aprendizagem | Examine o layout inicial antes de testar fluxos individuais. | Demo |
| [Verificação de fatos com fonte inacessível](#case-94) | Comparações e limitações | Exija uma referência consultável antes de agir com base no veredito sobre uma captura. | Limit |
| [Um simulador urbano no estilo Cities: Skylines](#case-95) | Aplicativos e aprendizagem | Prototipe um construtor de cidades e veja como controles e simulações se integram. | Demo |
| [Hydrogen e Sol desenham um pelicano em 2D](#case-96) | Comparações e limitações | Compare duração e movimento numa tarefa simples de animação 2D. | Evaluation |
| [Uma sala do trono com Blender MCP](#case-97) | Agentes e fluxos de programação | Use Blender MCP para inspecionar no editor a composição de uma cena gerada. | Integration |
| [Quatro modelos criam um jogo de balanço em teias](#case-98) | Comparações e limitações | Compare deslocamento e controles em jogos com a mesma restrição de arquivo único. | Evaluation |
| [Um navio pirata em tons de cinza no Three.js](#case-99) | 3D interativo e interfaces | Limite a cena a tons de cinza e confira se a luz ainda revela a geometria. | Demo |
| [Quatro modelos fazem um diorama arquitetônico](#case-100) | Comparações e limitações | Compare os resultados com o mesmo briefing e observe as diferentes soluções de iluminação. | Evaluation |
| [Uma luminária paramétrica no CadXStudio](#case-101) | 3D interativo e interfaces | Inspecione dimensões e editabilidade das peças de um CAD gerado. | Integration |
| [Uma trilha de santuário animada em C++](#case-102) | 3D interativo e interfaces | Use uma cena pequena em código nativo para testar uma animação sem ferramentas web. | Demo |
| [Três modelos renderizam uma cena de trem](#case-103) | Comparações e limitações | Use a mesma cena para comparar tempos nas configurações escolhidas. | Evaluation |
| [Uma Chinatown chuvosa com raciocínio Extra](#case-104) | Comparações e limitações | Meça a duração e confira o resultado antes de definir o nível de raciocínio de uma animação grande. | Evaluation |
| [Uma vila construída em 30 módulos](#case-105) | 3D interativo e interfaces | Gere a cena em módulos e revise o conjunto depois de integrá-los. | Demo |
| [Três modelos criam um visualizador de planetas](#case-106) | Comparações e limitações | Compare uma interface científica visual com a mesma instrução em diferentes modelos. | Evaluation |
| [Quatro modelos recriam o Chrome Dino](#case-107) | Comparações e limitações | Cronometre as recriações de um jogo conhecido e compare os resultados jogáveis. | Evaluation |
| [Uma agência dos correios em uma ilha flutuante](#case-108) | 3D interativo e interfaces | Peça um prédio em miniatura e avalie o efeito dos materiais e da iluminação. | Demo |
| [Dois agentes de programação constroem navios diferentes](#case-109) | Comparações e limitações | Compare o primeiro resultado aproveitável e o custo de revisão no ambiente escolhido. | Evaluation |
| [Água e peixes em um jardim de carpas](#case-110) | 3D interativo e interfaces | Use peixes em movimento para verificar a coerência dos reflexos e da iluminação da água. | Demo |
| [Quatro modelos simulam um cerco com trabuco](#case-111) | Comparações e limitações | Compare protótipos jogáveis de física na mesma tarefa e registre os níveis de raciocínio. | Evaluation |
| [Uma cena 3D ao vivo no aplicativo Gemini](#case-112) | 3D interativo e interfaces | Prototipe iluminação interativa e partículas na interface web do Gemini. | Demo |
| [Montagem de uma betoneira em CAD no navegador](#case-113) | Agentes e fluxos de programação | Revise a árvore de peças e os encaixes antes de usar o conjunto em CAD. | Integration |
| [Modelagem procedural de um machado no Blender](#case-114) | Agentes e fluxos de programação | Use uma silhueta de referência e revise o modelo em várias inspeções na vista 3D. | Integration |
| [Uma cena 3D cor-de-rosa em um único HTML](#case-115) | 3D interativo e interfaces | Teste uma cena Three.js sem recursos externos e confira se a composição é legível. | Demo |
| [Memória persistente no FrontierMemory](#case-116) | Comparações e limitações | Compare desempenho e gasto por execução ao escolher um modelo para memória de longo prazo. | Benchmark |
| [Hydrogen em um agente de voz LiveKit com falhas](#case-117) | Comparações e limitações | Provoque uma falha controlada e verifique se o agente relata resultados sem evidência. | Evaluation |
| [Ember Isle em 28 módulos](#case-118) | Agentes e fluxos de programação | Divida uma cena grande em módulos e acompanhe a duração de cada geração. | Demo |
| [Simulação do Big Bang feita só com código](#case-119) | 3D interativo e interfaces | Use uma animação curta como protótipo de explicação e confira o rigor científico. | Demo |
| [Um helicóptero com vistas explodidas](#case-120) | 3D interativo e interfaces | Teste se um protótipo 3D combina controle de voo e modos de inspeção úteis. | Demo |
| [Hydrogen Express com raio X e malha](#case-121) | 3D interativo e interfaces | Acrescente modos de inspeção a um protótipo 3D controlável. | Demo |
| [Um posto de abastecimento no céu](#case-122) | 3D interativo e interfaces | Inclua objetos móveis e estados de iluminação para demonstrar o comportamento da cena. | Demo |
| [Três modelos Gemini animam um ciclista](#case-123) | Comparações e limitações | Compare cenas curtas com o mesmo briefing e registre a duração de cada execução. | Evaluation |
| [Um livro de química vira aula interativa](#case-124) | Aplicativos e aprendizagem | Monte uma aula autônoma com dicas, narração e texto opcional. | Demo |
| [Um protótipo de música Vocaloid](#case-125) | Aplicativos e aprendizagem | Confira se uma composição de uma tentativa atende ao personagem e ao estilo solicitados. | Demo |
| [Dois modelos constroem um mundo LEGO](#case-126) | Comparações e limitações | Compare a parte do mundo que cada modelo consegue criar no tempo disponível. | Evaluation |
| [Correção de bugs reintroduzidos em dois repositórios](#case-127) | Comparações e limitações | Introduza falhas conhecidas para medir o que o agente consegue detectar e corrigir. | Benchmark |
| [Boneco palito contra o cursor em dois modelos](#case-128) | Comparações e limitações | Compare como as animações interativas respondem ao ponteiro. | Evaluation |
| [Um moinho d’água em um único HTML](#case-129) | 3D interativo e interfaces | Teste um protótipo 3D rápido com uma paisagem pequena e elementos móveis reconhecíveis. | Demo |
| [Dois modelos renderizam uma paisagem de montanha](#case-130) | Comparações e limitações | Compare composição, tempo de geração e custo separadamente em uma paisagem animada. | Evaluation |
| [Tradução do inglês para o persa em ambiente próprio](#case-131) | Comparações e limitações | Avalie um trecho difícil com uma referência produzida por uma pessoa. | Evaluation |
| [Uma cena no Blender com Hydrogen Extra](#case-132) | 3D interativo e interfaces | Confirme geometria e materiais no Blender antes de ampliar os detalhes. | Demo |
| [Quatro modelos criam um navio afundando](#case-133) | Comparações e limitações | Meça fidelidade visual, tempo e custo separadamente para a mesma cena. | Evaluation |
| [Leitura de uma integral densa a partir de imagem](#case-134) | Aplicativos e aprendizagem | Confira se o modelo reconhece limites iguais antes de tentar simplificar uma expressão longa. | Evaluation |
| [Comparação cega de redação com quatro modelos](#case-135) | Comparações e limitações | Oculte os nomes dos modelos antes de escolher o texto a utilizar. | Evaluation |
| [Detecção visual e leitura por nível de raciocínio](#case-136) | Comparações e limitações | Meça separadamente precisão da detecção e leitura, custo e latência em cada nível. | Benchmark |
| [Quatro modelos recriam a casa de Up](#case-137) | Comparações e limitações | Compare as escolhas de modelagem 3D com a mesma imagem e o mesmo briefing. | Evaluation |
| [Uma enciclopédia da célula humana em WebGL2](#case-138) | Aplicativos e aprendizagem | Use um corte interativo para ensinar as relações espaciais da célula. | Demo |
| [Duas animações de partículas com Hydrogen](#case-139) | 3D interativo e interfaces | Compare cenas de partículas para observar forma e movimento em efeitos simples. | Demo |
| [Um oponente que só vê o tabuleiro no Parking Bench](#case-140) | Aplicativos e aprendizagem | Teste um oponente de quebra-cabeça que recebe apenas uma imagem do tabuleiro como estado. | Integration |
| [Um vídeo com instruções de Google Docs](#case-141) | Aplicativos e aprendizagem | Use capturas e indicações numeradas para ensinar um fluxo de edição no celular. | Demo |
| [Um seletor de dia e noite num mundo em miniatura](#case-142) | 3D interativo e interfaces | Use um seletor simples para testar a continuidade da animação entre os estados. | Demo |
| [Um cenário construído em 65 módulos](#case-143) | 3D interativo e interfaces | Acompanhe o tempo e o esforço de integração conforme a cena cresce. | Demo |
| [Uma dança com câmera fixa](#case-144) | Comparações e limitações | Verifique se uma animação de referência mantém desenho, composição e câmera. | Evaluation |
| [Um agente de programação fica preso no teste inicial](#case-145) | Comparações e limitações | Defina um tempo máximo e acompanhe o progresso do teste de referência antes de esperar uma correção. | Limit |
| [Um ambiente BASIC para o MZ-1500](#case-146) | Aplicativos e aprendizagem | Prototipe um BASIC retrô e verifique o suporte a periféricos. | Demo |
| [Dois modelos criam um braço robótico interativo](#case-147) | Comparações e limitações | Cheque se as juntas do braço em Three.js reagem de forma coerente à interação. | Evaluation |
| [Um mapa jogável de uma suspensão de voos da FAA](#case-148) | Planilhas e Search | Use um mapa e uma linha do tempo para mostrar por que a fila persiste depois do fim da suspensão. | Demo |
| [Um jardim em miniatura com pagode](#case-149) | 3D interativo e interfaces | Confira se uma miniatura gerada equilibra arquitetura e paisagismo. | Demo |
| [Planejar, executar e revisar com modelos distintos](#case-150) | Agentes e fluxos de programação | Separe as funções e compare os totais por tarefa de cada modelo. | Demo |
| [Hydrogen e Sol constroem uma vila nevada](#case-151) | Comparações e limitações | Avalie duração, gasto e qualidade da cena como resultados separados. | Evaluation |
| [Uma ilha em Three.js com níveis High e Ultra](#case-152) | Comparações e limitações | Compare aspecto e duração considerando os níveis de raciocínio, sem equiparar cotas de produtos distintos. | Evaluation |
| [Diorama de aeródromo da Segunda Guerra Mundial](#case-153) | 3D interativo e interfaces | Inclua referências e requisitos de movimento mecânico para testar além da aparência. | Demo |
| [Configurando Hydrogen em um cliente de código](#case-154) | Agentes e fluxos de programação | Use o identificador exato do modelo ao configurar uma chave da API Google em um cliente compatível. | Tutorial |
| [Uma equipe de pesquisa SuperARIS com Hydrogen](#case-155) | Agentes e fluxos de programação | Delegue tarefas específicas de pesquisa e redação ao Hydrogen em uma equipe de agentes. | Integration |
| [Quatro modelos reescrevem um módulo do zero](#case-156) | Agentes e fluxos de programação | Compare compreensão do código, projeto da solução e implementação ao avaliar uma reescrita. | Evaluation |
| [Comparação dos detalhes de um controle PS5 em 3D](#case-157) | Comparações e limitações | Observe o sombreamento dos botões e os detalhes da parte traseira. | Evaluation |
| [Muse delega tarefas ao Antigravity CLI](#case-158) | Agentes e fluxos de programação | Conecte um assistente remoto a um ambiente local e escolha um modelo padrão de redação. | Integration |
| [CursorBench com diferentes orçamentos de raciocínio](#case-159) | Comparações e limitações | Compare taxas de sucesso entre níveis antes de definir uma configuração mais rápida. | Benchmark |
| [Três modelos renderizam um templo estelar](#case-160) | Comparações e limitações | Meça a estabilidade da renderização separadamente do detalhe visual. | Evaluation |
| [Um jogo de tiro em HTML em um minuto](#case-161) | Aplicativos e aprendizagem | Use um HTML para testar controles básicos e feedback de um jogo de tiro. | Demo |
| [Reavaliação de um desenho de migração existente](#case-162) | Comparações e limitações | Peça aos agentes que considerem se a migração deve substituir a arquitetura atual. | Limit |
| [Conversas com Hydrogen no AITuber OnAir](#case-163) | Aplicativos e aprendizagem | Experimente Hydrogen como modelo de conversa por trás de um avatar Live2D. | Integration |
| [Um vídeo promocional feito por código](#case-164) | Aplicativos e aprendizagem | Passe um briefing promocional curto e revise os elementos gráficos em movimento. | Demo |
| [Dois modelos criam um jogo de fuga de um templo](#case-165) | Comparações e limitações | Compare se iluminação e clima tornam o mesmo jogo legível. | Evaluation |
| [Três modelos Gemini animam um buggy de rali](#case-166) | Comparações e limitações | Verifique se a suspensão e a aderência fazem sentido em uma curva inclinada. | Evaluation |
| [Um pisco animado de forma procedural](#case-167) | 3D interativo e interfaces | Examine o movimento do corpo e das asas numa animação de voo gerada. | Demo |
| [Escolhendo entre Orchestrator e Swarm no Antigravity](#case-168) | Agentes e fluxos de programação | Use repasses entre modelos nas tarefas sequenciais e agentes independentes com revisores nas paralelas. | Tutorial |
| [Dois modelos animam Chasing Views](#case-169) | Comparações e limitações | Compare resultado e duração com o nível de raciocínio de cada modelo em vista. | Evaluation |
| [Velocidade e custo no Design Creativity Bench](#case-170) | Comparações e limitações | Compare tempo e custo por projeto com a nota de criatividade. | Benchmark |
| [De uma imagem de referência ao CAD no SolidWorks](#case-171) | Agentes e fluxos de programação | Use uma imagem 3D para avaliar o fluxo de modelagem do agente no SolidWorks. | Integration |
| [Quatro modelos animam um galope no deserto](#case-172) | Comparações e limitações | Compare o contato das patas e a transferência de peso antes de julgar luz e detalhes da malha. | Evaluation |
| [Uma apresentação sobre a sincronicidade de Jung](#case-173) | Aplicativos e aprendizagem | Teste a geração de slides em um tema que exija explicar bem conceitos relacionados. | Demo |
| [Pesquisa em computação no FrontierCS 2](#case-174) | Comparações e limitações | Use um teste de pesquisa ao lado da programação comum e registre o ambiente. | Benchmark |
| [Quatro modelos em Rio Above the Clouds](#case-175) | Comparações e limitações | Compare custo, duração e qualidade percebida com o mesmo briefing criativo. | Evaluation |
| [Hydrogen em tarefas técnicas do GBENCH](#case-176) | Comparações e limitações | Use resultados verificáveis de programação e de outras tarefas junto com preço e duração. | Benchmark |
| [Treinamento de carros para estacionar em paralelo](#case-177) | Comparações e limitações | Compare o progresso do aprendizado e as taxas finais de sucesso em simulações geradas. | Evaluation |
| [Um motor mitocondrial manipulável](#case-178) | Aplicativos e aprendizagem | Use um diagrama interativo para conectar movimento molecular à produção de ATP. | Demo |
| [Um jogo de território no estilo Qix](#case-179) | Aplicativos e aprendizagem | Use um briefing curto de arcade para verificar se a primeira versão já é interativa. | Demo |
| [Geração de slides HTML com Hydrogen](#case-180) | Aplicativos e aprendizagem | Revise hierarquia e layout enquanto avalia a velocidade de geração de HTML. | Demo |
| [Hydrogen no Terminal-Bench 4.0](#case-181) | Comparações e limitações | Observe conclusão e custo das tarefas ao escolher um modelo de programação para terminal. | Benchmark |
| [Uma ilustração em um único arquivo HTML](#case-182) | 3D interativo e interfaces | Teste se uma referência visual pode ser recriada com código e sem recursos externos. | Demo |
| [Três modelos Gemini animam um polvo](#case-183) | Comparações e limitações | Observe se o contato com a rocha impulsiona o corpo quando o polvo se agarra. | Evaluation |
| [Um resumo estruturado do YouTube no Chrome](#case-184) | Planilhas e Search | Peça ao Gemini no Chrome um resumo com marcas de tempo e fontes claras para o contexto adicional. | Tutorial |
| [Uma aula vira um vídeo curto](#case-185) | Aplicativos e aprendizagem | Verifique precisão didática e ritmo ao transformar uma aula em vídeo. | Demo |
| [Animação de um papagaio-do-mar a partir de cena estática](#case-186) | 3D interativo e interfaces | Use uma cena HTML existente como primeiro quadro de uma animação procedural. | Demo |
| [Um teste de modelagem de castelos](#case-187) | Comparações e limitações | Compare os castelos e o consumo de recursos em diferentes execuções. | Evaluation |
| [Uso do navegador em um Swarm do Antigravity](#case-188) | Agentes e fluxos de programação | Inspecione a atividade no navegador junto com as tarefas dos agentes. | Demo |
| [Repasse de pesquisa ao Muse pelo Google Drive](#case-189) | Agentes e fluxos de programação | Use uma pasta monitorada quando outro agente for assumir a próxima etapa. | Integration |
| [Um guia de flauta doce no Gemini Canvas](#case-190) | Aplicativos e aprendizagem | Experimente o modo rápido para combinar partitura e instruções de prática. | Demo |
| [Uma estimativa muda com o aumento do escopo](#case-191) | Comparações e limitações | Peça que o modelo explique o escopo e as premissas sempre que a estimativa variar muito. | Limit |
| [Um Swarm do Antigravity anima um pelicano](#case-192) | Agentes e fluxos de programação | Distribua animação e áudio entre agentes e confira a cena montada. | Demo |
| [Uma pergunta de calendário com anos bissextos](#case-193) | Comparações e limitações | Use uma conversão simples para verificar se a resposta contempla casos especiais do calendário. | Evaluation |
| [TAJ VICE em um único arquivo HTML](#case-194) | Aplicativos e aprendizagem | Prototipe um mapa explorável em um arquivo e investigue os defeitos restantes. | Demo |
| [Antigravity em um projeto Google Cloud](#case-195) | Agentes e fluxos de programação | Confira como autenticação e cobrança funcionam ao habilitar Hydrogen com credenciais gerenciadas. | Tutorial |
| [Limites de assinatura desatualizados em uma resposta](#case-196) | Comparações e limitações | Consulte fontes primárias para confirmar os termos atuais e os nomes dos modelos. | Limit |
| [Revisão da narrativa de uma animação WebGL](#case-197) | Comparações e limitações | Peça uma história que avance com clareza se a primeira versão for complexa visualmente, mas sem progressão. | Limit |
| [Carbon planeja e Hydrogen implementa um aplicativo móvel](#case-198) | Agentes e fluxos de programação | Delegue o desenho das interações ao planejador e separe a implementação. | Demo |
| [Dois modelos programam uma luta de dragões](#case-199) | Comparações e limitações | Compare como cada animação coordena dois personagens na mesma cena. | Evaluation |
| [Uma ilha 3D em miniatura com uma instrução](#case-200) | 3D interativo e interfaces | Confira se a cena organiza prédios, terreno e água de modo legível. | Demo |
| [Uma instrução reproduzível de pelicano em Three.js](#case-201) | Comparações e limitações | Confira se patas, rodas e direção se movem de forma coordenada. | Evaluation |
| [Hydrogen no T3 Code](#case-202) | Agentes e fluxos de programação | Teste um cliente dedicado e monitore cotas móvel e semanal durante uma sessão realista. | Integration |
| [Um vídeo de utilidade pública em estilo desenhado à mão](#case-203) | Aplicativos e aprendizagem | Use uma mensagem curta de utilidade pública para avaliar uma estética de desenho. | Demo |
| [Um pavão ciclista em dez estilos de arte](#case-204) | Agentes e fluxos de programação | Use um grupo de modelos para programar transições visuais e sincronizar o som. | Demo |
| [Uma instrução sobre uma cabana em três plataformas](#case-205) | Comparações e limitações | Confira o formato de saída ao mover uma tarefa visual entre configurações e plataformas. | Evaluation |
| [Dois painéis com a mesma instrução](#case-206) | Comparações e limitações | Compare layout e hierarquia de informação usando o mesmo briefing de interface. | Evaluation |
| [Recriando o site React.gg a partir de imagem](#case-207) | Aplicativos e aprendizagem | Comece pela imagem de referência e veja quais detalhes ainda precisam de revisão. | Demo |
| [Um painel interativo sobre a singularidade](#case-208) | 3D interativo e interfaces | Prototipe uma sequência interativa curta em torno de um só conceito visual. | Demo |
| [Dois modelos animam uma cena com deslocamento lateral](#case-209) | Comparações e limitações | Observe continuidade de movimento e custo ao comparar cenas de ação. | Evaluation |
| [Gemini como treinador de corrida](#case-210) | Aplicativos e aprendizagem | Compare o registro do treino com as sugestões e ajuste as metas ao seu ponto de partida. | Demo |
| [Um jogo de navegador com pontos na blockchain](#case-211) | Aplicativos e aprendizagem | Teste a jogabilidade em um navegador de computador e revise separadamente o registro de pontos. | Demo |
| [Fórmulas sem renderização numa resposta em japonês](#case-212) | Comparações e limitações | Verifique apresentação e exatidão quando a resposta contém comandos TeX. | Limit |
| [Um aplicativo transforma instruções em MIDI](#case-213) | Aplicativos e aprendizagem | Prototipe uma ferramenta que leve um briefing em japonês até MIDI, WAV e piano roll. | Demo |
| [Teste de uma instrução para permanecer em silêncio](#case-214) | Comparações e limitações | Confira se o modelo consegue não responder quando o fluxo exige. | Evaluation |
| [Resumo de um show em uma página](#case-215) | Aplicativos e aprendizagem | Transforme informações de evento em um resumo visual fácil de consultar. | Demo |
| [Três modelos explicam um motor elétrico](#case-216) | Comparações e limitações | Compare clareza visual e controles didáticos com a mesma instrução de simulação. | Evaluation |
| [Dois fluxos animam uma cena de mesa](#case-217) | Comparações e limitações | Confira detalhes, volume e o quadro final imóvel em relação ao briefing. | Evaluation |
| [Uma montagem do cotidiano a partir de um avatar](#case-218) | Aplicativos e aprendizagem | Use um avatar de referência e quatro cenas cotidianas para testar uma adaptação curta. | Demo |
| [Hydrogen planeja um clipe de personagem para ComfyUI](#case-219) | Aplicativos e aprendizagem | Mantenha figurino e cenário ao variar expressões e ações no briefing. | Integration |
| [Ampliação de Almance Vale para 100 módulos](#case-220) | Agentes e fluxos de programação | Leve um aplicativo a um agente de código e peça novos módulos com o estilo existente. | Demo |
| [Uma vila 2D com áudio procedural](#case-221) | Comparações e limitações | Verifique se o som muda com os eventos na tela e anote a duração da criação. | Evaluation |
| [Um visual panorâmico para uma música](#case-222) | Aplicativos e aprendizagem | Forneça a música e o formato para ver se o movimento transmite sua energia. | Demo |
| [Cataratas do Niágara com sete subagentes Hydrogen](#case-223) | Agentes e fluxos de programação | Divida o cenário para que um coordenador distribua componentes entre agentes de implementação. | Demo |
| [Continuidade entre duas cenas de romance de época](#case-224) | Aplicativos e aprendizagem | Especifique o que deve permanecer quando uma cena continua em outro clipe. | Demo |
| [Uma esfera de água no aplicativo Gemini](#case-225) | 3D interativo e interfaces | Use uma cena óptica simples para inspecionar reflexos e refração. | Demo |

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

<a id="case-59"></a>
### Caso 59: [Um fluxo com ferramentas do Hydrogen no n8n](https://x.com/n8n_io/status/2120947273534197886) (por [@n8n_io](https://x.com/n8n_io))

**Delegue ao Hydrogen as chamadas de ferramentas no n8n e mantenha o planejamento à parte.**

O n8n documenta o suporte ao Hydrogen e sugere planejar com Carbon ou Argon e executar com Hydrogen. A publicação traz o link de configuração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-12

---

<a id="case-69"></a>
### Caso 69: [Rota de autenticação num fluxo multiagente](https://x.com/studio_yebisu/status/2120969033260646551) (por [@studio_yebisu](https://x.com/studio_yebisu))

**Verifique qual cliente se autentica quando um agente delega a tarefa a outro provedor.**

O autor pediu que Claude usasse Hydrogen pelo Antigravity CLI. Relata uma tentativa de autenticação direta pelo Claude Code e a suspensão do acesso ao Antigravity. A captura mostra o aviso. A explicação da causa é do autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-12

---

<a id="case-70"></a>
### Caso 70: [Uma execução de Goal Mode no Antigravity](https://x.com/Inmerson/status/2120973427788124345) (por [@Inmerson](https://x.com/Inmerson))

**Acompanhe planejamento, mudanças no código e resultados dos testes em sessões longas.**

O autor relata 105 minutos com Hydrogen Extra em Goal Mode, passando por planejamento, implementação e testes. Os resultados são os informados pelo autor.

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

Tipo: Demo | Data: 2026-11-12

---

<a id="case-73"></a>
### Caso 73: [Carbon e Hydrogen no Antigravity Orchestrator](https://x.com/Google/status/2120982566891356279) (por [@Google](https://x.com/Google))

**Recorra ao planejador quando o modelo de implementação mais rápido encontra um bloqueio.**

O Google descreve Carbon planejando e corrigindo impasses enquanto Hydrogen edita e testa. Relata desempenho próximo do Carbon no Terminal-Bench 4.0, com menor cota e duração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

Tipo: Integration | Data: 2026-11-12

---

<a id="case-87"></a>
### Caso 87: [Hydrogen no OpenClaw](https://x.com/openclaw/status/2121098531205501401) (por [@openclaw](https://x.com/openclaw))

**Confira a seleção de modelo no sistema de agentes que você vai usar.**

O OpenClaw anuncia suporte ao Hydrogen e inclui uma captura. Não apresenta um benchmark nem a sequência de configuração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-13

---

<a id="case-97"></a>
### Caso 97: [Uma sala do trono com Blender MCP](https://x.com/ashen_one/status/2121165467821936651) (por [@ashen_one](https://x.com/ashen_one))

**Use Blender MCP para inspecionar no editor a composição de uma cena gerada.**

O autor atribui ao Hydrogen a recriação da sala do Trono de Ferro de Game of Thrones com Blender MCP e compartilha uma gravação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

Tipo: Integration | Data: 2026-11-13

---

<a id="case-113"></a>
### Caso 113: [Montagem de uma betoneira em CAD no navegador](https://x.com/johnsanthosh01/status/2121243197901041869) (por [@johnsanthosh01](https://x.com/johnsanthosh01))

**Revise a árvore de peças e os encaixes antes de usar o conjunto em CAD.**

O autor relata que Hydrogen gerou uma betoneira de 265 peças no CadX Studio em 40 minutos, a partir de uma instrução e sem modelar peça por peça.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

Tipo: Integration | Data: 2026-11-13

---

<a id="case-114"></a>
### Caso 114: [Modelagem procedural de um machado no Blender](https://x.com/camperaigg/status/2121252572115951897) (por [@camperaigg](https://x.com/camperaigg))

**Use uma silhueta de referência e revise o modelo em várias inspeções na vista 3D.**

O autor usou Hydrogen pelo Antigravity CLI para criar um machado estilizado no Blender com módulos Python e revisões iterativas. Relata 51 minutos com captura e US$ 5,01 de API.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-13

---

<a id="case-118"></a>
### Caso 118: [Ember Isle em 28 módulos](https://x.com/IamEmily2050/status/2121258646759952644) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Divida uma cena grande em módulos e acompanhe a duração de cada geração.**

O autor usou Hydrogen High no aplicativo Gemini. Informa 28 módulos, uma instrução por módulo e 82 a 290 segundos por instrução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-150"></a>
### Caso 150: [Planejar, executar e revisar com modelos distintos](https://x.com/naufaldi/status/2121499487999013081) (por [@naufaldi](https://x.com/naufaldi))

**Separe as funções e compare os totais por tarefa de cada modelo.**

O autor usa Opus 5.5 para planejar, Hydrogen para executar com Sol de reserva e Sol 6.1 para revisar. Combina uso próprio do Antigravity com comparações públicas de outros testes.

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

Tipo: Demo | Data: 2026-11-14

---

<a id="case-154"></a>
### Caso 154: [Configurando Hydrogen em um cliente de código](https://x.com/k2sbhai/status/2121509825658147041) (por [@k2sbhai](https://x.com/k2sbhai))

**Use o identificador exato do modelo ao configurar uma chave da API Google em um cliente compatível.**

O autor explica como obter a chave no Google AI Studio e escolher gemini-4-hydrogen no OpenCode ou Cline. Acesso e limites dependem do provedor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

Tipo: Tutorial | Data: 2026-11-14

---

<a id="case-155"></a>
### Caso 155: [Uma equipe de pesquisa SuperARIS com Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Delegue tarefas específicas de pesquisa e redação ao Hydrogen em uma equipe de agentes.**

A publicação ensina a instalar e configurar SuperARIS. Sugere Hydrogen ou Carbon para discussão e redação com coordenação e implementação separadas. Não mede a qualidade da pesquisa.

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

Tipo: Integration | Data: 2026-11-14

---

<a id="case-156"></a>
### Caso 156: [Quatro modelos reescrevem um módulo do zero](https://x.com/oasisfeng/status/2121523934831276203) (por [@oasisfeng](https://x.com/oasisfeng))

**Compare compreensão do código, projeto da solução e implementação ao avaliar uma reescrita.**

O autor compara Hydrogen, Argon, GPT-6 Astra e Claude Opus 5.5 na reescrita de um módulo central. Destaca a execução do Hydrogen e distingue a capacidade de arquitetura de outros modelos.

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

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-158"></a>
### Caso 158: [Muse delega tarefas ao Antigravity CLI](https://x.com/tetumemo/status/2121528823061852166) (por [@tetumemo](https://x.com/tetumemo))

**Conecte um assistente remoto a um ambiente local e escolha um modelo padrão de redação.**

O autor descreve Muse enviando tarefas ao Antigravity CLI em um computador doméstico e recebendo resultados. Usa Hydrogen por padrão com opção de Argon. Os exemplos incluem texto japonês e material visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-14

---

<a id="case-168"></a>
### Caso 168: [Escolhendo entre Orchestrator e Swarm no Antigravity](https://x.com/ohayou792/status/2121624258984153452) (por [@ohayou792](https://x.com/ohayou792))

**Use repasses entre modelos nas tarefas sequenciais e agentes independentes com revisores nas paralelas.**

O autor ilustra Orchestrator com planejamento de um modelo avançado e implementação do Hydrogen. Contrasta com /swarm e propõe decidir pelas dependências.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

Tipo: Tutorial | Data: 2026-11-14

---

<a id="case-171"></a>
### Caso 171: [De uma imagem de referência ao CAD no SolidWorks](https://x.com/GoGoFly23/status/2121636952479080713) (por [@GoGoFly23](https://x.com/GoGoFly23))

**Use uma imagem 3D para avaliar o fluxo de modelagem do agente no SolidWorks.**

O autor deu uma imagem ao Hydrogen no Antigravity e mostra a peça. Depois menciona a integração SolidWorks MCP. Tolerâncias e adequação à engenharia não foram testadas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-14

---

<a id="case-188"></a>
### Caso 188: [Uso do navegador em um Swarm do Antigravity](https://x.com/Saboo_Shubham_/status/2121852445756477924) (por [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**Inspecione a atividade no navegador junto com as tarefas dos agentes.**

Um funcionário do Google mostra uma captura de Hydrogen e Swarm do Antigravity usando o navegador. Não há um registro completo de tarefas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-15

---

<a id="case-189"></a>
### Caso 189: [Repasse de pesquisa ao Muse pelo Google Drive](https://x.com/nasuvit_z/status/2121857992702525734) (por [@nasuvit_z](https://x.com/nasuvit_z))

**Use uma pasta monitorada quando outro agente for assumir a próxima etapa.**

O autor usa Hydrogen para reunir informações em um arquivo no Drive e faz Muse assumir quando o arquivo aparece. O diagrama mostra o repasse.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-15

---

<a id="case-192"></a>
### Caso 192: [Um Swarm do Antigravity anima um pelicano](https://x.com/chetaslua/status/2121885449509851415) (por [@chetaslua](https://x.com/chetaslua))

**Distribua animação e áudio entre agentes e confira a cena montada.**

O autor atribui a Carbon e Hydrogen uma cena em JavaScript em que o pelicano muda de estilo artístico. Relata que música e sons foram feitos por código.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-195"></a>
### Caso 195: [Antigravity em um projeto Google Cloud](https://x.com/loganlu51268/status/2121911409042719023) (por [@loganlu51268](https://x.com/loganlu51268))

**Confira como autenticação e cobrança funcionam ao habilitar Hydrogen com credenciais gerenciadas.**

O autor descreve a troca de um plano pessoal por um projeto Google Cloud Agent Platform com credenciais padrão de aplicativo. Inclui Hydrogen no seletor e explica a revisão de cobrança por SKU.

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

Tipo: Tutorial | Data: 2026-11-15

---

<a id="case-198"></a>
### Caso 198: [Carbon planeja e Hydrogen implementa um aplicativo móvel](https://x.com/thebuggeddev/status/2121945961555718334) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Delegue o desenho das interações ao planejador e separe a implementação.**

O autor atribui o planejamento a Carbon e a implementação a Hydrogen, incluindo a física com Reanimated. Descreve movimento fluido e mostra o resultado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-202"></a>
### Caso 202: [Hydrogen no T3 Code](https://x.com/bei351009016/status/2121964293906206916) (por [@bei351009016](https://x.com/bei351009016))

**Teste um cliente dedicado e monitore cotas móvel e semanal durante uma sessão realista.**

O autor relata cerca de meio dia com Hydrogen via Gemini Pro no T3 Code. As capturas e a publicação documentam as cotas e distinguem velocidade percebida de precisão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

Tipo: Integration | Data: 2026-11-15

---

<a id="case-204"></a>
### Caso 204: [Um pavão ciclista em dez estilos de arte](https://x.com/SahilPanhotra/status/2121995488425849064) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Use um grupo de modelos para programar transições visuais e sincronizar o som.**

O autor atribui a Carbon e Hydrogen um pavão pedalando em dez estilos. Relata que visuais, música e efeitos sonoros foram feitos com código.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-220"></a>
### Caso 220: [Ampliação de Almance Vale para 100 módulos](https://x.com/IamEmily2050/status/2122257581175410858) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Leve um aplicativo a um agente de código e peça novos módulos com o estilo existente.**

O autor transferiu Almance Vale do Gemini para o Antigravity. Relata que Hydrogen Extra com Swarm seguiu as convenções de código e ampliou a cena para 100 módulos em algumas horas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

Tipo: Demo | Data: 2026-11-16

---

<a id="case-223"></a>
### Caso 223: [Cataratas do Niágara com sete subagentes Hydrogen](https://x.com/SahilPanhotra/status/2122311637684424737) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Divida o cenário para que um coordenador distribua componentes entre agentes de implementação.**

O autor atribui a Carbon e sete subagentes Hydrogen a criação em menos de uma hora com uma instrução. O vídeo mostra água, barcos, pontos de vista e ambientes que mudam.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

Tipo: Demo | Data: 2026-11-16

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

<a id="case-58"></a>
### Caso 58: [Um protótipo estilo Minecraft em quinze minutos](https://x.com/RezAIT00/status/2120947124418293876) (por [@RezAIT00](https://x.com/RezAIT00))

**Use um ambiente de voxels para verificar como mineração e inventário funcionam juntos.**

O autor atribui ao Hydrogen Extra High um protótipo feito em 15 minutos. Cita construção, mineração e inventário, que o vídeo não demonstra por completo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-77"></a>
### Caso 77: [De um resumo de notícias a um vídeo narrado](https://x.com/gigabit_million/status/2121011957042163722) (por [@gigabit_million](https://x.com/gigabit_million))

**Transforme notícias pesquisadas em um vídeo curto e confira os fatos mencionados.**

O autor grava Hydrogen no aplicativo Gemini pesquisando notícias e fazendo um roteiro antes de pedir o vídeo. A gravação mostra dez segundos de reprodução. Tempo de geração e narração são relatos do autor, e o sistema de renderização é desconhecido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-90"></a>
### Caso 90: [Desenho no ar com uma webcam](https://x.com/CodeByPoonam/status/2121121804483969102) (por [@CodeByPoonam](https://x.com/CodeByPoonam))

**Trace linhas e observe se a interface de desenho acompanha seus movimentos.**

O autor atribui a um acesso antecipado ao Hydrogen a criação de uma ferramenta de desenho no ar por webcam e mostra uma gravação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-93"></a>
### Caso 93: [Um portal web em uma tentativa](https://x.com/kimura_0314/status/2121130305532878979) (por [@kimura_0314](https://x.com/kimura_0314))

**Examine o layout inicial antes de testar fluxos individuais.**

O autor mostra um portal gerado uma vez com Hydrogen no Antigravity. A captura não confirma o funcionamento das interações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-13

---

<a id="case-95"></a>
### Caso 95: [Um simulador urbano no estilo Cities: Skylines](https://x.com/yohakujpn/status/2121146464466604147) (por [@yohakujpn](https://x.com/yohakujpn))

**Prototipe um construtor de cidades e veja como controles e simulações se integram.**

O autor atribui o protótipo ao Hydrogen e relata menos de 30 minutos. O vídeo mostra o resultado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-124"></a>
### Caso 124: [Um livro de química vira aula interativa](https://x.com/smalkalbani/status/2121282231759155617) (por [@smalkalbani](https://x.com/smalkalbani))

**Monte uma aula autônoma com dicas, narração e texto opcional.**

A demonstração é uma aula de química do nono ano com orientação falada e sugestões. A fonte não mede a aprendizagem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-125"></a>
### Caso 125: [Um protótipo de música Vocaloid](https://x.com/peach2k2/status/2121284159565902188) (por [@peach2k2](https://x.com/peach2k2))

**Confira se uma composição de uma tentativa atende ao personagem e ao estilo solicitados.**

O autor publica um trecho e atribui a composição ao Hydrogen. A publicação não identifica as ferramentas de renderização do áudio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-134"></a>
### Caso 134: [Leitura de uma integral densa a partir de imagem](https://x.com/HarshithLucky3/status/2121303778548908228) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Confira se o modelo reconhece limites iguais antes de tentar simplificar uma expressão longa.**

O autor grava Hydrogen High no Gemini respondendo a uma captura de uma integral densa. O teste é reconhecer que os limites externos são iguais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-138"></a>
### Caso 138: [Uma enciclopédia da célula humana em WebGL2](https://x.com/soumyadesign/status/2121354542344466565) (por [@soumyadesign](https://x.com/soumyadesign))

**Use um corte interativo para ensinar as relações espaciais da célula.**

O autor diz que fez uma enciclopédia 3D com Hydrogen no Antigravity, WebGL2 e sem bibliotecas externas. Destaca a vista em corte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-140"></a>
### Caso 140: [Um oponente que só vê o tabuleiro no Parking Bench](https://x.com/agenticjay/status/2121391300822081713) (por [@agenticjay](https://x.com/agenticjay))

**Teste um oponente de quebra-cabeça que recebe apenas uma imagem do tabuleiro como estado.**

Segundo o autor, Carbon criou o jogo e o jogador enfrenta Hydrogen ou Gemini Decision 1 por API em cinco níveis. Ambos recebem um PNG sem os dados da grade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

Tipo: Integration | Data: 2026-11-13

---

<a id="case-141"></a>
### Caso 141: [Um vídeo com instruções de Google Docs](https://x.com/nin222/status/2121395008863621390) (por [@nin222](https://x.com/nin222))

**Use capturas e indicações numeradas para ensinar um fluxo de edição no celular.**

O autor atribui a Hydrogen um vídeo editado sobre seleção de texto, estilos, cores, fontes e salvamento no Google Docs móvel. Os quadros mostram o resultado anotado, sem especificar o método de edição.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-146"></a>
### Caso 146: [Um ambiente BASIC para o MZ-1500](https://x.com/hiromsa/status/2121465784715338065) (por [@hiromsa](https://x.com/hiromsa))

**Prototipe um BASIC retrô e verifique o suporte a periféricos.**

O autor atribui a demonstração ao Hydrogen e informa cerca de 15 minutos de trabalho. Inclui PCG, PSG e QuickDisk, este último limitado a LOAD.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-14

---

<a id="case-161"></a>
### Caso 161: [Um jogo de tiro em HTML em um minuto](https://x.com/SahilPanhotra/status/2121561371951399133) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Use um HTML para testar controles básicos e feedback de um jogo de tiro.**

O autor relata que Hydrogen fez um jogo jogável em menos de um minuto com uma instrução, sem frameworks ou instalação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-163"></a>
### Caso 163: [Conversas com Hydrogen no AITuber OnAir](https://x.com/shinshin86/status/2121571590442017094) (por [@shinshin86](https://x.com/shinshin86))

**Experimente Hydrogen como modelo de conversa por trás de um avatar Live2D.**

O mantenedor anuncia suporte ao Hydrogen e apresenta avatares de teste, inclusive Live2D. A gravação demonstra a integração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

Tipo: Integration | Data: 2026-11-14

---

<a id="case-164"></a>
### Caso 164: [Um vídeo promocional feito por código](https://x.com/xiangning0/status/2121594643540480293) (por [@xiangning0](https://x.com/xiangning0))

**Passe um briefing promocional curto e revise os elementos gráficos em movimento.**

O autor apresenta um vídeo sobre GPT-6.2 Astra e diz que Hydrogen o produziu só com código. A peça exemplifica esse processo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-173"></a>
### Caso 173: [Uma apresentação sobre a sincronicidade de Jung](https://x.com/soumyadesign/status/2121676345835241916) (por [@soumyadesign](https://x.com/soumyadesign))

**Teste a geração de slides em um tema que exija explicar bem conceitos relacionados.**

O autor atribui a Hydrogen e a uma ferramenta própria os slides sobre sincronicidade e ordem acausal de Carl Jung. Diz ter desenvolvido a ferramenta no Antigravity e mostra resultados.

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

Tipo: Demo | Data: 2026-11-14

---

<a id="case-178"></a>
### Caso 178: [Um motor mitocondrial manipulável](https://x.com/SidraMiconi/status/2121745863827697687) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Use um diagrama interativo para conectar movimento molecular à produção de ATP.**

O autor relata que Hydrogen High fez um aplicativo de ATP sintase com uma instrução e recebeu um ajuste posterior de câmera. A forma usa coordenadas de crio-EM e o movimento é simplificado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-179"></a>
### Caso 179: [Um jogo de território no estilo Qix](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (por [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**Use um briefing curto de arcade para verificar se a primeira versão já é interativa.**

O autor pediu um jogo estilo Qix no Gemini gratuito e mostra a demonstração. Marca Hydrogen e informa um único pedido.

**Instrução:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-180"></a>
### Caso 180: [Geração de slides HTML com Hydrogen](https://x.com/yamachan_ai_log/status/2121772023710118043) (por [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**Revise hierarquia e layout enquanto avalia a velocidade de geração de HTML.**

O autor mostra Hydrogen criando slides e os descreve como rápidos e detalhados. O vídeo mostra a apresentação, sem comparar tempos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-185"></a>
### Caso 185: [Uma aula vira um vídeo curto](https://x.com/smalkalbani/status/2121844887033458954) (por [@smalkalbani](https://x.com/smalkalbani))

**Verifique precisão didática e ritmo ao transformar uma aula em vídeo.**

O autor atribui o fluxo ao Hydrogen e publica dois vídeos. A publicação não identifica o sistema que renderizou o vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-190"></a>
### Caso 190: [Um guia de flauta doce no Gemini Canvas](https://x.com/nin222/status/2121877676042682538) (por [@nin222](https://x.com/nin222))

**Experimente o modo rápido para combinar partitura e instruções de prática.**

O vídeo mostra um guia feito no Canvas com Hydrogen no modo rápido. O autor diz que também poderia usar uma partitura importada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-194"></a>
### Caso 194: [TAJ VICE em um único arquivo HTML](https://x.com/SahilPanhotra/status/2121909681514074328) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Prototipe um mapa explorável em um arquivo e investigue os defeitos restantes.**

O autor usou Hydrogen por menos de 12 horas para um jogo inspirado em GTA em uma Agra fictícia. Usou JavaScript e um HTML sem recursos externos e reconhece bugs pendentes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-203"></a>
### Caso 203: [Um vídeo de utilidade pública em estilo desenhado à mão](https://x.com/shengtang135754/status/2121965385356612020) (por [@shengtang135754](https://x.com/shengtang135754))

**Use uma mensagem curta de utilidade pública para avaliar uma estética de desenho.**

O autor atribui o vídeo de aparência artesanal a Gemini 4 Hydrogen e diz que saiu em uma tentativa. Não identifica um modelo de renderização nem explica o processo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-207"></a>
### Caso 207: [Recriando o site React.gg a partir de imagem](https://x.com/thebuggeddev/status/2122019549117911473) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Comece pela imagem de referência e veja quais detalhes ainda precisam de revisão.**

O autor aponta que usou uma imagem para Hydrogen recriar React.gg em algumas instruções. Mostra uma demonstração e reconhece que o resultado não é idêntico.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-210"></a>
### Caso 210: [Gemini como treinador de corrida](https://x.com/ivanleomk/status/2122036783307469199) (por [@ivanleomk](https://x.com/ivanleomk))

**Compare o registro do treino com as sugestões e ajuste as metas ao seu ponto de partida.**

O autor atribui a Gemini Hydrogen a orientação e publica uma captura da corrida após relatar sua maior distância em cerca de um ano. É um caso pessoal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-15

---

<a id="case-211"></a>
### Caso 211: [Um jogo de navegador com pontos na blockchain](https://x.com/itshoseyn/status/2122063851143246140) (por [@itshoseyn](https://x.com/itshoseyn))

**Teste a jogabilidade em um navegador de computador e revise separadamente o registro de pontos.**

O autor atribui ao Hydrogen parte do desenvolvimento de Sheytonak, integrado à Base com pontos em blockchain. Relata otimização para computador e reconhece problemas em dispositivos móveis e outros bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-213"></a>
### Caso 213: [Um aplicativo transforma instruções em MIDI](https://x.com/Awed_Urshy/status/2122161392828727738) (por [@Awed_Urshy](https://x.com/Awed_Urshy))

**Prototipe uma ferramenta que leve um briefing em japonês até MIDI, WAV e piano roll.**

O autor mostra um aplicativo feito com Hydrogen que traduz a entrada para uma instrução musical em inglês, gera MIDI, renderiza WAV e grava um vídeo de piano roll. São funções do aplicativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

Tipo: Demo | Data: 2026-11-16

---

<a id="case-215"></a>
### Caso 215: [Resumo de um show em uma página](https://x.com/fukubaya/status/2122215495474794640) (por [@fukubaya](https://x.com/fukubaya))

**Transforme informações de evento em um resumo visual fácil de consultar.**

O autor atribui ao Hydrogen um resumo visual em japonês de um show do Batten Girls. Não mostra todo o material de origem nem a instrução completa.

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

Tipo: Demo | Data: 2026-11-16

---

<a id="case-218"></a>
### Caso 218: [Uma montagem do cotidiano a partir de um avatar](https://x.com/antiAIvo/status/2122251181112353276) (por [@antiAIvo](https://x.com/antiAIvo))

**Use um avatar de referência e quatro cenas cotidianas para testar uma adaptação curta.**

O autor forneceu um avatar do X com cenas de estudo, refeição, celular e exercício. Atribui ao Hydrogen um resultado de cerca de dez segundos sem identificar o renderizador.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

Tipo: Demo | Data: 2026-11-16

---

<a id="case-219"></a>
### Caso 219: [Hydrogen planeja um clipe de personagem para ComfyUI](https://x.com/nyapan_mohy/status/2122253350808744004) (por [@nyapan_mohy](https://x.com/nyapan_mohy))

**Mantenha figurino e cenário ao variar expressões e ações no briefing.**

O autor atribui o planejamento ao Hydrogen e a renderização a um fluxo separado de imagem para vídeo com MiniMax no ComfyUI. Preparou um quadro inicial novo e uma instrução de 30 planos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

Tipo: Integration | Data: 2026-11-16

---

<a id="case-222"></a>
### Caso 222: [Um visual panorâmico para uma música](https://x.com/ivy432hz/status/2122283590180589791) (por [@ivy432hz](https://x.com/ivy432hz))

**Forneça a música e o formato para ver se o movimento transmite sua energia.**

O autor diz ter dado ao Hydrogen XHigh apenas a música, o formato 21:9 e um pedido de sensação de velocidade. O vídeo mostra uma estrada em alta velocidade sem explicar a renderização.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

Tipo: Demo | Data: 2026-11-16

---

<a id="case-224"></a>
### Caso 224: [Continuidade entre duas cenas de romance de época](https://x.com/AvaSinclairAi_/status/2122315627113107670) (por [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**Especifique o que deve permanecer quando uma cena continua em outro clipe.**

O autor atribui a um fluxo Gemini com Hydrogen um romance breve a bordo de um transatlântico. Publica um briefing em duas partes sobre continuidade de personagens e figurino, sem identificar o modelo de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

Tipo: Demo | Data: 2026-11-16

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

<a id="case-60"></a>
### Caso 60: [Um agente da Box para documentos empresariais complexos](https://x.com/levie/status/2120947988143198302) (por [@levie](https://x.com/levie))

**Meça precisão, tempo e tokens em uma carga realista de documentos.**

Em acesso antecipado, a Box relata cinco pontos a mais de precisão, menos da metade do tempo e cerca de 12% menos tokens em uma tarefa típica, em comparação com Gemini 3.8 Flash.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-74"></a>
### Caso 74: [Gráfico e relatório a partir de dados do Workspace](https://x.com/nin222/status/2120989168247652674) (por [@nin222](https://x.com/nin222))

**Veja se uma nova interação corrige lacunas da análise, do gráfico ou do relatório.**

Em uma demonstração do Google Workspace for Education Fundamentals, o autor usou Hydrogen para analisar dados, criar um gráfico e gerar um arquivo de relatório. Relata duas interações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-12

---

<a id="case-81"></a>
### Caso 81: [Arte em pixels em diferentes modos do Gemini](https://x.com/kkitase/status/2121041283640926401) (por [@kkitase](https://x.com/kkitase))

**Use a mesma tarefa de desenho no Google Sheets para comparar opções de modelo.**

O autor mostra Hydrogen desenhando em pixels e inclui execuções separadas com Antigravity Orchestrator, Carbon e Argon. É uma demonstração sem pontuação formal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-148"></a>
### Caso 148: [Um mapa jogável de uma suspensão de voos da FAA](https://x.com/SidraMiconi/status/2121486870341370204) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Use um mapa e uma linha do tempo para mostrar por que a fila persiste depois do fim da suspensão.**

O autor relata 222 segundos para criar o mapa com Hydrogen e uma etiqueta corrigida. A cronologia segue relatos oficiais e o tráfego simulado usa horários típicos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-184"></a>
### Caso 184: [Um resumo estruturado do YouTube no Chrome](https://x.com/studio_yebisu/status/2121835594674561098) (por [@studio_yebisu](https://x.com/studio_yebisu))

**Peça ao Gemini no Chrome um resumo com marcas de tempo e fontes claras para o contexto adicional.**

A publicação em japonês mostra o resumo de um vídeo aberto. A instrução pública pede sinopse, pontos principais, capítulos, contexto com fontes separadas, ressalvas e recursos.

**Instrução:**

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

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

Tipo: Tutorial | Data: 2026-11-15

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

<a id="case-41"></a>
### Caso 41: [De referências espaciais a uma cena HTML](https://x.com/Inmerson/status/2120482539907559651) (por [@Inmerson](https://x.com/Inmerson))

**Use algumas referências para testar se uma cena gerada conserva um estilo reconhecível.**

O autor atribui a visualização espacial ao Hydrogen. A fonte mostra imagens de planetas usadas como referência e uma cena HTML com um planeta anelado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-11

---

<a id="case-42"></a>
### Caso 42: [Um protótipo de Fórmula 1 no Gemini Canvas](https://x.com/auricxofficial/status/2120843585914605830) (por [@auricxofficial](https://x.com/auricxofficial))

**Inclua vários ângulos de câmera para examinar um veículo gerado.**

O autor atribui o visualizador de um carro de Fórmula 1 à primeira tentativa com Hydrogen no Gemini Canvas. A gravação mostra opções de câmera e vistas da suspensão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-48"></a>
### Caso 48: [Vista lateral de um BMW em SVG](https://x.com/HarshithLucky3/status/2120932649938382894) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Use uma vista lateral em SVG para avaliar as proporções, a silhueta e os detalhes do veículo.**

O autor atribui ao Hydrogen High no aplicativo Gemini um SVG lateral de um BMW M4 CS e relata geração em menos de 30 segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-12

---

<a id="case-49"></a>
### Caso 49: [A ilha flutuante de um astrônomo](https://x.com/pankajkumar_dev/status/2120933196221333791) (por [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Dê um tema claro a uma cena pequena e verifique se objetos e iluminação o reforçam.**

O autor atribui uma ilha flutuante de astrônomo a uma versão do Hydrogen no Arena e relata quatro minutos de geração. A atribuição é específica dessa execução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-50"></a>
### Caso 50: [De uma imagem a uma paisagem 3D explorável](https://x.com/HarshithLucky3/status/2120935535422374055) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Verifique se uma cena baseada em imagem mantém a aparência e permite deslocamento.**

O autor atribui ao Hydrogen no aplicativo Gemini uma paisagem 3D explorável e descreve reflexos em GLSL, geometria procedural e física de natação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-51"></a>
### Caso 51: [Um diorama em miniatura com blocos 3D](https://x.com/abhinavflac/status/2120936501961969990) (por [@abhinavflac](https://x.com/abhinavflac))

**Peça uma miniatura de blocos e confira se as formas compõem uma cena coerente.**

O autor mostra uma gravação do diorama e atribui a criação ao Hydrogen. O tempo e a configuração exata não são informados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-52"></a>
### Caso 52: [Uma cerejeira florida interativa](https://x.com/hakmgpt/status/2120936640436642231) (por [@hakmgpt](https://x.com/hakmgpt))

**Use um objeto animado e alguns controles para explorar mudanças em tempo real.**

O autor atribui ao Hydrogen a interface da cerejeira da captura. Ela mostra controles de cena, sem detalhar a implementação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-12

---

<a id="case-62"></a>
### Caso 62: [Refração em uma animação interativa pequena](https://x.com/chanelluuh/status/2120951519470399710) (por [@chanelluuh](https://x.com/chanelluuh))

**Use prévias rápidas para refinar um efeito óptico antes de ampliar a cena.**

O autor atribui ao Hydrogen uma animação da série Small Delights e destaca a refração. A fonte descreve um processo criativo iterativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-63"></a>
### Caso 63: [Um rio que corre para cima](https://x.com/xKaka1456/status/2120952404225265983) (por [@xKaka1456](https://x.com/xKaka1456))

**Teste um sentido de movimento incomum e avalie o efeito visualmente.**

O autor relata ter criado um rio que corre ao contrário usando Hydrogen na web e mostra o resultado. Tempo e consumo de cota são observações do autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

Tipo: Demo | Data: 2026-11-12

---

<a id="case-67"></a>
### Caso 67: [Um retrato em 3D com Hydrogen](https://x.com/soyamiruku/status/2120959893943251322) (por [@soyamiruku](https://x.com/soyamiruku))

**Use um retrato para verificar se a representação 3D é reconhecível.**

O autor atribui ao Hydrogen um retrato 3D da pessoa mencionada e compartilha uma imagem. A fonte dá poucos detalhes do processo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

Tipo: Demo | Data: 2026-11-12

---

<a id="case-82"></a>
### Caso 82: [Um apartamento impresso em 3D a partir de imagem](https://x.com/bijanbowen/status/2121042010928709932) (por [@bijanbowen](https://x.com/bijanbowen))

**Leve um teste de imagem para 3D até a impressão física.**

O autor compartilha uma referência visual e uma impressão física do apartamento de Seinfeld que atribui ao Hydrogen.

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

Tipo: Demo | Data: 2026-11-13

---

<a id="case-86"></a>
### Caso 86: [Uma cena náutica com o Golden Merry](https://x.com/xKaka1456/status/2121063351136739388) (por [@xKaka1456](https://x.com/xKaka1456))

**Use um navio fictício conhecido para testar a composição náutica estilizada.**

O autor atribui ao Hydrogen uma cena do Golden Merry em águas azuis. A publicação não especifica instruções, ajustes ou iterações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-88"></a>
### Caso 88: [Uma baleia entre nuvens](https://x.com/xKaka1456/status/2121100318150898144) (por [@xKaka1456](https://x.com/xKaka1456))

**Analise separadamente o movimento da criatura e o desenho dos olhos.**

A fonte mostra uma baleia animada por código entre nuvens e relata cerca de dois minutos com Hydrogen. Tempo e cota são observações do autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-92"></a>
### Caso 92: [Uma cidade submarina no Gemini Canvas](https://x.com/ayyh_18/status/2121128385690693821) (por [@ayyh_18](https://x.com/ayyh_18))

**Comece com uma cena 3D pequena e acrescente áreas exploráveis e animais em várias etapas.**

O autor desenvolveu a cidade no aplicativo Gemini com peixes, águas-vivas, corais e cúpulas de vidro navegáveis. A fonte descreve várias instruções.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-99"></a>
### Caso 99: [Um navio pirata em tons de cinza no Three.js](https://x.com/parves075/status/2121172856889618528) (por [@parves075](https://x.com/parves075))

**Limite a cena a tons de cinza e confira se a luz ainda revela a geometria.**

O autor usou Hydrogen no Antigravity para construir um navio pirata em Three.js e gravou o teste de iluminação e detalhe 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-101"></a>
### Caso 101: [Uma luminária paramétrica no CadXStudio](https://x.com/CadX_Studio/status/2121175785356853312) (por [@CadX_Studio](https://x.com/CadX_Studio))

**Inspecione dimensões e editabilidade das peças de um CAD gerado.**

O CadXStudio mostra uma luminária no navegador e informa 35 peças editáveis. O exemplo é do fornecedor da ferramenta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

Tipo: Integration | Data: 2026-11-13

---

<a id="case-102"></a>
### Caso 102: [Uma trilha de santuário animada em C++](https://x.com/nehstrr3/status/2121184399245128137) (por [@nehstrr3](https://x.com/nehstrr3))

**Use uma cena pequena em código nativo para testar uma animação sem ferramentas web.**

O autor atribui ao Hydrogen Extra High a animação de um caminho sob portões de santuário. Identifica C++ próprio como linguagem de implementação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-105"></a>
### Caso 105: [Uma vila construída em 30 módulos](https://x.com/IamEmily2050/status/2121200010574598655) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Gere a cena em módulos e revise o conjunto depois de integrá-los.**

O autor atribui ao Hydrogen High no aplicativo Gemini o resultado de 30 módulos, com uma instrução por módulo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-108"></a>
### Caso 108: [Uma agência dos correios em uma ilha flutuante](https://x.com/pankajkumar_dev/status/2121220537984954448) (por [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Peça um prédio em miniatura e avalie o efeito dos materiais e da iluminação.**

O autor pediu ao Hydrogen uma agência dos correios 3D em uma ilha flutuante. No vídeo destaca texturas, cores e luz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-110"></a>
### Caso 110: [Água e peixes em um jardim de carpas](https://x.com/SahilPanhotra/status/2121225566779023432) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Use peixes em movimento para verificar a coerência dos reflexos e da iluminação da água.**

O autor destaca as cáusticas, os reflexos e o movimento dos peixes no Koi Courtyard do Hydrogen. Também inclui a versão com Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-112"></a>
### Caso 112: [Uma cena 3D ao vivo no aplicativo Gemini](https://x.com/YxzRainy/status/2121232725185339869) (por [@YxzRainy](https://x.com/YxzRainy))

**Prototipe iluminação interativa e partículas na interface web do Gemini.**

O autor mostra uma cena 3D no navegador com Hydrogen, partículas, luz animada e controles em tempo real.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-115"></a>
### Caso 115: [Uma cena 3D cor-de-rosa em um único HTML](https://x.com/SahilPanhotra/status/2121254256288137484) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Teste uma cena Three.js sem recursos externos e confira se a composição é legível.**

O autor atribui ao Hydrogen uma cena estilizada em um HTML com Three.js puro e sem recursos externos. O Koi Courtyard citado é outro projeto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-119"></a>
### Caso 119: [Simulação do Big Bang feita só com código](https://x.com/ash_twtz/status/2121268140630000020) (por [@ash_twtz](https://x.com/ash_twtz))

**Use uma animação curta como protótipo de explicação e confira o rigor científico.**

O autor atribui ao Hydrogen no Gemini uma visualização de 15 segundos, toda em código, sem web, texturas, recursos externos ou modelos 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-120"></a>
### Caso 120: [Um helicóptero com vistas explodidas](https://x.com/LuminaBench/status/2121273297715277930) (por [@LuminaBench](https://x.com/LuminaBench))

**Teste se um protótipo 3D combina controle de voo e modos de inspeção úteis.**

O autor mostra um helicóptero pilotável e vistas montada e explodida. Atribui o protótipo ao Hydrogen com raciocínio Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-121"></a>
### Caso 121: [Hydrogen Express com raio X e malha](https://x.com/LuminaBench/status/2121277060983234788) (por [@LuminaBench](https://x.com/LuminaBench))

**Acrescente modos de inspeção a um protótipo 3D controlável.**

O autor mostra um trem com controle de velocidade, vista explodida, malha e raio X. Informa cerca de cinco minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-122"></a>
### Caso 122: [Um posto de abastecimento no céu](https://x.com/doe_naps/status/2121279837512106168) (por [@doe_naps](https://x.com/doe_naps))

**Inclua objetos móveis e estados de iluminação para demonstrar o comportamento da cena.**

O autor atribui ao Hydrogen um posto aéreo com carro voador retrô, turbinas e transição do dia para a noite. Relata uma tentativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-129"></a>
### Caso 129: [Um moinho d’água em um único HTML](https://x.com/NovaXCode/status/2121294356875509851) (por [@NovaXCode](https://x.com/NovaXCode))

**Teste um protótipo 3D rápido com uma paisagem pequena e elementos móveis reconhecíveis.**

O autor atribui ao Hydrogen a cena de moinho em um HTML em cerca de 30 segundos e compartilha uma gravação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-132"></a>
### Caso 132: [Uma cena no Blender com Hydrogen Extra](https://x.com/SPAC89/status/2121302218347270625) (por [@SPAC89](https://x.com/SPAC89))

**Confirme geometria e materiais no Blender antes de ampliar os detalhes.**

O autor mostra uma cena atribuída ao Hydrogen Extra e apresenta uma estimativa de consumo de cota daquela sessão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-139"></a>
### Caso 139: [Duas animações de partículas com Hydrogen](https://x.com/gwammyy/status/2121355401392189746) (por [@gwammyy](https://x.com/gwammyy))

**Compare cenas de partículas para observar forma e movimento em efeitos simples.**

O autor atribui ao Hydrogen duas gravações curtas de efeitos de partículas. A publicação não documenta a configuração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

Tipo: Demo | Data: 2026-11-13

---

<a id="case-142"></a>
### Caso 142: [Um seletor de dia e noite num mundo em miniatura](https://x.com/vib3coded/status/2121398359395283027) (por [@vib3coded](https://x.com/vib3coded))

**Use um seletor simples para testar a continuidade da animação entre os estados.**

O autor mostra uma transição do dia para a noite controlada pelo seletor e relata US$ 0,21 de custo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-143"></a>
### Caso 143: [Um cenário construído em 65 módulos](https://x.com/IamEmily2050/status/2121400396002492781) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Acompanhe o tempo e o esforço de integração conforme a cena cresce.**

O autor relata 65 módulos e uma instrução por módulo no aplicativo Gemini e mostra uma gravação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-149"></a>
### Caso 149: [Um jardim em miniatura com pagode](https://x.com/auricxofficial/status/2121498286926540970) (por [@auricxofficial](https://x.com/auricxofficial))

**Confira se uma miniatura gerada equilibra arquitetura e paisagismo.**

O autor atribui ao Hydrogen um vídeo de um pagode feito de blocos com jardim. Não detalha a implementação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-153"></a>
### Caso 153: [Diorama de aeródromo da Segunda Guerra Mundial](https://x.com/doe_naps/status/2121508105947320688) (por [@doe_naps](https://x.com/doe_naps))

**Inclua referências e requisitos de movimento mecânico para testar além da aparência.**

O autor deu referências e uma instrução curta ao Hydrogen para construir um aeródromo em um HTML. O pedido incluía um avião e um tanque funcionais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-167"></a>
### Caso 167: [Um pisco animado de forma procedural](https://x.com/LuminaBench/status/2121620820791562291) (por [@LuminaBench](https://x.com/LuminaBench))

**Examine o movimento do corpo e das asas numa animação de voo gerada.**

O autor atribui ao Hydrogen o código do voo de um pisco. Depois mostra um diagrama de Swarm no Antigravity referente ao mesmo trabalho.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

Tipo: Demo | Data: 2026-11-14

---

<a id="case-182"></a>
### Caso 182: [Uma ilustração em um único arquivo HTML](https://x.com/vamsibatchuk/status/2121788887823778297) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Teste se uma referência visual pode ser recriada com código e sem recursos externos.**

Um integrante da DeepMind mostra a ilustração em um arquivo e afirma que não usou bibliotecas, gerador de imagens, skills ou recursos incorporados.

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

Tipo: Demo | Data: 2026-11-15

---

<a id="case-186"></a>
### Caso 186: [Animação de um papagaio-do-mar a partir de cena estática](https://x.com/vamsibatchuk/status/2121846407950639541) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Use uma cena HTML existente como primeiro quadro de uma animação procedural.**

O autor pediu ao Hydrogen 50 quadros de continuação em um HTML. No vídeo, um papagaio-do-mar pega o chapéu do personagem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-200"></a>
### Caso 200: [Uma ilha 3D em miniatura com uma instrução](https://x.com/CodeByPoonam/status/2121952483132289270) (por [@CodeByPoonam](https://x.com/CodeByPoonam))

**Confira se a cena organiza prédios, terreno e água de modo legível.**

O autor atribui ao Hydrogen a ilha criada em uma tentativa. O vídeo mostra edifícios e outros pontos de referência.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-208"></a>
### Caso 208: [Um painel interativo sobre a singularidade](https://x.com/Moleh1ll/status/2122032596263776351) (por [@Moleh1ll](https://x.com/Moleh1ll))

**Prototipe uma sequência interativa curta em torno de um só conceito visual.**

O autor atribui o painel sobre singularidade ao Hydrogen. A gravação mostra o resultado com pouco contexto de implementação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

Tipo: Demo | Data: 2026-11-15

---

<a id="case-225"></a>
### Caso 225: [Uma esfera de água no aplicativo Gemini](https://x.com/Google/status/2122366286659289502) (por [@Google](https://x.com/Google))

**Use uma cena óptica simples para inspecionar reflexos e refração.**

O Google apresenta uma esfera de aspecto aquoso com a inscrição Hydrogen e atribui o visual ao modelo no Gemini. Não explica o processo de renderização.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

Tipo: Demo | Data: 2026-11-16

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

<a id="case-43"></a>
### Caso 43: [Hydrogen pela API e Carbon no Antigravity](https://x.com/huang18825/status/2120876396264444314) (por [@huang18825](https://x.com/huang18825))

**Registre o ambiente de cada execução ao comparar imagens geradas com a mesma instrução.**

O autor mostra lado a lado o Hydrogen pela API e o Carbon pelo Antigravity. Os 4 minutos e 47 segundos correspondem ao Hydrogen nesse ambiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-44"></a>
### Caso 44: [Sombras na comparação entre Hydrogen e Astra](https://x.com/SPAC89/status/2120911537296515321) (por [@SPAC89](https://x.com/SPAC89))

**Avalie detalhes de renderização junto com o custo e o tempo de ambas as execuções.**

O autor preferiu o resultado do Hydrogen porque incluía uma sombra e relata que terminou mais rápido no ambiente usado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-45"></a>
### Caso 45: [Comparação de movimento 3D procedural](https://x.com/SPAC89/status/2120923185981915156) (por [@SPAC89](https://x.com/SPAC89))

**Registre o tempo de geração ao comparar a continuidade e a composição das animações.**

O autor atribui uma forma 3D listrada ao Hydrogen High, relata menos de cinco minutos e compara o resultado com modelos mais caros no próprio teste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-46"></a>
### Caso 46: [Um teste visual de 89 minutos no PokéBench](https://x.com/StatsWire/status/2120923685296988296) (por [@StatsWire](https://x.com/StatsWire))

**Registre turnos e falhas de API junto com o resultado de um teste prolongado de agente visual.**

A fonte relata que, antes do lançamento, o Hydrogen High derrotou Brock no Vertex em 365 turnos e 89 minutos, sem chamadas de API com falha. O resultado é específico desse ambiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-47"></a>
### Caso 47: [Hydrogen e DeepSeek criam a mesma cena 3D](https://x.com/AiHubMix/status/2120928687537418581) (por [@AiHubMix](https://x.com/AiHubMix))

**Registre tempo e custo de API separadamente ao comparar os resultados visuais.**

A AIHubMix usou a mesma instrução de cena 3D com Hydrogen e DeepSeek V4.1 Flash no maior nível de raciocínio disponível. Relata 3 minutos e US$ 1,30 para Hydrogen e 100 minutos e US$ 0,90 para DeepSeek.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-53"></a>
### Caso 53: [Tempo e custo por tarefa no Agent Arena](https://x.com/arena/status/2120940869889175840) (por [@arena](https://x.com/arena))

**Compare latência, custo e tokens de saída por tarefa com a taxa de sucesso geral.**

O Agent Arena informa medianas de 5,3 minutos e US$ 1,60 por tarefa para Hydrogen High. O modelo usou mais tokens de saída que Carbon e Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-54"></a>
### Caso 54: [Testes de documentos visuais e de terminal](https://x.com/ArtificialAnlys/status/2120941511223185722) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Considere separadamente os resultados em documentos e terminal ao escolher o orçamento de raciocínio.**

A Artificial Analysis aponta bom desempenho em documentos visuais e ganhos desiguais no terminal. Raciocínio extra elevou a nota do terminal científico, enquanto a do Terminal-Bench geral ficou em 54%.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-55"></a>
### Caso 55: [Resultados no Vals Index e no Tax Agent](https://x.com/ValsAI/status/2120943893894303808) (por [@ValsAI](https://x.com/ValsAI))

**Consulte o resultado em uma tarefa especializada junto com a avaliação agregada.**

A Vals AI informa 68,5% no índice e primeira posição em Tax Agent no momento do teste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-56"></a>
### Caso 56: [Hydrogen no CursorBench com raciocínio padrão](https://x.com/cursor_ai/status/2120944639633211619) (por [@cursor_ai](https://x.com/cursor_ai))

**Use a pontuação padrão como referência para testar seu próprio repositório.**

O Cursor informa 54,3% para Hydrogen com o raciocínio padrão e 39,6% para Gemini 3.8 Flash em seu benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-57"></a>
### Caso 57: [Quatro modelos animam uma batalha de arqueiros](https://x.com/IndependentEco/status/2120945011277590733) (por [@IndependentEco](https://x.com/IndependentEco))

**Compare a clareza das ações em cada animação.**

O autor mostra lado a lado Hydrogen, Fable 5.2, GPT-6.1 Sol e Carbon em uma batalha de arqueiros.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-61"></a>
### Caso 61: [Hydrogen no FrontierCode da Devin](https://x.com/cognition/status/2120950876248641588) (por [@cognition](https://x.com/cognition))

**Avalie se os patches podem ser integrados e registre o ambiente de cada agente.**

A Cognition informa 38,2% no FrontierCode 2.0. O ambiente usado para Hydrogen difere do Devin CLI usado com os demais modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-64"></a>
### Caso 64: [Busca na web apesar de uma restrição explícita](https://x.com/amanunreal/status/2120954045615768054) (por [@amanunreal](https://x.com/amanunreal))

**Confira se o modelo evitou ferramentas quando o fluxo exige uma resposta sem navegação.**

O autor relata que Hydrogen fez uma busca apesar do pedido para evitar pesquisa e chamadas de ferramentas. É um exemplo isolado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-12

---

<a id="case-65"></a>
### Caso 65: [Consumo de cota num Swarm do Antigravity](https://x.com/HarshithLucky3/status/2120954399971487774) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Registre o volume de tokens e a cota consumida em uma execução multiagente.**

O autor relata 17 milhões de tokens e 21% de uma cota de cinco horas ao usar Swarm no seu plano. Os números se referem a essa sessão.

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

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-66"></a>
### Caso 66: [Chamadas de ferramentas em tarefas profissionais](https://x.com/mercor/status/2120957582139642095) (por [@mercor](https://x.com/mercor))

**Observe como um agente reúne contexto antes de agir em tarefas profissionais.**

A Mercor informa 78,0% de Pass@1 no APEX-Agents e média de 93 chamadas de ferramentas por tarefa. A avaliação abrange direito, consultoria e bancos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-68"></a>
### Caso 68: [Quatro modelos animam um mago e um dragão](https://x.com/IndependentEco/status/2120964690906161461) (por [@IndependentEco](https://x.com/IndependentEco))

**Compare encenação, clareza da ação e efeitos em versões da mesma cena.**

O vídeo mostra Hydrogen e três modelos Claude em uma luta entre mago e dragão. O autor preferiu o resultado do Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-71"></a>
### Caso 71: [MazeBench mostra taxas de sucesso baixas](https://x.com/patience_cave/status/2120973681937809766) (por [@patience_cave](https://x.com/patience_cave))

**Teste labirintos antes de depender do raciocínio espacial.**

Com a configuração usada, a comparação do MazeBench informa 1% para Hydrogen, 4% para Sonnet 5.5 e 8% para GPT-6.1 Terra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-72"></a>
### Caso 72: [Três modelos Gemini criam cenas de veleiros](https://x.com/Octoberry/status/2120974412144902376) (por [@Octoberry](https://x.com/Octoberry))

**Compare movimento e detalhes do ambiente em uma cena temática no Three.js.**

O autor mostra veleiros feitos com Hydrogen, Argon e Carbon. Preferiu os detalhes do Carbon e considerou o Hydrogen próximo do Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-75"></a>
### Caso 75: [A leitura de um número de camisa esgota o orçamento](https://x.com/skalskip92/status/2120994631072776235) (por [@skalskip92](https://x.com/skalskip92))

**Defina um limite de raciocínio e uma alternativa ao ler um detalhe pequeno em uma imagem.**

O avaliador relata 131.069 tokens de raciocínio com Hydrogen XHigh e nenhum número de camisa após 9 minutos e 55 segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-12

---

<a id="case-76"></a>
### Caso 76: [Comparação de famílias de modelos no ClutterBench](https://x.com/AdamHoltererer/status/2121000759118459138) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Use um teste com elementos sobrepostos para verificar se os pontos fortes gerais do modelo se aplicam à tarefa.**

Nos resultados compartilhados pelo autor, Hydrogen lidera os modelos Gemini mostrados, mas fica abaixo dos modelos OpenAI da comparação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-12

---

<a id="case-78"></a>
### Caso 78: [Um busto anatômico em corte no estilo Minecraft](https://x.com/jan_volad/status/2121026531472339340) (por [@jan_volad](https://x.com/jan_volad))

**Verifique se um corte gerado contém as estruturas internas solicitadas.**

O autor deu a Hydrogen e Argon a mesma tarefa em uma tentativa. Relata que identificou crânio, costelas e coluna no busto estilo Minecraft feito pelo Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-79"></a>
### Caso 79: [Três modelos renderizam o mesmo objeto](https://x.com/luckeyfaraday/status/2121030005899825504) (por [@luckeyfaraday](https://x.com/luckeyfaraday))

**Acompanhe tokens e qualidade separadamente quando um modelo mais barato puder consumir mais tokens.**

Hydrogen, Carbon e Fable 5.2 reproduzem um objeto em forma de rifle. O autor relata 3,69 milhões de tokens e US$ 1,62 para Hydrogen, ante 398.000 tokens e US$ 0,77 para Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

Tipo: Evaluation | Data: 2026-11-12

---

<a id="case-80"></a>
### Caso 80: [Raciocínio indutivo e consumo de tokens](https://x.com/s_batzoglou/status/2121037853258129811) (por [@s_batzoglou](https://x.com/s_batzoglou))

**Acompanhe os tokens de entrada e saída faturados junto com a nota de raciocínio.**

O avaliador coloca Hydrogen em quarto lugar num teste de indução com 100 problemas, perto de Opus 5.5. Relata 55 milhões de tokens de saída e 307 milhões de entrada faturados e deixa o cálculo em aberto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-83"></a>
### Caso 83: [Três modelos animam um animal em 3D](https://x.com/leo114119/status/2121054098753785915) (por [@leo114119](https://x.com/leo114119))

**Observe anatomia e movimento no mesmo teste de modelagem.**

A fonte compara Hydrogen, GPT-6.1 Terra e Claude Haiku 5.5. O autor aponta problemas no Hydrogen, e o vídeo se limita a essa tarefa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-84"></a>
### Caso 84: [Hydrogen e Qwen no ts-bench](https://x.com/gosrum/status/2121058334552060102) (por [@gosrum](https://x.com/gosrum))

**Analise falhas de chamadas a ferramentas junto com a avaliação geral.**

A fonte compara Hydrogen e Qwen4 Max Preview no ts-bench e comenta a confiabilidade das chamadas nessas execuções. A captura mostra os resultados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-85"></a>
### Caso 85: [Simulação de negócios no Vending-Bench](https://x.com/andonlabs/status/2121061429889642497) (por [@andonlabs](https://x.com/andonlabs))

**Compare a receita simulada com o custo de operar o agente.**

A Andon Labs informa que Hydrogen ficou em terceiro no Vending-Bench 2 e gerou mais receita que modelos de preço semelhante na simulação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-89"></a>
### Caso 89: [Quatro modelos constroem uma ilha em miniatura](https://x.com/xKaka1456/status/2121111495358697924) (por [@xKaka1456](https://x.com/xKaka1456))

**Compare os projetos junto com o tempo e o preço do ambiente de cada execução.**

A fonte mostra quatro ilhas e informa 4 minutos com Hydrogen, 20 com GPT-6.1 Terra, 40 com Sol e 60 com DeepSeek. O Hydrogen não gerou custo adicional no ambiente do autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-91"></a>
### Caso 91: [Rasgamento de tecidos em animações feitas com código](https://x.com/MichaelLee009/status/2121126779276402904) (por [@MichaelLee009](https://x.com/MichaelLee009))

**Teste elasticidade, rasgos e interação com pelos na mesma instrução.**

O autor compara animações feitas com Hydrogen e Claude Fable 5.2 e prefere visualmente a segunda. Não informa ajustes equivalentes nem validação física independente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-94"></a>
### Caso 94: [Verificação de fatos com fonte inacessível](https://x.com/cagrimbakirci/status/2121130756684886279) (por [@cagrimbakirci](https://x.com/cagrimbakirci))

**Exija uma referência consultável antes de agir com base no veredito sobre uma captura.**

O autor perguntou se uma publicação em uma captura era verdadeira. Relata que Hydrogen confirmou, abriu repetidamente uma ferramenta de verificação e não mostrou a fonte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-13

---

<a id="case-96"></a>
### Caso 96: [Hydrogen e Sol desenham um pelicano em 2D](https://x.com/YxzRainy/status/2121148582166491164) (por [@YxzRainy](https://x.com/YxzRainy))

**Compare duração e movimento numa tarefa simples de animação 2D.**

O vídeo mostra Hydrogen e GPT-6.1 Sol animando um pelicano ciclista. O autor relata 28 segundos e 6 minutos e 51 segundos, sem comprovar equivalência dos ajustes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-98"></a>
### Caso 98: [Quatro modelos criam um jogo de balanço em teias](https://x.com/StatsWire/status/2121172215182065807) (por [@StatsWire](https://x.com/StatsWire))

**Compare deslocamento e controles em jogos com a mesma restrição de arquivo único.**

Quatro modelos Gemini encaram o mesmo desafio 3D em um HTML autônomo sem recursos externos. Hydrogen usou Extra High e Gemini 3.8 Flash, Argon e Carbon usaram High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-100"></a>
### Caso 100: [Quatro modelos fazem um diorama arquitetônico](https://x.com/Jackson77li/status/2121172890838352306) (por [@Jackson77li](https://x.com/Jackson77li))

**Compare os resultados com o mesmo briefing e observe as diferentes soluções de iluminação.**

Hydrogen, GPT-6.2, Claude Fable 5.2 e DeepSeek receberam a mesma instrução segundo o autor. A ordem e os comentários sobre velocidade são subjetivos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-103"></a>
### Caso 103: [Três modelos renderizam uma cena de trem](https://x.com/xKaka1456/status/2121193705810104515) (por [@xKaka1456](https://x.com/xKaka1456))

**Use a mesma cena para comparar tempos nas configurações escolhidas.**

O autor relata cerca de 3 minutos com Hydrogen, 20 com GPT-6.1 Terra e 68 com Qwen4 Max Preview. O vídeo não documenta ajustes nem iterações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-104"></a>
### Caso 104: [Uma Chinatown chuvosa com raciocínio Extra](https://x.com/qingzhoucloud/status/2121198911515967952) (por [@qingzhoucloud](https://x.com/qingzhoucloud))

**Meça a duração e confira o resultado antes de definir o nível de raciocínio de uma animação grande.**

O autor usou Hydrogen Extra com uma instrução de outro criador e relata quase quatro horas para o MP4. A comparação com Claude Fable 5.2 usa ambientes pouco comparáveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-106"></a>
### Caso 106: [Três modelos criam um visualizador de planetas](https://x.com/Stargridcompass/status/2121208957276713181) (por [@Stargridcompass](https://x.com/Stargridcompass))

**Compare uma interface científica visual com a mesma instrução em diferentes modelos.**

O vídeo mostra Claude Fable 5.2, GPT-6.2 Sol e Hydrogen. A ordem é uma avaliação visual do autor, sem ajustes equivalentes ou pontuação objetiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-107"></a>
### Caso 107: [Quatro modelos recriam o Chrome Dino](https://x.com/noclipepe/status/2121219775170761044) (por [@noclipepe](https://x.com/noclipepe))

**Cronometre as recriações de um jogo conhecido e compare os resultados jogáveis.**

O autor relata 18 minutos e 41 segundos para Hydrogen no AI Studio e 45 minutos e 30 segundos para Fable 5.2. O vídeo inclui Qwen4-Max-Preview, Carbon e notas visuais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-109"></a>
### Caso 109: [Dois agentes de programação constroem navios diferentes](https://x.com/marcthecreatorr/status/2121221667619852660) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Compare o primeiro resultado aproveitável e o custo de revisão no ambiente escolhido.**

A mesma instrução foi usada com Sonnet no Claude Code e Hydrogen no Cursor. O autor relata que Hydrogen foi mais rápido, mas precisou de uma segunda versão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-111"></a>
### Caso 111: [Quatro modelos simulam um cerco com trabuco](https://x.com/StatsWire/status/2121226579141386285) (por [@StatsWire](https://x.com/StatsWire))

**Compare protótipos jogáveis de física na mesma tarefa e registre os níveis de raciocínio.**

A cena usa centenas de blocos de pedra. O autor relata 10 minutos e 3 segundos para Hydrogen Extra High e 23 minutos e 33 segundos para Carbon High. Gemini 3.8 Flash High foi o mais rápido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-116"></a>
### Caso 116: [Memória persistente no FrontierMemory](https://x.com/Letta_AI/status/2121255895745351874) (por [@Letta_AI](https://x.com/Letta_AI))

**Compare desempenho e gasto por execução ao escolher um modelo para memória de longo prazo.**

A Letta informa 64,4% com Hydrogen, igual ao Argon, a cerca de US$ 100 por execução de memória. Carbon obteve 71,1% a cerca de US$ 94 nessa configuração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-117"></a>
### Caso 117: [Hydrogen em um agente de voz LiveKit com falhas](https://x.com/livekit/status/2121256982023672076) (por [@livekit](https://x.com/livekit))

**Provoque uma falha controlada e verifique se o agente relata resultados sem evidência.**

A LiveKit testou Hydrogen em um agente de voz com falhas intencionais e relata zero resultados falsos. O fornecedor compara com Gemini 3.8 Flash e inclui seu relatório.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-123"></a>
### Caso 123: [Três modelos Gemini animam um ciclista](https://x.com/AI_Screening/status/2121281026916057443) (por [@AI_Screening](https://x.com/AI_Screening))

**Compare cenas curtas com o mesmo briefing e registre a duração de cada execução.**

O autor mostra Carbon, Argon e Hydrogen animando um ciclista. Relata cerca de 90 segundos para Hydrogen e mais de cinco minutos para Argon, e prefere Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-126"></a>
### Caso 126: [Dois modelos constroem um mundo LEGO](https://x.com/kepochnik/status/2121286219669836027) (por [@kepochnik](https://x.com/kepochnik))

**Compare a parte do mundo que cada modelo consegue criar no tempo disponível.**

O autor mostra versões de Fable 5.2 e Hydrogen de um mundo LEGO e relata 44 e 28 minutos, respectivamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-127"></a>
### Caso 127: [Correção de bugs reintroduzidos em dois repositórios](https://x.com/PawelHuryn/status/2121286545223086302) (por [@PawelHuryn](https://x.com/PawelHuryn))

**Introduza falhas conhecidas para medir o que o agente consegue detectar e corrigir.**

O avaliador plantou 105 bugs em dois repositórios. Nesse ambiente Hydrogen Extra High ficou logo atrás de Sonnet 5.5 Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-128"></a>
### Caso 128: [Boneco palito contra o cursor em dois modelos](https://x.com/DanielZambrini/status/2121289822677483740) (por [@DanielZambrini](https://x.com/DanielZambrini))

**Compare como as animações interativas respondem ao ponteiro.**

O autor preferiu o resultado do Fable, mas considerou Hydrogen adequado para uma execução de menor custo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-130"></a>
### Caso 130: [Dois modelos renderizam uma paisagem de montanha](https://x.com/ZryMiller/status/2121295750122594440) (por [@ZryMiller](https://x.com/ZryMiller))

**Compare composição, tempo de geração e custo separadamente em uma paisagem animada.**

O autor mostra Hydrogen e Opus 5.5 e relata 20 minutos e 30 segundos e US$ 0,50 para Hydrogen, ante 11 minutos e 23 segundos e US$ 2,50 para Opus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-131"></a>
### Caso 131: [Tradução do inglês para o persa em ambiente próprio](https://x.com/MatinSenPai/status/2121296733258887365) (por [@MatinSenPai](https://x.com/MatinSenPai))

**Avalie um trecho difícil com uma referência produzida por uma pessoa.**

O autor deu 94 de 100 ao Hydrogen numa tarefa própria em ambiente personalizado. As notas são subjetivas e dependem dessa configuração.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-133"></a>
### Caso 133: [Quatro modelos criam um navio afundando](https://x.com/remoteugur/status/2121302956741902451) (por [@remoteugur](https://x.com/remoteugur))

**Meça fidelidade visual, tempo e custo separadamente para a mesma cena.**

O autor informa 8,6 minutos e US$ 1,16 com Hydrogen, contra 10,8 minutos e US$ 1,06 com Gemini 3.8 Flash. Também testou Carbon e Opus 5.5 e preferiu o realismo do Opus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-135"></a>
### Caso 135: [Comparação cega de redação com quatro modelos](https://x.com/quintanilha/status/2121315967447757299) (por [@quintanilha](https://x.com/quintanilha))

**Oculte os nomes dos modelos antes de escolher o texto a utilizar.**

O autor preferiu Hydrogen em um teste cego de redação com quatro modelos. Também o considerou mais rápido e mais barato que Carbon nesse teste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-136"></a>
### Caso 136: [Detecção visual e leitura por nível de raciocínio](https://x.com/skalskip92/status/2121322414453694489) (por [@skalskip92](https://x.com/skalskip92))

**Meça separadamente precisão da detecção e leitura, custo e latência em cada nível.**

O avaliador compara Hydrogen, Argon e Carbon. Hydrogen High teve média de 29,3 segundos por imagem e notas de 64,6 em detecção e 87,2 em leitura. Carbon High obteve notas maiores nas duas, com maior custo e latência.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-13

---

<a id="case-137"></a>
### Caso 137: [Quatro modelos recriam a casa de Up](https://x.com/noclipepe/status/2121326233044537688) (por [@noclipepe](https://x.com/noclipepe))

**Compare as escolhas de modelagem 3D com a mesma imagem e o mesmo briefing.**

O autor afirma que Hydrogen foi o mais rápido e mais barato entre quatro opções e prefere o resultado de Fable. Ajustes e custos foram informados pela fonte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

Tipo: Evaluation | Data: 2026-11-13

---

<a id="case-144"></a>
### Caso 144: [Uma dança com câmera fixa](https://x.com/notoro_ai/status/2121427503952834562) (por [@notoro_ai](https://x.com/notoro_ai))

**Verifique se uma animação de referência mantém desenho, composição e câmera.**

O autor mostra uma instrução em japonês e um clipe associado ao Hydrogen no Gemini. A instrução exige câmera fixa e preservar o estilo. O modelo de vídeo não é identificado.

**Instrução:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-145"></a>
### Caso 145: [Um agente de programação fica preso no teste inicial](https://x.com/Its_lakshya_ai/status/2121431788266659919) (por [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**Defina um tempo máximo e acompanhe o progresso do teste de referência antes de esperar uma correção.**

Uma captura do Antigravity mostra Hydrogen ainda rodando um teste após longa espera. Registra um pedido para parar e investigar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-14

---

<a id="case-147"></a>
### Caso 147: [Dois modelos criam um braço robótico interativo](https://x.com/gmi_cloud/status/2121467337119588834) (por [@gmi_cloud](https://x.com/gmi_cloud))

**Cheque se as juntas do braço em Three.js reagem de forma coerente à interação.**

A GMI Cloud mostra Hydrogen e Sonnet 5.5 na tarefa do braço em Three.js. O fornecedor preferiu Sonnet e compartilha as gravações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-151"></a>
### Caso 151: [Hydrogen e Sol constroem uma vila nevada](https://x.com/badboyfoxy/status/2121501015442669866) (por [@badboyfoxy](https://x.com/badboyfoxy))

**Avalie duração, gasto e qualidade da cena como resultados separados.**

O autor relata 3 minutos e US$ 1,37 para Hydrogen High e 15 minutos e US$ 4,03 para Sol High. Preferiu a solução visual do Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-152"></a>
### Caso 152: [Uma ilha em Three.js com níveis High e Ultra](https://x.com/laopai1990/status/2121502334866096160) (por [@laopai1990](https://x.com/laopai1990))

**Compare aspecto e duração considerando os níveis de raciocínio, sem equiparar cotas de produtos distintos.**

O autor compara Hydrogen High com GPT-6.1 Sol Ultra e relata cerca de 90 segundos e 30 minutos, respectivamente. Os custos são estimados e os níveis diferem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-157"></a>
### Caso 157: [Comparação dos detalhes de um controle PS5 em 3D](https://x.com/Stargridcompass/status/2121528563254043015) (por [@Stargridcompass](https://x.com/Stargridcompass))

**Observe o sombreamento dos botões e os detalhes da parte traseira.**

O autor relata cerca de três minutos com Hydrogen High e onze com GPT-6.2 Sol. Considerou mais completos os controles laterais e traseiros do Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-159"></a>
### Caso 159: [CursorBench com diferentes orçamentos de raciocínio](https://x.com/Beamsters1/status/2121538515909628111) (por [@Beamsters1](https://x.com/Beamsters1))

**Compare taxas de sucesso entre níveis antes de definir uma configuração mais rápida.**

O autor observou uma alta acentuada no CursorBench 4.0 ao ampliar o raciocínio do Hydrogen. O resultado se limita aos ajustes testados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-14

---

<a id="case-160"></a>
### Caso 160: [Três modelos renderizam um templo estelar](https://x.com/YxzRainy/status/2121551796766376081) (por [@YxzRainy](https://x.com/YxzRainy))

**Meça a estabilidade da renderização separadamente do detalhe visual.**

O autor compara Hydrogen, DeepSeek V4.1 1017 e Qwen4 Max Preview em uma cena 3D. Relata Hydrogen mais rápido, sem tela preta ou oscilação nesse ensaio e com menos detalhes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-162"></a>
### Caso 162: [Reavaliação de um desenho de migração existente](https://x.com/is_llll/status/2121565725072490559) (por [@is_llll](https://x.com/is_llll))

**Peça aos agentes que considerem se a migração deve substituir a arquitetura atual.**

O autor mostra uma revisão em que Hydrogen e Argon apoiaram a abordagem existente. Claude Opus propôs substituir e migrar mais cedo. É uma avaliação de um projeto.

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

Tipo: Limit | Data: 2026-11-14

---

<a id="case-165"></a>
### Caso 165: [Dois modelos criam um jogo de fuga de um templo](https://x.com/runable_hq/status/2121596515474964556) (por [@runable_hq](https://x.com/runable_hq))

**Compare se iluminação e clima tornam o mesmo jogo legível.**

A Runable apresenta implementações de Hydrogen e Argon. O fornecedor descreve a iluminação de Hydrogen como mais sombria e a de Argon como mais clara.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-166"></a>
### Caso 166: [Três modelos Gemini animam um buggy de rali](https://x.com/teddyaisi/status/2121604816380010719) (por [@teddyaisi](https://x.com/teddyaisi))

**Verifique se a suspensão e a aderência fazem sentido em uma curva inclinada.**

O autor compara Carbon, Argon e Hydrogen em uma animação Three.js numa pedreira. A tarefa pede compressão da suspensão e derrapagem em pista de terra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-169"></a>
### Caso 169: [Dois modelos animam Chasing Views](https://x.com/VulKan42069/status/2121625271493382166) (por [@VulKan42069](https://x.com/VulKan42069))

**Compare resultado e duração com o nível de raciocínio de cada modelo em vista.**

O autor mostra Chasing Views com Hydrogen Extra High e Opus 5.5 High. Relata 22 e 18 minutos, respectivamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-170"></a>
### Caso 170: [Velocidade e custo no Design Creativity Bench](https://x.com/Kombaico/status/2121635837180031129) (por [@Kombaico](https://x.com/Kombaico))

**Compare tempo e custo por projeto com a nota de criatividade.**

O responsável informa 49,4 para Hydrogen e medianas de 3,4 minutos e US$ 0,39 por projeto. Nessa avaliação Argon foi mais lento e barato, e Carbon, mais lento e caro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

Tipo: Benchmark | Data: 2026-11-14

---

<a id="case-172"></a>
### Caso 172: [Quatro modelos animam um galope no deserto](https://x.com/Marlenuii/status/2121664345818235177) (por [@Marlenuii](https://x.com/Marlenuii))

**Compare o contato das patas e a transferência de peso antes de julgar luz e detalhes da malha.**

O autor comparou Astra, Carbon, Fable 5.2 e Hydrogen na animação de um cavalo. Preferiu o galope do Astra e criticou a construção do cavalo do Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-174"></a>
### Caso 174: [Pesquisa em computação no FrontierCS 2](https://x.com/wenhaocha1/status/2121679887400403308) (por [@wenhaocha1](https://x.com/wenhaocha1))

**Use um teste de pesquisa ao lado da programação comum e registre o ambiente.**

A fonte relata Hydrogen em sétimo pela taxa de sucesso no FrontierCS 2 usando Antigravity. O benchmark trata de problemas de pesquisa em computação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

Tipo: Benchmark | Data: 2026-11-14

---

<a id="case-175"></a>
### Caso 175: [Quatro modelos em Rio Above the Clouds](https://x.com/EnvolDev/status/2121701704139956250) (por [@EnvolDev](https://x.com/EnvolDev))

**Compare custo, duração e qualidade percebida com o mesmo briefing criativo.**

O avaliador relata US$ 6,21 para Hydrogen Extra High e diz que foi seu resultado menos preferido. Astra levou menos tempo. A fonte não confirma vídeo gerado nativamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-176"></a>
### Caso 176: [Hydrogen em tarefas técnicas do GBENCH](https://x.com/leo_linsky/status/2121710421891780864) (por [@leo_linsky](https://x.com/leo_linsky))

**Use resultados verificáveis de programação e de outras tarefas junto com preço e duração.**

O GBENCH inclui projeto de circuitos e raciocínio abstrato na avaliação do Hydrogen. O responsável descreve Sol como mais competitivo com preço e velocidade semelhantes.

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

Tipo: Benchmark | Data: 2026-11-14

---

<a id="case-177"></a>
### Caso 177: [Treinamento de carros para estacionar em paralelo](https://x.com/noclipepe/status/2121734795738652934) (por [@noclipepe](https://x.com/noclipepe))

**Compare o progresso do aprendizado e as taxas finais de sucesso em simulações geradas.**

O autor usou a mesma instrução e relata 5 de 44 carros estacionados com Hydrogen e 26 de 40 com Fable 5.2. As execuções duraram 5,6 e 24 minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

Tipo: Evaluation | Data: 2026-11-14

---

<a id="case-181"></a>
### Caso 181: [Hydrogen no Terminal-Bench 4.0](https://x.com/gosrum/status/2121785156273160558) (por [@gosrum](https://x.com/gosrum))

**Observe conclusão e custo das tarefas ao escolher um modelo de programação para terminal.**

O teste independente do Terminal-Bench 4.0 compara Hydrogen, Claude Opus 5.5 e GPT-6.1 Sol. O avaliador relata notas semelhantes e custo intermediário para Hydrogen, com ressalva sobre a maturidade dos ambientes.

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

Tipo: Benchmark | Data: 2026-11-15

---

<a id="case-183"></a>
### Caso 183: [Três modelos Gemini animam um polvo](https://x.com/teddyaisi/status/2121800606406885880) (por [@teddyaisi](https://x.com/teddyaisi))

**Observe se o contato com a rocha impulsiona o corpo quando o polvo se agarra.**

O autor mostra Carbon, Argon e Hydrogen em Three.js. Pede comparar como o tentáculo se prende à borda do recife e faz o corpo avançar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-187"></a>
### Caso 187: [Um teste de modelagem de castelos](https://x.com/nemumusitocha/status/2121848375998063012) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Compare os castelos e o consumo de recursos em diferentes execuções.**

O autor mostra um castelo 3D com Hydrogen e cita testes anteriores. Os 3% da cota semanal de Google AI Pro se referem a essa execução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-191"></a>
### Caso 191: [Uma estimativa muda com o aumento do escopo](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (por [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Peça que o modelo explique o escopo e as premissas sempre que a estimativa variar muito.**

O autor mostra uma conversa em que a estimativa passou de um mês a um ano após pedir um prazo realista com os recursos previstos. A duração real não é determinada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-15

---

<a id="case-193"></a>
### Caso 193: [Uma pergunta de calendário com anos bissextos](https://x.com/itsvishaltwt/status/2121891117050589249) (por [@itsvishaltwt](https://x.com/itsvishaltwt))

**Use uma conversão simples para verificar se a resposta contempla casos especiais do calendário.**

O autor perguntou a Hydrogen High e GPT quantos segundos existem em um ano. As duas capturas dão resultados para anos comuns e bissextos, e Hydrogen também calcula a média do calendário gregoriano.

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

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-196"></a>
### Caso 196: [Limites de assinatura desatualizados em uma resposta](https://x.com/take14262/status/2121934737539514533) (por [@take14262](https://x.com/take14262))

**Consulte fontes primárias para confirmar os termos atuais e os nomes dos modelos.**

O autor mostra Hydrogen confundindo nomes semelhantes e indicando janelas desatualizadas de um plano Qwen. As capturas documentam esses aparentes erros.

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

Tipo: Limit | Data: 2026-11-15

---

<a id="case-197"></a>
### Caso 197: [Revisão da narrativa de uma animação WebGL](https://x.com/snakajima/status/2121939899242996058) (por [@snakajima](https://x.com/snakajima))

**Peça uma história que avance com clareza se a primeira versão for complexa visualmente, mas sem progressão.**

O autor inclui a primeira versão e uma revisão após pedir menos ruído e mais história. Preferiu a revisão e ainda avaliou melhor o resultado do Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

Tipo: Limit | Data: 2026-11-15

---

<a id="case-199"></a>
### Caso 199: [Dois modelos programam uma luta de dragões](https://x.com/DrstaOne/status/2121947540509831302) (por [@DrstaOne](https://x.com/DrstaOne))

**Compare como cada animação coordena dois personagens na mesma cena.**

O autor compara Qwen-4 Max e Hydrogen em uma luta feita com código sobre um templo na montanha. A instrução é creditada a outro criador.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-201"></a>
### Caso 201: [Uma instrução reproduzível de pelicano em Three.js](https://x.com/Aki_LIG/status/2121960943361896596) (por [@Aki_LIG](https://x.com/Aki_LIG))

**Confira se patas, rodas e direção se movem de forma coordenada.**

O autor divulga a instrução completa em japonês e mostra Hydrogen numa estrada litorânea. Diz que já usou a mesma instrução com GPT-6.1 Terra. O vídeo associado mostra Hydrogen.

**Instrução:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-205"></a>
### Caso 205: [Uma instrução sobre uma cabana em três plataformas](https://x.com/doe_naps/status/2121999317628330476) (por [@doe_naps](https://x.com/doe_naps))

**Confira o formato de saída ao mover uma tarefa visual entre configurações e plataformas.**

O autor relata saída estática com Hydrogen High no Antigravity, Hydrogen Extra High no AI Studio e Carbon High no Antigravity. Uma execução com o rótulo Hydrogen no Arena fez SVG animado, sem identificação independente dessa versão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-206"></a>
### Caso 206: [Dois painéis com a mesma instrução](https://x.com/fiapp_pro/status/2122014257667846338) (por [@fiapp_pro](https://x.com/fiapp_pro))

**Compare layout e hierarquia de informação usando o mesmo briefing de interface.**

O autor publica capturas atribuídas a GPT-6.1 Sol e Hydrogen. É possível comparar a aparência, mas não a implementação, os ajustes ou o funcionamento.

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

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-209"></a>
### Caso 209: [Dois modelos animam uma cena com deslocamento lateral](https://x.com/rubenssoto_ai/status/2122035198728814753) (por [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Observe continuidade de movimento e custo ao comparar cenas de ação.**

O autor compara Hydrogen e GPT-6 Astra em uma animação lateral. Prefere o movimento do Hydrogen e relata custo menor nessas duas execuções.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

Tipo: Evaluation | Data: 2026-11-15

---

<a id="case-212"></a>
### Caso 212: [Fórmulas sem renderização numa resposta em japonês](https://x.com/ToraMutton/status/2122131489718759930) (por [@ToraMutton](https://x.com/ToraMutton))

**Verifique apresentação e exatidão quando a resposta contém comandos TeX.**

O autor mostra o Gemini exibindo notação bruta em vez de equações formatadas após a transição para Hydrogen. A captura mostra uma falha na interface.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

Tipo: Limit | Data: 2026-11-16

---

<a id="case-214"></a>
### Caso 214: [Teste de uma instrução para permanecer em silêncio](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (por [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Confira se o modelo consegue não responder quando o fluxo exige.**

O autor compartilha uma captura de um teste sem resposta e relata diferenças entre Carbon e Argon. A fonte mostra apenas esse conjunto de testes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

Tipo: Evaluation | Data: 2026-11-16

---

<a id="case-216"></a>
### Caso 216: [Três modelos explicam um motor elétrico](https://x.com/analogalok/status/2122221106304352257) (por [@analogalok](https://x.com/analogalok))

**Compare clareza visual e controles didáticos com a mesma instrução de simulação.**

O autor comparou Hydrogen com dois modelos Qwen e preferiu o motor 3D e as explicações de física do Hydrogen. É a avaliação de um único teste.

**Instrução:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

Tipo: Evaluation | Data: 2026-11-16

---

<a id="case-217"></a>
### Caso 217: [Dois fluxos animam uma cena de mesa](https://x.com/GeroXBT/status/2122234332102435128) (por [@GeroXBT](https://x.com/GeroXBT))

**Confira detalhes, volume e o quadro final imóvel em relação ao briefing.**

O autor compara animações assistidas por Hydrogen e Astra com a mesma instrução via API. Prefere a fluidez da versão do Gemini, mas relata áudio mais baixo e movimento no final. O renderizador não é identificado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

Tipo: Evaluation | Data: 2026-11-16

---

<a id="case-221"></a>
### Caso 221: [Uma vila 2D com áudio procedural](https://x.com/marcthecreatorr/status/2122266495216459841) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Verifique se o som muda com os eventos na tela e anote a duração da criação.**

O autor compara Qwen 4 Max e Hydrogen com Extra High. Relata cerca de 75 minutos e US$ 0,90 com Qwen, contra 12 minutos e US$ 1,70 com Hydrogen. Preferiu a sintonia da música do Hydrogen com os eventos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[Reproduzir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

Tipo: Evaluation | Data: 2026-11-16

---

<a id="related-repositories"></a>
## Repositórios relacionados

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Exemplos e comparações do Gemini 4 Carbon

<a id="acknowledge"></a>
## 🙏 Agradecimentos

Obrigado aos criadores, desenvolvedores e avaliadores que compartilharam publicamente seu trabalho com o Hydrogen.

**Criadores das fontes:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*A atribuição segue as fontes públicas citadas e pode não identificar o criador original. Para correções ou solicitações de remoção, abra uma questão com uma fonte pública.*

Sugira um exemplo respaldado por fontes por meio de uma questão ou solicitação de integração, seguindo a lista de contribuição.
