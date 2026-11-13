<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API](https://img.shields.io/badge/Gemini_Native_API-Quick_Start-f22f3d)](https://evolink.ai/docs/es/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=docs_link)

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

**40 ejemplos seleccionados muestran qué crearon sus autores, cómo trabajaron y dónde los resultados no cumplieron las expectativas.**

Cada caso enlaza su fuente y reconoce a su autor. Las notas identifican demostraciones, ejemplos del proveedor y comparaciones de creadores; no se reconstruyen las instrucciones que faltan.

## 📊 Resumen

- 40 casos seleccionados entre 75 publicaciones de demostraciones revisadas en una colección de X limitada a 500 publicaciones, recopilada el 13 de noviembre de 2026.
- Cinco categorías abarcan agentes, aprendizaje y aplicaciones, hojas de cálculo y Search, 3D interactivo, y comparaciones y limitaciones.
- Se conservan los 41 recursos visuales seleccionados: 38 vídeos reproducibles con imágenes de portada y 3 imágenes.
- Gemini 4 Hydrogen se anunció el 12 de noviembre de 2026. Explora el modelo y sus opciones actuales de acceso en EvoLink.

> [!NOTE]
> La atribución del modelo, los costes, los tiempos y los resultados son afirmaciones de las fuentes salvo indicación contraria. Los vídeos se revisaron mediante fotogramas muestreados, no mediante pruebas funcionales completas. Las grabaciones de aplicaciones programadas no demuestran generación nativa de vídeo. Las diferencias de entornos de ejecución, niveles de razonamiento o número de iteraciones impiden considerar controladas las comparaciones.

**Referencias oficiales: [Anuncio de Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Ficha del modelo de Google DeepMind](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**Empieza aquí: [Explora Hydrogen en EvoLink](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [Obtén una clave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)**

<a id="quick-start"></a>
## ⚡ Inicio rápido

Empieza en EvoLink y utiliza después la API nativa de Gemini cuando quieras integrar Hydrogen en una aplicación.

1. [Ver Gemini 4 Hydrogen en el navegador](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [Crea o administra una clave de API de EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=api_key)

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

[Lee la guía de inicio rápido de la API nativa de Gemini](https://evolink.ai/docs/es/api-manual/language-series/gemini/native-api/native-api-quickstart?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=first_run)

> [!TIP]
> Lee el texto generado en los campos candidates[].content.parts[].text de la respuesta.

> [!IMPORTANT]
> Guarda tu clave de API en una variable de entorno y nunca la incluyas en un commit. Consulta la documentación de la API para conocer las opciones de transmisión, razonamiento y otras solicitudes.

## 📑 Menú

| Sección | Casos |
|---|---|
| [⚡ Agentes y flujos de programación](#agents) | 5 |
| [💻 Aplicaciones y aprendizaje](#apps-learning) | 5 |
| [📊 Hojas de cálculo y Search](#data-search) | 4 |
| [🎮 3D interactivo e interfaces](#interactive-3d) | 9 |
| [🧪 Comparaciones y limitaciones](#comparisons-limits) | 17 |
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

<a id="related-repositories"></a>
## Repositorios relacionados

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Ejemplos y comparaciones de Gemini 4 Carbon

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Gracias a los creadores, desarrolladores y evaluadores que compartieron públicamente su trabajo con Hydrogen.

**Creadores de las fuentes:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening)

*La atribución sigue las fuentes públicas citadas y puede no identificar al creador original. Para solicitar correcciones o retiradas, abre una incidencia con una fuente pública.*

Propón un ejemplo respaldado por fuentes mediante una incidencia o una solicitud de incorporación de cambios, siguiendo la lista de contribución.
