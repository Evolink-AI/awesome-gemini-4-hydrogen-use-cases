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

# Guía y casos de uso destacados de Gemini 4 Hydrogen

## 🍌 Introducción

Explora Gemini 4 Hydrogen mediante aplicaciones con fuentes, flujos de programación y comparaciones prácticas.

**225 ejemplos muestran cómo se usa Hydrogen y dónde los resultados se quedan cortos.**

Cada caso enlaza su fuente y reconoce a su autor. Las notas identifican demostraciones, ejemplos del proveedor y comparaciones de creadores; no se reconstruyen las instrucciones que faltan.

## 📊 Resumen

- 225 casos en total, incluidos 185 añadidos el 17 de noviembre tras revisar 1.304 publicaciones de X. Las nuevas fuentes tenían más de 30 Me gusta al recopilarse.
- Cinco categorías abarcan agentes, aprendizaje y aplicaciones, hojas de cálculo y Search, 3D interactivo, y comparaciones y limitaciones.
- 264 recursos visuales originales, incluidos 168 videos reproducibles con miniatura y 96 imágenes.
- Gemini 4 Hydrogen se anunció el 12 de noviembre de 2026. Explora el modelo y sus opciones actuales de acceso en EvoLink.

> [!NOTE]
> La atribución del modelo, los costes, los tiempos y los resultados son afirmaciones de las fuentes salvo indicación contraria. Los vídeos se revisaron mediante fotogramas muestreados, no mediante pruebas funcionales completas. Las grabaciones de aplicaciones programadas no demuestran generación nativa de vídeo. Las diferencias de entornos de ejecución, niveles de razonamiento o número de iteraciones impiden considerar controladas las comparaciones.

**Referencias oficiales: [Anuncio de Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Ficha del modelo de Google DeepMind](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**Empieza aquí: [Explora Hydrogen en EvoLink](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [Obtén una clave de API (desde la página del modelo)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)**

<a id="quick-start"></a>
## ⚡ Inicio rápido

Empieza en EvoLink y utiliza después la API nativa de Gemini cuando quieras integrar Hydrogen en una aplicación.

1. [Ver Gemini 4 Hydrogen en el navegador](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [Crea o administra una clave de API de EvoLink (desde la página del modelo)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)

Solicitud mínima a la API nativa

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

[Lee la guía de inicio rápido de la API nativa de Gemini (desde la página del modelo)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

> [!TIP]
> Lee el texto generado en los campos candidates[].content.parts[].text de la respuesta.

> [!IMPORTANT]
> Guarda tu clave de API en una variable de entorno y nunca la incluyas en un commit. Consulta la documentación de la API para conocer las opciones de transmisión, razonamiento y otras solicitudes.

## 📑 Menú

| Sección | Casos |
|---|---|
| [⚡ Agentes y flujos de programación](#agents) | 30 |
| [💻 Aplicaciones y aprendizaje](#apps-learning) | 37 |
| [📊 Hojas de cálculo y Search](#data-search) | 9 |
| [🎮 3D interactivo e interfaces](#interactive-3d) | 48 |
| [🧪 Comparaciones y limitaciones](#comparisons-limits) | 101 |
| [Repositorios relacionados](#related-repositories) |  |
| [Inicio rápido](#quick-start) |  |
| [Agradecimientos](#acknowledge) |  |

| Caso | Categoría | Qué probar | Tipo |
|---|---|---|---|
| [Mantenimiento de código en Antigravity](#case-1) | Agentes y flujos de programación | Usa una tarea de mantenimiento acotada para evaluar conjuntamente modificaciones, uso de herramientas y verificación. | Demo |
| [Dieciséis aplicaciones canvas en paralelo](#case-2) | Agentes y flujos de programación | Divide el desarrollo en módulos independientes y define explícitamente las funciones de planificación, implementación y control de calidad. | Demo |
| [Polilla carmesí con un enjambre de varios modelos](#case-3) | Agentes y flujos de programación | Separa la orquestación de la implementación en un proyecto interactivo de programación creativa. | Demo |
| [Inspección y reparación con 3D Medic](#case-4) | Agentes y flujos de programación | Explora un agente que inspecciona un archivo 3D, detecta errores y propone reparaciones antes de exportarlo. | Demo |
| [Una escena de velero creada en Devin](#case-5) | Agentes y flujos de programación | Evalúa un modelo en el entorno de agente de programación que realmente piensas utilizar. | Demo |
| [Práctica de idiomas en Lingo City](#case-6) | Aplicaciones y aprendizaje | Combina tarjetas didácticas con una escena callejera interactiva para practicar idiomas en contexto. | Demo |
| [Romeo y Julieta como teatro de papel en 3D](#case-7) | Aplicaciones y aprendizaje | Convierte una lección concreta en una escena interactiva con un objetivo de aprendizaje claro. | Demo |
| [De una imagen de diseño a una web de lectura](#case-8) | Aplicaciones y aprendizaje | Usa un diseño de referencia para evaluar la comprensión visual y una implementación funcional de la interfaz. | Demo |
| [Un jardín de carpas koi construido en veinte módulos](#case-9) | Aplicaciones y aprendizaje | Construye una escena más grande con módulos pequeños en lugar de esperar un resultado completo de una sola instrucción. | Demo |
| [Un juego educativo sobre fusión de protones](#case-10) | Aplicaciones y aprendizaje | Crea un prototipo de explicación interactiva de un proceso científico y comprueba después su base científica. | Demo |
| [Un paisaje animado en Google Sheets](#case-11) | Hojas de cálculo y Search | Usa una animación poco convencional en una hoja de cálculo para inspeccionar el código generado y las actualizaciones de celdas. | Demo |
| [Web de datos interactivos Folio](#case-12) | Hojas de cálculo y Search | Combina el diseño de una página de presentación con visualizaciones de datos interactivas en un pequeño prototipo web. | Demo |
| [Respuestas visuales a búsquedas con varias partes](#case-13) | Hojas de cálculo y Search | Compara la disposición de la respuesta y los enlaces citados al probar una búsqueda matizada con varias restricciones. | Demo |
| [Previsiones financieras interactivas en Sheets](#case-14) | Hojas de cálculo y Search | Crea un prototipo de modelo financiero con supuestos visibles e inspecciona las fórmulas y gráficos generados. | Demo |
| [Un comedor interactivo](#case-15) | 3D interactivo e interfaces | Comprueba las interacciones de objetos, la iluminación y los cambios de estado en lugar de juzgar una escena por una imagen fija. | Demo |
| [Un control de volumen con un mundo en miniatura](#case-16) | 3D interactivo e interfaces | Usa un control conocido para probar tanto el diseño de interacción como el detalle de la escena animada. | Demo |
| [Una casa japonesa en Three.js](#case-17) | 3D interactivo e interfaces | Separa la generación de código del tiempo de renderizado al evaluar un recorrido 3D detallado. | Demo |
| [Un pelícano en bicicleta en 3D](#case-18) | 3D interactivo e interfaces | Usa un personaje en movimiento para inspeccionar coordinación, movimiento y coherencia de la escena. | Demo |
| [Un simulador planetario que empieza por el plan](#case-19) | 3D interactivo e interfaces | Da al modelo de programación un plan concreto antes de pedirle que edite una escena compleja. | Demo |
| [Una isla portuaria con Antigravity Swarm](#case-20) | 3D interactivo e interfaces | Usa un pequeño entorno navegable para inspeccionar cómo varios agentes construyen escenas. | Demo |
| [Una isla flotante con la torre Eiffel](#case-21) | 3D interactivo e interfaces | Evalúa composición, movimiento de cámara y código generado en una escena compacta de un monumento. | Demo |
| [Una ciudad futurista que se puede sobrevolar](#case-22) | 3D interactivo e interfaces | Prueba modificaciones posteriores en un mundo procedural en lugar de asumir que el primer resultado es definitivo. | Demo |
| [Un hidroavión del amanecer a la noche](#case-23) | 3D interactivo e interfaces | Inspecciona controles ambientales y transiciones de iluminación en una escena 3D interactiva. | Demo |
| [Animación de figuras de neón: Hydrogen y Opus](#case-24) | Comparaciones y limitaciones | Compara la animación terminada junto con el tiempo y coste declarados sin asumir entornos idénticos. | Evaluation |
| [Tareas robóticas y errores reconocidos](#case-25) | Comparaciones y limitaciones | Incluye la finalización de tareas y el reconocimiento de pequeños errores en una evaluación de robótica. | Evaluation |
| [Una célula de trabajo de laboratorio en lenguaje natural](#case-26) | Comparaciones y limitaciones | Evalúa la ejecución de herramientas y la gestión de fallos por separado de las puntuaciones principales de las pruebas. | Evaluation |
| [Iceberg y remolcador: Hydrogen y Carbon](#case-27) | Comparaciones y limitaciones | Registra el nivel de razonamiento y las restricciones del entorno al comparar un desarrollo 3D largo. | Evaluation |
| [Un estanque de koi gelatinoso: Hydrogen y Sonnet](#case-28) | Comparaciones y limitaciones | Inspecciona una escena concreta antes de convertir una clasificación de pruebas en una elección de modelo. | Evaluation |
| [Una colección de programación creativa con instrucciones compartidas](#case-29) | Comparaciones y limitaciones | Usa tareas visuales variadas para evitar generalizar a partir de un único resultado atractivo. | Evaluation |
| [Vóxeles de Megamind: un contraejemplo de coste y calidad](#case-30) | Comparaciones y limitaciones | Conserva los casos fallidos al evaluar si un modelo es sistemáticamente más barato o visualmente mejor. | Limit |
| [Un león malabarista en las cuatro estaciones](#case-31) | Comparaciones y limitaciones | Comprueba el movimiento solicitado, no solo el acabado visual de la interfaz que lo rodea. | Limit |
| [Pelea de figuras con tres modelos: un resultado más lento y caro](#case-32) | Comparaciones y limitaciones | Conserva contraejemplos al comparar la eficiencia anunciada de un modelo con informes de tareas reales. | Limit |
| [Una escena de bicicleta en una granja: Hydrogen y Flash](#case-33) | Comparaciones y limitaciones | Compara el movimiento y la calidad de la escena junto con el tiempo de finalización declarado por el creador. | Evaluation |
| [Una chica y un gato en bicicletas tándem](#case-34) | Comparaciones y limitaciones | Compara la fidelidad a la instrucción y los detalles adicionales dejando claras las diferencias de entornos de programación. | Evaluation |
| [Cuatro modelos construyen un juego de Mario en Three.js](#case-35) | Comparaciones y limitaciones | Registra las diferencias de razonamiento antes de interpretar una comparación de juegos con la misma instrucción. | Evaluation |
| [Tres modelos Gemini dibujan un mando](#case-36) | Comparaciones y limitaciones | Busca retrocesos y mejoras específicos de la tarea en lugar de asumir una jerarquía de la familia. | Evaluation |
| [Respuestas visuales distintas entre la aplicación y Studio](#case-37) | Comparaciones y limitaciones | Prueba la misma imagen en el producto que vas a utilizar antes de confiar en un resultado visual. | Limit |
| [Una escena de lanzamiento de cohete: Hydrogen y Flash](#case-38) | Comparaciones y limitaciones | Compara la animación real del lanzamiento además de la duración de construcción declarada. | Evaluation |
| [Cuatro tareas de animación SVG](#case-39) | Comparaciones y limitaciones | Usa varios motivos de interacción y animación para inspeccionar la coherencia entre tareas. | Evaluation |
| [Tres modelos animan un caballo en la sabana](#case-40) | Comparaciones y limitaciones | Inspecciona directamente el movimiento y el detalle visual antes de aceptar afirmaciones generales de coste o calidad. | Evaluation |
| [De imágenes del espacio a una escena HTML](#case-41) | 3D interactivo e interfaces | Usa unas pocas referencias para comprobar si la escena conserva un estilo reconocible. | Demo |
| [Un prototipo de Fórmula 1 en Gemini Canvas](#case-42) | 3D interactivo e interfaces | Añade varias posiciones de cámara para inspeccionar un vehículo generado desde distintos ángulos. | Demo |
| [Hydrogen por API y Carbon en Antigravity](#case-43) | Comparaciones y limitaciones | Anota el entorno de cada ejecución al comparar dos resultados visuales obtenidos con la misma instrucción. | Evaluation |
| [Las sombras al comparar Hydrogen y Astra](#case-44) | Comparaciones y limitaciones | Valora los detalles del renderizado junto con el coste y el tiempo de ambas ejecuciones. | Evaluation |
| [Comparación de movimiento 3D procedural](#case-45) | Comparaciones y limitaciones | Anota el tiempo de generación al comparar la continuidad y la composición de las animaciones. | Evaluation |
| [Una ejecución visual de 89 minutos en PokéBench](#case-46) | Comparaciones y limitaciones | Registra los turnos y los fallos de API además del resultado cuando pruebes un agente visual durante mucho tiempo. | Benchmark |
| [Hydrogen y DeepSeek crean la misma escena 3D](#case-47) | Comparaciones y limitaciones | Anota por separado el tiempo y el coste de API al comparar los resultados visuales. | Evaluation |
| [El perfil de un BMW en SVG](#case-48) | 3D interactivo e interfaces | Usa una vista lateral en SVG para revisar las proporciones, la silueta y los detalles del vehículo. | Demo |
| [La isla flotante de un astrónomo](#case-49) | 3D interactivo e interfaces | Da un tema claro a una escena pequeña y comprueba si los objetos y la iluminación lo refuerzan. | Demo |
| [De una imagen a un paisaje 3D explorable](#case-50) | 3D interactivo e interfaces | Comprueba si una escena hecha a partir de una imagen conserva su aspecto y permite recorrerla. | Demo |
| [Diorama en miniatura con bloques 3D](#case-51) | 3D interactivo e interfaces | Pide una miniatura hecha de bloques y comprueba si las formas componen una escena coherente. | Demo |
| [Un cerezo en flor interactivo](#case-52) | 3D interactivo e interfaces | Usa un objeto animado y unos pocos controles para explorar cambios en tiempo real. | Demo |
| [Tiempo y coste por tarea en Agent Arena](#case-53) | Comparaciones y limitaciones | Compara latencia, coste y tokens de salida por tarea con la tasa de éxito global. | Benchmark |
| [Pruebas de documentos visuales y de terminal](#case-54) | Comparaciones y limitaciones | Consulta por separado los resultados con documentos y con la terminal para elegir el nivel de razonamiento. | Benchmark |
| [Hydrogen en Vals Index y Tax Agent](#case-55) | Comparaciones y limitaciones | Consulta los resultados en tareas especializadas junto con la puntuación global. | Benchmark |
| [Hydrogen con ajustes predeterminados en CursorBench](#case-56) | Comparaciones y limitaciones | Toma una puntuación con la configuración de serie como referencia para probar tu propio repositorio. | Benchmark |
| [Cuatro modelos animan un combate de arqueros](#case-57) | Comparaciones y limitaciones | Compara si se entiende con claridad lo que hace cada arquero. | Evaluation |
| [Un prototipo al estilo de Minecraft en quince minutos](#case-58) | Aplicaciones y aprendizaje | Usa un entorno de vóxeles para comprobar cómo encajan sistemas generados como la minería y el inventario. | Demo |
| [Uso de herramientas con Hydrogen en n8n](#case-59) | Agentes y flujos de programación | Encarga a Hydrogen los ciclos de herramientas en n8n y reserva la planificación para un paso aparte. | Integration |
| [Un agente de Box para documentos empresariales complejos](#case-60) | Hojas de cálculo y Search | Mide aciertos, tiempo y tokens con una carga de documentos realista. | Benchmark |
| [Hydrogen en FrontierCode de Devin](#case-61) | Comparaciones y limitaciones | Evalúa si los parches pueden integrarse y anota el entorno de cada agente. | Benchmark |
| [Refracción en una pequeña animación interactiva](#case-62) | 3D interactivo e interfaces | Afina un efecto óptico con previsualizaciones antes de complicar la escena. | Demo |
| [Un río que fluye hacia arriba](#case-63) | 3D interactivo e interfaces | Prueba con un sentido de movimiento inusual y revisa el efecto en una escena pequeña. | Demo |
| [Búsqueda web pese a una instrucción explícita](#case-64) | Comparaciones y limitaciones | Comprueba que el agente no use herramientas cuando la tarea exige responder sin navegar. | Limit |
| [Consumo de cuota al usar Swarm en Antigravity](#case-65) | Comparaciones y limitaciones | Registra los tokens y la cuota consumida al probar una ejecución multiagente. | Evaluation |
| [Uso de herramientas en tareas profesionales](#case-66) | Comparaciones y limitaciones | Examina cómo reúne contexto un agente antes de actuar en una tarea profesional. | Benchmark |
| [Un retrato en 3D con Hydrogen](#case-67) | 3D interactivo e interfaces | Usa un retrato para evaluar si una representación 3D transmite un parecido reconocible. | Demo |
| [Cuatro modelos animan a un mago y un dragón](#case-68) | Comparaciones y limitaciones | Compara la puesta en escena, la claridad de la acción y los efectos en distintas versiones generadas. | Evaluation |
| [Qué cliente autentica en un flujo multiagente](#case-69) | Agentes y flujos de programación | Comprueba qué cliente se autentica realmente cuando un agente delega en otro proveedor. | Limit |
| [Una sesión de Goal Mode en Antigravity](#case-70) | Agentes y flujos de programación | Sigue el plan, los cambios de código y las pruebas durante una sesión larga. | Demo |
| [MazeBench muestra tasas de éxito bajas](#case-71) | Comparaciones y limitaciones | Prueba problemas de laberintos antes de confiar en el razonamiento espacial de un modelo. | Benchmark |
| [Tres modelos Gemini crean escenas de veleros](#case-72) | Comparaciones y limitaciones | Compara el movimiento y los detalles ambientales de una escena temática en Three.js. | Evaluation |
| [Carbon y Hydrogen en Antigravity Orchestrator](#case-73) | Agentes y flujos de programación | Recurre al modelo planificador cuando se atasque el que implementa más rápido. | Integration |
| [Un gráfico y un informe con datos de Workspace](#case-74) | Hojas de cálculo y Search | Comprueba si un segundo intercambio completa el análisis, el gráfico o el informe que falte. | Demo |
| [Leer un dorsal agota el presupuesto de razonamiento](#case-75) | Comparaciones y limitaciones | Fija un límite de razonamiento y una alternativa para leer detalles pequeños en imágenes. | Limit |
| [Comparación de familias de modelos en ClutterBench](#case-76) | Comparaciones y limitaciones | Usa una prueba con entornos saturados de elementos para ver si las fortalezas generales del modelo se mantienen. | Benchmark |
| [De un resumen de noticias a un vídeo narrado](#case-77) | Aplicaciones y aprendizaje | Convierte noticias investigadas en un vídeo breve con narración y comprueba los hechos que menciona. | Demo |
| [Un busto anatómico seccionado al estilo de Minecraft](#case-78) | Comparaciones y limitaciones | Comprueba si un corte generado contiene las estructuras internas solicitadas. | Evaluation |
| [Tres modelos recrean el mismo objeto](#case-79) | Comparaciones y limitaciones | Anota por separado los tokens y la calidad cuando un modelo de menor precio pueda usar más tokens en una prueba. | Evaluation |
| [Consumo de tokens en una prueba de inducción](#case-80) | Comparaciones y limitaciones | Registra los totales facturados de entrada y salida junto con la puntuación de razonamiento en problemas difíciles. | Benchmark |
| [Arte de píxeles en Sheets con varios modos de Gemini](#case-81) | Hojas de cálculo y Search | Usa el mismo dibujo en Google Sheets para comparar distintos modelos y configuraciones. | Evaluation |
| [Impresión de un apartamento a partir de una imagen](#case-82) | 3D interactivo e interfaces | Lleva una prueba de conversión de imagen a 3D hasta la impresión física. | Demo |
| [Tres modelos animan un animal en 3D](#case-83) | Comparaciones y limitaciones | Revisa la anatomía y el movimiento en una tarea común de modelado. | Evaluation |
| [Hydrogen y Qwen en ts-bench](#case-84) | Comparaciones y limitaciones | Revisa los fallos en las llamadas a herramientas junto con los resultados globales. | Benchmark |
| [Simulación de negocio en Vending-Bench](#case-85) | Comparaciones y limitaciones | Compara los ingresos simulados con el coste de operar al agente. | Benchmark |
| [Una escena náutica con el Golden Merry](#case-86) | 3D interactivo e interfaces | Usa un barco de ficción conocido para comprobar la composición de una escena marítima estilizada. | Demo |
| [Hydrogen disponible en OpenClaw](#case-87) | Agentes y flujos de programación | Comprueba cómo se selecciona el modelo en el sistema de agentes que vas a usar. | Integration |
| [Una ballena entre nubes](#case-88) | 3D interactivo e interfaces | Examina por separado la fluidez del movimiento y el diseño de los ojos de un animal animado mediante código. | Demo |
| [Cuatro modelos construyen una isla en miniatura](#case-89) | Comparaciones y limitaciones | Compara las islas junto con el tiempo y el coste del entorno de cada ejecución. | Evaluation |
| [Dibujar en el aire con una cámara web](#case-90) | Aplicaciones y aprendizaje | Traza líneas y observa cómo las sigue la interfaz para evaluar el dibujo con cámara. | Demo |
| [Comparación de roturas de tela mediante código](#case-91) | Comparaciones y limitaciones | Prueba la elasticidad, los desgarros y la interacción con el pelaje en una misma animación. | Evaluation |
| [Una ciudad submarina en Gemini Canvas](#case-92) | 3D interactivo e interfaces | Empieza con una escena 3D pequeña y añade espacios explorables y fauna animada en varios pasos. | Demo |
| [Un portal web en un intento](#case-93) | Aplicaciones y aprendizaje | Evalúa el diseño inicial del portal antes de probar cada recorrido del usuario. | Demo |
| [Verificación de hechos con una fuente inaccesible](#case-94) | Comparaciones y limitaciones | Exige una referencia que puedas consultar antes de actuar según un veredicto. | Limit |
| [Un simulador urbano al estilo Cities: Skylines](#case-95) | Aplicaciones y aprendizaje | Prototipa un constructor de ciudades y comprueba cómo encajan sus controles y simulaciones. | Demo |
| [Hydrogen y Sol dibujan un pelícano en 2D](#case-96) | Comparaciones y limitaciones | Compara el tiempo y el movimiento con una misma tarea de animación sencilla. | Evaluation |
| [Un salón del trono con Blender MCP](#case-97) | Agentes y flujos de programación | Usa Blender MCP para revisar en el editor la composición de una escena generada. | Integration |
| [Cuatro modelos crean un juego de balanceo con telarañas](#case-98) | Comparaciones y limitaciones | Compara el desplazamiento y los controles en juegos sujetos al mismo límite de un archivo. | Evaluation |
| [Un barco pirata en escala de grises con Three.js](#case-99) | 3D interactivo e interfaces | Limita la escena a grises y comprueba si la luz sigue revelando la geometría. | Demo |
| [Cuatro modelos crean un diorama arquitectónico](#case-100) | Comparaciones y limitaciones | Compara los resultados con el mismo encargo arquitectónico y examina la iluminación. | Evaluation |
| [Una lámpara paramétrica en CadXStudio](#case-101) | 3D interactivo e interfaces | Revisa las dimensiones y la posibilidad de editar las piezas de un modelo CAD generado. | Integration |
| [Un sendero de santuario animado en C++](#case-102) | 3D interactivo e interfaces | Usa una escena pequeña en código nativo para comprobar si el modelo puede crear una animación sin herramientas web. | Demo |
| [Tres modelos renderizan una escena de tren](#case-103) | Comparaciones y limitaciones | Usa la misma escena de tren para comparar los tiempos de las configuraciones elegidas. | Evaluation |
| [Un Chinatown lluvioso con razonamiento Extra](#case-104) | Comparaciones y limitaciones | Mide el tiempo y revisa la escena final antes de elegir el nivel de razonamiento de una animación grande. | Evaluation |
| [Un pueblo construido en 30 módulos](#case-105) | 3D interactivo e interfaces | Genera la escena por módulos y revisa el conjunto una vez integrado. | Demo |
| [Tres modelos crean un visualizador de planetas](#case-106) | Comparaciones y limitaciones | Compara una interfaz científica visual con la misma instrucción en distintos modelos. | Evaluation |
| [Cuatro modelos recrean Chrome Dino](#case-107) | Comparaciones y limitaciones | Cronometra las recreaciones de un juego conocido y compara los resultados jugables. | Evaluation |
| [Una oficina de correos en una isla flotante](#case-108) | 3D interactivo e interfaces | Encarga un edificio en miniatura y revisa el papel de los materiales y la iluminación. | Demo |
| [Dos agentes de código construyen barcos distintos](#case-109) | Comparaciones y limitaciones | Compara el primer resultado utilizable y el coste de revisarlo en el entorno elegido. | Evaluation |
| [Agua y peces en un jardín de carpas koi](#case-110) | 3D interactivo e interfaces | Usa peces en movimiento para comprobar si los reflejos y la iluminación del agua son coherentes. | Demo |
| [Cuatro modelos simulan un asedio con trabuquete](#case-111) | Comparaciones y limitaciones | Compara prototipos de física jugables con un reto común y registra sus niveles de razonamiento. | Evaluation |
| [Una escena 3D en directo en la aplicación Gemini](#case-112) | 3D interactivo e interfaces | Prototipa iluminación interactiva y partículas en la interfaz web de Gemini. | Demo |
| [Una hormigonera ensamblada con CAD en el navegador](#case-113) | Agentes y flujos de programación | Inspecciona el árbol de piezas y su encaje antes de usar el conjunto generado en CAD. | Integration |
| [Modelado procedural de un hacha en Blender](#case-114) | Agentes y flujos de programación | Revisa el modelo con una silueta de referencia y varias comprobaciones en la vista 3D. | Integration |
| [Una escena rosa 3D en un solo HTML](#case-115) | 3D interactivo e interfaces | Prueba una escena Three.js sin recursos externos y comprueba que la composición se entienda. | Demo |
| [Memoria persistente en FrontierMemory](#case-116) | Comparaciones y limitaciones | Compara puntuación y coste por ejecución al elegir un modelo para la memoria del agente. | Benchmark |
| [Hydrogen en un agente de voz de LiveKit averiado](#case-117) | Comparaciones y limitaciones | Provoca un fallo controlado de herramientas y comprueba si el agente afirma resultados sin respaldo. | Evaluation |
| [Ember Isle en 28 módulos](#case-118) | Agentes y flujos de programación | Divide una escena grande en módulos y registra el tiempo de cada generación. | Demo |
| [Una simulación del Big Bang hecha con código](#case-119) | 3D interactivo e interfaces | Usa una animación breve para prototipar una explicación visual y comprueba su rigor científico. | Demo |
| [Un helicóptero con vistas de despiece](#case-120) | 3D interactivo e interfaces | Comprueba si un prototipo 3D combina los controles de vuelo con vistas útiles de inspección. | Demo |
| [Hydrogen Express con rayos X y malla de alambre](#case-121) | 3D interactivo e interfaces | Añade varios modos de inspección a un prototipo 3D controlable. | Demo |
| [Una estación de servicio en el cielo](#case-122) | 3D interactivo e interfaces | Da a la escena objetos en movimiento y estados de luz distintos para mostrar su comportamiento. | Demo |
| [Tres modelos Gemini animan a un ciclista](#case-123) | Comparaciones y limitaciones | Compara escenas breves de movimiento con el mismo encargo y registra los tiempos. | Evaluation |
| [Un libro de química convertido en una lección interactiva](#case-124) | Aplicaciones y aprendizaje | Diseña una lección de autoaprendizaje con pistas, narración y texto opcional. | Demo |
| [Un prototipo de canción Vocaloid](#case-125) | Aplicaciones y aprendizaje | Comprueba si una composición de un solo intento cumple el encargo de personaje y estilo. | Demo |
| [Dos modelos construyen un mundo LEGO](#case-126) | Comparaciones y limitaciones | Compara cuánto logra construir cada modelo en el tiempo que emplea. | Evaluation |
| [Reparación de fallos reintroducidos en dos repositorios](#case-127) | Comparaciones y limitaciones | Introduce defectos conocidos para medir qué puede detectar y reparar un agente. | Benchmark |
| [Un muñeco de palitos contra el cursor](#case-128) | Comparaciones y limitaciones | Compara cómo responde cada animación interactiva al puntero. | Evaluation |
| [Un molino de agua en un archivo HTML](#case-129) | 3D interactivo e interfaces | Usa un paisaje pequeño con elementos móviles reconocibles para probar un prototipo 3D rápido. | Demo |
| [Dos modelos renderizan un paisaje montañoso](#case-130) | Comparaciones y limitaciones | Compara por separado la composición, el tiempo de generación y el coste de una animación de paisaje. | Evaluation |
| [Traducción del inglés al persa con un entorno propio](#case-131) | Comparaciones y limitaciones | Evalúa un texto difícil comparándolo con una traducción humana de referencia. | Evaluation |
| [Una escena en Blender con Hydrogen Extra](#case-132) | 3D interactivo e interfaces | Revisa la geometría y los materiales en Blender antes de aumentar el detalle visual. | Demo |
| [Cuatro modelos crean un barco que se hunde](#case-133) | Comparaciones y limitaciones | Mide por separado la fidelidad visual, el tiempo y el coste en la misma escena. | Evaluation |
| [Lectura de una integral densa a partir de una imagen](#case-134) | Aplicaciones y aprendizaje | Comprueba si el modelo detecta límites iguales antes de simplificar una expresión larga. | Evaluation |
| [Comparación a ciegas de cuatro modelos de redacción](#case-135) | Comparaciones y limitaciones | Oculta los nombres de los modelos antes de elegir qué texto usar. | Evaluation |
| [Detección y lectura visual por nivel de razonamiento](#case-136) | Comparaciones y limitaciones | Mide por separado la precisión de detección y lectura, el coste y la latencia en cada nivel. | Benchmark |
| [Cuatro modelos recrean la casa de Up](#case-137) | Comparaciones y limitaciones | Usa la misma referencia y el mismo encargo para comparar las diferencias de construcción 3D. | Evaluation |
| [Una enciclopedia de la célula humana en WebGL2](#case-138) | Aplicaciones y aprendizaje | Usa un corte interactivo para enseñar relaciones espaciales dentro de una célula. | Demo |
| [Dos animaciones de partículas con Hydrogen](#case-139) | 3D interactivo e interfaces | Compara escenas de partículas para revisar forma y movimiento en efectos sencillos. | Demo |
| [Un rival que solo ve el tablero en Parking Bench](#case-140) | Aplicaciones y aprendizaje | Prueba un rival para un puzle que solo reciba una imagen del tablero como estado. | Integration |
| [Una guía en vídeo para Google Docs](#case-141) | Aplicaciones y aprendizaje | Usa capturas y anotaciones numeradas para enseñar un flujo de edición en el móvil. | Demo |
| [Un interruptor de día y noche para un mundo en miniatura](#case-142) | 3D interactivo e interfaces | Usa un interruptor sencillo para comprobar la continuidad de la animación entre estados. | Demo |
| [Un entorno construido en 65 módulos](#case-143) | 3D interactivo e interfaces | Controla el tiempo de construcción y la integración a medida que crece la escena. | Demo |
| [Un baile con cámara fija](#case-144) | Comparaciones y limitaciones | Comprueba si la animación conserva el diseño del personaje, la composición y el encuadre de referencia. | Evaluation |
| [Un agente de código se atasca en la prueba de referencia](#case-145) | Comparaciones y limitaciones | Fija un límite de tiempo para la prueba inicial y comprueba el progreso antes de esperar una corrección. | Limit |
| [Un entorno BASIC para el MZ-1500](#case-146) | Aplicaciones y aprendizaje | Prototipa un entorno BASIC retro y comprueba el soporte de los periféricos. | Demo |
| [Dos modelos crean un brazo robótico interactivo](#case-147) | Comparaciones y limitaciones | Comprueba si las articulaciones del brazo Three.js responden de forma coherente a las acciones del usuario. | Evaluation |
| [Un mapa jugable de una suspensión de vuelos de la FAA](#case-148) | Hojas de cálculo y Search | Combina mapa y cronología para mostrar por qué la cola persiste después de levantar la suspensión. | Demo |
| [Un jardín en miniatura con pagoda](#case-149) | 3D interactivo e interfaces | Comprueba el equilibrio entre la arquitectura y el paisajismo de una miniatura generada. | Demo |
| [Planificación, ejecución y revisión con modelos distintos](#case-150) | Agentes y flujos de programación | Asigna cada papel a un modelo y compara sus costes por tarea. | Demo |
| [Hydrogen y Sol construyen un pueblo nevado](#case-151) | Comparaciones y limitaciones | Mide por separado el tiempo, el coste y la calidad de la escena. | Evaluation |
| [Una isla en Three.js con niveles High y Ultra](#case-152) | Comparaciones y limitaciones | Compara el aspecto y el tiempo con los niveles de razonamiento a la vista, sin equiparar cuotas de productos distintos. | Evaluation |
| [Diorama de un aeródromo de la Segunda Guerra Mundial](#case-153) | 3D interactivo e interfaces | Añade referencias y requisitos de movimiento para evaluar algo más que el aspecto de la escena. | Demo |
| [Configurar Hydrogen en un cliente de código](#case-154) | Agentes y flujos de programación | Usa el identificador exacto del modelo al configurar la clave de Google en un cliente compatible. | Tutorial |
| [Un equipo de investigación SuperARIS con Hydrogen](#case-155) | Agentes y flujos de programación | Asigna tareas concretas de investigación y redacción a Hydrogen dentro de un equipo con varios modelos. | Integration |
| [Cuatro modelos reescriben un módulo desde cero](#case-156) | Agentes y flujos de programación | Compara comprensión del código, diseño e implementación al elegir un agente para una reescritura. | Evaluation |
| [Comparación de detalles de un mando PS5 en 3D](#case-157) | Comparaciones y limitaciones | Inspecciona el sombreado de los botones y los elementos traseros al comparar los mandos. | Evaluation |
| [Muse delega tareas a Antigravity CLI](#case-158) | Agentes y flujos de programación | Conecta un asistente remoto a un entorno de programación local y selecciona un modelo de escritura predeterminado. | Integration |
| [CursorBench con distintos presupuestos de razonamiento](#case-159) | Comparaciones y limitaciones | Compara las tasas de éxito por nivel antes de elegir una configuración rápida. | Benchmark |
| [Tres modelos renderizan un templo estelar](#case-160) | Comparaciones y limitaciones | Evalúa la estabilidad del renderizado por separado del detalle visual. | Evaluation |
| [Un juego de disparos en HTML en un minuto](#case-161) | Aplicaciones y aprendizaje | Usa un HTML para probar los controles y la respuesta básica de un juego de disparos. | Demo |
| [Revisión de un plan de migración existente](#case-162) | Comparaciones y limitaciones | Pide a los agentes que evalúen si la migración exige sustituir la arquitectura actual. | Limit |
| [Conversaciones con Hydrogen en AITuber OnAir](#case-163) | Aplicaciones y aprendizaje | Prueba a Hydrogen como modelo de conversación para un avatar Live2D. | Integration |
| [Un vídeo promocional hecho con código](#case-164) | Aplicaciones y aprendizaje | Da un encargo promocional breve y revisa los gráficos en movimiento que produce el modelo. | Demo |
| [Dos modelos interpretan un juego de fuga de un templo](#case-165) | Comparaciones y limitaciones | Compara si la iluminación y el ambiente permiten leer bien el mismo concepto de juego. | Evaluation |
| [Tres modelos Gemini animan un buggy de rally](#case-166) | Comparaciones y limitaciones | Comprueba si la suspensión y el agarre de las ruedas son coherentes al tomar una curva peraltada. | Evaluation |
| [Un petirrojo animado de forma procedural](#case-167) | 3D interactivo e interfaces | Revisa el movimiento de las alas y el cuerpo en una animación de vuelo generada. | Demo |
| [Cuándo usar Orchestrator o Swarm en Antigravity](#case-168) | Agentes y flujos de programación | Usa transferencias entre modelos para tareas secuenciales y trabajadores autónomos con revisores para tareas paralelas. | Tutorial |
| [Dos modelos animan Chasing Views](#case-169) | Comparaciones y limitaciones | Compara el resultado y el tiempo teniendo en cuenta el nivel de razonamiento de cada modelo. | Evaluation |
| [Velocidad y coste en Design Creativity Bench](#case-170) | Comparaciones y limitaciones | Compara el tiempo y el coste por diseño junto con la puntuación de creatividad. | Benchmark |
| [De una imagen de referencia a CAD en SolidWorks](#case-171) | Agentes y flujos de programación | Evalúa el flujo de modelado de un agente de SolidWorks a partir de una imagen 3D. | Integration |
| [Cuatro modelos animan un galope en el desierto](#case-172) | Comparaciones y limitaciones | Compara el apoyo de los cascos y los cambios de peso antes de juzgar la luz o la malla. | Evaluation |
| [Diapositivas sobre la sincronicidad de Jung](#case-173) | Aplicaciones y aprendizaje | Prueba la generación de diapositivas con un tema donde importe explicar bien conceptos relacionados. | Demo |
| [Investigación informática en FrontierCS 2](#case-174) | Comparaciones y limitaciones | Usa una prueba de investigación junto a las pruebas de programación y anota el entorno. | Benchmark |
| [Cuatro modelos en Rio Above the Clouds](#case-175) | Comparaciones y limitaciones | Compara coste, tiempo y calidad percibida con un encargo creativo común. | Evaluation |
| [Hydrogen en las tareas técnicas de GBENCH](#case-176) | Comparaciones y limitaciones | Usa resultados verificables de código y de otras tareas para valorar el rendimiento junto al precio y el tiempo. | Benchmark |
| [Entrenar coches para aparcar en paralelo](#case-177) | Comparaciones y limitaciones | Compara el progreso del aprendizaje y la tasa final de éxito en simulaciones generadas. | Evaluation |
| [Un motor mitocondrial interactivo](#case-178) | Aplicaciones y aprendizaje | Conecta el movimiento molecular con la producción de ATP mediante un diagrama interactivo. | Demo |
| [Un juego territorial al estilo de Qix](#case-179) | Aplicaciones y aprendizaje | Usa un encargo de arcade sencillo para comprobar si el primer resultado ya permite jugar. | Demo |
| [Diapositivas HTML generadas con Hydrogen](#case-180) | Aplicaciones y aprendizaje | Revisa la jerarquía y la composición al probar la velocidad de generación de HTML. | Demo |
| [Hydrogen en Terminal-Bench 4.0](#case-181) | Comparaciones y limitaciones | Considera tanto las tareas completadas como su coste al elegir un modelo para la terminal. | Benchmark |
| [Una ilustración en un solo archivo HTML](#case-182) | 3D interactivo e interfaces | Comprueba si una referencia visual puede recrearse con código y sin recursos externos. | Demo |
| [Tres modelos Gemini animan un pulpo](#case-183) | Comparaciones y limitaciones | Observa si el contacto con la roca impulsa visiblemente el cuerpo cuando el pulpo se agarra. | Evaluation |
| [Un resumen estructurado de YouTube en Chrome](#case-184) | Hojas de cálculo y Search | Pide al panel de Gemini un resumen con marcas de tiempo y referencias claras al contexto adicional. | Tutorial |
| [Una lección convertida en vídeo breve](#case-185) | Aplicaciones y aprendizaje | Comprueba el rigor de la explicación y el ritmo al convertir una lección en vídeo. | Demo |
| [Animar un frailecillo desde una escena fija](#case-186) | 3D interactivo e interfaces | Usa una escena HTML existente como primer fotograma de una animación procedural. | Demo |
| [Una prueba de modelado de castillos](#case-187) | Comparaciones y limitaciones | Compara los castillos y los recursos consumidos en distintas ejecuciones. | Evaluation |
| [Uso del navegador en un Swarm de Antigravity](#case-188) | Agentes y flujos de programación | Revisa la actividad del navegador junto con las tareas del equipo multiagente. | Demo |
| [Transferir una investigación a Muse mediante Drive](#case-189) | Agentes y flujos de programación | Usa una carpeta vigilada de Drive cuando otro agente deba asumir el paso siguiente. | Integration |
| [Una guía de flauta dulce en Gemini Canvas](#case-190) | Aplicaciones y aprendizaje | Prueba el modo rápido para combinar partitura e indicaciones de práctica instrumental. | Demo |
| [La estimación de un proyecto cambia al ampliar el alcance](#case-191) | Comparaciones y limitaciones | Pide que se expliquen el alcance y los supuestos cuando cambie mucho el plazo previsto. | Limit |
| [Un Swarm de Antigravity anima un pelícano](#case-192) | Agentes y flujos de programación | Asigna la animación y el sonido al equipo y revisa el montaje final. | Demo |
| [Una pregunta de calendario que incluye los años bisiestos](#case-193) | Comparaciones y limitaciones | Usa una conversión sencilla para comprobar si la respuesta contempla casos especiales del calendario. | Evaluation |
| [TAJ VICE en un solo archivo HTML](#case-194) | Aplicaciones y aprendizaje | Prototipa un mapa explorable dentro de un archivo y prueba los fallos pendientes. | Demo |
| [Antigravity con un proyecto de Google Cloud](#case-195) | Agentes y flujos de programación | Comprueba la autenticación y la facturación del proyecto al activar Hydrogen con credenciales gestionadas. | Tutorial |
| [Límites de suscripción obsoletos en una respuesta](#case-196) | Comparaciones y limitaciones | Verifica los términos vigentes y el nombre del modelo en fuentes primarias al evaluar un asistente de investigación. | Limit |
| [Replantear la historia de una animación WebGL](#case-197) | Comparaciones y limitaciones | Pide una narrativa más clara cuando una primera versión elaborada no tenga progresión. | Limit |
| [Carbon planifica y Hydrogen implementa una aplicación móvil](#case-198) | Agentes y flujos de programación | Separa el diseño de interacciones de su implementación entre dos modelos. | Demo |
| [Dos modelos programan un combate de dragones](#case-199) | Comparaciones y limitaciones | Compara cómo la animación de cada modelo coordina dos personajes que interactúan. | Evaluation |
| [Una isla 3D en miniatura con una sola instrucción](#case-200) | 3D interactivo e interfaces | Comprueba si la escena sitúa de manera clara los edificios, el relieve y el agua. | Demo |
| [Una instrucción reproducible para animar un pelícano en Three.js](#case-201) | Comparaciones y limitaciones | Comprueba si las patas, las ruedas y la dirección se mueven coordinadamente. | Evaluation |
| [Hydrogen en T3 Code](#case-202) | Agentes y flujos de programación | Prueba un cliente de programación y sigue las cuotas móviles y semanales durante una sesión realista. | Integration |
| [Un vídeo de interés público con estética de dibujo a mano](#case-203) | Aplicaciones y aprendizaje | Usa un mensaje breve de interés público para evaluar un tratamiento visual dibujado. | Demo |
| [Un pavo real ciclista en diez estilos gráficos](#case-204) | Agentes y flujos de programación | Usa un equipo de varios modelos para programar las transiciones visuales y sincronizar el sonido. | Demo |
| [Una instrucción sobre una casa rural en tres plataformas](#case-205) | Comparaciones y limitaciones | Comprueba el formato de salida al mover una tarea visual entre configuraciones y plataformas. | Evaluation |
| [Dos paneles con la misma instrucción](#case-206) | Comparaciones y limitaciones | Compara la disposición y jerarquía informativa a partir del mismo encargo de interfaz. | Evaluation |
| [Recrear React.gg a partir de una imagen](#case-207) | Aplicaciones y aprendizaje | Parte de una imagen y comprueba qué detalles todavía necesitan cambios. | Demo |
| [Un panel interactivo sobre la singularidad](#case-208) | 3D interactivo e interfaces | Prototipa una secuencia interactiva breve a partir de una sola idea visual. | Demo |
| [Dos modelos animan una escena de desplazamiento lateral](#case-209) | Comparaciones y limitaciones | Compara la continuidad del movimiento y el coste de creación de una escena de acción. | Evaluation |
| [Gemini como entrenador de carrera](#case-210) | Aplicaciones y aprendizaje | Compara el registro de entrenamiento con las sugerencias y ajusta las metas a tu punto de partida. | Demo |
| [Un juego de navegador con puntos en cadena](#case-211) | Aplicaciones y aprendizaje | Prueba el juego en un navegador de escritorio y verifica por separado cómo registra los puntos. | Demo |
| [Fórmulas sin renderizar en una respuesta en japonés](#case-212) | Comparaciones y limitaciones | Comprueba la presentación y la exactitud cuando la respuesta contenga comandos TeX. | Limit |
| [Una aplicación de composición de instrucciones a MIDI](#case-213) | Aplicaciones y aprendizaje | Prototipa una herramienta que convierta un encargo en japonés en MIDI, WAV y una vista de piano roll. | Demo |
| [Prueba de una instrucción de guardar silencio](#case-214) | Comparaciones y limitaciones | Comprueba si el modelo puede abstenerse de responder cuando el flujo lo exija. | Evaluation |
| [Resumen de un concierto en una página](#case-215) | Aplicaciones y aprendizaje | Convierte los datos de un evento en un resumen visual que se pueda recorrer de un vistazo. | Demo |
| [Tres modelos explican un motor eléctrico](#case-216) | Comparaciones y limitaciones | Compara la claridad visual y los controles didácticos con un mismo encargo de simulación. | Evaluation |
| [Dos flujos animan una escena de escritorio](#case-217) | Comparaciones y limitaciones | Comprueba los detalles, el volumen y la pausa final frente al encargo original. | Evaluation |
| [Un montaje de escenas cotidianas a partir de un avatar](#case-218) | Aplicaciones y aprendizaje | Usa un avatar y cuatro escenas diarias para evaluar si el modelo adapta una secuencia breve. | Demo |
| [Hydrogen planifica un vídeo de personaje para ComfyUI](#case-219) | Aplicaciones y aprendizaje | Mantén el vestuario y el fondo mientras cambian expresiones y acciones en la instrucción. | Integration |
| [Ampliar Almance Vale hasta 100 módulos](#case-220) | Agentes y flujos de programación | Lleva una aplicación a un agente de programación y pídele nuevos módulos con el mismo estilo. | Demo |
| [Un pueblo 2D con sonido procedural](#case-221) | Comparaciones y limitaciones | Comprueba si el sonido cambia con lo que ocurre en pantalla y anota el tiempo de creación. | Evaluation |
| [Un tratamiento panorámico para una canción](#case-222) | Aplicaciones y aprendizaje | Entrega una canción y un formato para explorar si el movimiento transmite su energía. | Demo |
| [Las cataratas del Niágara con siete subagentes Hydrogen](#case-223) | Agentes y flujos de programación | Divide la escena para que un coordinador reparta los componentes entre agentes de implementación. | Demo |
| [Continuidad entre dos escenas románticas de época](#case-224) | Aplicaciones y aprendizaje | Especifica qué detalles deben permanecer al continuar una escena en otro vídeo. | Demo |
| [Una esfera de agua en la aplicación Gemini](#case-225) | 3D interactivo e interfaces | Usa una escena óptica sencilla para observar reflejos y refracción. | Demo |

<a id="agents"></a>
## ⚡ Agentes y flujos de programación

<a id="case-1"></a>
### Caso 1: [Mantenimiento de código en Antigravity](https://x.com/antigravity/status/2120944334023389476) (por [@antigravity](https://x.com/antigravity))

**Usa una tarea de mantenimiento acotada para evaluar conjuntamente modificaciones, uso de herramientas y verificación.**

La demostración de lanzamiento de Antigravity muestra a Hydrogen manteniendo una base de código. Es un ejemplo producido por la plataforma, no una prueba de ingeniería reproducida de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-2"></a>
### Caso 2: [Dieciséis aplicaciones canvas en paralelo](https://x.com/shengzheyao/status/2120944141559550409) (por [@shengzheyao](https://x.com/shengzheyao))

**Divide el desarrollo en módulos independientes y define explícitamente las funciones de planificación, implementación y control de calidad.**

Un creador de Antigravity CLI en Google DeepMind describe cómo Carbon coordina, verifica e integra mientras Hydrogen construye 16 miniaplicaciones canvas sin dependencias. El flujo combina modelos, por lo que su resultado no debe atribuirse únicamente a Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-3"></a>
### Caso 3: [Polilla carmesí con un enjambre de varios modelos](https://x.com/thtbee_/status/2120958666480513310) (por [@thtbee_](https://x.com/thtbee_))

**Separa la orquestación de la implementación en un proyecto interactivo de programación creativa.**

El creador afirma que Carbon orquestó un enjambre de Antigravity mientras trabajadores Hydrogen construían la obra de la polilla carmesí. Los 45 minutos declarados incluyen ese flujo multimodelo y no se cronometraron de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-4"></a>
### Caso 4: [Inspección y reparación con 3D Medic](https://x.com/GoogleAI/status/2120940683233984862) (por [@GoogleAI](https://x.com/GoogleAI))

**Explora un agente que inspecciona un archivo 3D, detecta errores y propone reparaciones antes de exportarlo.**

La demostración 3D Medic de Google AI utiliza una aplicación Managed Agent creada en AI Studio. Muestra un flujo de reparación de archivos, no pruebas de que cualquier recurso 3D vaya a repararse correctamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-5"></a>
### Caso 5: [Una escena de velero creada en Devin](https://x.com/Da7_Tech/status/2120967690722677144) (por [@Da7_Tech](https://x.com/Da7_Tech))

**Evalúa un modelo en el entorno de agente de programación que realmente piensas utilizar.**

La fuente presenta una escena de velero atribuida a Hydrogen ejecutado en Devin. La breve publicación no revela la instrucción completa, el historial de iteraciones ni una configuración reproducible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-59"></a>
### Caso 59: [Uso de herramientas con Hydrogen en n8n](https://x.com/n8n_io/status/2120947273534197886) (por [@n8n_io](https://x.com/n8n_io))

**Encarga a Hydrogen los ciclos de herramientas en n8n y reserva la planificación para un paso aparte.**

n8n documenta la compatibilidad con Hydrogen y recomienda planificar con Carbon o Argon y ejecutar con Hydrogen. La publicación enlaza la configuración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-12

---

<a id="case-69"></a>
### Caso 69: [Qué cliente autentica en un flujo multiagente](https://x.com/studio_yebisu/status/2120969033260646551) (por [@studio_yebisu](https://x.com/studio_yebisu))

**Comprueba qué cliente se autentica realmente cuando un agente delega en otro proveedor.**

El autor pidió a Claude usar Hydrogen mediante Antigravity CLI. Afirma que Claude Code intentó autenticarse directamente y que su acceso a Antigravity se suspendió. La captura muestra el aviso y el autor lo atribuye a esa ruta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-70"></a>
### Caso 70: [Una sesión de Goal Mode en Antigravity](https://x.com/Inmerson/status/2120973427788124345) (por [@Inmerson](https://x.com/Inmerson))

**Sigue el plan, los cambios de código y las pruebas durante una sesión larga.**

El autor afirma que usó Hydrogen Extra en Goal Mode durante 105 minutos para planificar, implementar y probar. Los resultados de pruebas son los que declara.

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

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-73"></a>
### Caso 73: [Carbon y Hydrogen en Antigravity Orchestrator](https://x.com/Google/status/2120982566891356279) (por [@Google](https://x.com/Google))

**Recurre al modelo planificador cuando se atasque el que implementa más rápido.**

Google describe a Carbon planificando y resolviendo bloqueos mientras Hydrogen edita y prueba. Informa de resultados cercanos a Carbon en Terminal-Bench 4.0, con menor consumo de cuota y menor duración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

Tipo: Integration | Fecha: 2026-11-12

---

<a id="case-87"></a>
### Caso 87: [Hydrogen disponible en OpenClaw](https://x.com/openclaw/status/2121098531205501401) (por [@openclaw](https://x.com/openclaw))

**Comprueba cómo se selecciona el modelo en el sistema de agentes que vas a usar.**

OpenClaw anunció la compatibilidad con Hydrogen e incluyó una captura. La publicación no contiene pruebas de rendimiento ni un registro de la configuración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-97"></a>
### Caso 97: [Un salón del trono con Blender MCP](https://x.com/ashen_one/status/2121165467821936651) (por [@ashen_one](https://x.com/ashen_one))

**Usa Blender MCP para revisar en el editor la composición de una escena generada.**

El autor atribuye a Hydrogen la recreación del salón del Trono de Hierro de Juego de Tronos con Blender MCP y comparte un vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-113"></a>
### Caso 113: [Una hormigonera ensamblada con CAD en el navegador](https://x.com/johnsanthosh01/status/2121243197901041869) (por [@johnsanthosh01](https://x.com/johnsanthosh01))

**Inspecciona el árbol de piezas y su encaje antes de usar el conjunto generado en CAD.**

El autor afirma que Hydrogen creó una hormigonera de 265 piezas en CadX Studio en 40 minutos con una instrucción y sin modelar las piezas manualmente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-114"></a>
### Caso 114: [Modelado procedural de un hacha en Blender](https://x.com/camperaigg/status/2121252572115951897) (por [@camperaigg](https://x.com/camperaigg))

**Revisa el modelo con una silueta de referencia y varias comprobaciones en la vista 3D.**

El autor usó Hydrogen en Antigravity CLI para crear un hacha estilizada en Blender con módulos Python y revisiones en la vista 3D. Informa de 51 minutos, incluida la captura, y USD 5,01 de API.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-118"></a>
### Caso 118: [Ember Isle en 28 módulos](https://x.com/IamEmily2050/status/2121258646759952644) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Divide una escena grande en módulos y registra el tiempo de cada generación.**

El autor usó Hydrogen High en la aplicación Gemini para Ember Isle. Indica 28 módulos, una instrucción por módulo y entre 82 y 290 segundos por instrucción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-150"></a>
### Caso 150: [Planificación, ejecución y revisión con modelos distintos](https://x.com/naufaldi/status/2121499487999013081) (por [@naufaldi](https://x.com/naufaldi))

**Asigna cada papel a un modelo y compara sus costes por tarea.**

El autor usa Opus 5.5 para planificar, Hydrogen para ejecutar con Sol de respaldo y Sol 6.1 para revisar. Combina su propio uso en Antigravity con comparaciones públicas de otras pruebas.

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

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-154"></a>
### Caso 154: [Configurar Hydrogen en un cliente de código](https://x.com/k2sbhai/status/2121509825658147041) (por [@k2sbhai](https://x.com/k2sbhai))

**Usa el identificador exacto del modelo al configurar la clave de Google en un cliente compatible.**

El autor explica cómo obtener una clave de Google AI Studio y seleccionar gemini-4-hydrogen en OpenCode o Cline. El acceso y los límites dependen del proveedor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

Tipo: Tutorial | Fecha: 2026-11-14

---

<a id="case-155"></a>
### Caso 155: [Un equipo de investigación SuperARIS con Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Asigna tareas concretas de investigación y redacción a Hydrogen dentro de un equipo con varios modelos.**

La publicación explica cómo instalar SuperARIS y configurar un equipo. Propone Hydrogen o Carbon para debatir y redactar, con otros roles para coordinar e implementar. No mide la calidad de la investigación.

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

Tipo: Integration | Fecha: 2026-11-14

---

<a id="case-156"></a>
### Caso 156: [Cuatro modelos reescriben un módulo desde cero](https://x.com/oasisfeng/status/2121523934831276203) (por [@oasisfeng](https://x.com/oasisfeng))

**Compara comprensión del código, diseño e implementación al elegir un agente para una reescritura.**

El autor compara el trabajo de Hydrogen, Argon, GPT-6 Astra y Claude Opus 5.5 en un módulo central. Destaca la ejecución de Hydrogen y distingue capacidades de diseño en las otras pruebas.

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

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-158"></a>
### Caso 158: [Muse delega tareas a Antigravity CLI](https://x.com/tetumemo/status/2121528823061852166) (por [@tetumemo](https://x.com/tetumemo))

**Conecta un asistente remoto a un entorno de programación local y selecciona un modelo de escritura predeterminado.**

El autor describe cómo Muse encarga tareas a Antigravity CLI en un ordenador doméstico y recibe los resultados. Usa Hydrogen por defecto y también dispone de Argon. Los ejemplos incluyen texto japonés y material visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-14

---

<a id="case-168"></a>
### Caso 168: [Cuándo usar Orchestrator o Swarm en Antigravity](https://x.com/ohayou792/status/2121624258984153452) (por [@ohayou792](https://x.com/ohayou792))

**Usa transferencias entre modelos para tareas secuenciales y trabajadores autónomos con revisores para tareas paralelas.**

El autor representa Orchestrator con un modelo de alto rendimiento que planifica y Hydrogen que implementa. Lo compara con /swarm y propone elegir según las dependencias entre tareas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

Tipo: Tutorial | Fecha: 2026-11-14

---

<a id="case-171"></a>
### Caso 171: [De una imagen de referencia a CAD en SolidWorks](https://x.com/GoGoFly23/status/2121636952479080713) (por [@GoGoFly23](https://x.com/GoGoFly23))

**Evalúa el flujo de modelado de un agente de SolidWorks a partir de una imagen 3D.**

El autor dice que entregó una imagen a Hydrogen en Antigravity y muestra la pieza resultante. Después identifica la integración SolidWorks MCP. No se comprobaron tolerancias ni idoneidad para ingeniería.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-14

---

<a id="case-188"></a>
### Caso 188: [Uso del navegador en un Swarm de Antigravity](https://x.com/Saboo_Shubham_/status/2121852445756477924) (por [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**Revisa la actividad del navegador junto con las tareas del equipo multiagente.**

Una persona de Google comparte una captura de uso del navegador con Hydrogen y un Swarm de Antigravity. La publicación no incluye un registro completo de tareas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-189"></a>
### Caso 189: [Transferir una investigación a Muse mediante Drive](https://x.com/nasuvit_z/status/2121857992702525734) (por [@nasuvit_z](https://x.com/nasuvit_z))

**Usa una carpeta vigilada de Drive cuando otro agente deba asumir el paso siguiente.**

El autor usa Hydrogen para reunir y ordenar información en un archivo de Drive y hace que Muse continúe cuando aparece el archivo. El diagrama documenta el traspaso.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-15

---

<a id="case-192"></a>
### Caso 192: [Un Swarm de Antigravity anima un pelícano](https://x.com/chetaslua/status/2121885449509851415) (por [@chetaslua](https://x.com/chetaslua))

**Asigna la animación y el sonido al equipo y revisa el montaje final.**

El autor atribuye a Carbon y Hydrogen una escena en JavaScript donde el pelícano cambia de estilo artístico. Dice que la música y el sonido se crean con código.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-195"></a>
### Caso 195: [Antigravity con un proyecto de Google Cloud](https://x.com/loganlu51268/status/2121911409042719023) (por [@loganlu51268](https://x.com/loganlu51268))

**Comprueba la autenticación y la facturación del proyecto al activar Hydrogen con credenciales gestionadas.**

El autor describe el paso de un plan personal a un proyecto Google Cloud Agent Platform con credenciales predeterminadas de aplicación. Incluye Hydrogen en el selector y explica la revisión de cargos por SKU.

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

Tipo: Tutorial | Fecha: 2026-11-15

---

<a id="case-198"></a>
### Caso 198: [Carbon planifica y Hydrogen implementa una aplicación móvil](https://x.com/thebuggeddev/status/2121945961555718334) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Separa el diseño de interacciones de su implementación entre dos modelos.**

El autor atribuye la planificación a Carbon y la implementación a Hydrogen, incluida la física con Reanimated. Describe un movimiento fluido y comparte un vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-202"></a>
### Caso 202: [Hydrogen en T3 Code](https://x.com/bei351009016/status/2121964293906206916) (por [@bei351009016](https://x.com/bei351009016))

**Prueba un cliente de programación y sigue las cuotas móviles y semanales durante una sesión realista.**

El autor dice que usó Hydrogen con Gemini Pro en T3 Code durante aproximadamente medio día. Las capturas y el texto documentan las cuotas y distinguen velocidad percibida de precisión.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

Tipo: Integration | Fecha: 2026-11-15

---

<a id="case-204"></a>
### Caso 204: [Un pavo real ciclista en diez estilos gráficos](https://x.com/SahilPanhotra/status/2121995488425849064) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Usa un equipo de varios modelos para programar las transiciones visuales y sincronizar el sonido.**

El autor atribuye a un equipo de Carbon y Hydrogen un pavo real que pedalea a través de diez estilos. Dice que programó la imagen, la música y los efectos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-220"></a>
### Caso 220: [Ampliar Almance Vale hasta 100 módulos](https://x.com/IamEmily2050/status/2122257581175410858) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Lleva una aplicación a un agente de programación y pídele nuevos módulos con el mismo estilo.**

El autor movió Almance Vale de la aplicación Gemini a Antigravity. Indica que Hydrogen Extra en modo Swarm mantuvo las convenciones del código y amplió la escena a 100 módulos en unas horas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

Tipo: Demo | Fecha: 2026-11-16

---

<a id="case-223"></a>
### Caso 223: [Las cataratas del Niágara con siete subagentes Hydrogen](https://x.com/SahilPanhotra/status/2122311637684424737) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Divide la escena para que un coordinador reparta los componentes entre agentes de implementación.**

El autor atribuye a Carbon y siete subagentes Hydrogen una recreación en menos de una hora a partir de una instrucción. El vídeo muestra agua, barcos, perspectivas y entornos que cambian.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

Tipo: Demo | Fecha: 2026-11-16

---


<a id="apps-learning"></a>
## 💻 Aplicaciones y aprendizaje

<a id="case-6"></a>
### Caso 6: [Práctica de idiomas en Lingo City](https://x.com/tulseedoshi/status/2121095754844713427) (por [@tulseedoshi](https://x.com/tulseedoshi))

**Combina tarjetas didácticas con una escena callejera interactiva para practicar idiomas en contexto.**

Tulsee Doshi comparte un ejemplo de Google que transmite tarjetas personalizadas en 2D y 3D y permite practicar conversaciones con comerciantes en una ciudad virtual. Es una demostración del proveedor, no un estudio independiente de resultados de aprendizaje.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-7"></a>
### Caso 7: [Romeo y Julieta como teatro de papel en 3D](https://x.com/techartist_/status/2120957446202253803) (por [@techartist_](https://x.com/techartist_))

**Convierte una lección concreta en una escena interactiva con un objetivo de aprendizaje claro.**

El creador construyó una lección de teatro de papel en 3D sobre la escena del balcón de Romeo y Julieta para Literatura Inglesa de GCSE. La fuente demuestra la interfaz, pero no mide resultados de aprendizaje.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-8"></a>
### Caso 8: [De una imagen de diseño a una web de lectura](https://x.com/thebuggeddev/status/2120952661046689992) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Usa un diseño de referencia para evaluar la comprensión visual y una implementación funcional de la interfaz.**

El creador afirma que Hydrogen convirtió una imagen de diseño en una web funcional de gestión de lecturas en 5 minutos y 27 segundos. La duración y la integridad son afirmaciones de la fuente; esta colección no incluye una prueba funcional independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-9"></a>
### Caso 9: [Un jardín de carpas koi construido en veinte módulos](https://x.com/IamEmily2050/status/2120951069874532806) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Construye una escena más grande con módulos pequeños en lugar de esperar un resultado completo de una sola instrucción.**

El creador informa de 20 instrucciones para 20 módulos en la aplicación Gemini, cada uno de 90–270 segundos. El autor declaró acceso anticipado y el ejemplo es explícitamente iterativo, no un resultado de un solo intento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-10"></a>
### Caso 10: [Un juego educativo sobre fusión de protones](https://x.com/SidraMiconi/status/2120948703095820743) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Crea un prototipo de explicación interactiva de un proceso científico y comprueba después su base científica.**

El juego del creador recorre la cadena protón–protón dentro de una estrella joven. La única instrucción, los 78 segundos de ejecución y el coste aproximado de $0.19 son afirmaciones de la fuente, no resultados reproducidos de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-58"></a>
### Caso 58: [Un prototipo al estilo de Minecraft en quince minutos](https://x.com/RezAIT00/status/2120947124418293876) (por [@RezAIT00](https://x.com/RezAIT00))

**Usa un entorno de vóxeles para comprobar cómo encajan sistemas generados como la minería y el inventario.**

El autor afirma haber construido el prototipo con Hydrogen Extra High en 15 minutos. Menciona la colocación de objetos, la minería y el inventario, aunque el vídeo no muestra todo su funcionamiento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-77"></a>
### Caso 77: [De un resumen de noticias a un vídeo narrado](https://x.com/gigabit_million/status/2121011957042163722) (por [@gigabit_million](https://x.com/gigabit_million))

**Convierte noticias investigadas en un vídeo breve con narración y comprueba los hechos que menciona.**

El autor graba a Hydrogen en la aplicación móvil Gemini buscando noticias y redactando un esquema antes de pedir el vídeo. Se ven diez segundos de reproducción. El tiempo de generación y la narración son datos del autor, y no se identifica el motor de renderizado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-90"></a>
### Caso 90: [Dibujar en el aire con una cámara web](https://x.com/CodeByPoonam/status/2121121804483969102) (por [@CodeByPoonam](https://x.com/CodeByPoonam))

**Traza líneas y observa cómo las sigue la interfaz para evaluar el dibujo con cámara.**

El autor afirma haber usado el acceso temprano a Hydrogen para crear una herramienta de dibujo en el aire y comparte un vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-93"></a>
### Caso 93: [Un portal web en un intento](https://x.com/kimura_0314/status/2121130305532878979) (por [@kimura_0314](https://x.com/kimura_0314))

**Evalúa el diseño inicial del portal antes de probar cada recorrido del usuario.**

El autor muestra una captura de un portal creado con Hydrogen en Antigravity y dice que lo generó una vez. La captura no demuestra que funcionen las interacciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-95"></a>
### Caso 95: [Un simulador urbano al estilo Cities: Skylines](https://x.com/yohakujpn/status/2121146464466604147) (por [@yohakujpn](https://x.com/yohakujpn))

**Prototipa un constructor de ciudades y comprueba cómo encajan sus controles y simulaciones.**

El autor atribuye a Hydrogen un prototipo al estilo Cities: Skylines y dice que tardó menos de 30 minutos. El vídeo muestra el resultado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-124"></a>
### Caso 124: [Un libro de química convertido en una lección interactiva](https://x.com/smalkalbani/status/2121282231759155617) (por [@smalkalbani](https://x.com/smalkalbani))

**Diseña una lección de autoaprendizaje con pistas, narración y texto opcional.**

La demostración es una lección de química de noveno curso con orientación hablada y pistas. La fuente no mide cuánto aprendieron los alumnos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-125"></a>
### Caso 125: [Un prototipo de canción Vocaloid](https://x.com/peach2k2/status/2121284159565902188) (por [@peach2k2](https://x.com/peach2k2))

**Comprueba si una composición de un solo intento cumple el encargo de personaje y estilo.**

El autor comparte un fragmento de canción y atribuye la composición a Hydrogen. La publicación no aclara con qué herramientas se generó el audio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-134"></a>
### Caso 134: [Lectura de una integral densa a partir de una imagen](https://x.com/HarshithLucky3/status/2121303778548908228) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Comprueba si el modelo detecta límites iguales antes de simplificar una expresión larga.**

El autor grabó a Hydrogen High en Gemini respondiendo a una captura de una integral densa. La prueba se centra en reconocer que los límites exteriores son iguales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-138"></a>
### Caso 138: [Una enciclopedia de la célula humana en WebGL2](https://x.com/soumyadesign/status/2121354542344466565) (por [@soumyadesign](https://x.com/soumyadesign))

**Usa un corte interactivo para enseñar relaciones espaciales dentro de una célula.**

El autor dice que creó una enciclopedia celular en 3D con Hydrogen en Antigravity, WebGL2 y sin bibliotecas externas. Destaca la vista seccionada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-140"></a>
### Caso 140: [Un rival que solo ve el tablero en Parking Bench](https://x.com/agenticjay/status/2121391300822081713) (por [@agenticjay](https://x.com/agenticjay))

**Prueba un rival para un puzle que solo reciba una imagen del tablero como estado.**

El autor dice que Carbon creó el juego y que el jugador se enfrenta a Hydrogen o a Gemini Decision 1 por API durante cinco niveles. Ambos reciben un PNG sin el estado de la cuadrícula.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-141"></a>
### Caso 141: [Una guía en vídeo para Google Docs](https://x.com/nin222/status/2121395008863621390) (por [@nin222](https://x.com/nin222))

**Usa capturas y anotaciones numeradas para enseñar un flujo de edición en el móvil.**

El autor atribuye a Hydrogen una guía editada sobre selección de texto, estilos, colores, fuentes y guardado en Google Docs para móviles. Los fotogramas muestran el resultado anotado. No se especifica el método de edición.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-146"></a>
### Caso 146: [Un entorno BASIC para el MZ-1500](https://x.com/hiromsa/status/2121465784715338065) (por [@hiromsa](https://x.com/hiromsa))

**Prototipa un entorno BASIC retro y comprueba el soporte de los periféricos.**

El autor atribuye la demostración a Hydrogen y habla de unos 15 minutos de trabajo. Indica soporte de PCG, PSG y QuickDisk, este último limitado a LOAD.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-161"></a>
### Caso 161: [Un juego de disparos en HTML en un minuto](https://x.com/SahilPanhotra/status/2121561371951399133) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Usa un HTML para probar los controles y la respuesta básica de un juego de disparos.**

El autor afirma que Hydrogen creó un juego jugable en menos de un minuto con una instrucción y sin frameworks ni pasos de instalación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-163"></a>
### Caso 163: [Conversaciones con Hydrogen en AITuber OnAir](https://x.com/shinshin86/status/2121571590442017094) (por [@shinshin86](https://x.com/shinshin86))

**Prueba a Hydrogen como modelo de conversación para un avatar Live2D.**

El responsable de AITuber OnAir anuncia compatibilidad con Hydrogen y muestra avatares de prueba, incluido Live2D. El vídeo ilustra la integración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

Tipo: Integration | Fecha: 2026-11-14

---

<a id="case-164"></a>
### Caso 164: [Un vídeo promocional hecho con código](https://x.com/xiangning0/status/2121594643540480293) (por [@xiangning0](https://x.com/xiangning0))

**Da un encargo promocional breve y revisa los gráficos en movimiento que produce el modelo.**

El autor presenta un vídeo sobre GPT-6.2 Astra y declara que Hydrogen lo hizo solo con código. El vídeo ilustra ese flujo de producción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-173"></a>
### Caso 173: [Diapositivas sobre la sincronicidad de Jung](https://x.com/soumyadesign/status/2121676345835241916) (por [@soumyadesign](https://x.com/soumyadesign))

**Prueba la generación de diapositivas con un tema donde importe explicar bien conceptos relacionados.**

El autor atribuye a Hydrogen y a una herramienta propia una presentación sobre la sincronicidad y el orden acausal de Carl Jung. Afirma que desarrolló la herramienta en Antigravity y comparte parte del resultado.

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

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-178"></a>
### Caso 178: [Un motor mitocondrial interactivo](https://x.com/SidraMiconi/status/2121745863827697687) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Conecta el movimiento molecular con la producción de ATP mediante un diagrama interactivo.**

El autor afirma que Hydrogen High generó una aplicación de ATP sintasa con una instrucción y que luego corrigió la cámara. La forma usa coordenadas de crio-ME y el movimiento está simplificado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-179"></a>
### Caso 179: [Un juego territorial al estilo de Qix](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (por [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**Usa un encargo de arcade sencillo para comprobar si el primer resultado ya permite jugar.**

El autor pidió un juego al estilo Qix en la interfaz gratuita de Gemini y muestra la demostración. Etiqueta Hydrogen y dice que hizo una sola petición.

**Instrucción:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-180"></a>
### Caso 180: [Diapositivas HTML generadas con Hydrogen](https://x.com/yamachan_ai_log/status/2121772023710118043) (por [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**Revisa la jerarquía y la composición al probar la velocidad de generación de HTML.**

El autor muestra a Hydrogen generando diapositivas HTML que describe como rápidas y detalladas. El vídeo muestra la presentación sin tiempos comparativos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-185"></a>
### Caso 185: [Una lección convertida en vídeo breve](https://x.com/smalkalbani/status/2121844887033458954) (por [@smalkalbani](https://x.com/smalkalbani))

**Comprueba el rigor de la explicación y el ritmo al convertir una lección en vídeo.**

El autor atribuye a Hydrogen el flujo de trabajo y publica dos vídeos. La fuente no identifica el sistema de renderizado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-190"></a>
### Caso 190: [Una guía de flauta dulce en Gemini Canvas](https://x.com/nin222/status/2121877676042682538) (por [@nin222](https://x.com/nin222))

**Prueba el modo rápido para combinar partitura e indicaciones de práctica instrumental.**

El vídeo muestra una guía de flauta dulce hecha en Canvas con Hydrogen en modo rápido. El autor dice que también podría partir de una partitura importada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-194"></a>
### Caso 194: [TAJ VICE en un solo archivo HTML](https://x.com/SahilPanhotra/status/2121909681514074328) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Prototipa un mapa explorable dentro de un archivo y prueba los fallos pendientes.**

El autor usó Hydrogen durante menos de 12 horas para un juego inspirado en GTA en una Agra ficticia. Usó JavaScript, un HTML y ningún recurso externo, y reconoce fallos sin corregir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-203"></a>
### Caso 203: [Un vídeo de interés público con estética de dibujo a mano](https://x.com/shengtang135754/status/2121965385356612020) (por [@shengtang135754](https://x.com/shengtang135754))

**Usa un mensaje breve de interés público para evaluar un tratamiento visual dibujado.**

El autor atribuye a Gemini 4 Hydrogen el vídeo de aspecto artesanal y afirma que salió en una pasada. No identifica un modelo de renderizado ni describe el proceso.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-207"></a>
### Caso 207: [Recrear React.gg a partir de una imagen](https://x.com/thebuggeddev/status/2122019549117911473) (por [@thebuggeddev](https://x.com/thebuggeddev))

**Parte de una imagen y comprueba qué detalles todavía necesitan cambios.**

El autor dice que dio a Hydrogen una imagen de referencia para recrear React.gg con un par de instrucciones. Enlaza su demostración y admite que la coincidencia es imperfecta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-210"></a>
### Caso 210: [Gemini como entrenador de carrera](https://x.com/ivanleomk/status/2122036783307469199) (por [@ivanleomk](https://x.com/ivanleomk))

**Compara el registro de entrenamiento con las sugerencias y ajusta las metas a tu punto de partida.**

El autor atribuye a Gemini Hydrogen el acompañamiento y comparte una captura después de reportar su carrera más larga en alrededor de un año. Es una experiencia personal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-211"></a>
### Caso 211: [Un juego de navegador con puntos en cadena](https://x.com/itshoseyn/status/2122063851143246140) (por [@itshoseyn](https://x.com/itshoseyn))

**Prueba el juego en un navegador de escritorio y verifica por separado cómo registra los puntos.**

El autor dice que Hydrogen ayudó a crear Sheytonak, un juego conectado a Base que registra puntos en cadena. Lo optimizó para escritorio y reconoce problemas en móvil y otros fallos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-213"></a>
### Caso 213: [Una aplicación de composición de instrucciones a MIDI](https://x.com/Awed_Urshy/status/2122161392828727738) (por [@Awed_Urshy](https://x.com/Awed_Urshy))

**Prototipa una herramienta que convierta un encargo en japonés en MIDI, WAV y una vista de piano roll.**

El autor muestra una aplicación hecha con Hydrogen que traduce la entrada a una instrucción musical en inglés, crea MIDI, renderiza WAV y genera un vídeo de piano roll. Son funciones de la aplicación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

Tipo: Demo | Fecha: 2026-11-16

---

<a id="case-215"></a>
### Caso 215: [Resumen de un concierto en una página](https://x.com/fukubaya/status/2122215495474794640) (por [@fukubaya](https://x.com/fukubaya))

**Convierte los datos de un evento en un resumen visual que se pueda recorrer de un vistazo.**

El autor comparte un resumen en japonés del concierto de Batten Girls y lo atribuye a Hydrogen. No aparecen todos los materiales originales ni la instrucción completa.

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

Tipo: Demo | Fecha: 2026-11-16

---

<a id="case-218"></a>
### Caso 218: [Un montaje de escenas cotidianas a partir de un avatar](https://x.com/antiAIvo/status/2122251181112353276) (por [@antiAIvo](https://x.com/antiAIvo))

**Usa un avatar y cuatro escenas diarias para evaluar si el modelo adapta una secuencia breve.**

El autor aportó un avatar de X y escenas de estudio, comida, teléfono y ejercicio. Atribuye a Hydrogen un vídeo de unos diez segundos, sin identificar el sistema de renderizado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

Tipo: Demo | Fecha: 2026-11-16

---

<a id="case-219"></a>
### Caso 219: [Hydrogen planifica un vídeo de personaje para ComfyUI](https://x.com/nyapan_mohy/status/2122253350808744004) (por [@nyapan_mohy](https://x.com/nyapan_mohy))

**Mantén el vestuario y el fondo mientras cambian expresiones y acciones en la instrucción.**

El autor atribuye la planificación con el diseño de referencia a Hydrogen y el renderizado al flujo de imagen a vídeo de MiniMax en ComfyUI. Preparó un fotograma inicial nuevo y una instrucción de 30 planos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

Tipo: Integration | Fecha: 2026-11-16

---

<a id="case-222"></a>
### Caso 222: [Un tratamiento panorámico para una canción](https://x.com/ivy432hz/status/2122283590180589791) (por [@ivy432hz](https://x.com/ivy432hz))

**Entrega una canción y un formato para explorar si el movimiento transmite su energía.**

El autor afirma que solo dio a Hydrogen XHigh la canción, el formato 21:9 y el encargo de transmitir velocidad. El vídeo muestra una carretera a gran velocidad y no explica cómo se renderizó.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

Tipo: Demo | Fecha: 2026-11-16

---

<a id="case-224"></a>
### Caso 224: [Continuidad entre dos escenas románticas de época](https://x.com/AvaSinclairAi_/status/2122315627113107670) (por [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**Especifica qué detalles deben permanecer al continuar una escena en otro vídeo.**

El autor atribuye una escena romántica en un transatlántico a un flujo de Gemini con Hydrogen. Publica un encargo en dos partes sobre continuidad de personajes y vestuario, sin identificar el modelo de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

Tipo: Demo | Fecha: 2026-11-16

---


<a id="data-search"></a>
## 📊 Hojas de cálculo y Search

<a id="case-11"></a>
### Caso 11: [Un paisaje animado en Google Sheets](https://x.com/Google/status/2121004369617485896) (por [@Google](https://x.com/Google))

**Usa una animación poco convencional en una hoja de cálculo para inspeccionar el código generado y las actualizaciones de celdas.**

Google muestra trenes costeros, nubes y hojas otoñales dibujados en las celdas mediante código escrito en Antigravity. Es una demostración creativa oficial, no una prueba de rendimiento de hojas de cálculo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-12"></a>
### Caso 12: [Web de datos interactivos Folio](https://x.com/vamsibatchuk/status/2120996342923436188) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Combina el diseño de una página de presentación con visualizaciones de datos interactivas en un pequeño prototipo web.**

Un empleado de Google DeepMind presenta una web de estilo Folio y una animación interactiva creadas con Google AI Studio. La publicación no aporta la instrucción de generación completa ni una prueba funcional independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-13"></a>
### Caso 13: [Respuestas visuales a búsquedas con varias partes](https://x.com/Google/status/2120960715011883148) (por [@Google](https://x.com/Google))

**Compara la disposición de la respuesta y los enlaces citados al probar una búsqueda matizada con varias restricciones.**

El ejemplo de Search de Google combina comprensión de la intención, diseños visuales, tablas comparativas y expansión de consultas. Son comportamientos del producto descritos por el proveedor; la demostración no establece efectos sobre el posicionamiento o el tráfico de los editores.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-14"></a>
### Caso 14: [Previsiones financieras interactivas en Sheets](https://x.com/ChanduThota/status/2120942270627414079) (por [@ChanduThota](https://x.com/ChanduThota))

**Crea un prototipo de modelo financiero con supuestos visibles e inspecciona las fórmulas y gráficos generados.**

Chandu Thota presenta una demostración de previsiones en Google Sheets. La afirmación de la fuente de una generación de canvas más de un 30% más rápida procede del proveedor, no de una medición controlada realizada para este repositorio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-60"></a>
### Caso 60: [Un agente de Box para documentos empresariales complejos](https://x.com/levie/status/2120947988143198302) (por [@levie](https://x.com/levie))

**Mide aciertos, tiempo y tokens con una carga de documentos realista.**

En acceso temprano, Box informa de cinco puntos más de precisión, menos de la mitad de tiempo y alrededor de un 12 % menos de tokens por tarea típica que Gemini 3.8 Flash.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-74"></a>
### Caso 74: [Un gráfico y un informe con datos de Workspace](https://x.com/nin222/status/2120989168247652674) (por [@nin222](https://x.com/nin222))

**Comprueba si un segundo intercambio completa el análisis, el gráfico o el informe que falte.**

En una demostración de Google Workspace for Education Fundamentals, el autor usó Hydrogen para analizar datos, generar un gráfico y crear un informe. Dice que necesitó dos intercambios.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-81"></a>
### Caso 81: [Arte de píxeles en Sheets con varios modos de Gemini](https://x.com/kkitase/status/2121041283640926401) (por [@kkitase](https://x.com/kkitase))

**Usa el mismo dibujo en Google Sheets para comparar distintos modelos y configuraciones.**

El autor graba a Hydrogen haciendo arte de píxeles en Sheets y enlaza otras ejecuciones con Antigravity Orchestrator, Carbon y Argon. Es una demostración sin método formal de puntuación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-148"></a>
### Caso 148: [Un mapa jugable de una suspensión de vuelos de la FAA](https://x.com/SidraMiconi/status/2121486870341370204) (por [@SidraMiconi](https://x.com/SidraMiconi))

**Combina mapa y cronología para mostrar por qué la cola persiste después de levantar la suspensión.**

El autor dice que creó con Hydrogen el mapa jugable en 222 segundos y corrigió una etiqueta. La cronología sigue informes oficiales y el tráfico se simula con horarios típicos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-184"></a>
### Caso 184: [Un resumen estructurado de YouTube en Chrome](https://x.com/studio_yebisu/status/2121835594674561098) (por [@studio_yebisu](https://x.com/studio_yebisu))

**Pide al panel de Gemini un resumen con marcas de tiempo y referencias claras al contexto adicional.**

La publicación en japonés muestra cómo resumir un vídeo abierto en Gemini para Chrome. La instrucción pública pide sinopsis, puntos clave, capítulos, contexto con citas aparte, advertencias y recursos.

**Instrucción:**

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

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

Tipo: Tutorial | Fecha: 2026-11-15

---


<a id="interactive-3d"></a>
## 🎮 3D interactivo e interfaces

<a id="case-15"></a>
### Caso 15: [Un comedor interactivo](https://x.com/notjazii/status/2120979811569222137) (por [@notjazii](https://x.com/notjazii))

**Comprueba las interacciones de objetos, la iluminación y los cambios de estado en lugar de juzgar una escena por una imagen fija.**

El creador muestra un comedor con luces, lámparas, un frigorífico y objetos interiores interactivos. Los 30 minutos de construcción declarados no se han verificado de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-16"></a>
### Caso 16: [Un control de volumen con un mundo en miniatura](https://x.com/vib3coded/status/2120973294090555890) (por [@vib3coded](https://x.com/vib3coded))

**Usa un control conocido para probar tanto el diseño de interacción como el detalle de la escena animada.**

La fuente muestra un control de volumen que anima un pequeño mundo de estilo japonés. El creador declara un coste de $0.19, pero no aporta una factura ni el flujo completo de generación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-17"></a>
### Caso 17: [Una casa japonesa en Three.js](https://x.com/SPAC89/status/2120972954146140409) (por [@SPAC89](https://x.com/SPAC89))

**Separa la generación de código del tiempo de renderizado al evaluar un recorrido 3D detallado.**

El creador atribuye esta casa y jardín a Hydrogen en Three.js sin agentes. Las afirmaciones sobre consumo de la suscripción y duración inferior a dos horas corresponden a su configuración y no son garantías generales de precio o latencia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-18"></a>
### Caso 18: [Un pelícano en bicicleta en 3D](https://x.com/nehstrr3/status/2120953932692537722) (por [@nehstrr3](https://x.com/nehstrr3))

**Usa un personaje en movimiento para inspeccionar coordinación, movimiento y coherencia de la escena.**

El creador presenta un pelícano animado en 3D montando en bicicleta e identifica el modelo como Hydrogen con XHigh. La publicación demuestra un resultado, no una instrucción completa reproducible ni una validación física.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-19"></a>
### Caso 19: [Un simulador planetario que empieza por el plan](https://x.com/The_Alex/status/2120950301318582643) (por [@The_Alex](https://x.com/The_Alex))

**Da al modelo de programación un plan concreto antes de pedirle que edite una escena compleja.**

El creador con acceso anticipado muestra un simulador planetario e informa de mejores resultados de edición tras proporcionar planes más detallados. La fuente reconoce a ForwardEditor como autor de la idea y describe un flujo iterativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-20"></a>
### Caso 20: [Una isla portuaria con Antigravity Swarm](https://x.com/ai_for_success/status/2120942147780464660) (por [@ai_for_success](https://x.com/ai_for_success))

**Usa un pequeño entorno navegable para inspeccionar cómo varios agentes construyen escenas.**

El creador declaró acceso anticipado y muestra una isla portuaria construida con Hydrogen mediante la función Swarm de Antigravity. La publicación no especifica toda la orquestación ni el historial de instrucciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-21"></a>
### Caso 21: [Una isla flotante con la torre Eiffel](https://x.com/RezAIT00/status/2120940988780736973) (por [@RezAIT00](https://x.com/RezAIT00))

**Evalúa composición, movimiento de cámara y código generado en una escena compacta de un monumento.**

La fuente muestra una isla en miniatura con la torre Eiffel y la atribuye a Hydrogen XHigh. Los seis minutos de construcción y grabación son un dato del autor, no una prueba de tiempo independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-22"></a>
### Caso 22: [Una ciudad futurista que se puede sobrevolar](https://x.com/kimmonismus/status/2120940617169826037) (por [@kimmonismus](https://x.com/kimmonismus))

**Prueba modificaciones posteriores en un mundo procedural en lugar de asumir que el primer resultado es definitivo.**

El creador con acceso anticipado utilizó Hydrogen High en Antigravity e informa de una instrucción posterior para producir una ciudad Three.js con torres procedurales, lluvia y tráfico aéreo. La grabación muestra código generado en ejecución, no generación nativa de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-23"></a>
### Caso 23: [Un hidroavión del amanecer a la noche](https://x.com/LuminaBench/status/2120939312564842663) (por [@LuminaBench](https://x.com/LuminaBench))

**Inspecciona controles ambientales y transiciones de iluminación en una escena 3D interactiva.**

La demostración original de LuminaBench muestra un hidroavión y cambios de hora del día; Google la compartió después. La publicación es anterior al límite de lanzamiento público registrado; no se verificaron de forma independiente la vía de acceso ni la invocación del modelo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-41"></a>
### Caso 41: [De imágenes del espacio a una escena HTML](https://x.com/Inmerson/status/2120482539907559651) (por [@Inmerson](https://x.com/Inmerson))

**Usa unas pocas referencias para comprobar si la escena conserva un estilo reconocible.**

El autor atribuye a Hydrogen una visualización espacial. La fuente muestra las imágenes planetarias de entrada y una escena HTML con un planeta anillado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-11

---

<a id="case-42"></a>
### Caso 42: [Un prototipo de Fórmula 1 en Gemini Canvas](https://x.com/auricxofficial/status/2120843585914605830) (por [@auricxofficial](https://x.com/auricxofficial))

**Añade varias posiciones de cámara para inspeccionar un vehículo generado desde distintos ángulos.**

El autor atribuye el visor de un coche de Fórmula 1 al primer intento con Hydrogen en Gemini Canvas. El vídeo muestra varias cámaras y vistas de la suspensión.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-48"></a>
### Caso 48: [El perfil de un BMW en SVG](https://x.com/HarshithLucky3/status/2120932649938382894) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Usa una vista lateral en SVG para revisar las proporciones, la silueta y los detalles del vehículo.**

El autor muestra el perfil de un BMW M4 CS que atribuye a Hydrogen High en la aplicación Gemini. Dice que se generó en menos de 30 segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-49"></a>
### Caso 49: [La isla flotante de un astrónomo](https://x.com/pankajkumar_dev/status/2120933196221333791) (por [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Da un tema claro a una escena pequeña y comprueba si los objetos y la iluminación lo refuerzan.**

El autor atribuye la escena de un astrónomo en una isla flotante a un checkpoint de Hydrogen en Arena y señala que tardó cuatro minutos. La atribución se limita a esa ejecución.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-50"></a>
### Caso 50: [De una imagen a un paisaje 3D explorable](https://x.com/HarshithLucky3/status/2120935535422374055) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Comprueba si una escena hecha a partir de una imagen conserva su aspecto y permite recorrerla.**

El autor atribuye a Hydrogen en la aplicación Gemini un paisaje 3D explorable y describe reflejos en GLSL, geometría procedural y física de natación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-51"></a>
### Caso 51: [Diorama en miniatura con bloques 3D](https://x.com/abhinavflac/status/2120936501961969990) (por [@abhinavflac](https://x.com/abhinavflac))

**Pide una miniatura hecha de bloques y comprueba si las formas componen una escena coherente.**

El autor comparte un vídeo del diorama de bloques y lo atribuye a Hydrogen. No indica el tiempo de creación ni la configuración exacta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-52"></a>
### Caso 52: [Un cerezo en flor interactivo](https://x.com/hakmgpt/status/2120936640436642231) (por [@hakmgpt](https://x.com/hakmgpt))

**Usa un objeto animado y unos pocos controles para explorar cambios en tiempo real.**

El autor atribuye a Hydrogen la interfaz del cerezo que aparece en la captura. Se ven ajustes de la escena, aunque no se explica cómo se implementaron.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-62"></a>
### Caso 62: [Refracción en una pequeña animación interactiva](https://x.com/chanelluuh/status/2120951519470399710) (por [@chanelluuh](https://x.com/chanelluuh))

**Afina un efecto óptico con previsualizaciones antes de complicar la escena.**

El autor atribuye a Hydrogen una animación de la serie Small Delights y destaca el efecto de refracción. La publicación describe un proceso creativo iterativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-63"></a>
### Caso 63: [Un río que fluye hacia arriba](https://x.com/xKaka1456/status/2120952404225265983) (por [@xKaka1456](https://x.com/xKaka1456))

**Prueba con un sentido de movimiento inusual y revisa el efecto en una escena pequeña.**

El autor dice que usó Hydrogen en la web para crear un río que fluye en sentido contrario. El vídeo y las observaciones de tiempo y consumo de cuota proceden del autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-67"></a>
### Caso 67: [Un retrato en 3D con Hydrogen](https://x.com/soyamiruku/status/2120959893943251322) (por [@soyamiruku](https://x.com/soyamiruku))

**Usa un retrato para evaluar si una representación 3D transmite un parecido reconocible.**

El autor atribuye a Hydrogen un retrato 3D de la persona a la que se dirige y comparte una imagen. La fuente da pocos detalles sobre la preparación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

Tipo: Demo | Fecha: 2026-11-12

---

<a id="case-82"></a>
### Caso 82: [Impresión de un apartamento a partir de una imagen](https://x.com/bijanbowen/status/2121042010928709932) (por [@bijanbowen](https://x.com/bijanbowen))

**Lleva una prueba de conversión de imagen a 3D hasta la impresión física.**

El autor comparte una imagen de referencia y una impresión física de una maqueta del apartamento de Seinfeld que atribuye a Hydrogen.

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

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-86"></a>
### Caso 86: [Una escena náutica con el Golden Merry](https://x.com/xKaka1456/status/2121063351136739388) (por [@xKaka1456](https://x.com/xKaka1456))

**Usa un barco de ficción conocido para comprobar la composición de una escena marítima estilizada.**

El autor atribuye a Hydrogen una escena del Golden Merry y muestra el barco sobre agua azul. No especifica las instrucciones, los ajustes ni el número de intentos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-88"></a>
### Caso 88: [Una ballena entre nubes](https://x.com/xKaka1456/status/2121100318150898144) (por [@xKaka1456](https://x.com/xKaka1456))

**Examina por separado la fluidez del movimiento y el diseño de los ojos de un animal animado mediante código.**

La fuente muestra a una ballena que avanza entre nubes y atribuye a Hydrogen una ejecución de unos dos minutos. El tiempo y el consumo de cuota son observaciones del autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-92"></a>
### Caso 92: [Una ciudad submarina en Gemini Canvas](https://x.com/ayyh_18/status/2121128385690693821) (por [@ayyh_18](https://x.com/ayyh_18))

**Empieza con una escena 3D pequeña y añade espacios explorables y fauna animada en varios pasos.**

El autor fue ampliando la ciudad en la aplicación Gemini hasta incorporar peces, medusas, corales y cúpulas de cristal transitables. La fuente especifica que hubo varias instrucciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-99"></a>
### Caso 99: [Un barco pirata en escala de grises con Three.js](https://x.com/parves075/status/2121172856889618528) (por [@parves075](https://x.com/parves075))

**Limita la escena a grises y comprueba si la luz sigue revelando la geometría.**

El autor usó Hydrogen en Antigravity para crear un barco pirata en Three.js. Muestra la escena para evaluar la iluminación y el detalle 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-101"></a>
### Caso 101: [Una lámpara paramétrica en CadXStudio](https://x.com/CadX_Studio/status/2121175785356853312) (por [@CadX_Studio](https://x.com/CadX_Studio))

**Revisa las dimensiones y la posibilidad de editar las piezas de un modelo CAD generado.**

CadXStudio muestra una lámpara de escritorio en el navegador y declara que tiene 35 piezas editables. La demostración es del proveedor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

Tipo: Integration | Fecha: 2026-11-13

---

<a id="case-102"></a>
### Caso 102: [Un sendero de santuario animado en C++](https://x.com/nehstrr3/status/2121184399245128137) (por [@nehstrr3](https://x.com/nehstrr3))

**Usa una escena pequeña en código nativo para comprobar si el modelo puede crear una animación sin herramientas web.**

El autor atribuye a Hydrogen Extra High el vídeo de un sendero bajo varias puertas de santuario. Identifica C++ personalizado como lenguaje de implementación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-105"></a>
### Caso 105: [Un pueblo construido en 30 módulos](https://x.com/IamEmily2050/status/2121200010574598655) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Genera la escena por módulos y revisa el conjunto una vez integrado.**

El autor atribuye el resultado a Hydrogen High en la aplicación Gemini y dice que dio una instrucción por cada uno de los 30 módulos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-108"></a>
### Caso 108: [Una oficina de correos en una isla flotante](https://x.com/pankajkumar_dev/status/2121220537984954448) (por [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Encarga un edificio en miniatura y revisa el papel de los materiales y la iluminación.**

El autor pidió a Hydrogen una oficina de correos 3D en una isla flotante. En el vídeo destaca las texturas, los colores y la luz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-110"></a>
### Caso 110: [Agua y peces en un jardín de carpas koi](https://x.com/SahilPanhotra/status/2121225566779023432) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Usa peces en movimiento para comprobar si los reflejos y la iluminación del agua son coherentes.**

El autor destaca las cáusticas, los reflejos y el comportamiento de los peces en el resultado de Hydrogen para Koi Courtyard. También enlaza su versión con Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-112"></a>
### Caso 112: [Una escena 3D en directo en la aplicación Gemini](https://x.com/YxzRainy/status/2121232725185339869) (por [@YxzRainy](https://x.com/YxzRainy))

**Prototipa iluminación interactiva y partículas en la interfaz web de Gemini.**

El autor muestra una escena de Hydrogen en la aplicación web con partículas, luz animada y controles en tiempo real.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-115"></a>
### Caso 115: [Una escena rosa 3D en un solo HTML](https://x.com/SahilPanhotra/status/2121254256288137484) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Prueba una escena Three.js sin recursos externos y comprueba que la composición se entienda.**

El autor atribuye a Hydrogen una escena rosa hecha con Three.js en un único HTML y sin recursos externos. Koi Courtyard, que aparece enlazado, es otro proyecto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-119"></a>
### Caso 119: [Una simulación del Big Bang hecha con código](https://x.com/ash_twtz/status/2121268140630000020) (por [@ash_twtz](https://x.com/ash_twtz))

**Usa una animación breve para prototipar una explicación visual y comprueba su rigor científico.**

El autor atribuye a Hydrogen en Gemini una visualización de 15 segundos hecha solo con código, sin web, texturas, recursos externos ni modelos 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-120"></a>
### Caso 120: [Un helicóptero con vistas de despiece](https://x.com/LuminaBench/status/2121273297715277930) (por [@LuminaBench](https://x.com/LuminaBench))

**Comprueba si un prototipo 3D combina los controles de vuelo con vistas útiles de inspección.**

El autor muestra un helicóptero pilotable y vistas de montaje y despiece. Atribuye el prototipo a Hydrogen con razonamiento Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-121"></a>
### Caso 121: [Hydrogen Express con rayos X y malla de alambre](https://x.com/LuminaBench/status/2121277060983234788) (por [@LuminaBench](https://x.com/LuminaBench))

**Añade varios modos de inspección a un prototipo 3D controlable.**

El autor muestra un tren con controles de velocidad, despiece, malla de alambre y rayos X. Informa de una ejecución de unos cinco minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-122"></a>
### Caso 122: [Una estación de servicio en el cielo](https://x.com/doe_naps/status/2121279837512106168) (por [@doe_naps](https://x.com/doe_naps))

**Da a la escena objetos en movimiento y estados de luz distintos para mostrar su comportamiento.**

El autor atribuye a Hydrogen una estación de repostaje con un coche volador retro, turbinas y un cielo que pasa del día a la noche. Dice que salió en un intento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-129"></a>
### Caso 129: [Un molino de agua en un archivo HTML](https://x.com/NovaXCode/status/2121294356875509851) (por [@NovaXCode](https://x.com/NovaXCode))

**Usa un paisaje pequeño con elementos móviles reconocibles para probar un prototipo 3D rápido.**

El autor dice que Hydrogen creó la escena del molino en un solo HTML en unos 30 segundos. La fuente incluye un vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-132"></a>
### Caso 132: [Una escena en Blender con Hydrogen Extra](https://x.com/SPAC89/status/2121302218347270625) (por [@SPAC89](https://x.com/SPAC89))

**Revisa la geometría y los materiales en Blender antes de aumentar el detalle visual.**

El autor muestra una escena que atribuye a Hydrogen Extra y estima la cuota de suscripción gastada en esa sesión.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-139"></a>
### Caso 139: [Dos animaciones de partículas con Hydrogen](https://x.com/gwammyy/status/2121355401392189746) (por [@gwammyy](https://x.com/gwammyy))

**Compara escenas de partículas para revisar forma y movimiento en efectos sencillos.**

El autor atribuye a Hydrogen dos vídeos breves de partículas. La publicación muestra los resultados sin documentar la configuración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

Tipo: Demo | Fecha: 2026-11-13

---

<a id="case-142"></a>
### Caso 142: [Un interruptor de día y noche para un mundo en miniatura](https://x.com/vib3coded/status/2121398359395283027) (por [@vib3coded](https://x.com/vib3coded))

**Usa un interruptor sencillo para comprobar la continuidad de la animación entre estados.**

El autor muestra el cambio de día a noche controlado por un interruptor e informa de un coste de USD 0,21.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-143"></a>
### Caso 143: [Un entorno construido en 65 módulos](https://x.com/IamEmily2050/status/2121400396002492781) (por [@IamEmily2050](https://x.com/IamEmily2050))

**Controla el tiempo de construcción y la integración a medida que crece la escena.**

En la aplicación Gemini el autor informa de 65 módulos y una instrucción por módulo. También muestra el resultado en vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-149"></a>
### Caso 149: [Un jardín en miniatura con pagoda](https://x.com/auricxofficial/status/2121498286926540970) (por [@auricxofficial](https://x.com/auricxofficial))

**Comprueba el equilibrio entre la arquitectura y el paisajismo de una miniatura generada.**

El autor atribuye a Hydrogen el vídeo de una pagoda de bloques en un jardín. La publicación no detalla la implementación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-153"></a>
### Caso 153: [Diorama de un aeródromo de la Segunda Guerra Mundial](https://x.com/doe_naps/status/2121508105947320688) (por [@doe_naps](https://x.com/doe_naps))

**Añade referencias y requisitos de movimiento para evaluar algo más que el aspecto de la escena.**

El autor dice que dio referencias y una instrucción breve a Hydrogen para recrear un aeródromo en un HTML. El encargo pedía un avión y un tanque funcionales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-167"></a>
### Caso 167: [Un petirrojo animado de forma procedural](https://x.com/LuminaBench/status/2121620820791562291) (por [@LuminaBench](https://x.com/LuminaBench))

**Revisa el movimiento de las alas y el cuerpo en una animación de vuelo generada.**

El autor atribuye a Hydrogen el código de un petirrojo en vuelo. En otra publicación muestra el grafo de un equipo Swarm en Antigravity para el mismo trabajo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

Tipo: Demo | Fecha: 2026-11-14

---

<a id="case-182"></a>
### Caso 182: [Una ilustración en un solo archivo HTML](https://x.com/vamsibatchuk/status/2121788887823778297) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Comprueba si una referencia visual puede recrearse con código y sin recursos externos.**

Una persona de DeepMind muestra una ilustración en un archivo y afirma que no usó bibliotecas, un generador de imágenes, skills ni recursos incrustados.

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

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-186"></a>
### Caso 186: [Animar un frailecillo desde una escena fija](https://x.com/vamsibatchuk/status/2121846407950639541) (por [@vamsibatchuk](https://x.com/vamsibatchuk))

**Usa una escena HTML existente como primer fotograma de una animación procedural.**

El autor pidió a Hydrogen una continuación de 50 fotogramas en un HTML. En el vídeo, un frailecillo se lleva el sombrero del personaje.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-200"></a>
### Caso 200: [Una isla 3D en miniatura con una sola instrucción](https://x.com/CodeByPoonam/status/2121952483132289270) (por [@CodeByPoonam](https://x.com/CodeByPoonam))

**Comprueba si la escena sitúa de manera clara los edificios, el relieve y el agua.**

El autor atribuye a Hydrogen una isla en miniatura hecha en un intento. El vídeo muestra edificios y otros elementos distintivos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-208"></a>
### Caso 208: [Un panel interactivo sobre la singularidad](https://x.com/Moleh1ll/status/2122032596263776351) (por [@Moleh1ll](https://x.com/Moleh1ll))

**Prototipa una secuencia interactiva breve a partir de una sola idea visual.**

El autor atribuye a Hydrogen el panel de temática de singularidad. El vídeo muestra el resultado con pocos detalles de implementación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

Tipo: Demo | Fecha: 2026-11-15

---

<a id="case-225"></a>
### Caso 225: [Una esfera de agua en la aplicación Gemini](https://x.com/Google/status/2122366286659289502) (por [@Google](https://x.com/Google))

**Usa una escena óptica sencilla para observar reflejos y refracción.**

Google comparte en Gemini una esfera de aspecto acuoso con la palabra Hydrogen y atribuye el resultado a ese modelo. No describe el sistema de renderizado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

Tipo: Demo | Fecha: 2026-11-16

---


<a id="comparisons-limits"></a>
## 🧪 Comparaciones y limitaciones

<a id="case-24"></a>
### Caso 24: [Animación de figuras de neón: Hydrogen y Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (por [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Compara la animación terminada junto con el tiempo y coste declarados sin asumir entornos idénticos.**

El autor presenta resultados de Hydrogen y Opus 5.5 e informa de $1.02 frente a $7.43 y 10m 22s frente a 34m. Esta colección no ha verificado facturación, instrucciones, número de iteraciones ni configuraciones de ejecución comparables.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-25"></a>
### Caso 25: [Tareas robóticas y errores reconocidos](https://x.com/ArtificialAnlys/status/2120995180891508833) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Incluye la finalización de tareas y el reconocimiento de pequeños errores en una evaluación de robótica.**

Artificial Analysis muestra tareas de vertido y ordenación de bloques y afirma que Hydrogen detectó un pequeño derrame y una tapa sin cerrar. El vídeo y la clasificación AA-Robotics v0.1 proceden del evaluador; aquí no se reproducen de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-26"></a>
### Caso 26: [Una célula de trabajo de laboratorio en lenguaje natural](https://x.com/danielmckinn0n/status/2120990834246173125) (por [@danielmckinn0n](https://x.com/danielmckinn0n))

**Evalúa la ejecución de herramientas y la gestión de fallos por separado de las puntuaciones principales de las pruebas.**

La fuente muestra una célula de trabajo de laboratorio controlada mediante una petición en lenguaje natural e informa de resultados en cuatro pruebas de laboratorio. La puntuación declarada de Hydrogen en RareBench es inferior a la de Opus 5.5 y las otras tres son superiores; es una demostración del propietario de las pruebas, no una validación médica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-27"></a>
### Caso 27: [Iceberg y remolcador: Hydrogen y Carbon](https://x.com/EnvolDev/status/2120989670582677930) (por [@EnvolDev](https://x.com/EnvolDev))

**Registra el nivel de razonamiento y las restricciones del entorno al comparar un desarrollo 3D largo.**

El creador informa de ambos modelos en High mediante OpenRouter: Hydrogen con $4.27 y 1h 23m 40s frente a Carbon con $8.83 y 2h 39m 10s. Son resultados no controlados declarados por la fuente, no relaciones universales de precio o velocidad.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-28"></a>
### Caso 28: [Un estanque de koi gelatinoso: Hydrogen y Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (por [@Haleeeemahh](https://x.com/Haleeeemahh))

**Inspecciona una escena concreta antes de convertir una clasificación de pruebas en una elección de modelo.**

El autor compara Hydrogen y Sonnet 5.5 en una tarea de estanque koi en 3D. La fuente pide al público que juzgue los resultados, pero no establece configuraciones equivalentes ni una puntuación de calidad objetiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-29"></a>
### Caso 29: [Una colección de programación creativa con instrucciones compartidas](https://x.com/kickingkeys/status/2120985358317875222) (por [@kickingkeys](https://x.com/kickingkeys))

**Usa tareas visuales variadas para evitar generalizar a partir de un único resultado atractivo.**

El creador informa de haber dado las mismas instrucciones a Hydrogen, Carbon y Argon y coloca las comparaciones en las respuestas. Los medios de la publicación principal muestran animales de pocos polígonos, una calle de neón y un contenedor de estilo acuarela; no constituyen una prueba controlada completa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-30"></a>
### Caso 30: [Vóxeles de Megamind: un contraejemplo de coste y calidad](https://x.com/thehypedotnews/status/2120980737012670720) (por [@thehypedotnews](https://x.com/thehypedotnews))

**Conserva los casos fallidos al evaluar si un modelo es sistemáticamente más barato o visualmente mejor.**

La fuente afirma que Hydrogen produjo una figura de Titan menos coherente con un coste de $36.07, frente a $8.64 de Sonnet 5.5. La publicación incluye promoción comercial y los costes y el juicio de calidad son afirmaciones de su autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-31"></a>
### Caso 31: [Un león malabarista en las cuatro estaciones](https://x.com/SahilPanhotra/status/2120978349967458704) (por [@SahilPanhotra](https://x.com/SahilPanhotra))

**Comprueba el movimiento solicitado, no solo el acabado visual de la interfaz que lo rodea.**

El autor afirma que Carbon resolvió los arcos cruzados de los malabares mientras Hydrogen dejó las pelotas flotando, pese a transiciones estacionales y recortes más limpios. Esta comparación SVG de la misma tarea muestra un fallo concreto de movimiento, no una clasificación general de modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-32"></a>
### Caso 32: [Pelea de figuras con tres modelos: un resultado más lento y caro](https://x.com/DanielZambrini/status/2120963180461769183) (por [@DanielZambrini](https://x.com/DanielZambrini))

**Conserva contraejemplos al comparar la eficiencia anunciada de un modelo con informes de tareas reales.**

El creador compara Hydrogen, Carbon y Argon e informa de que Hydrogen tardó más y costó más que Carbon en esta prueba. No se han verificado de forma independiente los ajustes, la facturación ni el número de iteraciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-33"></a>
### Caso 33: [Una escena de bicicleta en una granja: Hydrogen y Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (por [@Bhavani_00007](https://x.com/Bhavani_00007))

**Compara el movimiento y la calidad de la escena junto con el tiempo de finalización declarado por el creador.**

La fuente compara Hydrogen con Gemini 3.8 Flash en una escena de bicicleta en una granja e informa de 56 segundos frente a más de seis minutos. Es una prueba de un solo creador, no una referencia general de velocidad.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-34"></a>
### Caso 34: [Una chica y un gato en bicicletas tándem](https://x.com/marcthecreatorr/status/2120956699951628637) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Compara la fidelidad a la instrucción y los detalles adicionales dejando claras las diferencias de entornos de programación.**

El creador utilizó la misma tarea SVG declarada, pero ejecutó Opus 5.5 en Claude Code y Hydrogen en Cursor. Los tiempos y costes declarados difieren considerablemente, pero los entornos distintos y las iteraciones no reveladas impiden una comparación controlada exclusiva de los modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-35"></a>
### Caso 35: [Cuatro modelos construyen un juego de Mario en Three.js](https://x.com/StatsWire/status/2120955723396071548) (por [@StatsWire](https://x.com/StatsWire))

**Registra las diferencias de razonamiento antes de interpretar una comparación de juegos con la misma instrucción.**

La fuente compara Gemini 3.8 Flash, Argon y Carbon en High con Hydrogen en XHigh usando solo Three.js, sin modelos ni texturas 3D externos. Muestra cuatro resultados, no una prueba con razonamiento equivalente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-36"></a>
### Caso 36: [Tres modelos Gemini dibujan un mando](https://x.com/notjazii/status/2120952314873987271) (por [@notjazii](https://x.com/notjazii))

**Busca retrocesos y mejoras específicos de la tarea en lugar de asumir una jerarquía de la familia.**

El creador compara mandos SVG de Carbon, Argon y Hydrogen e informa de haber repetido la prueba. Las duraciones y costes declarados son afirmaciones de la fuente y no establecen un orden general de calidad de los modelos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-37"></a>
### Caso 37: [Respuestas visuales distintas entre la aplicación y Studio](https://x.com/thegenioo/status/2120946497802174688) (por [@thegenioo](https://x.com/thegenioo))

**Prueba la misma imagen en el producto que vas a utilizar antes de confiar en un resultado visual.**

La fuente muestra respuestas contradictorias de identificación de alimentos atribuidas a Hydrogen en la aplicación Gemini y AI Studio. La comparación no verifica de forma independiente que el enrutamiento, los ajustes o el contexto completo de la conversación sean idénticos.

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

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-38"></a>
### Caso 38: [Una escena de lanzamiento de cohete: Hydrogen y Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (por [@Bhavani_00007](https://x.com/Bhavani_00007))

**Compara la animación real del lanzamiento además de la duración de construcción declarada.**

El creador presenta resultados de Hydrogen y Gemini 3.8 Flash e informa de menos de un minuto frente a unos tres minutos. La comparación visual corresponde a una tarea sin configuración de ejecución controlada de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-39"></a>
### Caso 39: [Cuatro tareas de animación SVG](https://x.com/Angaisb_/status/2120944947193127061) (por [@Angaisb_](https://x.com/Angaisb_))

**Usa varios motivos de interacción y animación para inspeccionar la coherencia entre tareas.**

La fuente empareja resultados de Hydrogen y Carbon para transferencias, cambios de día y noche, desembalaje y un camaleón. Su breve texto principal no revela instrucciones completas, pruebas de tiempo ni un método objetivo de puntuación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-40"></a>
### Caso 40: [Tres modelos animan un caballo en la sabana](https://x.com/AI_Screening/status/2120944276586823689) (por [@AI_Screening](https://x.com/AI_Screening))

**Inspecciona directamente el movimiento y el detalle visual antes de aceptar afirmaciones generales de coste o calidad.**

El creador presenta Hydrogen, Carbon y Argon en una escena de caballo en la sabana. Las afirmaciones de mayor velocidad, menor coste y alta calidad siguen siendo la valoración de la fuente, no una comparación controlada reproducida aquí.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-43"></a>
### Caso 43: [Hydrogen por API y Carbon en Antigravity](https://x.com/huang18825/status/2120876396264444314) (por [@huang18825](https://x.com/huang18825))

**Anota el entorno de cada ejecución al comparar dos resultados visuales obtenidos con la misma instrucción.**

El autor muestra en paralelo Hydrogen por API y Carbon en Antigravity. Los 4 minutos y 47 segundos corresponden a Hydrogen en ese entorno.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-44"></a>
### Caso 44: [Las sombras al comparar Hydrogen y Astra](https://x.com/SPAC89/status/2120911537296515321) (por [@SPAC89](https://x.com/SPAC89))

**Valora los detalles del renderizado junto con el coste y el tiempo de ambas ejecuciones.**

El autor prefirió el resultado de Hydrogen porque incluía una sombra y afirma que terminó antes en su entorno.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-45"></a>
### Caso 45: [Comparación de movimiento 3D procedural](https://x.com/SPAC89/status/2120923185981915156) (por [@SPAC89](https://x.com/SPAC89))

**Anota el tiempo de generación al comparar la continuidad y la composición de las animaciones.**

El autor atribuye una forma 3D rayada a Hydrogen High y dice que tardó menos de cinco minutos. En su prueba la compara con resultados de modelos más caros.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-46"></a>
### Caso 46: [Una ejecución visual de 89 minutos en PokéBench](https://x.com/StatsWire/status/2120923685296988296) (por [@StatsWire](https://x.com/StatsWire))

**Registra los turnos y los fallos de API además del resultado cuando pruebes un agente visual durante mucho tiempo.**

En una prueba previa al anuncio en Vertex y con nivel High, Hydrogen derrotó a Brock en 365 turnos y 89 minutos, sin fallos de API según la fuente. El resultado depende del entorno de prueba.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-47"></a>
### Caso 47: [Hydrogen y DeepSeek crean la misma escena 3D](https://x.com/AiHubMix/status/2120928687537418581) (por [@AiHubMix](https://x.com/AiHubMix))

**Anota por separado el tiempo y el coste de API al comparar los resultados visuales.**

AIHubMix usó la misma instrucción 3D con Hydrogen y DeepSeek V4.1 Flash al máximo nivel de razonamiento disponible. El proveedor informa de 3 minutos y USD 1,30 para Hydrogen frente a 100 minutos y USD 0,90 para DeepSeek.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-53"></a>
### Caso 53: [Tiempo y coste por tarea en Agent Arena](https://x.com/arena/status/2120940869889175840) (por [@arena](https://x.com/arena))

**Compara latencia, coste y tokens de salida por tarea con la tasa de éxito global.**

Agent Arena informa de una mediana de 5,3 minutos y USD 1,60 por tarea con Hydrogen High. También indica que usó más tokens de salida que Carbon y Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-54"></a>
### Caso 54: [Pruebas de documentos visuales y de terminal](https://x.com/ArtificialAnlys/status/2120941511223185722) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Consulta por separado los resultados con documentos y con la terminal para elegir el nivel de razonamiento.**

Artificial Analysis destaca los resultados en documentos visuales y mejoras desiguales en terminal. Con razonamiento adicional subió la puntuación en tareas científicas de terminal, pero la general en Terminal-Bench siguió en 54 %.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-55"></a>
### Caso 55: [Hydrogen en Vals Index y Tax Agent](https://x.com/ValsAI/status/2120943893894303808) (por [@ValsAI](https://x.com/ValsAI))

**Consulta los resultados en tareas especializadas junto con la puntuación global.**

Vals AI informó de un 68,5 % en su índice y del primer puesto en Tax Agent en el momento de la prueba.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-56"></a>
### Caso 56: [Hydrogen con ajustes predeterminados en CursorBench](https://x.com/cursor_ai/status/2120944639633211619) (por [@cursor_ai](https://x.com/cursor_ai))

**Toma una puntuación con la configuración de serie como referencia para probar tu propio repositorio.**

Cursor informa de un 54,3 % para Hydrogen con el nivel de razonamiento predeterminado y de un 39,6 % para Gemini 3.8 Flash en su prueba.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-57"></a>
### Caso 57: [Cuatro modelos animan un combate de arqueros](https://x.com/IndependentEco/status/2120945011277590733) (por [@IndependentEco](https://x.com/IndependentEco))

**Compara si se entiende con claridad lo que hace cada arquero.**

El autor muestra en paralelo las animaciones de Hydrogen, Fable 5.2, GPT-6.1 Sol y Carbon para un combate de arqueros.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-61"></a>
### Caso 61: [Hydrogen en FrontierCode de Devin](https://x.com/cognition/status/2120950876248641588) (por [@cognition](https://x.com/cognition))

**Evalúa si los parches pueden integrarse y anota el entorno de cada agente.**

Cognition informa de un 38,2 % en FrontierCode 2.0. Su entorno de prueba para Hydrogen difiere de Devin CLI, el que usó con los modelos de comparación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-64"></a>
### Caso 64: [Búsqueda web pese a una instrucción explícita](https://x.com/amanunreal/status/2120954045615768054) (por [@amanunreal](https://x.com/amanunreal))

**Comprueba que el agente no use herramientas cuando la tarea exige responder sin navegar.**

El autor afirma que Hydrogen buscó en la web pese a haberle pedido evitar búsquedas y llamadas a herramientas. La publicación muestra un caso aislado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-65"></a>
### Caso 65: [Consumo de cuota al usar Swarm en Antigravity](https://x.com/HarshithLucky3/status/2120954399971487774) (por [@HarshithLucky3](https://x.com/HarshithLucky3))

**Registra los tokens y la cuota consumida al probar una ejecución multiagente.**

El autor informa de 17 millones de tokens y del 21 % de una cuota de cinco horas al usar Swarm con su plan. Las cifras corresponden a esa sesión.

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

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-66"></a>
### Caso 66: [Uso de herramientas en tareas profesionales](https://x.com/mercor/status/2120957582139642095) (por [@mercor](https://x.com/mercor))

**Examina cómo reúne contexto un agente antes de actuar en una tarea profesional.**

Mercor informa de un 78,0 % de Pass@1 en APEX-Agents y de 93 llamadas a herramientas por tarea de media. La prueba abarca derecho, consultoría y banca.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-68"></a>
### Caso 68: [Cuatro modelos animan a un mago y un dragón](https://x.com/IndependentEco/status/2120964690906161461) (por [@IndependentEco](https://x.com/IndependentEco))

**Compara la puesta en escena, la claridad de la acción y los efectos en distintas versiones generadas.**

El vídeo compara a Hydrogen con tres modelos Claude en un enfrentamiento entre un mago y un dragón. El autor prefirió el resultado de Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-71"></a>
### Caso 71: [MazeBench muestra tasas de éxito bajas](https://x.com/patience_cave/status/2120973681937809766) (por [@patience_cave](https://x.com/patience_cave))

**Prueba problemas de laberintos antes de confiar en el razonamiento espacial de un modelo.**

Con su configuración, la comparación de MazeBench recoge un 1 % para Hydrogen, un 4 % para Sonnet 5.5 y un 8 % para GPT-6.1 Terra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-72"></a>
### Caso 72: [Tres modelos Gemini crean escenas de veleros](https://x.com/Octoberry/status/2120974412144902376) (por [@Octoberry](https://x.com/Octoberry))

**Compara el movimiento y los detalles ambientales de una escena temática en Three.js.**

El autor muestra veleros creados por Hydrogen, Argon y Carbon. Prefiere el detalle de Carbon y considera que Hydrogen se acercó a Argon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-75"></a>
### Caso 75: [Leer un dorsal agota el presupuesto de razonamiento](https://x.com/skalskip92/status/2120994631072776235) (por [@skalskip92](https://x.com/skalskip92))

**Fija un límite de razonamiento y una alternativa para leer detalles pequeños en imágenes.**

El evaluador informa de que Hydrogen XHigh usó 131 069 tokens de razonamiento y no devolvió el número del dorsal tras 9 minutos y 55 segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-12

---

<a id="case-76"></a>
### Caso 76: [Comparación de familias de modelos en ClutterBench](https://x.com/AdamHoltererer/status/2121000759118459138) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Usa una prueba con entornos saturados de elementos para ver si las fortalezas generales del modelo se mantienen.**

Según los resultados compartidos por el autor, Hydrogen encabeza los modelos Gemini mostrados, pero queda por debajo de los modelos OpenAI de la comparación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-12

---

<a id="case-78"></a>
### Caso 78: [Un busto anatómico seccionado al estilo de Minecraft](https://x.com/jan_volad/status/2121026531472339340) (por [@jan_volad](https://x.com/jan_volad))

**Comprueba si un corte generado contiene las estructuras internas solicitadas.**

El autor encargó a Hydrogen y Argon el mismo busto anatómico al estilo Minecraft en un solo intento. Dice haber distinguido el cráneo, las costillas y la columna en el resultado de Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-79"></a>
### Caso 79: [Tres modelos recrean el mismo objeto](https://x.com/luckeyfaraday/status/2121030005899825504) (por [@luckeyfaraday](https://x.com/luckeyfaraday))

**Anota por separado los tokens y la calidad cuando un modelo de menor precio pueda usar más tokens en una prueba.**

El vídeo muestra a Hydrogen, Carbon y Fable 5.2 recreando un objeto con forma de fusil. El autor informa de 3,69 millones de tokens y USD 1,62 con Hydrogen frente a 398 000 tokens y USD 0,77 con Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

Tipo: Evaluation | Fecha: 2026-11-12

---

<a id="case-80"></a>
### Caso 80: [Consumo de tokens en una prueba de inducción](https://x.com/s_batzoglou/status/2121037853258129811) (por [@s_batzoglou](https://x.com/s_batzoglou))

**Registra los totales facturados de entrada y salida junto con la puntuación de razonamiento en problemas difíciles.**

El evaluador sitúa a Hydrogen en cuarto lugar en su prueba de inducción de 100 problemas, cerca de Opus 5.5. Indica 55 millones de tokens de salida y 307 millones de entrada facturados y deja abierta la explicación del cómputo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-83"></a>
### Caso 83: [Tres modelos animan un animal en 3D](https://x.com/leo114119/status/2121054098753785915) (por [@leo114119](https://x.com/leo114119))

**Revisa la anatomía y el movimiento en una tarea común de modelado.**

La fuente muestra una comparación entre Hydrogen, GPT-6.1 Terra y Claude Haiku 5.5. El autor señala deficiencias en Hydrogen y el vídeo solo cubre esta tarea.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-84"></a>
### Caso 84: [Hydrogen y Qwen en ts-bench](https://x.com/gosrum/status/2121058334552060102) (por [@gosrum](https://x.com/gosrum))

**Revisa los fallos en las llamadas a herramientas junto con los resultados globales.**

La fuente compara Hydrogen y Qwen4 Max Preview en ts-bench y comenta la fiabilidad de las llamadas en esas ejecuciones. La captura muestra los resultados de la prueba.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-85"></a>
### Caso 85: [Simulación de negocio en Vending-Bench](https://x.com/andonlabs/status/2121061429889642497) (por [@andonlabs](https://x.com/andonlabs))

**Compara los ingresos simulados con el coste de operar al agente.**

Andon Labs indica que Hydrogen quedó tercero en Vending-Bench 2 y generó más ingresos que otros modelos de precio similar en su simulación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-89"></a>
### Caso 89: [Cuatro modelos construyen una isla en miniatura](https://x.com/xKaka1456/status/2121111495358697924) (por [@xKaka1456](https://x.com/xKaka1456))

**Compara las islas junto con el tiempo y el coste del entorno de cada ejecución.**

La fuente compara cuatro islas y reporta 4 minutos con Hydrogen, 20 con GPT-6.1 Terra, 40 con Sol y 60 con DeepSeek. Hydrogen no tuvo coste adicional en el entorno del autor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-91"></a>
### Caso 91: [Comparación de roturas de tela mediante código](https://x.com/MichaelLee009/status/2121126779276402904) (por [@MichaelLee009](https://x.com/MichaelLee009))

**Prueba la elasticidad, los desgarros y la interacción con el pelaje en una misma animación.**

El autor compara animaciones de Hydrogen y Claude Fable 5.2 generadas con código. Prefiere visualmente la segunda, sin documentar ajustes equivalentes ni aportar una validación física independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-94"></a>
### Caso 94: [Verificación de hechos con una fuente inaccesible](https://x.com/cagrimbakirci/status/2121130756684886279) (por [@cagrimbakirci](https://x.com/cagrimbakirci))

**Exige una referencia que puedas consultar antes de actuar según un veredicto.**

El autor preguntó a Hydrogen si una publicación que aparecía en una captura era verídica. Dice que el modelo la dio por correcta, abrió varias veces una herramienta de verificación y no mostró la fuente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-13

---

<a id="case-96"></a>
### Caso 96: [Hydrogen y Sol dibujan un pelícano en 2D](https://x.com/YxzRainy/status/2121148582166491164) (por [@YxzRainy](https://x.com/YxzRainy))

**Compara el tiempo y el movimiento con una misma tarea de animación sencilla.**

El vídeo muestra a Hydrogen y GPT-6.1 Sol animando un pelícano ciclista en 2D. El autor informa de 28 segundos frente a 6 minutos y 51 segundos, sin acreditar configuraciones equivalentes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-98"></a>
### Caso 98: [Cuatro modelos crean un juego de balanceo con telarañas](https://x.com/StatsWire/status/2121172215182065807) (por [@StatsWire](https://x.com/StatsWire))

**Compara el desplazamiento y los controles en juegos sujetos al mismo límite de un archivo.**

Cuatro modelos Gemini afrontan el mismo reto 3D en un HTML autónomo, sin recursos externos. Hydrogen usó Extra High y Gemini 3.8 Flash, Argon y Carbon usaron High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-100"></a>
### Caso 100: [Cuatro modelos crean un diorama arquitectónico](https://x.com/Jackson77li/status/2121172890838352306) (por [@Jackson77li](https://x.com/Jackson77li))

**Compara los resultados con el mismo encargo arquitectónico y examina la iluminación.**

Hydrogen, GPT-6.2, Claude Fable 5.2 y DeepSeek realizaron el mismo diorama según el autor. Su clasificación y sus comentarios de velocidad son subjetivos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-103"></a>
### Caso 103: [Tres modelos renderizan una escena de tren](https://x.com/xKaka1456/status/2121193705810104515) (por [@xKaka1456](https://x.com/xKaka1456))

**Usa la misma escena de tren para comparar los tiempos de las configuraciones elegidas.**

El autor informa de unos 3 minutos con Hydrogen, 20 con GPT-6.1 Terra y 68 con Qwen4 Max Preview. El vídeo muestra los resultados, sin documentar ajustes ni iteraciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-104"></a>
### Caso 104: [Un Chinatown lluvioso con razonamiento Extra](https://x.com/qingzhoucloud/status/2121198911515967952) (por [@qingzhoucloud](https://x.com/qingzhoucloud))

**Mide el tiempo y revisa la escena final antes de elegir el nivel de razonamiento de una animación grande.**

El autor usó Hydrogen Extra y atribuye la instrucción a otro creador. Indica que el MP4 tardó casi cuatro horas y lo compara con una ejecución de Claude Fable 5.2 en condiciones poco comparables.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-106"></a>
### Caso 106: [Tres modelos crean un visualizador de planetas](https://x.com/Stargridcompass/status/2121208957276713181) (por [@Stargridcompass](https://x.com/Stargridcompass))

**Compara una interfaz científica visual con la misma instrucción en distintos modelos.**

El vídeo muestra a Claude Fable 5.2, GPT-6.2 Sol y Hydrogen. El orden que propone el autor se basa en su valoración visual, sin ajustes equivalentes ni una puntuación objetiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-107"></a>
### Caso 107: [Cuatro modelos recrean Chrome Dino](https://x.com/noclipepe/status/2121219775170761044) (por [@noclipepe](https://x.com/noclipepe))

**Cronometra las recreaciones de un juego conocido y compara los resultados jugables.**

Según el autor, Hydrogen tardó 18 minutos y 41 segundos en AI Studio y Fable 5.2, 45 minutos y 30 segundos. El vídeo también muestra Qwen4-Max-Preview, Carbon y puntuaciones visuales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-109"></a>
### Caso 109: [Dos agentes de código construyen barcos distintos](https://x.com/marcthecreatorr/status/2121221667619852660) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Compara el primer resultado utilizable y el coste de revisarlo en el entorno elegido.**

Se usó la misma instrucción, con Sonnet en Claude Code y Hydrogen en Cursor. El autor indica que Hydrogen tardó menos, pero necesitó una segunda versión.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-111"></a>
### Caso 111: [Cuatro modelos simulan un asedio con trabuquete](https://x.com/StatsWire/status/2121226579141386285) (por [@StatsWire](https://x.com/StatsWire))

**Compara prototipos de física jugables con un reto común y registra sus niveles de razonamiento.**

La escena usa cientos de bloques de piedra. El autor informa de 10 minutos y 3 segundos con Hydrogen Extra High y 23 minutos y 33 segundos con Carbon High. Gemini 3.8 Flash High fue el más rápido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-116"></a>
### Caso 116: [Memoria persistente en FrontierMemory](https://x.com/Letta_AI/status/2121255895745351874) (por [@Letta_AI](https://x.com/Letta_AI))

**Compara puntuación y coste por ejecución al elegir un modelo para la memoria del agente.**

Letta informa de un 64,4 % con Hydrogen, igual que Argon, y unos USD 100 por ejecución. Carbon obtuvo un 71,1 % con unos USD 94 en esa configuración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-117"></a>
### Caso 117: [Hydrogen en un agente de voz de LiveKit averiado](https://x.com/livekit/status/2121256982023672076) (por [@livekit](https://x.com/livekit))

**Provoca un fallo controlado de herramientas y comprueba si el agente afirma resultados sin respaldo.**

LiveKit prueba Hydrogen en un agente de voz averiado a propósito y declara cero informes falsos. El proveedor compara con Gemini 3.8 Flash y enlaza su informe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-123"></a>
### Caso 123: [Tres modelos Gemini animan a un ciclista](https://x.com/AI_Screening/status/2121281026916057443) (por [@AI_Screening](https://x.com/AI_Screening))

**Compara escenas breves de movimiento con el mismo encargo y registra los tiempos.**

El autor muestra a Carbon, Argon y Hydrogen animando un ciclista. Informa de unos 90 segundos con Hydrogen y más de cinco minutos con Argon. Prefiere la versión de Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-126"></a>
### Caso 126: [Dos modelos construyen un mundo LEGO](https://x.com/kepochnik/status/2121286219669836027) (por [@kepochnik](https://x.com/kepochnik))

**Compara cuánto logra construir cada modelo en el tiempo que emplea.**

El autor comparte las versiones de Fable 5.2 y Hydrogen de un mundo LEGO. Indica 44 y 28 minutos, respectivamente, en sus propias ejecuciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-127"></a>
### Caso 127: [Reparación de fallos reintroducidos en dos repositorios](https://x.com/PawelHuryn/status/2121286545223086302) (por [@PawelHuryn](https://x.com/PawelHuryn))

**Introduce defectos conocidos para medir qué puede detectar y reparar un agente.**

El evaluador reintrodujo 105 fallos en dos repositorios. En ese entorno, Hydrogen Extra High quedó justo detrás de Sonnet 5.5 Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-128"></a>
### Caso 128: [Un muñeco de palitos contra el cursor](https://x.com/DanielZambrini/status/2121289822677483740) (por [@DanielZambrini](https://x.com/DanielZambrini))

**Compara cómo responde cada animación interactiva al puntero.**

El autor prefirió el resultado de Fable, aunque valoró Hydrogen como una opción adecuada para una pasada de menor coste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-130"></a>
### Caso 130: [Dos modelos renderizan un paisaje montañoso](https://x.com/ZryMiller/status/2121295750122594440) (por [@ZryMiller](https://x.com/ZryMiller))

**Compara por separado la composición, el tiempo de generación y el coste de una animación de paisaje.**

El autor muestra una montaña animada con Hydrogen y Opus 5.5. Indica 20 minutos y 30 segundos y USD 0,50 con Hydrogen, frente a 11 minutos y 23 segundos y USD 2,50 con Opus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-131"></a>
### Caso 131: [Traducción del inglés al persa con un entorno propio](https://x.com/MatinSenPai/status/2121296733258887365) (por [@MatinSenPai](https://x.com/MatinSenPai))

**Evalúa un texto difícil comparándolo con una traducción humana de referencia.**

El autor dio a Hydrogen 94 sobre 100 en una tarea personal con un entorno propio. Las notas son subjetivas y dependen de esa configuración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-133"></a>
### Caso 133: [Cuatro modelos crean un barco que se hunde](https://x.com/remoteugur/status/2121302956741902451) (por [@remoteugur](https://x.com/remoteugur))

**Mide por separado la fidelidad visual, el tiempo y el coste en la misma escena.**

El autor informa de 8,6 minutos y USD 1,16 con Hydrogen frente a 10,8 minutos y USD 1,06 con Gemini 3.8 Flash. También probó Carbon y Opus 5.5 y prefirió el realismo de Opus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-135"></a>
### Caso 135: [Comparación a ciegas de cuatro modelos de redacción](https://x.com/quintanilha/status/2121315967447757299) (por [@quintanilha](https://x.com/quintanilha))

**Oculta los nombres de los modelos antes de elegir qué texto usar.**

El autor prefirió el resultado de Hydrogen en una prueba a ciegas de redacción con cuatro modelos. También lo encontró más rápido y barato que Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-136"></a>
### Caso 136: [Detección y lectura visual por nivel de razonamiento](https://x.com/skalskip92/status/2121322414453694489) (por [@skalskip92](https://x.com/skalskip92))

**Mide por separado la precisión de detección y lectura, el coste y la latencia en cada nivel.**

El evaluador separa detección y lectura para Hydrogen, Argon y Carbon. Hydrogen High promedió 29,3 segundos por imagen con 64,6 en detección y 87,2 en lectura. Carbon High puntuó más en ambas con mayor coste y latencia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-13

---

<a id="case-137"></a>
### Caso 137: [Cuatro modelos recrean la casa de Up](https://x.com/noclipepe/status/2121326233044537688) (por [@noclipepe](https://x.com/noclipepe))

**Usa la misma referencia y el mismo encargo para comparar las diferencias de construcción 3D.**

El autor dice que Hydrogen fue el más rápido y barato de los cuatro. Prefirió el resultado de Fable. Los ajustes y costes son los declarados en la fuente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

Tipo: Evaluation | Fecha: 2026-11-13

---

<a id="case-144"></a>
### Caso 144: [Un baile con cámara fija](https://x.com/notoro_ai/status/2121427503952834562) (por [@notoro_ai](https://x.com/notoro_ai))

**Comprueba si la animación conserva el diseño del personaje, la composición y el encuadre de referencia.**

El autor comparte una instrucción en japonés y un baile asociado a Hydrogen en Gemini. La instrucción exige cámara fija y conservar el estilo. La fuente no identifica el modelo de vídeo subyacente.

**Instrucción:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-145"></a>
### Caso 145: [Un agente de código se atasca en la prueba de referencia](https://x.com/Its_lakshya_ai/status/2121431788266659919) (por [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**Fija un límite de tiempo para la prueba inicial y comprueba el progreso antes de esperar una corrección.**

El autor muestra una sesión de Antigravity en la que Hydrogen seguía ejecutando una prueba tras una espera larga. La captura registra una petición de detenerla e investigar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-14

---

<a id="case-147"></a>
### Caso 147: [Dos modelos crean un brazo robótico interactivo](https://x.com/gmi_cloud/status/2121467337119588834) (por [@gmi_cloud](https://x.com/gmi_cloud))

**Comprueba si las articulaciones del brazo Three.js responden de forma coherente a las acciones del usuario.**

GMI Cloud compara Hydrogen con Sonnet 5.5 en un brazo interactivo en Three.js. El proveedor prefirió Sonnet y muestra ambos resultados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-151"></a>
### Caso 151: [Hydrogen y Sol construyen un pueblo nevado](https://x.com/badboyfoxy/status/2121501015442669866) (por [@badboyfoxy](https://x.com/badboyfoxy))

**Mide por separado el tiempo, el coste y la calidad de la escena.**

El autor informa de tres minutos y USD 1,37 con Hydrogen High frente a 15 minutos y USD 4,03 con Sol High. Prefirió el resultado creativo de Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-152"></a>
### Caso 152: [Una isla en Three.js con niveles High y Ultra](https://x.com/laopai1990/status/2121502334866096160) (por [@laopai1990](https://x.com/laopai1990))

**Compara el aspecto y el tiempo con los niveles de razonamiento a la vista, sin equiparar cuotas de productos distintos.**

El autor compara Hydrogen High con GPT-6.1 Sol Ultra e indica unos 90 segundos frente a 30 minutos. Los costes son estimados y los niveles de razonamiento difieren.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-157"></a>
### Caso 157: [Comparación de detalles de un mando PS5 en 3D](https://x.com/Stargridcompass/status/2121528563254043015) (por [@Stargridcompass](https://x.com/Stargridcompass))

**Inspecciona el sombreado de los botones y los elementos traseros al comparar los mandos.**

El autor informa de unos tres minutos con Hydrogen High y once con GPT-6.2 Sol. Encontró controles laterales y traseros más completos en Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-159"></a>
### Caso 159: [CursorBench con distintos presupuestos de razonamiento](https://x.com/Beamsters1/status/2121538515909628111) (por [@Beamsters1](https://x.com/Beamsters1))

**Compara las tasas de éxito por nivel antes de elegir una configuración rápida.**

El autor observó un aumento marcado en CursorBench 4.0 al elevar el presupuesto de razonamiento de Hydrogen. El resultado se limita a los ajustes probados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-14

---

<a id="case-160"></a>
### Caso 160: [Tres modelos renderizan un templo estelar](https://x.com/YxzRainy/status/2121551796766376081) (por [@YxzRainy](https://x.com/YxzRainy))

**Evalúa la estabilidad del renderizado por separado del detalle visual.**

El autor compara Hydrogen, DeepSeek V4.1 1017 y Qwen4 Max Preview en una escena 3D. Describe a Hydrogen como más rápido y sin pantallas negras ni parpadeo en esa prueba, aunque con menos detalle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-162"></a>
### Caso 162: [Revisión de un plan de migración existente](https://x.com/is_llll/status/2121565725072490559) (por [@is_llll](https://x.com/is_llll))

**Pide a los agentes que evalúen si la migración exige sustituir la arquitectura actual.**

En la revisión del autor, Hydrogen y Argon respaldaron el diseño existente. Claude Opus propuso sustituirlo y migrar antes. Es una valoración de un proyecto concreto.

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

Tipo: Limit | Fecha: 2026-11-14

---

<a id="case-165"></a>
### Caso 165: [Dos modelos interpretan un juego de fuga de un templo](https://x.com/runable_hq/status/2121596515474964556) (por [@runable_hq](https://x.com/runable_hq))

**Compara si la iluminación y el ambiente permiten leer bien el mismo concepto de juego.**

Runable muestra las versiones de Hydrogen y Argon. El proveedor describe la luz de Hydrogen como más sombría y la de Argon como más luminosa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-166"></a>
### Caso 166: [Tres modelos Gemini animan un buggy de rally](https://x.com/teddyaisi/status/2121604816380010719) (por [@teddyaisi](https://x.com/teddyaisi))

**Comprueba si la suspensión y el agarre de las ruedas son coherentes al tomar una curva peraltada.**

El autor compara Carbon, Argon y Hydrogen sobre un buggy en Three.js en una cantera. La prueba pide que se comprima la suspensión y que el vehículo derrape sobre tierra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-169"></a>
### Caso 169: [Dos modelos animan Chasing Views](https://x.com/VulKan42069/status/2121625271493382166) (por [@VulKan42069](https://x.com/VulKan42069))

**Compara el resultado y el tiempo teniendo en cuenta el nivel de razonamiento de cada modelo.**

El autor muestra Chasing Views con Hydrogen Extra High y Opus 5.5 High. Reporta 22 y 18 minutos, respectivamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-170"></a>
### Caso 170: [Velocidad y coste en Design Creativity Bench](https://x.com/Kombaico/status/2121635837180031129) (por [@Kombaico](https://x.com/Kombaico))

**Compara el tiempo y el coste por diseño junto con la puntuación de creatividad.**

El responsable informa de 49,4 puntos para Hydrogen y medianas de 3,4 minutos y USD 0,39 por diseño. En esa prueba Argon fue más lento y barato, y Carbon más lento y caro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

Tipo: Benchmark | Fecha: 2026-11-14

---

<a id="case-172"></a>
### Caso 172: [Cuatro modelos animan un galope en el desierto](https://x.com/Marlenuii/status/2121664345818235177) (por [@Marlenuii](https://x.com/Marlenuii))

**Compara el apoyo de los cascos y los cambios de peso antes de juzgar la luz o la malla.**

El autor comparó a Astra, Carbon, Fable 5.2 y Hydrogen con un caballo al galope. Prefirió la zancada de Astra y criticó la construcción del caballo de Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-174"></a>
### Caso 174: [Investigación informática en FrontierCS 2](https://x.com/wenhaocha1/status/2121679887400403308) (por [@wenhaocha1](https://x.com/wenhaocha1))

**Usa una prueba de investigación junto a las pruebas de programación y anota el entorno.**

La fuente indica que Hydrogen quedó séptimo por tasa de éxito en FrontierCS 2 con Antigravity. La prueba aborda problemas de investigación informática.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

Tipo: Benchmark | Fecha: 2026-11-14

---

<a id="case-175"></a>
### Caso 175: [Cuatro modelos en Rio Above the Clouds](https://x.com/EnvolDev/status/2121701704139956250) (por [@EnvolDev](https://x.com/EnvolDev))

**Compara coste, tiempo y calidad percibida con un encargo creativo común.**

El evaluador dice que Hydrogen Extra High costó USD 6,21 y fue su resultado menos preferido. Astra tardó menos en esta prueba. La fuente no confirma generación de vídeo nativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-176"></a>
### Caso 176: [Hydrogen en las tareas técnicas de GBENCH](https://x.com/leo_linsky/status/2121710421891780864) (por [@leo_linsky](https://x.com/leo_linsky))

**Usa resultados verificables de código y de otras tareas para valorar el rendimiento junto al precio y el tiempo.**

GBENCH comunica resultados de Hydrogen que incluyen diseño de circuitos y razonamiento abstracto. En su medición Sol fue más competitivo con precio y velocidad parecidos.

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

Tipo: Benchmark | Fecha: 2026-11-14

---

<a id="case-177"></a>
### Caso 177: [Entrenar coches para aparcar en paralelo](https://x.com/noclipepe/status/2121734795738652934) (por [@noclipepe](https://x.com/noclipepe))

**Compara el progreso del aprendizaje y la tasa final de éxito en simulaciones generadas.**

Con el mismo encargo, el autor informa de 5 de 44 coches aparcados con Hydrogen frente a 26 de 40 con Fable 5.2. Las ejecuciones tardaron 5,6 y 24 minutos, respectivamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

Tipo: Evaluation | Fecha: 2026-11-14

---

<a id="case-181"></a>
### Caso 181: [Hydrogen en Terminal-Bench 4.0](https://x.com/gosrum/status/2121785156273160558) (por [@gosrum](https://x.com/gosrum))

**Considera tanto las tareas completadas como su coste al elegir un modelo para la terminal.**

La prueba independiente de Terminal-Bench 4.0 compara Hydrogen, Claude Opus 5.5 y GPT-6.1 Sol. El evaluador describe puntuaciones similares, un coste de Hydrogen entre los otros dos y diferencias de madurez entre entornos.

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

Tipo: Benchmark | Fecha: 2026-11-15

---

<a id="case-183"></a>
### Caso 183: [Tres modelos Gemini animan un pulpo](https://x.com/teddyaisi/status/2121800606406885880) (por [@teddyaisi](https://x.com/teddyaisi))

**Observa si el contacto con la roca impulsa visiblemente el cuerpo cuando el pulpo se agarra.**

El autor muestra a Carbon, Argon y Hydrogen resolviendo el mismo reto en Three.js. Pide comparar cómo el agarre del tentáculo al borde del arrecife se traduce en avance.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-187"></a>
### Caso 187: [Una prueba de modelado de castillos](https://x.com/nemumusitocha/status/2121848375998063012) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Compara los castillos y los recursos consumidos en distintas ejecuciones.**

El autor muestra un castillo 3D con Hydrogen y enlaza pruebas con modelos anteriores. El 3 % de cuota semanal de Google AI Pro corresponde a esa ejecución.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-191"></a>
### Caso 191: [La estimación de un proyecto cambia al ampliar el alcance](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (por [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Pide que se expliquen el alcance y los supuestos cuando cambie mucho el plazo previsto.**

El autor comparte una conversación en la que un mes pasó a un año al pedir un plazo realista con todas las funciones. El intercambio no establece la duración efectiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-15

---

<a id="case-193"></a>
### Caso 193: [Una pregunta de calendario que incluye los años bisiestos](https://x.com/itsvishaltwt/status/2121891117050589249) (por [@itsvishaltwt](https://x.com/itsvishaltwt))

**Usa una conversión sencilla para comprobar si la respuesta contempla casos especiales del calendario.**

El autor preguntó a Hydrogen High y GPT cuántos segundos tiene un año. Ambas capturas dan resultados para años comunes y bisiestos, y Hydrogen también calcula la media del calendario gregoriano.

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

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-196"></a>
### Caso 196: [Límites de suscripción obsoletos en una respuesta](https://x.com/take14262/status/2121934737539514533) (por [@take14262](https://x.com/take14262))

**Verifica los términos vigentes y el nombre del modelo en fuentes primarias al evaluar un asistente de investigación.**

El autor muestra a Hydrogen confundiendo nombres parecidos y dando detalles desactualizados sobre la ventana de un plan de Qwen. Las capturas documentan esos posibles errores.

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

Tipo: Limit | Fecha: 2026-11-15

---

<a id="case-197"></a>
### Caso 197: [Replantear la historia de una animación WebGL](https://x.com/snakajima/status/2121939899242996058) (por [@snakajima](https://x.com/snakajima))

**Pide una narrativa más clara cuando una primera versión elaborada no tenga progresión.**

El autor enlaza la primera versión y muestra una segunda tras comentar el ruido visual y la falta de historia. Prefirió la revisión, pero siguió prefiriendo su prueba con Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

Tipo: Limit | Fecha: 2026-11-15

---

<a id="case-199"></a>
### Caso 199: [Dos modelos programan un combate de dragones](https://x.com/DrstaOne/status/2121947540509831302) (por [@DrstaOne](https://x.com/DrstaOne))

**Compara cómo la animación de cada modelo coordina dos personajes que interactúan.**

El autor muestra a Qwen-4 Max y Hydrogen creando con código un combate sobre un templo de montaña. La fuente acredita a otra persona por la instrucción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-201"></a>
### Caso 201: [Una instrucción reproducible para animar un pelícano en Three.js](https://x.com/Aki_LIG/status/2121960943361896596) (por [@Aki_LIG](https://x.com/Aki_LIG))

**Comprueba si las patas, las ruedas y la dirección se mueven coordinadamente.**

El autor publica la instrucción completa en japonés y muestra el resultado de Hydrogen en una carretera costera. Dice que ya dio la misma instrucción a GPT-6.1 Terra. El vídeo asociado muestra Hydrogen.

**Instrucción:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-205"></a>
### Caso 205: [Una instrucción sobre una casa rural en tres plataformas](https://x.com/doe_naps/status/2121999317628330476) (por [@doe_naps](https://x.com/doe_naps))

**Comprueba el formato de salida al mover una tarea visual entre configuraciones y plataformas.**

El autor obtuvo imágenes fijas con Hydrogen High en Antigravity, Hydrogen Extra High en AI Studio y Carbon High en Antigravity. Una ejecución etiquetada Hydrogen en Arena produjo SVG animado, sin identificar de forma independiente ese checkpoint.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-206"></a>
### Caso 206: [Dos paneles con la misma instrucción](https://x.com/fiapp_pro/status/2122014257667846338) (por [@fiapp_pro](https://x.com/fiapp_pro))

**Compara la disposición y jerarquía informativa a partir del mismo encargo de interfaz.**

El autor muestra capturas atribuidas a GPT-6.1 Sol y Hydrogen. Permiten comparar el aspecto, pero no muestran el funcionamiento, la implementación ni los ajustes.

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

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-209"></a>
### Caso 209: [Dos modelos animan una escena de desplazamiento lateral](https://x.com/rubenssoto_ai/status/2122035198728814753) (por [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Compara la continuidad del movimiento y el coste de creación de una escena de acción.**

El autor compara Hydrogen y GPT-6 Astra en una animación lateral. Prefiere el movimiento natural de Hydrogen y declara un coste menor en estas dos ejecuciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

Tipo: Evaluation | Fecha: 2026-11-15

---

<a id="case-212"></a>
### Caso 212: [Fórmulas sin renderizar en una respuesta en japonés](https://x.com/ToraMutton/status/2122131489718759930) (por [@ToraMutton](https://x.com/ToraMutton))

**Comprueba la presentación y la exactitud cuando la respuesta contenga comandos TeX.**

El autor muestra una respuesta de Gemini con notación cruda en vez de ecuaciones compuestas tras cambiar a Hydrogen. La captura ilustra un fallo de formato en su interfaz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

Tipo: Limit | Fecha: 2026-11-16

---

<a id="case-214"></a>
### Caso 214: [Prueba de una instrucción de guardar silencio](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (por [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Comprueba si el modelo puede abstenerse de responder cuando el flujo lo exija.**

El autor publica una captura de una prueba sin respuesta y refiere comportamientos distintos en Carbon y Argon. La fuente muestra un solo grupo de ensayos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

Tipo: Evaluation | Fecha: 2026-11-16

---

<a id="case-216"></a>
### Caso 216: [Tres modelos explican un motor eléctrico](https://x.com/analogalok/status/2122221106304352257) (por [@analogalok](https://x.com/analogalok))

**Compara la claridad visual y los controles didácticos con un mismo encargo de simulación.**

El autor probó Hydrogen y dos modelos Qwen y prefirió el motor 3D y las explicaciones físicas de Hydrogen. Es la valoración de una prueba.

**Instrucción:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

Tipo: Evaluation | Fecha: 2026-11-16

---

<a id="case-217"></a>
### Caso 217: [Dos flujos animan una escena de escritorio](https://x.com/GeroXBT/status/2122234332102435128) (por [@GeroXBT](https://x.com/GeroXBT))

**Comprueba los detalles, el volumen y la pausa final frente al encargo original.**

El autor compara animaciones asistidas por Hydrogen y Astra con la misma instrucción y acceso por API. Describe la versión de Gemini como más fluida, con sonido más bajo y movimiento al final. El sistema de renderizado no se especifica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

Tipo: Evaluation | Fecha: 2026-11-16

---

<a id="case-221"></a>
### Caso 221: [Un pueblo 2D con sonido procedural](https://x.com/marcthecreatorr/status/2122266495216459841) (por [@marcthecreatorr](https://x.com/marcthecreatorr))

**Comprueba si el sonido cambia con lo que ocurre en pantalla y anota el tiempo de creación.**

El autor comparó Qwen 4 Max y Hydrogen con nivel Extra High. Informa de unos 75 minutos y USD 0,90 con Qwen y 12 minutos y USD 1,70 con Hydrogen. Prefirió cómo este último acompasó la música a la acción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[Reproducir vídeo original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

Tipo: Evaluation | Fecha: 2026-11-16

---

<a id="related-repositories"></a>
## Repositorios relacionados

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Ejemplos y comparaciones de Gemini 4 Carbon

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Gracias a los creadores, desarrolladores y evaluadores que compartieron públicamente su trabajo con Hydrogen.

**Creadores de las fuentes:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*La atribución sigue las fuentes públicas citadas y puede no identificar al creador original. Para solicitar correcciones o retiradas, abre una incidencia con una fuente pública.*

Propón un ejemplo respaldado por fuentes mediante una incidencia o una solicitud de incorporación de cambios, siguiendo la lista de contribución.
