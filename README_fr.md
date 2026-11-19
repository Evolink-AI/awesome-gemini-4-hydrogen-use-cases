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

# Guide et cas d’usage remarquables de Gemini 4 Hydrogen

## 🍌 Introduction

Découvrez Gemini 4 Hydrogen à travers des applications étayées par des sources, des méthodes de programmation et des comparaisons pratiques.

**225 exemples montrent comment Hydrogen est utilisé et où les résultats atteignent leurs limites.**

Chaque cas renvoie à sa source et cite son auteur. Les démonstrations, exemples de fournisseurs et comparaisons de créateurs sont signalés dans les notes ; les consignes manquantes ne sont pas reconstituées.

## 📊 Vue d’ensemble

- 225 cas au total  dont 185 ajoutés le 17 novembre après examen de 1 304 publications X. Les nouvelles sources avaient plus de 30 mentions J’aime lors de la collecte.
- Cinq catégories couvrent les agents, les applications et l’apprentissage, les tableurs et la recherche, la 3D interactive, ainsi que les comparaisons et limites.
- 264 visuels originaux, dont 168 vidéos avec image d’aperçu et 96 images.
- Gemini 4 Hydrogen a été annoncé le 12 novembre 2026. Découvrez le modèle et ses modalités d’accès actuelles sur EvoLink.

> [!NOTE]
> L’attribution au modèle, les coûts, les durées et les résultats restent des affirmations des sources, sauf indication contraire. L’examen vidéo repose sur des images échantillonnées, pas sur des tests fonctionnels complets. Les enregistrements d’applications programmées ne prouvent pas une génération vidéo native. Des environnements d’exécution, niveaux de raisonnement ou nombres d’itérations différents empêchent des comparaisons contrôlées.

**Références officielles: [Annonce de Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Fiche du modèle de Google DeepMind](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**Commencer ici: [Découvrir Hydrogen sur EvoLink](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [Obtenir une clé API (depuis la page du modèle)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)**

<a id="quick-start"></a>
## ⚡ Démarrage rapide

Commencez sur EvoLink, puis utilisez l’API native Gemini pour intégrer Hydrogen dans une application.

1. [Voir Gemini 4 Hydrogen dans votre navigateur](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [Créer ou gérer une clé API EvoLink (depuis la page du modèle)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)

Requête minimale à l’API native

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

[Lire le guide de démarrage rapide de l’API native Gemini (depuis la page du modèle)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

> [!TIP]
> Lisez le texte généré dans les champs candidates[].content.parts[].text de la réponse.

> [!IMPORTANT]
> Conservez votre clé API dans une variable d’environnement et ne l’ajoutez jamais à un commit. Consultez la documentation API pour la diffusion en continu, le raisonnement et les autres options de requête.

## 📑 Menu

| Section | Cas |
|---|---|
| [⚡ Agents et méthodes de programmation](#agents) | 30 |
| [💻 Applications et apprentissage](#apps-learning) | 37 |
| [📊 Tableurs et recherche](#data-search) | 9 |
| [🎮 3D interactive et interfaces](#interactive-3d) | 48 |
| [🧪 Comparaisons et limites](#comparisons-limits) | 101 |
| [Dépôts associés](#related-repositories) |  |
| [Démarrage rapide](#quick-start) |  |
| [Remerciements](#acknowledge) |  |

| Cas | Catégorie | À essayer | Type |
|---|---|---|---|
| [Maintenance d’une base de code dans Antigravity](#case-1) | Agents et méthodes de programmation | Utilisez une tâche de maintenance délimitée pour évaluer ensemble modifications, usage des outils et vérification. | Demo |
| [Seize applications Canvas en parallèle](#case-2) | Agents et méthodes de programmation | Découpez une réalisation en modules indépendants et explicitez les rôles de planification, d’implémentation et d’assurance qualité. | Demo |
| [Un papillon écarlate avec un essaim multimodèle](#case-3) | Agents et méthodes de programmation | Séparez orchestration et implémentation dans un projet interactif de code créatif. | Demo |
| [Inspection et réparation avec 3D Medic](#case-4) | Agents et méthodes de programmation | Explorez un agent qui inspecte un fichier 3D, détecte les erreurs et propose des réparations avant l’exportation. | Demo |
| [Une scène de voilier créée dans Devin](#case-5) | Agents et méthodes de programmation | Évaluez un modèle dans l’environnement d’agent de programmation que vous comptez réellement utiliser. | Demo |
| [Pratique des langues avec Lingo City](#case-6) | Applications et apprentissage | Associez des fiches de révision à une rue interactive pour pratiquer une langue en contexte. | Demo |
| [Roméo et Juliette dans un théâtre de papier 3D](#case-7) | Applications et apprentissage | Transformez une leçon précise en scène interactive avec un objectif pédagogique clair. | Demo |
| [D’une maquette visuelle à un site de lecture](#case-8) | Applications et apprentissage | Utilisez une maquette de référence pour évaluer la compréhension visuelle et une interface fonctionnelle. | Demo |
| [Un jardin de carpes koï en vingt modules](#case-9) | Applications et apprentissage | Construisez une grande scène par petits modules plutôt que d’attendre un résultat complet avec une seule consigne. | Demo |
| [Un jeu pédagogique sur la fusion des protons](#case-10) | Applications et apprentissage | Prototypez une explication interactive d’un processus scientifique, puis vérifiez la science sous-jacente. | Demo |
| [Un paysage animé dans Google Sheets](#case-11) | Tableurs et recherche | Utilisez une animation de tableur inhabituelle pour examiner le code généré et les mises à jour cellule par cellule. | Demo |
| [Un site de données interactif de style Folio](#case-12) | Tableurs et recherche | Associez une page d’accueil à des visualisations de données interactives dans un petit prototype web. | Demo |
| [Réponses visuelles aux recherches à plusieurs volets](#case-13) | Tableurs et recherche | Comparez la présentation des réponses et les liens cités pour une recherche nuancée à plusieurs contraintes. | Demo |
| [Prévisions financières interactives dans Sheets](#case-14) | Tableurs et recherche | Prototypez un modèle financier avec des hypothèses visibles et examinez les formules et graphiques générés. | Demo |
| [Une salle à manger interactive](#case-15) | 3D interactive et interfaces | Vérifiez les interactions avec les objets, l’éclairage et les changements d’état plutôt que de juger une scène sur une image fixe. | Demo |
| [Un curseur de volume avec un monde miniature](#case-16) | 3D interactive et interfaces | Utilisez une commande familière pour tester à la fois la conception des interactions et les détails animés. | Demo |
| [Une maison japonaise dans Three.js](#case-17) | 3D interactive et interfaces | Distinguez génération du code et temps de rendu pour évaluer une visite 3D détaillée. | Demo |
| [Un pélican à vélo en 3D](#case-18) | 3D interactive et interfaces | Utilisez un personnage mobile pour examiner coordination, mouvement et cohérence de la scène. | Demo |
| [Un simulateur planétaire avec planification préalable](#case-19) | 3D interactive et interfaces | Donnez au modèle de programmation un plan concret avant de lui demander de modifier une scène complexe. | Demo |
| [Une île portuaire avec Antigravity Swarm](#case-20) | 3D interactive et interfaces | Utilisez un petit environnement navigable pour examiner la construction de scènes par plusieurs agents. | Demo |
| [Une île flottante avec la tour Eiffel](#case-21) | 3D interactive et interfaces | Évaluez composition, mouvement de caméra et code généré sur une scène compacte de monument. | Demo |
| [Une ville futuriste à survoler](#case-22) | 3D interactive et interfaces | Testez les modifications ultérieures d’un monde procédural plutôt que de supposer le premier résultat définitif. | Demo |
| [Un hydravion du lever du soleil à la nuit](#case-23) | 3D interactive et interfaces | Examinez les commandes d’environnement et les transitions lumineuses dans une scène 3D interactive. | Demo |
| [Animation de bonhommes néon : Hydrogen et Opus](#case-24) | Comparaisons et limites | Comparez l’animation finale, les durées et les coûts annoncés sans supposer des environnements d’exécution identiques. | Evaluation |
| [Tâches robotiques et erreurs autodéclarées](#case-25) | Comparaisons et limites | Intégrez la réussite des tâches et la reconnaissance de petites erreurs dans une évaluation robotique. | Evaluation |
| [Une cellule de laboratoire commandée en langage naturel](#case-26) | Comparaisons et limites | Évaluez l’exécution des outils et la gestion des échecs séparément des scores principaux des tests. | Evaluation |
| [Iceberg et remorqueur : Hydrogen et Carbon](#case-27) | Comparaisons et limites | Consignez le niveau de raisonnement et les restrictions de l’environnement lors d’une longue construction 3D. | Evaluation |
| [Un bassin de koï gélatineux : Hydrogen et Sonnet](#case-28) | Comparaisons et limites | Examinez une scène concrète avant de déduire un choix de modèle d’un classement de tests. | Evaluation |
| [Une collection de code créatif aux consignes communes](#case-29) | Comparaisons et limites | Utilisez plusieurs tâches visuelles variées pour éviter de généraliser à partir d’un seul résultat séduisant. | Evaluation |
| [Voxels Megamind : un contre-exemple de coût et de qualité](#case-30) | Comparaisons et limites | Conservez les échecs pour déterminer si un modèle est systématiquement moins cher ou visuellement meilleur. | Limit |
| [Un lion jongleur au fil des quatre saisons](#case-31) | Comparaisons et limites | Vérifiez le mouvement demandé, pas seulement le soin visuel apporté à l’interface environnante. | Limit |
| [Combat de bonshommes à trois modèles : plus lent et plus cher](#case-32) | Comparaisons et limites | Gardez les contre-exemples lorsque vous confrontez l’efficacité annoncée d’un modèle aux retours sur des tâches réelles. | Limit |
| [Une scène de vélo à la ferme : Hydrogen et Flash](#case-33) | Comparaisons et limites | Comparez le mouvement et la qualité de la scène avec le temps de réalisation annoncé. | Evaluation |
| [Une fille et son chat sur des vélos tandem](#case-34) | Comparaisons et limites | Comparez la fidélité à la consigne et les détails supplémentaires tout en signalant les environnements de programmation différents. | Evaluation |
| [Quatre modèles créent un jeu Mario en Three.js](#case-35) | Comparaisons et limites | Notez les réglages de raisonnement inégaux avant d’interpréter une comparaison de jeux à consigne identique. | Evaluation |
| [Trois modèles Gemini dessinent une manette](#case-36) | Comparaisons et limites | Cherchez les régressions et améliorations propres à une tâche plutôt que de présumer une hiérarchie familiale. | Evaluation |
| [Des réponses visuelles différentes entre l’application et Studio](#case-37) | Comparaisons et limites | Testez la même image dans le produit prévu avant de vous fier à un résultat de vision. | Limit |
| [Une scène de lancement de fusée : Hydrogen et Flash](#case-38) | Comparaisons et limites | Comparez l’animation réelle du lancement ainsi que la durée de création annoncée. | Evaluation |
| [Quatre tâches d’animation SVG](#case-39) | Comparaisons et limites | Utilisez plusieurs motifs d’interaction et d’animation pour examiner la cohérence entre tâches. | Evaluation |
| [Trois modèles animent un cheval de savane](#case-40) | Comparaisons et limites | Examinez directement mouvement et détails visuels avant d’accepter des affirmations générales de coût ou de qualité. | Evaluation |
| [Une scène spatiale en HTML à partir de références](#case-41) | 3D interactive et interfaces | Vérifiez à partir de quelques références si le style visuel reste reconnaissable. | Demo |
| [Un prototype de Formule 1 dans Gemini Canvas](#case-42) | 3D interactive et interfaces | Prévoyez plusieurs angles de caméra pour inspecter le véhicule généré. | Demo |
| [Hydrogen via API et Carbon dans Antigravity](#case-43) | Comparaisons et limites | Notez l’environnement de chaque essai lorsque vous comparez des rendus issus de la même consigne. | Evaluation |
| [Les ombres dans un comparatif Hydrogen et Astra](#case-44) | Comparaisons et limites | Comparez les détails du rendu avec le coût et le temps de génération. | Evaluation |
| [Un comparatif de mouvements 3D procéduraux](#case-45) | Comparaisons et limites | Mesurez la durée de génération tout en comparant la fluidité et la composition. | Evaluation |
| [89 minutes de PokéBench avec la vision](#case-46) | Comparaisons et limites | Suivez les tours, les erreurs d’API et la réussite pendant un long test d’agent visuel. | Benchmark |
| [La même scène 3D avec Hydrogen et DeepSeek](#case-47) | Comparaisons et limites | Mesurez la durée et le coût API séparément des différences visuelles. | Evaluation |
| [Une BMW de profil en SVG](#case-48) | 3D interactive et interfaces | Utilisez une vue de profil pour examiner proportions, silhouette et détails. | Demo |
| [L’île flottante d’un astronome](#case-49) | 3D interactive et interfaces | Vérifiez si les objets et l’éclairage soutiennent le thème de la scène. | Demo |
| [Un paysage 3D explorable à partir d’une image](#case-50) | 3D interactive et interfaces | Testez à la fois la fidélité à l’image et les possibilités de déplacement. | Demo |
| [Un diorama miniature fait de blocs 3D](#case-51) | 3D interactive et interfaces | Vérifiez si les formes en blocs composent une scène cohérente. | Demo |
| [Un cerisier en fleurs interactif](#case-52) | 3D interactive et interfaces | Utilisez un objet animé et quelques contrôles pour explorer les variations de la scène. | Demo |
| [Temps et coût par tâche dans Agent Arena](#case-53) | Comparaisons et limites | Examinez la latence, le coût et les tokens de sortie en plus de la réussite globale. | Benchmark |
| [Tests de documents visuels et de terminal](#case-54) | Comparaisons et limites | Séparez les résultats sur les documents et le terminal avant de choisir le niveau de raisonnement. | Benchmark |
| [Résultats Vals Index et Tax Agent](#case-55) | Comparaisons et limites | Consultez les tâches spécialisées en complément du résultat global. | Benchmark |
| [Hydrogen avec le réglage par défaut dans CursorBench](#case-56) | Comparaisons et limites | Utilisez le score par défaut comme point de départ pour tester votre propre dépôt. | Benchmark |
| [Une bataille d’archers animée par quatre modèles](#case-57) | Comparaisons et limites | Comparez la lisibilité des actions des combattants dans chaque animation. | Evaluation |
| [Un prototype façon Minecraft en quinze minutes](#case-58) | Applications et apprentissage | Utilisez un bac à sable voxel pour évaluer l’articulation entre extraction et inventaire. | Demo |
| [Hydrogen appelle des outils dans n8n](#case-59) | Agents et méthodes de programmation | Confiez les appels d’outils à Hydrogen en gardant la planification à part. | Integration |
| [Box Agent sur des documents d’entreprise complexes](#case-60) | Tableurs et recherche | Évaluez la précision, la durée et le nombre de tokens sur une charge documentaire réaliste. | Benchmark |
| [Hydrogen dans Devin FrontierCode](#case-61) | Comparaisons et limites | Examinez si les correctifs peuvent être fusionnés et notez l’environnement d’exécution. | Benchmark |
| [Réfraction dans une petite animation interactive](#case-62) | 3D interactive et interfaces | Faites de courts aperçus pour affiner un effet optique avant de complexifier la scène. | Demo |
| [Une rivière qui coule vers le haut](#case-63) | 3D interactive et interfaces | Essayez un mouvement inhabituel dans une scène simple et inspectez l’effet obtenu. | Demo |
| [Une recherche Web malgré une consigne explicite](#case-64) | Comparaisons et limites | Vérifiez que les outils sont restés inutilisés si la réponse doit se passer de navigation. | Limit |
| [Suivre le quota lors d’un essaim Antigravity](#case-65) | Comparaisons et limites | Suivez les tokens et le quota consommé lors d’une session multiagents. | Evaluation |
| [Appels d’outils pour des tâches professionnelles](#case-66) | Comparaisons et limites | Étudiez la collecte de contexte avant l’exécution d’une tâche professionnelle. | Benchmark |
| [Un portrait en 3D attribué à Hydrogen](#case-67) | 3D interactive et interfaces | Testez la reconnaissance du sujet sur un exercice de portrait en volume. | Demo |
| [Quatre modèles animent un mage et un dragon](#case-68) | Comparaisons et limites | Comparez la mise en scène, la lisibilité des actions et les effets sur le même sujet. | Evaluation |
| [Circuit d’authentification dans une équipe d’agents](#case-69) | Agents et méthodes de programmation | Vérifiez quel client se connecte réellement quand l’agent délègue à un autre fournisseur. | Limit |
| [Une session Goal Mode dans Antigravity](#case-70) | Agents et méthodes de programmation | Suivez le plan, les changements de code et les tests lors d’une session longue. | Demo |
| [MazeBench révèle des taux de réussite faibles](#case-71) | Comparaisons et limites | Testez le raisonnement spatial sur des labyrinthes avant de vous y fier. | Benchmark |
| [Trois Gemini réalisent des scènes de voiliers](#case-72) | Comparaisons et limites | Comparez les mouvements et les détails du décor sur une scène Three.js. | Evaluation |
| [Carbon et Hydrogen dans Antigravity Orchestrator](#case-73) | Agents et méthodes de programmation | Prévoyez un planificateur capable de reprendre la main si le modèle d’exécution bloque. | Integration |
| [Graphique et rapport à partir de données Workspace](#case-74) | Tableurs et recherche | Vérifiez si une relance comble les lacunes du rapport, de l’analyse ou des graphiques. | Demo |
| [Un numéro de maillot épuise le budget de raisonnement](#case-75) | Comparaisons et limites | Prévoyez un plafond de raisonnement et une solution de repli pour les petits détails visuels. | Limit |
| [Plusieurs familles de modèles dans ClutterBench](#case-76) | Comparaisons et limites | Évaluez la robustesse au désordre visuel avec un test ciblé. | Benchmark |
| [Un sujet d’actualité en vidéo commentée](#case-77) | Applications et apprentissage | Transformez une synthèse documentée en courte vidéo narrée et vérifiez les faits retenus. | Demo |
| [Un buste anatomique en coupe façon Minecraft](#case-78) | Comparaisons et limites | Vérifiez que la coupe comporte les structures internes demandées. | Evaluation |
| [Trois modèles réalisent le même accessoire](#case-79) | Comparaisons et limites | Suivez séparément la consommation de tokens et la qualité, même si un modèle est moins cher par token. | Evaluation |
| [Benchmark d’induction et consommation de tokens](#case-80) | Comparaisons et limites | Relevez les entrées et sorties facturées en parallèle des scores de raisonnement. | Benchmark |
| [Dessin pixel dans Sheets selon le mode Gemini](#case-81) | Tableurs et recherche | Comparez les modes sur la même tâche de dessin dans Google Sheets. | Evaluation |
| [Imprimer un appartement à partir d’une image](#case-82) | 3D interactive et interfaces | Poussez l’essai de reconstruction 3D jusqu’à l’impression physique. | Demo |
| [Trois modèles animent un animal en 3D](#case-83) | Comparaisons et limites | Examinez l’anatomie et le mouvement sur une consigne commune. | Evaluation |
| [Hydrogen et Qwen sur ts-bench](#case-84) | Comparaisons et limites | Examinez les erreurs d’appels d’outils avec le résultat global. | Benchmark |
| [Une simulation commerciale dans Vending-Bench](#case-85) | Comparaisons et limites | Comparez les revenus simulés avec le coût de fonctionnement de l’agent. | Benchmark |
| [Une scène marine avec le Golden Merry](#case-86) | 3D interactive et interfaces | Utilisez un navire fictif connu pour vérifier la composition d’une scène stylisée. | Demo |
| [Hydrogen dans OpenClaw](#case-87) | Agents et méthodes de programmation | Vérifiez la sélection du modèle dans le cadre agentique que vous comptez utiliser. | Integration |
| [Une baleine traverse les nuages](#case-88) | 3D interactive et interfaces | Observez séparément le mouvement et le dessin des yeux dans une scène générée par code. | Demo |
| [Quatre modèles construisent une île miniature](#case-89) | Comparaisons et limites | Comparez les rendus avec le temps et les coûts dans chaque environnement. | Evaluation |
| [Dessiner dans l’air à la webcam](#case-90) | Applications et apprentissage | Testez le suivi des gestes en traçant des traits devant la caméra. | Demo |
| [Comparaison de déchirures de tissu en code](#case-91) | Comparaisons et limites | Testez l’étirement, la déchirure et l’interaction avec la fourrure sur une même consigne. | Evaluation |
| [Une ville sous-marine dans Gemini Canvas](#case-92) | 3D interactive et interfaces | Commencez petit puis ajoutez des zones à explorer et des animaux animés. | Demo |
| [Un portail Web en une seule tentative](#case-93) | Applications et apprentissage | Examinez la disposition du premier rendu puis vérifiez les parcours individuels. | Demo |
| [Une vérification avec une source introuvable](#case-94) | Comparaisons et limites | Exigez une référence consultable avant d’agir sur un verdict concernant une capture. | Limit |
| [Un simulateur urbain façon Cities: Skylines](#case-95) | Applications et apprentissage | Vérifiez comment les commandes et la simulation s’articulent dans le prototype. | Demo |
| [Hydrogen et Sol dessinent un pélican en 2D](#case-96) | Comparaisons et limites | Comparez le délai et le mouvement sur une même animation 2D simple. | Evaluation |
| [Une salle du trône avec Blender MCP](#case-97) | Agents et méthodes de programmation | Utilisez Blender MCP pour inspecter la composition dans l’éditeur. | Integration |
| [Quatre jeux de déplacement à la toile d’araignée](#case-98) | Comparaisons et limites | Comparez déplacement et commandes avec la même contrainte de fichier unique. | Evaluation |
| [Un bateau pirate en niveaux de gris dans Three.js](#case-99) | 3D interactive et interfaces | Vérifiez si l’éclairage révèle encore la géométrie sans couleurs. | Demo |
| [Quatre modèles réalisent un diorama architectural](#case-100) | Comparaisons et limites | Comparez les choix d’éclairage sur le même plan architectural. | Evaluation |
| [Une lampe paramétrique dans CadXStudio](#case-101) | 3D interactive et interfaces | Inspectez les dimensions et les pièces modifiables d’une maquette CAO. | Integration |
| [Un chemin de sanctuaire animé en C++](#case-102) | 3D interactive et interfaces | Testez la capacité à produire une animation native sur une petite scène. | Demo |
| [Trois modèles rendent une scène de train](#case-103) | Comparaisons et limites | Comparez le délai d’une même scène avec vos réglages de modèles. | Evaluation |
| [Un Chinatown pluvieux avec le réglage Extra](#case-104) | Comparaisons et limites | Chronométrez et inspectez le rendu avant de choisir un niveau de raisonnement pour une animation longue. | Evaluation |
| [Une ville bâtie en 30 modules](#case-105) | 3D interactive et interfaces | Construisez la scène par modules et inspectez l’ensemble. | Demo |
| [Trois modèles visualisent des planètes](#case-106) | Comparaisons et limites | Comparez les rendus d’une même consigne d’interface scientifique. | Evaluation |
| [Quatre modèles recréent Chrome Dino](#case-107) | Comparaisons et limites | Mesurez le temps de chaque reproduction et comparez les résultats jouables. | Evaluation |
| [Un bureau de poste sur une île flottante](#case-108) | 3D interactive et interfaces | Demandez un bâtiment miniature et observez les effets de la matière et de l’éclairage. | Demo |
| [Deux agents de code réalisent des navires différents](#case-109) | Comparaisons et limites | Comparez le premier résultat exploitable et le coût des révisions dans votre environnement. | Evaluation |
| [Eau et poissons dans une cour de carpes koï](#case-110) | 3D interactive et interfaces | Observez la cohérence des reflets et de la lumière pendant que les poissons bougent. | Demo |
| [Un siège au trébuchet testé avec quatre modèles](#case-111) | Comparaisons et limites | Comparez des prototypes de physique jouables et notez les niveaux de raisonnement. | Evaluation |
| [Une scène 3D interactive dans Gemini](#case-112) | 3D interactive et interfaces | Prototyper l’éclairage et les particules dans l’interface Web de Gemini. | Demo |
| [Une bétonnière assemblée en CAO Web](#case-113) | Agents et méthodes de programmation | Contrôlez l’arborescence et l’ajustement des pièces avant tout usage CAO. | Integration |
| [Modélisation procédurale d’une hache dans Blender](#case-114) | Agents et méthodes de programmation | Contrôlez une silhouette de référence depuis plusieurs vues de l’éditeur. | Integration |
| [Une scène 3D rose dans un seul HTML](#case-115) | 3D interactive et interfaces | Essayez une scène Three.js sans ressources externes et vérifiez si sa composition reste lisible. | Demo |
| [Mémoire persistante dans FrontierMemory](#case-116) | Comparaisons et limites | Comparez le score et le coût par exécution avant de choisir un modèle pour la mémoire d’un agent. | Benchmark |
| [Hydrogen dans un agent vocal LiveKit défaillant](#case-117) | Comparaisons et limites | Provoquez une panne contrôlée pour voir si l’agent annonce des résultats non vérifiés. | Evaluation |
| [Le projet Ember Isle en 28 modules](#case-118) | Agents et méthodes de programmation | Découpez une grande scène et suivez le délai de chaque génération. | Demo |
| [Une simulation du Big Bang entièrement en code](#case-119) | 3D interactive et interfaces | Faites un court prototype d’explication et vérifiez son cadre scientifique. | Demo |
| [Un hélicoptère en vue éclatée](#case-120) | 3D interactive et interfaces | Vérifiez que les commandes de vol coexistent avec des vues utiles à l’inspection. | Demo |
| [Hydrogen Express avec rayons X et filaire](#case-121) | 3D interactive et interfaces | Ajoutez plusieurs modes d’inspection à un prototype 3D contrôlable. | Demo |
| [Une station de ravitaillement dans le ciel](#case-122) | 3D interactive et interfaces | Ajoutez des objets mobiles et plusieurs éclairages pour rendre les comportements visibles. | Demo |
| [Trois Gemini animent un cycliste](#case-123) | Comparaisons et limites | Comparez les mouvements sur la même consigne et mesurez chaque essai. | Evaluation |
| [Un manuel de chimie devient une leçon interactive](#case-124) | Applications et apprentissage | Ajoutez des indices, une narration et du texte facultatif pour l’apprentissage autonome. | Demo |
| [Un prototype de chanson Vocaloid](#case-125) | Applications et apprentissage | Vérifiez si une composition en une passe respecte le personnage et le style demandés. | Demo |
| [Deux modèles construisent un monde LEGO](#case-126) | Comparaisons et limites | Comparez ce que chaque modèle construit dans le délai indiqué. | Evaluation |
| [Réparer des bugs réintroduits dans deux dépôts](#case-127) | Comparaisons et limites | Semez des défauts connus pour mesurer les réparations qu’un agent peut effectuer. | Benchmark |
| [Un bonhomme face au curseur avec deux modèles](#case-128) | Comparaisons et limites | Comparez la réaction des deux animations au pointeur. | Evaluation |
| [Un moulin à eau dans un seul HTML](#case-129) | 3D interactive et interfaces | Testez rapidement un prototype 3D avec un élément mobile reconnaissable. | Demo |
| [Deux modèles animent un paysage de montagne](#case-130) | Comparaisons et limites | Comparez séparément composition, délai et coût. | Evaluation |
| [Traduction de l’anglais au persan en environnement personnalisé](#case-131) | Comparaisons et limites | Notez un passage difficile par rapport à une traduction humaine. | Evaluation |
| [Une scène Blender créée avec Hydrogen Extra](#case-132) | 3D interactive et interfaces | Vérifiez la géométrie et les matériaux avant d’augmenter les détails. | Demo |
| [Quatre modèles construisent un navire qui coule](#case-133) | Comparaisons et limites | Évaluez séparément fidélité visuelle, coût et durée pour la même scène. | Evaluation |
| [Lire une intégrale complexe depuis une image](#case-134) | Applications et apprentissage | Vérifiez si le modèle remarque l’égalité des bornes avant de simplifier l’expression. | Evaluation |
| [Comparaison à l’aveugle de quatre textes](#case-135) | Comparaisons et limites | Masquez les noms des modèles avant de choisir le texte à retenir. | Evaluation |
| [Détection et lecture selon le niveau de raisonnement](#case-136) | Comparaisons et limites | Mesurez séparément la précision de détection, la lecture de texte, le coût et la latence. | Benchmark |
| [Quatre modèles recréent la maison de Là-haut](#case-137) | Comparaisons et limites | Comparez les compromis de construction 3D en gardant la même image et la même consigne. | Evaluation |
| [Une encyclopédie de la cellule humaine en WebGL2](#case-138) | Applications et apprentissage | Utilisez une coupe interactive pour expliquer la disposition des structures cellulaires. | Demo |
| [Deux animations de particules avec Hydrogen](#case-139) | 3D interactive et interfaces | Observez forme et mouvement sur deux scènes de particules contrastées. | Demo |
| [Un adversaire purement visuel dans Parking Bench](#case-140) | Applications et apprentissage | Testez un adversaire qui ne reçoit qu’une image du plateau. | Integration |
| [Un tutoriel vidéo pour Google Docs](#case-141) | Applications et apprentissage | Utilisez des captures et annotations numérotées pour expliquer l’édition sur mobile. | Demo |
| [Un interrupteur jour-nuit dans un monde miniature](#case-142) | 3D interactive et interfaces | Utilisez l’interrupteur pour contrôler la continuité entre deux états visuels. | Demo |
| [Construire un environnement en 65 modules](#case-143) | 3D interactive et interfaces | Suivez les délais et l’effort d’intégration à mesure que la scène grandit. | Demo |
| [Un clip de danse à caméra fixe](#case-144) | Comparaisons et limites | Vérifiez que l’animation conserve le personnage, le cadrage et l’angle de caméra. | Evaluation |
| [Un agent de code bloqué sur son test initial](#case-145) | Comparaisons et limites | Fixez une durée limite pour les tests de référence et inspectez leur progression. | Limit |
| [Un environnement BASIC pour le MZ-1500](#case-146) | Applications et apprentissage | Prototyper le BASIC d’un ancien ordinateur et validez ses périphériques. | Demo |
| [Deux modèles construisent un bras robotisé interactif](#case-147) | Comparaisons et limites | Vérifiez que les articulations Three.js réagissent de façon cohérente. | Evaluation |
| [Une carte interactive d’une suspension des vols FAA](#case-148) | Tableurs et recherche | Utilisez une carte et une chronologie pour expliquer pourquoi la file persiste après la levée de l’arrêt. | Demo |
| [Un jardin miniature avec pagode](#case-149) | 3D interactive et interfaces | Vérifiez l’équilibre entre l’architecture miniature et le paysage. | Demo |
| [Planifier, exécuter et relire avec des modèles distincts](#case-150) | Agents et méthodes de programmation | Séparez les rôles et comparez le volume de tâches de chaque modèle. | Demo |
| [Hydrogen et Sol construisent un village enneigé](#case-151) | Comparaisons et limites | Jugez séparément le délai, le coût et la qualité de la scène. | Evaluation |
| [Une île Three.js aux niveaux High et Ultra](#case-152) | Comparaisons et limites | Notez les niveaux de raisonnement et comparez les visuels et délais sans assimiler les quotas. | Evaluation |
| [Un diorama d’aérodrome de la Seconde Guerre mondiale](#case-153) | 3D interactive et interfaces | Fournissez des références et demandez des mouvements mécaniques pour tester davantage que l’apparence. | Demo |
| [Configurer Hydrogen dans un client de code](#case-154) | Agents et méthodes de programmation | Utilisez l’identifiant exact du modèle avec une clé API Google dans un client compatible. | Tutorial |
| [Une équipe de recherche SuperARIS avec Hydrogen](#case-155) | Agents et méthodes de programmation | Attribuez à Hydrogen des tâches précises de recherche et de rédaction. | Integration |
| [Quatre modèles réécrivent un module à partir de zéro](#case-156) | Agents et méthodes de programmation | Comparez compréhension du code, conception et mise en œuvre sur la même réécriture. | Evaluation |
| [Détails d’une manette PS5 en 3D](#case-157) | Comparaisons et limites | Comparez les ombres des boutons et les détails à l’arrière et sur les côtés. | Evaluation |
| [Muse délègue à Antigravity CLI](#case-158) | Agents et méthodes de programmation | Reliez un assistant distant à un outil local et choisissez un modèle d’écriture par défaut. | Integration |
| [CursorBench selon le budget de raisonnement](#case-159) | Comparaisons et limites | Comparez les taux de réussite de plusieurs réglages avant de choisir le plus rapide. | Benchmark |
| [Trois modèles réalisent un temple stellaire](#case-160) | Comparaisons et limites | Évaluez la stabilité du rendu indépendamment des détails visuels. | Evaluation |
| [Un prototype de jeu de tir HTML en une minute](#case-161) | Applications et apprentissage | Testez les entrées et le retour visuel d’un jeu de tir avec un seul fichier HTML. | Demo |
| [Remettre en question une stratégie de migration](#case-162) | Comparaisons et limites | Demandez à plusieurs agents si la migration doit remplacer l’architecture en place. | Limit |
| [Converser avec Hydrogen dans AITuber OnAir](#case-163) | Applications et apprentissage | Utilisez Hydrogen derrière un avatar Live2D pour tester une conversation. | Integration |
| [Une vidéo promotionnelle réalisée en code](#case-164) | Applications et apprentissage | Donnez une courte consigne promotionnelle à un modèle de code et inspectez les animations. | Demo |
| [Deux modèles interprètent une évasion d’un temple](#case-165) | Comparaisons et limites | Comparez l’effet de l’éclairage et de l’ambiance sur la lisibilité du même jeu. | Evaluation |
| [Trois modèles Gemini animent un buggy de rallye](#case-166) | Comparaisons et limites | Évaluez la suspension et l’adhérence dans un virage relevé. | Evaluation |
| [Un rouge-gorge animé de manière procédurale](#case-167) | 3D interactive et interfaces | Inspectez le mouvement du corps et des ailes en vol. | Demo |
| [Choisir entre Antigravity Orchestrator et Swarm](#case-168) | Agents et méthodes de programmation | Utilisez les relais pour les tâches séquentielles et des agents distincts pour le travail parallèle. | Tutorial |
| [Deux modèles animent Chasing Views](#case-169) | Comparaisons et limites | Comparez rendu et durée en tenant compte du niveau de raisonnement. | Evaluation |
| [Temps et coût dans Design Creativity Bench](#case-170) | Comparaisons et limites | Comparez délai et coût par création en plus de la note de créativité. | Benchmark |
| [Une pièce SolidWorks à partir d’une image](#case-171) | Agents et méthodes de programmation | Utilisez une image 3D comme référence pour évaluer un agent de modélisation SolidWorks. | Integration |
| [Quatre modèles animent un galop dans le désert](#case-172) | Comparaisons et limites | Comparez l’appui au sol et le transfert de poids avant l’éclairage ou les détails du maillage. | Evaluation |
| [Des diapositives sur la synchronicité de Jung](#case-173) | Applications et apprentissage | Évaluez la génération de diapositives sur un sujet qui exige de clarifier concepts voisins. | Demo |
| [Des problèmes de recherche dans FrontierCS 2](#case-174) | Comparaisons et limites | Complétez les tests de programmation par un examen orienté recherche et notez l’environnement utilisé. | Benchmark |
| [Rio Above the Clouds avec quatre modèles](#case-175) | Comparaisons et limites | Comparez durée, coût et qualité perçue à partir du même sujet. | Evaluation |
| [Hydrogen sur les tâches techniques de GBENCH](#case-176) | Comparaisons et limites | Évaluez des résultats vérifiables avec et sans code, en tenant compte du prix et de la durée. | Benchmark |
| [Apprendre le créneau à des voitures simulées](#case-177) | Comparaisons et limites | Comparez la progression et le taux de réussite des simulations. | Evaluation |
| [Un moteur mitochondrial manipulable](#case-178) | Applications et apprentissage | Reliez le mouvement moléculaire à la production d’ATP dans un schéma interactif. | Demo |
| [Un jeu de territoire dans l’esprit de Qix](#case-179) | Applications et apprentissage | Utilisez une consigne d’arcade courte pour tester la boucle interactive du premier rendu. | Demo |
| [Générer des diapositives HTML avec Hydrogen](#case-180) | Applications et apprentissage | Inspectez la hiérarchie et la mise en page en évaluant la génération de HTML. | Demo |
| [Hydrogen dans Terminal-Bench 4.0](#case-181) | Comparaisons et limites | Examinez à la fois le taux d’achèvement et le coût par tâche pour choisir un modèle de programmation en ligne de commande. | Benchmark |
| [Une illustration dans un seul fichier HTML](#case-182) | 3D interactive et interfaces | Vérifiez si une référence visuelle peut être recréée en code sans ressources externes. | Demo |
| [Trois modèles Gemini animent un poulpe](#case-183) | Comparaisons et limites | Vérifiez si la prise sur la roche entraîne un mouvement visible du corps vers l’avant. | Evaluation |
| [Un résumé YouTube structuré dans Chrome](#case-184) | Tableurs et recherche | Demandez au panneau Gemini un résumé horodaté et du contexte clairement sourcé. | Tutorial |
| [Transformer une leçon en courte vidéo](#case-185) | Applications et apprentissage | Contrôlez l’exactitude des explications et le rythme lorsque vous transformez un cours en vidéo. | Demo |
| [Animer un macareux à partir d’une scène fixe](#case-186) | 3D interactive et interfaces | Utilisez une scène HTML existante comme première image d’une animation procédurale. | Demo |
| [Un test de modélisation de château](#case-187) | Comparaisons et limites | Comparez les châteaux et les ressources consommées d’un essai à l’autre. | Evaluation |
| [Utilisation du navigateur dans un Swarm Antigravity](#case-188) | Agents et méthodes de programmation | Examinez l’activité du navigateur en parallèle des tâches déléguées. | Demo |
| [Passer le relais à Muse dans Google Drive](#case-189) | Agents et méthodes de programmation | Utilisez un dossier Drive surveillé lorsque la suite du travail revient à un autre agent. | Integration |
| [Un guide de flûte à bec dans Gemini Canvas](#case-190) | Applications et apprentissage | Testez le mode rapide pour associer une partition à des conseils de pratique instrumentale. | Demo |
| [Le délai estimé change quand le périmètre s’élargit](#case-191) | Comparaisons et limites | Demandez au modèle quelles hypothèses et fonctionnalités justifient un changement de délai important. | Limit |
| [Un Swarm Antigravity anime un pélican](#case-192) | Agents et méthodes de programmation | Répartissez l’animation et le son entre agents, puis inspectez la scène assemblée. | Demo |
| [Une conversion calendaire tenant compte des années bissextiles](#case-193) | Comparaisons et limites | Posez une question de conversion simple et vérifiez si la réponse couvre les cas particuliers du calendrier. | Evaluation |
| [TAJ VICE dans un seul fichier HTML](#case-194) | Applications et apprentissage | Prototyper une carte explorable dans un fichier permet de tester les défauts de jouabilité qui subsistent. | Demo |
| [Antigravity avec un projet Google Cloud](#case-195) | Agents et méthodes de programmation | Vérifiez l’authentification de l’agent et la facturation du projet lorsque vous activez Hydrogen avec des identifiants gérés. | Tutorial |
| [Des limites d’abonnement obsolètes dans une réponse](#case-196) | Comparaisons et limites | Confirmez le nom des modèles et les conditions actuelles auprès des sources primaires. | Limit |
| [Revoir le récit d’une animation WebGL](#case-197) | Comparaisons et limites | Demandez une progression narrative plus nette quand une première version élaborée manque de structure. | Limit |
| [Carbon conçoit et Hydrogen implémente une application mobile](#case-198) | Agents et méthodes de programmation | Confiez les interactions au modèle de planification et leur réalisation au modèle d’exécution. | Demo |
| [Deux modèles programment un combat de dragons](#case-199) | Comparaisons et limites | Comparez comment chaque animation coordonne les actions de deux personnages dans une même scène. | Evaluation |
| [Une île miniature 3D à partir d’une seule instruction](#case-200) | 3D interactive et interfaces | Vérifiez que la scène articule clairement les bâtiments, le relief et l’eau. | Demo |
| [Une instruction Three.js reproductible pour animer un pélican](#case-201) | Comparaisons et limites | Vérifiez la coordination des pattes, des roues et de la direction dans une animation cycliste. | Evaluation |
| [Hydrogen dans un environnement T3 Code](#case-202) | Agents et méthodes de programmation | Testez un client de programmation spécialisé et suivez les quotas glissants et hebdomadaires pendant une session réaliste. | Integration |
| [Une vidéo d’intérêt public à l’esthétique dessinée à la main](#case-203) | Applications et apprentissage | Utilisez un court message d’intérêt public pour évaluer un traitement graphique dessiné. | Demo |
| [Un paon à vélo dans dix styles artistiques](#case-204) | Agents et méthodes de programmation | Utilisez plusieurs modèles pour programmer les transitions visuelles et synchroniser l’audio. | Demo |
| [La même maison de campagne sur trois plateformes](#case-205) | Comparaisons et limites | Vérifiez le format de sortie quand une tâche visuelle change de configuration ou de plateforme. | Evaluation |
| [Deux tableaux de bord issus de la même instruction](#case-206) | Comparaisons et limites | Comparez la mise en page et la hiérarchie de l’information à partir d’un même brief d’interface. | Evaluation |
| [Recréer le site React.gg à partir d’une image](#case-207) | Applications et apprentissage | Partez d’une image de référence et repérez les détails encore à corriger. | Demo |
| [Un panneau interactif sur la singularité](#case-208) | 3D interactive et interfaces | Prototyper une courte séquence interactive permet d’explorer un seul concept visuel. | Demo |
| [Deux modèles programment une animation à défilement latéral](#case-209) | Comparaisons et limites | Comparez la continuité des mouvements et le coût pour une scène d’action. | Evaluation |
| [Gemini comme entraîneur de course à pied](#case-210) | Applications et apprentissage | Comparez le relevé d’activité aux conseils et ajustez les objectifs à votre niveau de départ. | Demo |
| [Un jeu de navigateur avec des scores enregistrés sur une blockchain](#case-211) | Applications et apprentissage | Testez le jeu dans un navigateur pour ordinateur et vérifiez séparément l’enregistrement des scores. | Demo |
| [Des formules sans mise en forme dans une réponse en japonais](#case-212) | Comparaisons et limites | Vérifiez le rendu et l’exactitude des réponses contenant des commandes TeX. | Limit |
| [Une application de composition MIDI à partir d’une instruction](#case-213) | Applications et apprentissage | Prototyper un outil permet de convertir un brief japonais en MIDI, WAV et vue de type piano roll. | Demo |
| [Tester une consigne de non-réponse](#case-214) | Comparaisons et limites | Vérifiez si le modèle peut s’abstenir de répondre lorsque le flux de travail l’exige. | Evaluation |
| [Un récapitulatif de concert sur une page](#case-215) | Applications et apprentissage | Transformez les informations d’un événement en un résumé visuel facile à parcourir. | Demo |
| [Trois modèles expliquent un moteur électrique](#case-216) | Comparaisons et limites | Comparez la lisibilité et les commandes pédagogiques à partir d’une même demande de simulation. | Evaluation |
| [Deux flux de travail animent une scène de bureau](#case-217) | Comparaisons et limites | Vérifiez les détails, le volume sonore et l’arrêt sur image final par rapport à la demande d’origine. | Evaluation |
| [Une journée en quatre scènes à partir d’un avatar](#case-218) | Applications et apprentissage | Utilisez un seul avatar et quatre scènes du quotidien pour évaluer l’adaptation d’un court storyboard. | Demo |
| [Hydrogen prépare un clip de personnage pour ComfyUI](#case-219) | Applications et apprentissage | Conservez le costume et le décor tout en variant les expressions et les actions dans le brief. | Integration |
| [Étendre Almance Vale à 100 modules](#case-220) | Agents et méthodes de programmation | Transférez une application existante dans un agent de programmation et demandez de nouveaux modules dans le style d’origine. | Demo |
| [Un village 2D au son procédural](#case-221) | Comparaisons et limites | Vérifiez si le son réagit à ce qui se passe à l’écran et suivez le temps de création. | Evaluation |
| [Un traitement panoramique pour une chanson](#case-222) | Applications et apprentissage | Donnez une chanson et un format pour tester si le mouvement en restitue l’énergie. | Demo |
| [Les chutes du Niagara avec sept sous-agents Hydrogen](#case-223) | Agents et méthodes de programmation | Divisez la scène pour qu’un coordinateur répartisse les composants entre agents. | Demo |
| [Continuité entre deux clips romantiques d’époque](#case-224) | Applications et apprentissage | Précisez quels éléments doivent rester identiques quand une scène se poursuit dans un autre clip. | Demo |
| [Une sphère d’eau dans l’application Gemini](#case-225) | 3D interactive et interfaces | Utilisez une scène optique simple pour examiner reflets et réfraction. | Demo |

<a id="agents"></a>
## ⚡ Agents et méthodes de programmation

<a id="case-1"></a>
### Cas 1: [Maintenance d’une base de code dans Antigravity](https://x.com/antigravity/status/2120944334023389476) (par [@antigravity](https://x.com/antigravity))

**Utilisez une tâche de maintenance délimitée pour évaluer ensemble modifications, usage des outils et vérification.**

La démonstration de lancement d’Antigravity montre Hydrogen entretenant une base de code. Il s’agit d’un exemple produit par la plateforme, pas d’un test d’ingénierie reproduit indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-2"></a>
### Cas 2: [Seize applications Canvas en parallèle](https://x.com/shengzheyao/status/2120944141559550409) (par [@shengzheyao](https://x.com/shengzheyao))

**Découpez une réalisation en modules indépendants et explicitez les rôles de planification, d’implémentation et d’assurance qualité.**

Un créateur d’Antigravity CLI chez Google DeepMind décrit Carbon coordonnant, vérifiant et intégrant, tandis que Hydrogen crée 16 mini-applications Canvas sans dépendances. Ce processus combine plusieurs modèles : son résultat ne doit donc pas être attribué à Hydrogen seul.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-3"></a>
### Cas 3: [Un papillon écarlate avec un essaim multimodèle](https://x.com/thtbee_/status/2120958666480513310) (par [@thtbee_](https://x.com/thtbee_))

**Séparez orchestration et implémentation dans un projet interactif de code créatif.**

Selon le créateur, Carbon orchestrait un essaim Antigravity pendant que les agents Hydrogen réalisaient l’œuvre au papillon écarlate. La durée annoncée de 45 minutes comprend ce processus multimodèle et n’a pas été chronométrée indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-4"></a>
### Cas 4: [Inspection et réparation avec 3D Medic](https://x.com/GoogleAI/status/2120940683233984862) (par [@GoogleAI](https://x.com/GoogleAI))

**Explorez un agent qui inspecte un fichier 3D, détecte les erreurs et propose des réparations avant l’exportation.**

La démonstration 3D Medic de Google AI utilise une application Managed Agent créée dans AI Studio. Elle montre un processus de réparation de fichiers, sans prouver que n’importe quelle ressource 3D sera réparée correctement.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-5"></a>
### Cas 5: [Une scène de voilier créée dans Devin](https://x.com/Da7_Tech/status/2120967690722677144) (par [@Da7_Tech](https://x.com/Da7_Tech))

**Évaluez un modèle dans l’environnement d’agent de programmation que vous comptez réellement utiliser.**

La source présente une scène de voilier attribuée à Hydrogen exécuté dans Devin. La courte publication ne fournit ni consigne complète, ni historique des itérations, ni configuration reproductible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-59"></a>
### Cas 59: [Hydrogen appelle des outils dans n8n](https://x.com/n8n_io/status/2120947273534197886) (par [@n8n_io](https://x.com/n8n_io))

**Confiez les appels d’outils à Hydrogen en gardant la planification à part.**

n8n documente l’intégration et suggère Carbon ou Argon pour planifier, Hydrogen pour exécuter. La publication fournit le lien de configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-12

---

<a id="case-69"></a>
### Cas 69: [Circuit d’authentification dans une équipe d’agents](https://x.com/studio_yebisu/status/2120969033260646551) (par [@studio_yebisu](https://x.com/studio_yebisu))

**Vérifiez quel client se connecte réellement quand l’agent délègue à un autre fournisseur.**

L’auteur demandait de passer par Antigravity CLI mais dit avoir vu Claude Code tenter de s’authentifier directement, puis l’accès à Antigravity être suspendu. Cette cause reste son interprétation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-12

---

<a id="case-70"></a>
### Cas 70: [Une session Goal Mode dans Antigravity](https://x.com/Inmerson/status/2120973427788124345) (par [@Inmerson](https://x.com/Inmerson))

**Suivez le plan, les changements de code et les tests lors d’une session longue.**

L’auteur rapporte 105 minutes en Goal Mode avec Hydrogen Extra pour planifier, implémenter et tester. Les résultats des tests viennent de l’auteur.

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

Type: Demo | Date: 2026-11-12

---

<a id="case-73"></a>
### Cas 73: [Carbon et Hydrogen dans Antigravity Orchestrator](https://x.com/Google/status/2120982566891356279) (par [@Google](https://x.com/Google))

**Prévoyez un planificateur capable de reprendre la main si le modèle d’exécution bloque.**

Google décrit Carbon pour le plan et la reprise, et Hydrogen pour les modifications et tests. Le taux de réussite Terminal-Bench 4.0 est proche de Carbon, avec une durée et un quota moindres selon Google.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

Type: Integration | Date: 2026-11-12

---

<a id="case-87"></a>
### Cas 87: [Hydrogen dans OpenClaw](https://x.com/openclaw/status/2121098531205501401) (par [@openclaw](https://x.com/openclaw))

**Vérifiez la sélection du modèle dans le cadre agentique que vous comptez utiliser.**

OpenClaw annonce la compatibilité avec Hydrogen et publie une capture. Il n’y a ni benchmark ni transcription de la configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-13

---

<a id="case-97"></a>
### Cas 97: [Une salle du trône avec Blender MCP](https://x.com/ashen_one/status/2121165467821936651) (par [@ashen_one](https://x.com/ashen_one))

**Utilisez Blender MCP pour inspecter la composition dans l’éditeur.**

L’auteur attribue à Hydrogen la reconstitution de la salle du Trône de Fer de Game of Thrones et montre une vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

Type: Integration | Date: 2026-11-13

---

<a id="case-113"></a>
### Cas 113: [Une bétonnière assemblée en CAO Web](https://x.com/johnsanthosh01/status/2121243197901041869) (par [@johnsanthosh01](https://x.com/johnsanthosh01))

**Contrôlez l’arborescence et l’ajustement des pièces avant tout usage CAO.**

L’auteur indique 265 pièces générées par Hydrogen dans CadX Studio en 40 minutes à partir d’une consigne, sans modéliser manuellement chaque pièce.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

Type: Integration | Date: 2026-11-13

---

<a id="case-114"></a>
### Cas 114: [Modélisation procédurale d’une hache dans Blender](https://x.com/camperaigg/status/2121252572115951897) (par [@camperaigg](https://x.com/camperaigg))

**Contrôlez une silhouette de référence depuis plusieurs vues de l’éditeur.**

L’auteur décrit un travail avec Hydrogen dans Antigravity CLI, des modules Python et des contrôles répétés dans Blender. Il annonce 51 minutes avec la capture et 5,01 dollars d’API.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-13

---

<a id="case-118"></a>
### Cas 118: [Le projet Ember Isle en 28 modules](https://x.com/IamEmily2050/status/2121258646759952644) (par [@IamEmily2050](https://x.com/IamEmily2050))

**Découpez une grande scène et suivez le délai de chaque génération.**

L’auteur utilise Hydrogen High dans Gemini et indique 28 modules, une consigne par module et 82 à 290 secondes par consigne.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-150"></a>
### Cas 150: [Planifier, exécuter et relire avec des modèles distincts](https://x.com/naufaldi/status/2121499487999013081) (par [@naufaldi](https://x.com/naufaldi))

**Séparez les rôles et comparez le volume de tâches de chaque modèle.**

L’auteur utilise Opus 5.5 pour le plan, Hydrogen avec Sol en secours pour l’exécution, puis Sol 6.1 pour la revue. Il mêle ses chiffres Antigravity et des benchmarks publics distincts.

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

Type: Demo | Date: 2026-11-14

---

<a id="case-154"></a>
### Cas 154: [Configurer Hydrogen dans un client de code](https://x.com/k2sbhai/status/2121509825658147041) (par [@k2sbhai](https://x.com/k2sbhai))

**Utilisez l’identifiant exact du modèle avec une clé API Google dans un client compatible.**

L’auteur décrit la création d’une clé dans Google AI Studio puis la sélection de gemini-4-hydrogen dans OpenCode ou Cline. Accès et limites dépendent du fournisseur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-11-14

---

<a id="case-155"></a>
### Cas 155: [Une équipe de recherche SuperARIS avec Hydrogen](https://x.com/NFT_Chen/status/2121520579304206443) (par [@NFT_Chen](https://x.com/NFT_Chen))

**Attribuez à Hydrogen des tâches précises de recherche et de rédaction.**

L’auteur décrit l’installation et la configuration de SuperARIS. Il propose Hydrogen ou Carbon pour la discussion et l’écriture, avec coordination et implémentation séparées. La qualité de la recherche n’est pas mesurée.

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

Type: Integration | Date: 2026-11-14

---

<a id="case-156"></a>
### Cas 156: [Quatre modèles réécrivent un module à partir de zéro](https://x.com/oasisfeng/status/2121523934831276203) (par [@oasisfeng](https://x.com/oasisfeng))

**Comparez compréhension du code, conception et mise en œuvre sur la même réécriture.**

L’auteur compare Hydrogen, Argon, GPT-6 Astra et Claude Opus 5.5 sur un module central. Il distingue les points forts d’exécution de Hydrogen des choix d’architecture des autres essais.

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

Type: Evaluation | Date: 2026-11-14

---

<a id="case-158"></a>
### Cas 158: [Muse délègue à Antigravity CLI](https://x.com/tetumemo/status/2121528823061852166) (par [@tetumemo](https://x.com/tetumemo))

**Reliez un assistant distant à un outil local et choisissez un modèle d’écriture par défaut.**

L’auteur décrit l’envoi de tâches par Muse à Antigravity CLI sur son ordinateur. Hydrogen est son choix par défaut et Argon est disponible. Les exemples incluent des textes en japonais et des visuels.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-14

---

<a id="case-168"></a>
### Cas 168: [Choisir entre Antigravity Orchestrator et Swarm](https://x.com/ohayou792/status/2121624258984153452) (par [@ohayou792](https://x.com/ohayou792))

**Utilisez les relais pour les tâches séquentielles et des agents distincts pour le travail parallèle.**

L’auteur explique comment Orchestrator confie l’implémentation à Hydrogen après la planification, et compare ce flux au mode /swarm selon les dépendances.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

Type: Tutorial | Date: 2026-11-14

---

<a id="case-171"></a>
### Cas 171: [Une pièce SolidWorks à partir d’une image](https://x.com/GoGoFly23/status/2121636952479080713) (par [@GoGoFly23](https://x.com/GoGoFly23))

**Utilisez une image 3D comme référence pour évaluer un agent de modélisation SolidWorks.**

L’auteur fournit une image à Hydrogen dans Antigravity et montre la pièce. Une suite identifie SolidWorks MCP. Les tolérances et l’usage d’ingénierie n’ont pas été testés ici.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-14

---

<a id="case-188"></a>
### Cas 188: [Utilisation du navigateur dans un Swarm Antigravity](https://x.com/Saboo_Shubham_/status/2121852445756477924) (par [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**Examinez l’activité du navigateur en parallèle des tâches déléguées.**

Un membre de Google partage une capture d’utilisation du navigateur avec Hydrogen et un Swarm Antigravity. La publication ne donne pas le journal complet des tâches.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-15

---

<a id="case-189"></a>
### Cas 189: [Passer le relais à Muse dans Google Drive](https://x.com/nasuvit_z/status/2121857992702525734) (par [@nasuvit_z](https://x.com/nasuvit_z))

**Utilisez un dossier Drive surveillé lorsque la suite du travail revient à un autre agent.**

L’auteur décrit comment Hydrogen rassemble les informations dans un fichier Drive puis comment Muse prend le relais à son apparition. Un diagramme montre ce transfert.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-15

---

<a id="case-192"></a>
### Cas 192: [Un Swarm Antigravity anime un pélican](https://x.com/chetaslua/status/2121885449509851415) (par [@chetaslua](https://x.com/chetaslua))

**Répartissez l’animation et le son entre agents, puis inspectez la scène assemblée.**

L’auteur attribue à Carbon et Hydrogen une scène JavaScript où le pélican traverse plusieurs styles. Il indique que la musique et les bruitages sont produits par code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-195"></a>
### Cas 195: [Antigravity avec un projet Google Cloud](https://x.com/loganlu51268/status/2121911409042719023) (par [@loganlu51268](https://x.com/loganlu51268))

**Vérifiez l’authentification de l’agent et la facturation du projet lorsque vous activez Hydrogen avec des identifiants gérés.**

L’auteur décrit le passage d’un abonnement personnel à un projet Google Cloud Agent Platform via les identifiants par défaut de l’application. Le sélecteur affiche Hydrogen et la source explique la consultation des frais par SKU.

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

Type: Tutorial | Date: 2026-11-15

---

<a id="case-198"></a>
### Cas 198: [Carbon conçoit et Hydrogen implémente une application mobile](https://x.com/thebuggeddev/status/2121945961555718334) (par [@thebuggeddev](https://x.com/thebuggeddev))

**Confiez les interactions au modèle de planification et leur réalisation au modèle d’exécution.**

L’auteur attribue la conception à Carbon et l’implémentation à Hydrogen, y compris la physique via Reanimated. Il décrit des mouvements fluides et montre le résultat dans une vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-202"></a>
### Cas 202: [Hydrogen dans un environnement T3 Code](https://x.com/bei351009016/status/2121964293906206916) (par [@bei351009016](https://x.com/bei351009016))

**Testez un client de programmation spécialisé et suivez les quotas glissants et hebdomadaires pendant une session réaliste.**

L’auteur rapporte une utilisation de Hydrogen via Gemini Pro dans T3 Code pendant environ une demi-journée. Les captures documentent le quota et distinguent rapidité perçue et précision.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

Type: Integration | Date: 2026-11-15

---

<a id="case-204"></a>
### Cas 204: [Un paon à vélo dans dix styles artistiques](https://x.com/SahilPanhotra/status/2121995488425849064) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Utilisez plusieurs modèles pour programmer les transitions visuelles et synchroniser l’audio.**

L’auteur attribue à un Swarm Carbon et Hydrogen le paon qui pédale à travers dix styles. Il dit avoir produit les visuels, la musique et les bruitages par code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-220"></a>
### Cas 220: [Étendre Almance Vale à 100 modules](https://x.com/IamEmily2050/status/2122257581175410858) (par [@IamEmily2050](https://x.com/IamEmily2050))

**Transférez une application existante dans un agent de programmation et demandez de nouveaux modules dans le style d’origine.**

L’auteur a transféré Almance Vale de Gemini vers Antigravity. Il rapporte que Hydrogen Extra en mode Swarm a respecté les conventions de code et étendu la scène à 100 modules en quelques heures.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

Type: Demo | Date: 2026-11-16

---

<a id="case-223"></a>
### Cas 223: [Les chutes du Niagara avec sept sous-agents Hydrogen](https://x.com/SahilPanhotra/status/2122311637684424737) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Divisez la scène pour qu’un coordinateur répartisse les composants entre agents.**

L’auteur attribue à Carbon et à sept sous-agents Hydrogen une réalisation en moins d’une heure à partir d’une instruction. La vidéo montre de l’eau, des bateaux, différents points de vue et des décors changeants.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

Type: Demo | Date: 2026-11-16

---


<a id="apps-learning"></a>
## 💻 Applications et apprentissage

<a id="case-6"></a>
### Cas 6: [Pratique des langues avec Lingo City](https://x.com/tulseedoshi/status/2121095754844713427) (par [@tulseedoshi](https://x.com/tulseedoshi))

**Associez des fiches de révision à une rue interactive pour pratiquer une langue en contexte.**

Tulsee Doshi partage un exemple de Google diffusant des fiches personnalisées en 2D et 3D et permettant de s’exercer à parler avec des commerçants dans une ville virtuelle. C’est une démonstration du fournisseur, pas une étude indépendante des acquis pédagogiques.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-7"></a>
### Cas 7: [Roméo et Juliette dans un théâtre de papier 3D](https://x.com/techartist_/status/2120957446202253803) (par [@techartist_](https://x.com/techartist_))

**Transformez une leçon précise en scène interactive avec un objectif pédagogique clair.**

Le créateur a conçu une leçon en théâtre de papier 3D sur la scène du balcon de Roméo et Juliette pour le programme GCSE English Literature. La source démontre l’interface, mais ne mesure pas les acquis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-8"></a>
### Cas 8: [D’une maquette visuelle à un site de lecture](https://x.com/thebuggeddev/status/2120952661046689992) (par [@thebuggeddev](https://x.com/thebuggeddev))

**Utilisez une maquette de référence pour évaluer la compréhension visuelle et une interface fonctionnelle.**

Selon le créateur, Hydrogen a transformé une image de maquette en site fonctionnel de gestion de lecture en 5 minutes 27 secondes. Durée et exhaustivité sont des affirmations de la source ; aucun test fonctionnel indépendant n’accompagne cette collection.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-9"></a>
### Cas 9: [Un jardin de carpes koï en vingt modules](https://x.com/IamEmily2050/status/2120951069874532806) (par [@IamEmily2050](https://x.com/IamEmily2050))

**Construisez une grande scène par petits modules plutôt que d’attendre un résultat complet avec une seule consigne.**

Le créateur rapporte 20 consignes pour 20 modules dans l’application Gemini, prenant chacune 90–270 secondes. L’auteur a déclaré son accès anticipé et l’exemple est explicitement itératif, plutôt qu’obtenu en une seule tentative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-10"></a>
### Cas 10: [Un jeu pédagogique sur la fusion des protons](https://x.com/SidraMiconi/status/2120948703095820743) (par [@SidraMiconi](https://x.com/SidraMiconi))

**Prototypez une explication interactive d’un processus scientifique, puis vérifiez la science sous-jacente.**

Le jeu du créateur parcourt la chaîne proton-proton dans une jeune étoile. La consigne unique, la durée de 78 secondes et le coût d’environ $0.19 sont rapportés par la source, et non reproduits indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-58"></a>
### Cas 58: [Un prototype façon Minecraft en quinze minutes](https://x.com/RezAIT00/status/2120947124418293876) (par [@RezAIT00](https://x.com/RezAIT00))

**Utilisez un bac à sable voxel pour évaluer l’articulation entre extraction et inventaire.**

L’auteur indique une création en quinze minutes avec Hydrogen Extra High et mentionne placement, extraction et inventaire. La vidéo ne présente qu’une partie de ces fonctions.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-77"></a>
### Cas 77: [Un sujet d’actualité en vidéo commentée](https://x.com/gigabit_million/status/2121011957042163722) (par [@gigabit_million](https://x.com/gigabit_million))

**Transformez une synthèse documentée en courte vidéo narrée et vérifiez les faits retenus.**

L’auteur montre la recherche d’actualités et la préparation d’un plan avec Hydrogen dans Gemini mobile, puis la lecture d’un clip de dix secondes. Le système de rendu n’est pas précisé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-90"></a>
### Cas 90: [Dessiner dans l’air à la webcam](https://x.com/CodeByPoonam/status/2121121804483969102) (par [@CodeByPoonam](https://x.com/CodeByPoonam))

**Testez le suivi des gestes en traçant des traits devant la caméra.**

L’auteur attribue ce prototype de dessin à un accès anticipé à Hydrogen et partage une vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-93"></a>
### Cas 93: [Un portail Web en une seule tentative](https://x.com/kimura_0314/status/2121130305532878979) (par [@kimura_0314](https://x.com/kimura_0314))

**Examinez la disposition du premier rendu puis vérifiez les parcours individuels.**

L’auteur montre un portail attribué à Hydrogen dans Antigravity. La capture ne prouve pas le fonctionnement de ses interactions.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-13

---

<a id="case-95"></a>
### Cas 95: [Un simulateur urbain façon Cities: Skylines](https://x.com/yohakujpn/status/2121146464466604147) (par [@yohakujpn](https://x.com/yohakujpn))

**Vérifiez comment les commandes et la simulation s’articulent dans le prototype.**

L’auteur attribue le prototype montré à Hydrogen et indique une séance de génération de moins de trente minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-124"></a>
### Cas 124: [Un manuel de chimie devient une leçon interactive](https://x.com/smalkalbani/status/2121282231759155617) (par [@smalkalbani](https://x.com/smalkalbani))

**Ajoutez des indices, une narration et du texte facultatif pour l’apprentissage autonome.**

L’auteur montre un cours de chimie de niveau collège avec guidage vocal et indices. L’apprentissage n’a pas été mesuré.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-125"></a>
### Cas 125: [Un prototype de chanson Vocaloid](https://x.com/peach2k2/status/2121284159565902188) (par [@peach2k2](https://x.com/peach2k2))

**Vérifiez si une composition en une passe respecte le personnage et le style demandés.**

L’auteur publie un extrait et attribue la composition à Hydrogen. Les outils de rendu audio ne sont pas établis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-134"></a>
### Cas 134: [Lire une intégrale complexe depuis une image](https://x.com/HarshithLucky3/status/2121303778548908228) (par [@HarshithLucky3](https://x.com/HarshithLucky3))

**Vérifiez si le modèle remarque l’égalité des bornes avant de simplifier l’expression.**

L’auteur enregistre une réponse de Hydrogen High dans Gemini à partir d’une capture. Le test porte sur les bornes identiques de l’intégrale extérieure.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-138"></a>
### Cas 138: [Une encyclopédie de la cellule humaine en WebGL2](https://x.com/soumyadesign/status/2121354542344466565) (par [@soumyadesign](https://x.com/soumyadesign))

**Utilisez une coupe interactive pour expliquer la disposition des structures cellulaires.**

L’auteur indique avoir créé l’encyclopédie en 3D avec Hydrogen dans Antigravity en WebGL2 sans bibliothèques externes. Il souligne la vue en coupe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-140"></a>
### Cas 140: [Un adversaire purement visuel dans Parking Bench](https://x.com/agenticjay/status/2121391300822081713) (par [@agenticjay](https://x.com/agenticjay))

**Testez un adversaire qui ne reçoit qu’une image du plateau.**

Carbon a construit le jeu selon l’auteur. Le joueur affronte Hydrogen ou Gemini Decision 1 via API sur cinq niveaux. Les modèles reçoivent un PNG sans état de grille.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

Type: Integration | Date: 2026-11-13

---

<a id="case-141"></a>
### Cas 141: [Un tutoriel vidéo pour Google Docs](https://x.com/nin222/status/2121395008863621390) (par [@nin222](https://x.com/nin222))

**Utilisez des captures et annotations numérotées pour expliquer l’édition sur mobile.**

L’auteur crédite Hydrogen pour un montage sur les sélections, styles, couleurs, polices et l’enregistrement. Les images montrent les annotations, mais la méthode de montage n’est pas précisée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-146"></a>
### Cas 146: [Un environnement BASIC pour le MZ-1500](https://x.com/hiromsa/status/2121465784715338065) (par [@hiromsa](https://x.com/hiromsa))

**Prototyper le BASIC d’un ancien ordinateur et validez ses périphériques.**

L’auteur attribue la démonstration à Hydrogen et indique environ 15 minutes. PCG, PSG et QuickDisk sont pris en charge, ce dernier uniquement avec LOAD.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-14

---

<a id="case-161"></a>
### Cas 161: [Un prototype de jeu de tir HTML en une minute](https://x.com/SahilPanhotra/status/2121561371951399133) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Testez les entrées et le retour visuel d’un jeu de tir avec un seul fichier HTML.**

L’auteur rapporte un prototype jouable avec Hydrogen en moins d’une minute sur une consigne, sans framework ni étape de configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-163"></a>
### Cas 163: [Converser avec Hydrogen dans AITuber OnAir](https://x.com/shinshin86/status/2121571590442017094) (par [@shinshin86](https://x.com/shinshin86))

**Utilisez Hydrogen derrière un avatar Live2D pour tester une conversation.**

Le mainteneur annonce l’intégration et fournit des avatars de démonstration, dont Live2D. La vidéo montre l’intégration en action.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

Type: Integration | Date: 2026-11-14

---

<a id="case-164"></a>
### Cas 164: [Une vidéo promotionnelle réalisée en code](https://x.com/xiangning0/status/2121594643540480293) (par [@xiangning0](https://x.com/xiangning0))

**Donnez une courte consigne promotionnelle à un modèle de code et inspectez les animations.**

L’auteur partage un clip sur GPT-6.2 Astra et l’attribue à Hydrogen en code pur. La vidéo illustre cette méthode de production.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-173"></a>
### Cas 173: [Des diapositives sur la synchronicité de Jung](https://x.com/soumyadesign/status/2121676345835241916) (par [@soumyadesign](https://x.com/soumyadesign))

**Évaluez la génération de diapositives sur un sujet qui exige de clarifier concepts voisins.**

L’auteur attribue la présentation sur la synchronicité et l’ordre acausal à Hydrogen et à un outil de présentation développé dans Antigravity.

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

Type: Demo | Date: 2026-11-14

---

<a id="case-178"></a>
### Cas 178: [Un moteur mitochondrial manipulable](https://x.com/SidraMiconi/status/2121745863827697687) (par [@SidraMiconi](https://x.com/SidraMiconi))

**Reliez le mouvement moléculaire à la production d’ATP dans un schéma interactif.**

L’auteur dit que Hydrogen High a créé le prototype d’ATP synthase sur une consigne, puis a corrigé la caméra. La forme suit des coordonnées cryo-EM et le mouvement est simplifié.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-179"></a>
### Cas 179: [Un jeu de territoire dans l’esprit de Qix](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (par [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**Utilisez une consigne d’arcade courte pour tester la boucle interactive du premier rendu.**

L’auteur montre le résultat dans la version gratuite de Gemini, indique Hydrogen et rapporte une seule demande.

**Consigne:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-180"></a>
### Cas 180: [Générer des diapositives HTML avec Hydrogen](https://x.com/yamachan_ai_log/status/2121772023710118043) (par [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**Inspectez la hiérarchie et la mise en page en évaluant la génération de HTML.**

L’auteur montre une présentation réalisée avec Hydrogen et décrit le résultat comme rapide et détaillé. La source ne donne pas de délai comparatif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-185"></a>
### Cas 185: [Transformer une leçon en courte vidéo](https://x.com/smalkalbani/status/2121844887033458954) (par [@smalkalbani](https://x.com/smalkalbani))

**Contrôlez l’exactitude des explications et le rythme lorsque vous transformez un cours en vidéo.**

L’auteur attribue à Hydrogen ce flux de travail et publie deux extraits. La publication n’identifie pas le système de rendu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-190"></a>
### Cas 190: [Un guide de flûte à bec dans Gemini Canvas](https://x.com/nin222/status/2121877676042682538) (par [@nin222](https://x.com/nin222))

**Testez le mode rapide pour associer une partition à des conseils de pratique instrumentale.**

La vidéo montre un guide de flûte à bec créé dans Canvas avec le mode rapide de Hydrogen. L’auteur indique qu’une partition importée peut aussi servir de point de départ.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-194"></a>
### Cas 194: [TAJ VICE dans un seul fichier HTML](https://x.com/SahilPanhotra/status/2121909681514074328) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Prototyper une carte explorable dans un fichier permet de tester les défauts de jouabilité qui subsistent.**

L’auteur a utilisé Hydrogen pendant moins de 12 heures pour un jeu inspiré de GTA dans une version fictive d’Agra. Il indique avoir utilisé JavaScript dans un seul HTML, sans ressources externes, et reconnaît des bugs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-203"></a>
### Cas 203: [Une vidéo d’intérêt public à l’esthétique dessinée à la main](https://x.com/shengtang135754/status/2121965385356612020) (par [@shengtang135754](https://x.com/shengtang135754))

**Utilisez un court message d’intérêt public pour évaluer un traitement graphique dessiné.**

L’auteur attribue la vidéo à Gemini 4 Hydrogen et indique l’avoir obtenue en un essai. Il ne précise ni le modèle de rendu ni les étapes de génération.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-207"></a>
### Cas 207: [Recréer le site React.gg à partir d’une image](https://x.com/thebuggeddev/status/2122019549117911473) (par [@thebuggeddev](https://x.com/thebuggeddev))

**Partez d’une image de référence et repérez les détails encore à corriger.**

L’auteur dit avoir fourni une image à Hydrogen pour recréer React.gg en quelques instructions. Il renvoie à sa démonstration et reconnaît que le résultat diffère de l’original.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-210"></a>
### Cas 210: [Gemini comme entraîneur de course à pied](https://x.com/ivanleomk/status/2122036783307469199) (par [@ivanleomk](https://x.com/ivanleomk))

**Comparez le relevé d’activité aux conseils et ajustez les objectifs à votre niveau de départ.**

L’auteur attribue des conseils d’entraînement à Gemini Hydrogen et partage une capture après avoir signalé sa plus longue sortie depuis environ un an. C’est un exemple personnel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-15

---

<a id="case-211"></a>
### Cas 211: [Un jeu de navigateur avec des scores enregistrés sur une blockchain](https://x.com/itshoseyn/status/2122063851143246140) (par [@itshoseyn](https://x.com/itshoseyn))

**Testez le jeu dans un navigateur pour ordinateur et vérifiez séparément l’enregistrement des scores.**

L’auteur indique que Hydrogen l’a aidé à développer Sheytonak, un jeu associé à Base qui inscrit les scores sur la blockchain. Il signale une optimisation pour ordinateur, des problèmes sur mobile et des bugs restants.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-213"></a>
### Cas 213: [Une application de composition MIDI à partir d’une instruction](https://x.com/Awed_Urshy/status/2122161392828727738) (par [@Awed_Urshy](https://x.com/Awed_Urshy))

**Prototyper un outil permet de convertir un brief japonais en MIDI, WAV et vue de type piano roll.**

L’auteur montre une application faite avec Hydrogen. Elle transforme le texte japonais en une instruction musicale en anglais, écrit le MIDI, génère le WAV et produit une vidéo de piano roll. Ces fonctions appartiennent à l’application.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

Type: Demo | Date: 2026-11-16

---

<a id="case-215"></a>
### Cas 215: [Un récapitulatif de concert sur une page](https://x.com/fukubaya/status/2122215495474794640) (par [@fukubaya](https://x.com/fukubaya))

**Transformez les informations d’un événement en un résumé visuel facile à parcourir.**

L’auteur attribue à Hydrogen le récapitulatif visuel en japonais d’un concert de Batten Girls. La source ne montre pas l’intégralité des documents ou de l’instruction.

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

Type: Demo | Date: 2026-11-16

---

<a id="case-218"></a>
### Cas 218: [Une journée en quatre scènes à partir d’un avatar](https://x.com/antiAIvo/status/2122251181112353276) (par [@antiAIvo](https://x.com/antiAIvo))

**Utilisez un seul avatar et quatre scènes du quotidien pour évaluer l’adaptation d’un court storyboard.**

L’auteur fournit un avatar X et des scènes d’étude, de repas, de téléphone et d’exercice. Il attribue à Hydrogen un résultat d’environ dix secondes, sans préciser quel système a rendu la vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

Type: Demo | Date: 2026-11-16

---

<a id="case-219"></a>
### Cas 219: [Hydrogen prépare un clip de personnage pour ComfyUI](https://x.com/nyapan_mohy/status/2122253350808744004) (par [@nyapan_mohy](https://x.com/nyapan_mohy))

**Conservez le costume et le décor tout en variant les expressions et les actions dans le brief.**

L’auteur attribue la préparation du clip à Hydrogen et identifie un flux image-vers-vidéo MiniMax distinct dans ComfyUI. Il a préparé une nouvelle image d’ouverture et une instruction de 30 plans.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

Type: Integration | Date: 2026-11-16

---

<a id="case-222"></a>
### Cas 222: [Un traitement panoramique pour une chanson](https://x.com/ivy432hz/status/2122283590180589791) (par [@ivy432hz](https://x.com/ivy432hz))

**Donnez une chanson et un format pour tester si le mouvement en restitue l’énergie.**

L’auteur dit avoir fourni à Hydrogen XHigh uniquement la chanson, un format 21:9 et une demande de sensation de vitesse. L’extrait montre une route qui défile et ne précise pas la technique de rendu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

Type: Demo | Date: 2026-11-16

---

<a id="case-224"></a>
### Cas 224: [Continuité entre deux clips romantiques d’époque](https://x.com/AvaSinclairAi_/status/2122315627113107670) (par [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**Précisez quels éléments doivent rester identiques quand une scène se poursuit dans un autre clip.**

L’auteur attribue à un flux Gemini avec Hydrogen une courte scène romantique sur un paquebot. Il publie une instruction en deux parties sur la continuité des personnages et des costumes, sans préciser le modèle vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

Type: Demo | Date: 2026-11-16

---


<a id="data-search"></a>
## 📊 Tableurs et recherche

<a id="case-11"></a>
### Cas 11: [Un paysage animé dans Google Sheets](https://x.com/Google/status/2121004369617485896) (par [@Google](https://x.com/Google))

**Utilisez une animation de tableur inhabituelle pour examiner le code généré et les mises à jour cellule par cellule.**

Google montre des trains côtiers, des nuages et des feuilles d’automne dessinés dans les cellules avec du code écrit dans Antigravity. C’est une démonstration créative officielle, pas un test de performance des tableurs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-12"></a>
### Cas 12: [Un site de données interactif de style Folio](https://x.com/vamsibatchuk/status/2120996342923436188) (par [@vamsibatchuk](https://x.com/vamsibatchuk))

**Associez une page d’accueil à des visualisations de données interactives dans un petit prototype web.**

Un membre de Google DeepMind présente un site de style Folio et une animation interactive réalisés dans Google AI Studio. La publication ne fournit ni consigne de génération complète ni test fonctionnel indépendant.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-13"></a>
### Cas 13: [Réponses visuelles aux recherches à plusieurs volets](https://x.com/Google/status/2120960715011883148) (par [@Google](https://x.com/Google))

**Comparez la présentation des réponses et les liens cités pour une recherche nuancée à plusieurs contraintes.**

L’exemple de Google Search combine compréhension de l’intention, mises en page visuelles, tableaux comparatifs et décomposition en requêtes multiples. Ces comportements du produit sont décrits par le fournisseur ; la démonstration ne prouve aucun effet sur le classement ou le trafic des éditeurs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-14"></a>
### Cas 14: [Prévisions financières interactives dans Sheets](https://x.com/ChanduThota/status/2120942270627414079) (par [@ChanduThota](https://x.com/ChanduThota))

**Prototypez un modèle financier avec des hypothèses visibles et examinez les formules et graphiques générés.**

Chandu Thota présente une démonstration de prévisions dans Google Sheets. L’affirmation d’une génération du canevas accélérée de plus de 30 % vient du fournisseur, pas d’un chronométrage contrôlé réalisé pour ce dépôt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-60"></a>
### Cas 60: [Box Agent sur des documents d’entreprise complexes](https://x.com/levie/status/2120947988143198302) (par [@levie](https://x.com/levie))

**Évaluez la précision, la durée et le nombre de tokens sur une charge documentaire réaliste.**

Dans son évaluation en accès anticipé, Box mesure cinq points de précision de plus que Gemini 3.8 Flash, une durée inférieure de plus de moitié et environ 12 % de tokens en moins pour une tâche type.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-74"></a>
### Cas 74: [Graphique et rapport à partir de données Workspace](https://x.com/nin222/status/2120989168247652674) (par [@nin222](https://x.com/nin222))

**Vérifiez si une relance comble les lacunes du rapport, de l’analyse ou des graphiques.**

L’auteur montre Hydrogen dans Google Workspace for Education Fundamentals pour analyser des données et produire un graphique et un fichier de rapport. Il indique deux échanges.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-12

---

<a id="case-81"></a>
### Cas 81: [Dessin pixel dans Sheets selon le mode Gemini](https://x.com/kkitase/status/2121041283640926401) (par [@kkitase](https://x.com/kkitase))

**Comparez les modes sur la même tâche de dessin dans Google Sheets.**

L’auteur montre le dessin de Hydrogen et relie des essais distincts avec Orchestrator, Carbon et Argon. Aucune notation formelle n’est fournie.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-148"></a>
### Cas 148: [Une carte interactive d’une suspension des vols FAA](https://x.com/SidraMiconi/status/2121486870341370204) (par [@SidraMiconi](https://x.com/SidraMiconi))

**Utilisez une carte et une chronologie pour expliquer pourquoi la file persiste après la levée de l’arrêt.**

L’auteur annonce 222 secondes avec Hydrogen et une correction d’étiquette. La chronologie suit les rapports officiels et le trafic simule des horaires typiques.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-184"></a>
### Cas 184: [Un résumé YouTube structuré dans Chrome](https://x.com/studio_yebisu/status/2121835594674561098) (par [@studio_yebisu](https://x.com/studio_yebisu))

**Demandez au panneau Gemini un résumé horodaté et du contexte clairement sourcé.**

La publication en japonais montre comment résumer une vidéo ouverte dans Gemini dans Chrome. L’instruction publique demande un aperçu, les points clés, les chapitres, du contexte cité à part, des réserves factuelles et des ressources.

**Consigne:**

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

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

Type: Tutorial | Date: 2026-11-15

---


<a id="interactive-3d"></a>
## 🎮 3D interactive et interfaces

<a id="case-15"></a>
### Cas 15: [Une salle à manger interactive](https://x.com/notjazii/status/2120979811569222137) (par [@notjazii](https://x.com/notjazii))

**Vérifiez les interactions avec les objets, l’éclairage et les changements d’état plutôt que de juger une scène sur une image fixe.**

Le créateur montre une salle à manger avec des éclairages, des lampes, un réfrigérateur et son contenu interactifs. La durée de création annoncée de 30 minutes n’a pas été vérifiée indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-16"></a>
### Cas 16: [Un curseur de volume avec un monde miniature](https://x.com/vib3coded/status/2120973294090555890) (par [@vib3coded](https://x.com/vib3coded))

**Utilisez une commande familière pour tester à la fois la conception des interactions et les détails animés.**

La source montre un curseur de volume animant un minuscule monde de style japonais. Le créateur rapporte un coût de $0.19, sans facture ni processus complet de génération.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-17"></a>
### Cas 17: [Une maison japonaise dans Three.js](https://x.com/SPAC89/status/2120972954146140409) (par [@SPAC89](https://x.com/SPAC89))

**Distinguez génération du code et temps de rendu pour évaluer une visite 3D détaillée.**

Le créateur attribue cette maison et son jardin à Hydrogen dans Three.js, sans agents. Les affirmations sur l’usage de l’abonnement et la durée inférieure à deux heures sont propres à sa configuration et ne garantissent pas des prix ou latences généraux.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-18"></a>
### Cas 18: [Un pélican à vélo en 3D](https://x.com/nehstrr3/status/2120953932692537722) (par [@nehstrr3](https://x.com/nehstrr3))

**Utilisez un personnage mobile pour examiner coordination, mouvement et cohérence de la scène.**

Le créateur présente un pélican animé en 3D à vélo et indique Hydrogen au niveau XHigh. La publication montre un résultat, pas une consigne complète reproductible ni une validation physique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-19"></a>
### Cas 19: [Un simulateur planétaire avec planification préalable](https://x.com/The_Alex/status/2120950301318582643) (par [@The_Alex](https://x.com/The_Alex))

**Donnez au modèle de programmation un plan concret avant de lui demander de modifier une scène complexe.**

Le créateur bénéficiant d’un accès anticipé montre un simulateur planétaire et rapporte de meilleures modifications après des plans plus détaillés. La source attribue l’idée à ForwardEditor et décrit un processus itératif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-20"></a>
### Cas 20: [Une île portuaire avec Antigravity Swarm](https://x.com/ai_for_success/status/2120942147780464660) (par [@ai_for_success](https://x.com/ai_for_success))

**Utilisez un petit environnement navigable pour examiner la construction de scènes par plusieurs agents.**

Le créateur a déclaré son accès anticipé et montre une île portuaire créée avec Hydrogen dans la fonction Swarm d’Antigravity. La publication ne précise pas toute l’orchestration ni l’historique des consignes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-21"></a>
### Cas 21: [Une île flottante avec la tour Eiffel](https://x.com/RezAIT00/status/2120940988780736973) (par [@RezAIT00](https://x.com/RezAIT00))

**Évaluez composition, mouvement de caméra et code généré sur une scène compacte de monument.**

La source montre une île miniature avec la tour Eiffel et l’attribue à Hydrogen XHigh. Les six minutes annoncées pour la création et l’enregistrement viennent de l’auteur, pas d’un chronométrage indépendant.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-22"></a>
### Cas 22: [Une ville futuriste à survoler](https://x.com/kimmonismus/status/2120940617169826037) (par [@kimmonismus](https://x.com/kimmonismus))

**Testez les modifications ultérieures d’un monde procédural plutôt que de supposer le premier résultat définitif.**

Le créateur en accès anticipé a utilisé Hydrogen High dans Antigravity et rapporte une consigne supplémentaire pour produire une ville Three.js avec tours procédurales, pluie et circulation aérienne. L’enregistrement montre du code généré en cours d’exécution, pas une génération vidéo native.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-23"></a>
### Cas 23: [Un hydravion du lever du soleil à la nuit](https://x.com/LuminaBench/status/2120939312564842663) (par [@LuminaBench](https://x.com/LuminaBench))

**Examinez les commandes d’environnement et les transitions lumineuses dans une scène 3D interactive.**

La démonstration originale de LuminaBench montre un hydravion et les heures changeantes de la journée ; Google l’a ensuite repartagée. La publication précède la limite de lancement public enregistrée ; sa voie d’accès et l’appel du modèle n’ont pas été vérifiés indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-41"></a>
### Cas 41: [Une scène spatiale en HTML à partir de références](https://x.com/Inmerson/status/2120482539907559651) (par [@Inmerson](https://x.com/Inmerson))

**Vérifiez à partir de quelques références si le style visuel reste reconnaissable.**

L’auteur attribue la visualisation à Hydrogen et montre les images planétaires fournies au modèle ainsi que la scène HTML obtenue, avec une planète à anneaux.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-11

---

<a id="case-42"></a>
### Cas 42: [Un prototype de Formule 1 dans Gemini Canvas](https://x.com/auricxofficial/status/2120843585914605830) (par [@auricxofficial](https://x.com/auricxofficial))

**Prévoyez plusieurs angles de caméra pour inspecter le véhicule généré.**

L’auteur attribue cette visionneuse à son premier essai de Hydrogen dans Gemini Canvas. La vidéo montre plusieurs caméras et des vues de la suspension.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-48"></a>
### Cas 48: [Une BMW de profil en SVG](https://x.com/HarshithLucky3/status/2120932649938382894) (par [@HarshithLucky3](https://x.com/HarshithLucky3))

**Utilisez une vue de profil pour examiner proportions, silhouette et détails.**

L’auteur montre une BMW M4 CS en SVG et attribue sa génération en moins de 30 secondes à Hydrogen High dans Gemini.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-12

---

<a id="case-49"></a>
### Cas 49: [L’île flottante d’un astronome](https://x.com/pankajkumar_dev/status/2120933196221333791) (par [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Vérifiez si les objets et l’éclairage soutiennent le thème de la scène.**

L’auteur attribue la scène à une version de Hydrogen testée sur Arena et indique quatre minutes de génération. L’attribution concerne cette session.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-50"></a>
### Cas 50: [Un paysage 3D explorable à partir d’une image](https://x.com/HarshithLucky3/status/2120935535422374055) (par [@HarshithLucky3](https://x.com/HarshithLucky3))

**Testez à la fois la fidélité à l’image et les possibilités de déplacement.**

L’auteur présente un paysage attribué à Hydrogen dans Gemini et décrit les reflets GLSL, la géométrie procédurale et les mouvements de nage.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-51"></a>
### Cas 51: [Un diorama miniature fait de blocs 3D](https://x.com/abhinavflac/status/2120936501961969990) (par [@abhinavflac](https://x.com/abhinavflac))

**Vérifiez si les formes en blocs composent une scène cohérente.**

L’auteur partage une vidéo du diorama et l’attribue à Hydrogen. La durée et la configuration sont inconnues.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-52"></a>
### Cas 52: [Un cerisier en fleurs interactif](https://x.com/hakmgpt/status/2120936640436642231) (par [@hakmgpt](https://x.com/hakmgpt))

**Utilisez un objet animé et quelques contrôles pour explorer les variations de la scène.**

L’auteur attribue à Hydrogen l’interface du cerisier en fleurs. Des paramètres sont visibles sur la capture, mais l’implémentation reste inconnue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-12

---

<a id="case-62"></a>
### Cas 62: [Réfraction dans une petite animation interactive](https://x.com/chanelluuh/status/2120951519470399710) (par [@chanelluuh](https://x.com/chanelluuh))

**Faites de courts aperçus pour affiner un effet optique avant de complexifier la scène.**

L’auteur attribue à Hydrogen une animation de la série Small Delights et attire l’attention sur la réfraction. Il décrit un travail itératif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-63"></a>
### Cas 63: [Une rivière qui coule vers le haut](https://x.com/xKaka1456/status/2120952404225265983) (par [@xKaka1456](https://x.com/xKaka1456))

**Essayez un mouvement inhabituel dans une scène simple et inspectez l’effet obtenu.**

L’auteur présente une rivière créée sur le Web avec Hydrogen. La durée et la consommation du quota sont ses observations.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-67"></a>
### Cas 67: [Un portrait en 3D attribué à Hydrogen](https://x.com/soyamiruku/status/2120959893943251322) (par [@soyamiruku](https://x.com/soyamiruku))

**Testez la reconnaissance du sujet sur un exercice de portrait en volume.**

L’auteur attribue à Hydrogen le portrait 3D du destinataire de la publication et partage une image. La configuration est peu documentée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

Type: Demo | Date: 2026-11-12

---

<a id="case-82"></a>
### Cas 82: [Imprimer un appartement à partir d’une image](https://x.com/bijanbowen/status/2121042010928709932) (par [@bijanbowen](https://x.com/bijanbowen))

**Poussez l’essai de reconstruction 3D jusqu’à l’impression physique.**

L’auteur montre la référence et l’impression d’un appartement de Seinfeld qu’il attribue à Hydrogen.

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

Type: Demo | Date: 2026-11-13

---

<a id="case-86"></a>
### Cas 86: [Une scène marine avec le Golden Merry](https://x.com/xKaka1456/status/2121063351136739388) (par [@xKaka1456](https://x.com/xKaka1456))

**Utilisez un navire fictif connu pour vérifier la composition d’une scène stylisée.**

L’auteur attribue à Hydrogen la scène du Golden Merry sur l’eau. Les consignes, réglages et itérations ne sont pas précisés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-88"></a>
### Cas 88: [Une baleine traverse les nuages](https://x.com/xKaka1456/status/2121100318150898144) (par [@xKaka1456](https://x.com/xKaka1456))

**Observez séparément le mouvement et le dessin des yeux dans une scène générée par code.**

L’auteur montre la baleine et indique environ deux minutes avec Hydrogen. La durée et le quota sont ses observations.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-92"></a>
### Cas 92: [Une ville sous-marine dans Gemini Canvas](https://x.com/ayyh_18/status/2121128385690693821) (par [@ayyh_18](https://x.com/ayyh_18))

**Commencez petit puis ajoutez des zones à explorer et des animaux animés.**

L’auteur décrit plusieurs consignes dans Gemini pour créer poissons, méduses, coraux et dômes vitrés accessibles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-99"></a>
### Cas 99: [Un bateau pirate en niveaux de gris dans Three.js](https://x.com/parves075/status/2121172856889618528) (par [@parves075](https://x.com/parves075))

**Vérifiez si l’éclairage révèle encore la géométrie sans couleurs.**

L’auteur réalise le bateau avec Hydrogen dans Antigravity et publie un enregistrement pour examiner la lumière et les détails 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-101"></a>
### Cas 101: [Une lampe paramétrique dans CadXStudio](https://x.com/CadX_Studio/status/2121175785356853312) (par [@CadX_Studio](https://x.com/CadX_Studio))

**Inspectez les dimensions et les pièces modifiables d’une maquette CAO.**

CadXStudio présente une lampe dans le navigateur et annonce 35 pièces modifiables. L’éditeur de l’outil fournit l’exemple.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

Type: Integration | Date: 2026-11-13

---

<a id="case-102"></a>
### Cas 102: [Un chemin de sanctuaire animé en C++](https://x.com/nehstrr3/status/2121184399245128137) (par [@nehstrr3](https://x.com/nehstrr3))

**Testez la capacité à produire une animation native sur une petite scène.**

L’auteur attribue la promenade sous les portiques à Hydrogen Extra High et indique une implémentation en C++.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-105"></a>
### Cas 105: [Une ville bâtie en 30 modules](https://x.com/IamEmily2050/status/2121200010574598655) (par [@IamEmily2050](https://x.com/IamEmily2050))

**Construisez la scène par modules et inspectez l’ensemble.**

L’auteur utilise Hydrogen High dans Gemini et indique une consigne par module pour les 30 modules.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-108"></a>
### Cas 108: [Un bureau de poste sur une île flottante](https://x.com/pankajkumar_dev/status/2121220537984954448) (par [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Demandez un bâtiment miniature et observez les effets de la matière et de l’éclairage.**

L’auteur demande à Hydrogen un bureau de poste en 3D. Il montre une vidéo et souligne les textures, les couleurs et la lumière.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-110"></a>
### Cas 110: [Eau et poissons dans une cour de carpes koï](https://x.com/SahilPanhotra/status/2121225566779023432) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Observez la cohérence des reflets et de la lumière pendant que les poissons bougent.**

L’auteur montre le rendu de Koi Courtyard avec Hydrogen et relève les caustiques, les reflets et les poissons. Il relie sa version Carbon pour comparaison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-112"></a>
### Cas 112: [Une scène 3D interactive dans Gemini](https://x.com/YxzRainy/status/2121232725185339869) (par [@YxzRainy](https://x.com/YxzRainy))

**Prototyper l’éclairage et les particules dans l’interface Web de Gemini.**

L’auteur montre des particules, un éclairage animé et des commandes en temps réel dans une scène attribuée à Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-115"></a>
### Cas 115: [Une scène 3D rose dans un seul HTML](https://x.com/SahilPanhotra/status/2121254256288137484) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Essayez une scène Three.js sans ressources externes et vérifiez si sa composition reste lisible.**

L’auteur attribue le rendu rose à Hydrogen et indique un seul fichier HTML en Three.js pur. Koi Courtyard est un autre projet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-119"></a>
### Cas 119: [Une simulation du Big Bang entièrement en code](https://x.com/ash_twtz/status/2121268140630000020) (par [@ash_twtz](https://x.com/ash_twtz))

**Faites un court prototype d’explication et vérifiez son cadre scientifique.**

L’auteur attribue à Hydrogen dans Gemini quinze secondes de visualisation sans accès Web, textures, ressources externes ou modèles 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-120"></a>
### Cas 120: [Un hélicoptère en vue éclatée](https://x.com/LuminaBench/status/2121273297715277930) (par [@LuminaBench](https://x.com/LuminaBench))

**Vérifiez que les commandes de vol coexistent avec des vues utiles à l’inspection.**

L’auteur montre un hélicoptère pilotable, sa vue d’assemblage et sa vue éclatée, attribués à Hydrogen Extra High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-121"></a>
### Cas 121: [Hydrogen Express avec rayons X et filaire](https://x.com/LuminaBench/status/2121277060983234788) (par [@LuminaBench](https://x.com/LuminaBench))

**Ajoutez plusieurs modes d’inspection à un prototype 3D contrôlable.**

L’auteur montre les commandes de vitesse, une vue éclatée et les modes filaire et rayons X. Il indique un essai d’environ cinq minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-122"></a>
### Cas 122: [Une station de ravitaillement dans le ciel](https://x.com/doe_naps/status/2121279837512106168) (par [@doe_naps](https://x.com/doe_naps))

**Ajoutez des objets mobiles et plusieurs éclairages pour rendre les comportements visibles.**

L’auteur attribue à Hydrogen une station avec voiture volante rétro, turbines mobiles et alternance jour-nuit. Il indique une seule génération.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-129"></a>
### Cas 129: [Un moulin à eau dans un seul HTML](https://x.com/NovaXCode/status/2121294356875509851) (par [@NovaXCode](https://x.com/NovaXCode))

**Testez rapidement un prototype 3D avec un élément mobile reconnaissable.**

L’auteur indique environ 30 secondes pour la scène du moulin avec Hydrogen et en montre une vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-132"></a>
### Cas 132: [Une scène Blender créée avec Hydrogen Extra](https://x.com/SPAC89/status/2121302218347270625) (par [@SPAC89](https://x.com/SPAC89))

**Vérifiez la géométrie et les matériaux avant d’augmenter les détails.**

L’auteur attribue à Hydrogen Extra sa scène Blender et estime la consommation de son quota pour cette session.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-139"></a>
### Cas 139: [Deux animations de particules avec Hydrogen](https://x.com/gwammyy/status/2121355401392189746) (par [@gwammyy](https://x.com/gwammyy))

**Observez forme et mouvement sur deux scènes de particules contrastées.**

L’auteur attribue les deux vidéos à Hydrogen. Il montre les résultats sans documenter les réglages.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

Type: Demo | Date: 2026-11-13

---

<a id="case-142"></a>
### Cas 142: [Un interrupteur jour-nuit dans un monde miniature](https://x.com/vib3coded/status/2121398359395283027) (par [@vib3coded](https://x.com/vib3coded))

**Utilisez l’interrupteur pour contrôler la continuité entre deux états visuels.**

L’auteur montre la transition jour-nuit et rapporte un coût de 0,21 dollar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-143"></a>
### Cas 143: [Construire un environnement en 65 modules](https://x.com/IamEmily2050/status/2121400396002492781) (par [@IamEmily2050](https://x.com/IamEmily2050))

**Suivez les délais et l’effort d’intégration à mesure que la scène grandit.**

L’auteur indique 65 modules et une consigne par module dans Gemini. La vidéo montre le résultat.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-149"></a>
### Cas 149: [Un jardin miniature avec pagode](https://x.com/auricxofficial/status/2121498286926540970) (par [@auricxofficial](https://x.com/auricxofficial))

**Vérifiez l’équilibre entre l’architecture miniature et le paysage.**

L’auteur attribue la vidéo d’une pagode en blocs et de son jardin à Hydrogen, sans détailler l’implémentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-153"></a>
### Cas 153: [Un diorama d’aérodrome de la Seconde Guerre mondiale](https://x.com/doe_naps/status/2121508105947320688) (par [@doe_naps](https://x.com/doe_naps))

**Fournissez des références et demandez des mouvements mécaniques pour tester davantage que l’apparence.**

L’auteur décrit un diorama créé par Hydrogen dans un seul HTML avec des références et une brève consigne. Le sujet exigeait un avion et un char fonctionnels.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-167"></a>
### Cas 167: [Un rouge-gorge animé de manière procédurale](https://x.com/LuminaBench/status/2121620820791562291) (par [@LuminaBench](https://x.com/LuminaBench))

**Inspectez le mouvement du corps et des ailes en vol.**

L’auteur attribue l’animation codée à Hydrogen. Un autre message montre le graphe Antigravity Swarm de la même réalisation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

Type: Demo | Date: 2026-11-14

---

<a id="case-182"></a>
### Cas 182: [Une illustration dans un seul fichier HTML](https://x.com/vamsibatchuk/status/2121788887823778297) (par [@vamsibatchuk](https://x.com/vamsibatchuk))

**Vérifiez si une référence visuelle peut être recréée en code sans ressources externes.**

Un membre de DeepMind montre une illustration dans un seul fichier et indique qu’il n’a utilisé ni bibliothèque, ni générateur d’images, ni skill, ni ressource intégrée.

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

Type: Demo | Date: 2026-11-15

---

<a id="case-186"></a>
### Cas 186: [Animer un macareux à partir d’une scène fixe](https://x.com/vamsibatchuk/status/2121846407950639541) (par [@vamsibatchuk](https://x.com/vamsibatchuk))

**Utilisez une scène HTML existante comme première image d’une animation procédurale.**

L’auteur a demandé à Hydrogen une suite de 50 images dans un seul fichier HTML. Dans la vidéo, un macareux emporte le chapeau du personnage.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-200"></a>
### Cas 200: [Une île miniature 3D à partir d’une seule instruction](https://x.com/CodeByPoonam/status/2121952483132289270) (par [@CodeByPoonam](https://x.com/CodeByPoonam))

**Vérifiez que la scène articule clairement les bâtiments, le relief et l’eau.**

L’auteur attribue à Hydrogen la création en un seul essai de l’île miniature montrée. La vidéo présente des bâtiments et d’autres points de repère.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-208"></a>
### Cas 208: [Un panneau interactif sur la singularité](https://x.com/Moleh1ll/status/2122032596263776351) (par [@Moleh1ll](https://x.com/Moleh1ll))

**Prototyper une courte séquence interactive permet d’explorer un seul concept visuel.**

L’auteur attribue à Hydrogen un panneau sur le thème de la singularité. La vidéo montre le résultat avec peu de détails d’implémentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

Type: Demo | Date: 2026-11-15

---

<a id="case-225"></a>
### Cas 225: [Une sphère d’eau dans l’application Gemini](https://x.com/Google/status/2122366286659289502) (par [@Google](https://x.com/Google))

**Utilisez une scène optique simple pour examiner reflets et réfraction.**

Google partage une sphère à l’aspect aqueux portant l’inscription Hydrogen et attribue le résultat à ce modèle dans Gemini. La technique de rendu n’est pas décrite.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

Type: Demo | Date: 2026-11-16

---


<a id="comparisons-limits"></a>
## 🧪 Comparaisons et limites

<a id="case-24"></a>
### Cas 24: [Animation de bonhommes néon : Hydrogen et Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (par [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Comparez l’animation finale, les durées et les coûts annoncés sans supposer des environnements d’exécution identiques.**

L’auteur présente les résultats de Hydrogen et Opus 5.5 et annonce $1.02 contre $7.43 et 10m 22s contre 34m. Cette collection n’a vérifié ni facturation, ni consignes, ni nombres d’itérations, ni comparabilité des paramètres d’exécution.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-25"></a>
### Cas 25: [Tâches robotiques et erreurs autodéclarées](https://x.com/ArtificialAnlys/status/2120995180891508833) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Intégrez la réussite des tâches et la reconnaissance de petites erreurs dans une évaluation robotique.**

Artificial Analysis montre des tâches de versement et de rangement de blocs et affirme que Hydrogen a remarqué un petit déversement et un couvercle non fermé. La vidéo et le classement AA-Robotics v0.1 viennent de l’évaluateur ; ils ne constituent pas ici une reproduction indépendante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-26"></a>
### Cas 26: [Une cellule de laboratoire commandée en langage naturel](https://x.com/danielmckinn0n/status/2120990834246173125) (par [@danielmckinn0n](https://x.com/danielmckinn0n))

**Évaluez l’exécution des outils et la gestion des échecs séparément des scores principaux des tests.**

La source montre une cellule de laboratoire pilotée par une demande en langage naturel et rapporte les résultats de quatre tests liés au laboratoire. Le score RareBench annoncé de Hydrogen est inférieur à celui d’Opus 5.5, tandis que les trois autres sont supérieurs ; c’est une démonstration du propriétaire des tests, pas une validation médicale.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-27"></a>
### Cas 27: [Iceberg et remorqueur : Hydrogen et Carbon](https://x.com/EnvolDev/status/2120989670582677930) (par [@EnvolDev](https://x.com/EnvolDev))

**Consignez le niveau de raisonnement et les restrictions de l’environnement lors d’une longue construction 3D.**

Le créateur indique que les deux modèles fonctionnent sur High via OpenRouter, avec Hydrogen à $4.27 et 1h 23m 40s, contre Carbon à $8.83 et 2h 39m 10s. Ces résultats non contrôlés sont rapportés par la source, et non des rapports universels de prix ou de vitesse.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-28"></a>
### Cas 28: [Un bassin de koï gélatineux : Hydrogen et Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (par [@Haleeeemahh](https://x.com/Haleeeemahh))

**Examinez une scène concrète avant de déduire un choix de modèle d’un classement de tests.**

L’auteur compare Hydrogen et Sonnet 5.5 pour un bassin de koï en 3D. La source invite le public à juger les résultats sans établir des paramètres équivalents ou un score de qualité objectif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-29"></a>
### Cas 29: [Une collection de code créatif aux consignes communes](https://x.com/kickingkeys/status/2120985358317875222) (par [@kickingkeys](https://x.com/kickingkeys))

**Utilisez plusieurs tâches visuelles variées pour éviter de généraliser à partir d’un seul résultat séduisant.**

Le créateur indique avoir donné les mêmes consignes à Hydrogen, Carbon et Argon et place les comparaisons dans les réponses. Les médias de la publication principale montrent des animaux à faible nombre de polygones, une rue néon et un contenant de style aquarelle ; ce n’est pas un test contrôlé complet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-30"></a>
### Cas 30: [Voxels Megamind : un contre-exemple de coût et de qualité](https://x.com/thehypedotnews/status/2120980737012670720) (par [@thehypedotnews](https://x.com/thehypedotnews))

**Conservez les échecs pour déterminer si un modèle est systématiquement moins cher ou visuellement meilleur.**

Selon la source, Hydrogen a produit une figure de Titan moins cohérente pour $36.07, contre $8.64 pour Sonnet 5.5. La publication comporte une promotion commerciale ; les coûts et le jugement de qualité sont les affirmations de l’éditeur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

Type: Limit | Date: 2026-11-12

---

<a id="case-31"></a>
### Cas 31: [Un lion jongleur au fil des quatre saisons](https://x.com/SahilPanhotra/status/2120978349967458704) (par [@SahilPanhotra](https://x.com/SahilPanhotra))

**Vérifiez le mouvement demandé, pas seulement le soin visuel apporté à l’interface environnante.**

L’auteur rapporte que Carbon gérait les arcs de jonglage croisés, tandis que Hydrogen laissait les balles flotter malgré des transitions saisonnières et un découpage plus propres. Cette comparaison SVG sur une même tâche révèle un défaut précis de mouvement, pas un classement général des modèles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

Type: Limit | Date: 2026-11-12

---

<a id="case-32"></a>
### Cas 32: [Combat de bonshommes à trois modèles : plus lent et plus cher](https://x.com/DanielZambrini/status/2120963180461769183) (par [@DanielZambrini](https://x.com/DanielZambrini))

**Gardez les contre-exemples lorsque vous confrontez l’efficacité annoncée d’un modèle aux retours sur des tâches réelles.**

Le créateur compare Hydrogen, Carbon et Argon et rapporte que Hydrogen a pris plus de temps et coûté plus cher que Carbon dans ce test. Paramètres, facturation et nombres d’itérations n’ont pas été vérifiés indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

Type: Limit | Date: 2026-11-12

---

<a id="case-33"></a>
### Cas 33: [Une scène de vélo à la ferme : Hydrogen et Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (par [@Bhavani_00007](https://x.com/Bhavani_00007))

**Comparez le mouvement et la qualité de la scène avec le temps de réalisation annoncé.**

La source compare Hydrogen à Gemini 3.8 Flash pour une scène de vélo à la ferme et annonce 56 secondes contre plus de six minutes. C’est un test unique d’un créateur, pas une mesure générale de vitesse.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-34"></a>
### Cas 34: [Une fille et son chat sur des vélos tandem](https://x.com/marcthecreatorr/status/2120956699951628637) (par [@marcthecreatorr](https://x.com/marcthecreatorr))

**Comparez la fidélité à la consigne et les détails supplémentaires tout en signalant les environnements de programmation différents.**

Le créateur a utilisé la même tâche SVG déclarée, mais exécuté Opus 5.5 dans Claude Code et Hydrogen dans Cursor. Temps et coûts annoncés diffèrent fortement, mais les environnements différents et les itérations non précisées empêchent une comparaison contrôlée des seuls modèles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-35"></a>
### Cas 35: [Quatre modèles créent un jeu Mario en Three.js](https://x.com/StatsWire/status/2120955723396071548) (par [@StatsWire](https://x.com/StatsWire))

**Notez les réglages de raisonnement inégaux avant d’interpréter une comparaison de jeux à consigne identique.**

La source compare Gemini 3.8 Flash, Argon et Carbon sur High à Hydrogen sur XHigh, en Three.js pur sans modèles 3D ni textures externes. Elle présente quatre résultats, pas un test à raisonnement égal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-36"></a>
### Cas 36: [Trois modèles Gemini dessinent une manette](https://x.com/notjazii/status/2120952314873987271) (par [@notjazii](https://x.com/notjazii))

**Cherchez les régressions et améliorations propres à une tâche plutôt que de présumer une hiérarchie familiale.**

Le créateur compare les manettes SVG de Carbon, Argon et Hydrogen et dit avoir recommencé le test. Durées et coûts sont rapportés par la source et n’établissent pas un classement général de qualité des modèles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-11-12

---

<a id="case-37"></a>
### Cas 37: [Des réponses visuelles différentes entre l’application et Studio](https://x.com/thegenioo/status/2120946497802174688) (par [@thegenioo](https://x.com/thegenioo))

**Testez la même image dans le produit prévu avant de vous fier à un résultat de vision.**

La source montre des réponses contradictoires d’identification d’aliments attribuées à Hydrogen dans l’application Gemini et AI Studio. La comparaison ne vérifie pas indépendamment l’identité du routage, des paramètres ou du contexte complet de conversation.

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

Type: Limit | Date: 2026-11-12

---

<a id="case-38"></a>
### Cas 38: [Une scène de lancement de fusée : Hydrogen et Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (par [@Bhavani_00007](https://x.com/Bhavani_00007))

**Comparez l’animation réelle du lancement ainsi que la durée de création annoncée.**

Le créateur présente les résultats de Hydrogen et Gemini 3.8 Flash et annonce moins d’une minute contre environ trois minutes. Cette comparaison visuelle porte sur une tâche sans configuration d’exécution contrôlée indépendamment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-39"></a>
### Cas 39: [Quatre tâches d’animation SVG](https://x.com/Angaisb_/status/2120944947193127061) (par [@Angaisb_](https://x.com/Angaisb_))

**Utilisez plusieurs motifs d’interaction et d’animation pour examiner la cohérence entre tâches.**

La source associe les résultats de Hydrogen et Carbon pour des transferts, des changements jour/nuit, un déballage et un caméléon. Son court texte principal ne fournit ni consignes complètes, ni preuves de durée, ni méthode de notation objective.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-40"></a>
### Cas 40: [Trois modèles animent un cheval de savane](https://x.com/AI_Screening/status/2120944276586823689) (par [@AI_Screening](https://x.com/AI_Screening))

**Examinez directement mouvement et détails visuels avant d’accepter des affirmations générales de coût ou de qualité.**

Le créateur présente Hydrogen, Carbon et Argon sur une scène de cheval de savane. Les affirmations de vitesse supérieure, de coût inférieur et de qualité élevée restent l’appréciation de la source, pas une comparaison contrôlée reproduite ici.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-43"></a>
### Cas 43: [Hydrogen via API et Carbon dans Antigravity](https://x.com/huang18825/status/2120876396264444314) (par [@huang18825](https://x.com/huang18825))

**Notez l’environnement de chaque essai lorsque vous comparez des rendus issus de la même consigne.**

L’auteur utilise Hydrogen via l’API et Carbon via Antigravity. Les 4 minutes et 47 secondes annoncées concernent Hydrogen dans ce cadre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-44"></a>
### Cas 44: [Les ombres dans un comparatif Hydrogen et Astra](https://x.com/SPAC89/status/2120911537296515321) (par [@SPAC89](https://x.com/SPAC89))

**Comparez les détails du rendu avec le coût et le temps de génération.**

L’auteur préfère le rendu de Hydrogen en raison d’une ombre absente de l’autre version et indique qu’il a terminé plus vite dans sa configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-45"></a>
### Cas 45: [Un comparatif de mouvements 3D procéduraux](https://x.com/SPAC89/status/2120923185981915156) (par [@SPAC89](https://x.com/SPAC89))

**Mesurez la durée de génération tout en comparant la fluidité et la composition.**

L’auteur montre une forme rayée en 3D attribuée à Hydrogen High. Il indique moins de cinq minutes et compare ce rendu à ceux de modèles plus coûteux dans son essai.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-46"></a>
### Cas 46: [89 minutes de PokéBench avec la vision](https://x.com/StatsWire/status/2120923685296988296) (par [@StatsWire](https://x.com/StatsWire))

**Suivez les tours, les erreurs d’API et la réussite pendant un long test d’agent visuel.**

La source rapporte une session Vertex avant l’annonce où Hydrogen High bat Brock en 365 tours et 89 minutes, sans appel API en échec.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-47"></a>
### Cas 47: [La même scène 3D avec Hydrogen et DeepSeek](https://x.com/AiHubMix/status/2120928687537418581) (par [@AiHubMix](https://x.com/AiHubMix))

**Mesurez la durée et le coût API séparément des différences visuelles.**

AIHubMix utilise le niveau de raisonnement maximal disponible pour chaque modèle. Le fournisseur indique 3 minutes et 1,30 dollar pour Hydrogen, contre 100 minutes et 0,90 dollar pour DeepSeek V4.1 Flash.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-53"></a>
### Cas 53: [Temps et coût par tâche dans Agent Arena](https://x.com/arena/status/2120940869889175840) (par [@arena](https://x.com/arena))

**Examinez la latence, le coût et les tokens de sortie en plus de la réussite globale.**

Agent Arena indique une médiane de 5,3 minutes et 1,60 dollar par tâche pour Hydrogen High. Le modèle consomme davantage de tokens de sortie que Carbon et Argon lors de cette évaluation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-54"></a>
### Cas 54: [Tests de documents visuels et de terminal](https://x.com/ArtificialAnlys/status/2120941511223185722) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Séparez les résultats sur les documents et le terminal avant de choisir le niveau de raisonnement.**

Artificial Analysis rapporte de bons résultats sur les documents visuels. Le niveau supérieur améliore le score sur les tâches scientifiques, mais le score Terminal-Bench général reste à 54 %.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-55"></a>
### Cas 55: [Résultats Vals Index et Tax Agent](https://x.com/ValsAI/status/2120943893894303808) (par [@ValsAI](https://x.com/ValsAI))

**Consultez les tâches spécialisées en complément du résultat global.**

Vals AI indique 68,5 % sur son indice et une première place sur Tax Agent au moment du test.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-56"></a>
### Cas 56: [Hydrogen avec le réglage par défaut dans CursorBench](https://x.com/cursor_ai/status/2120944639633211619) (par [@cursor_ai](https://x.com/cursor_ai))

**Utilisez le score par défaut comme point de départ pour tester votre propre dépôt.**

Cursor rapporte 54,3 % pour Hydrogen avec le réglage par défaut et 39,6 % pour Gemini 3.8 Flash sur son benchmark.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-57"></a>
### Cas 57: [Une bataille d’archers animée par quatre modèles](https://x.com/IndependentEco/status/2120945011277590733) (par [@IndependentEco](https://x.com/IndependentEco))

**Comparez la lisibilité des actions des combattants dans chaque animation.**

L’auteur montre côte à côte les versions de Hydrogen, Fable 5.2, GPT-6.1 Sol et Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-61"></a>
### Cas 61: [Hydrogen dans Devin FrontierCode](https://x.com/cognition/status/2120950876248641588) (par [@cognition](https://x.com/cognition))

**Examinez si les correctifs peuvent être fusionnés et notez l’environnement d’exécution.**

Cognition annonce 38,2 % dans FrontierCode 2.0. Hydrogen y utilise un environnement différent de Devin CLI, utilisé pour les modèles de comparaison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-64"></a>
### Cas 64: [Une recherche Web malgré une consigne explicite](https://x.com/amanunreal/status/2120954045615768054) (par [@amanunreal](https://x.com/amanunreal))

**Vérifiez que les outils sont restés inutilisés si la réponse doit se passer de navigation.**

L’auteur indique que Hydrogen a fait une recherche malgré l’interdiction de rechercher et d’appeler des outils. Il présente un exemple sans mesurer sa fréquence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-12

---

<a id="case-65"></a>
### Cas 65: [Suivre le quota lors d’un essaim Antigravity](https://x.com/HarshithLucky3/status/2120954399971487774) (par [@HarshithLucky3](https://x.com/HarshithLucky3))

**Suivez les tokens et le quota consommé lors d’une session multiagents.**

L’auteur indique 17 millions de tokens et 21 % d’un plafond de cinq heures avec Swarm sur son forfait. Ces chiffres concernent sa session.

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

Type: Evaluation | Date: 2026-11-12

---

<a id="case-66"></a>
### Cas 66: [Appels d’outils pour des tâches professionnelles](https://x.com/mercor/status/2120957582139642095) (par [@mercor](https://x.com/mercor))

**Étudiez la collecte de contexte avant l’exécution d’une tâche professionnelle.**

Mercor rapporte 78,0 % de réussite à la première tentative sur APEX-Agents et 93 appels d’outils en moyenne. L’évaluation couvre le droit, le conseil et la banque.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-68"></a>
### Cas 68: [Quatre modèles animent un mage et un dragon](https://x.com/IndependentEco/status/2120964690906161461) (par [@IndependentEco](https://x.com/IndependentEco))

**Comparez la mise en scène, la lisibilité des actions et les effets sur le même sujet.**

La vidéo compare Hydrogen et trois modèles Claude dans un combat entre un mage et un dragon. L’auteur préfère le rendu de Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-71"></a>
### Cas 71: [MazeBench révèle des taux de réussite faibles](https://x.com/patience_cave/status/2120973681937809766) (par [@patience_cave](https://x.com/patience_cave))

**Testez le raisonnement spatial sur des labyrinthes avant de vous y fier.**

Le comparatif affiche 1 % pour Hydrogen, 4 % pour Sonnet 5.5 et 8 % pour GPT-6.1 Terra dans cette configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-72"></a>
### Cas 72: [Trois Gemini réalisent des scènes de voiliers](https://x.com/Octoberry/status/2120974412144902376) (par [@Octoberry](https://x.com/Octoberry))

**Comparez les mouvements et les détails du décor sur une scène Three.js.**

L’auteur montre les versions Hydrogen, Argon et Carbon. Il préfère les détails de Carbon et juge Hydrogen proche d’Argon dans son test.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-75"></a>
### Cas 75: [Un numéro de maillot épuise le budget de raisonnement](https://x.com/skalskip92/status/2120994631072776235) (par [@skalskip92](https://x.com/skalskip92))

**Prévoyez un plafond de raisonnement et une solution de repli pour les petits détails visuels.**

L’évaluateur indique que Hydrogen XHigh a consommé 131 069 tokens de raisonnement sans donner le numéro après 9 minutes et 55 secondes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-12

---

<a id="case-76"></a>
### Cas 76: [Plusieurs familles de modèles dans ClutterBench](https://x.com/AdamHoltererer/status/2121000759118459138) (par [@AdamHoltererer](https://x.com/AdamHoltererer))

**Évaluez la robustesse au désordre visuel avec un test ciblé.**

Dans les résultats publiés, Hydrogen devance les Gemini présentés et reste derrière les modèles OpenAI du comparatif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-12

---

<a id="case-78"></a>
### Cas 78: [Un buste anatomique en coupe façon Minecraft](https://x.com/jan_volad/status/2121026531472339340) (par [@jan_volad](https://x.com/jan_volad))

**Vérifiez que la coupe comporte les structures internes demandées.**

L’auteur confie le même exercice à Hydrogen et Argon en une seule tentative. Il reconnaît, selon son compte rendu, le crâne, les côtes et la colonne dans le rendu Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-79"></a>
### Cas 79: [Trois modèles réalisent le même accessoire](https://x.com/luckeyfaraday/status/2121030005899825504) (par [@luckeyfaraday](https://x.com/luckeyfaraday))

**Suivez séparément la consommation de tokens et la qualité, même si un modèle est moins cher par token.**

Le rendu d’un accessoire en forme de fusil compare Hydrogen, Carbon et Fable 5.2. L’auteur annonce 3,69 millions de tokens et 1,62 dollar pour Hydrogen, contre 398 000 et 0,77 dollar pour Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

Type: Evaluation | Date: 2026-11-12

---

<a id="case-80"></a>
### Cas 80: [Benchmark d’induction et consommation de tokens](https://x.com/s_batzoglou/status/2121037853258129811) (par [@s_batzoglou](https://x.com/s_batzoglou))

**Relevez les entrées et sorties facturées en parallèle des scores de raisonnement.**

L’évaluateur place Hydrogen quatrième sur 100 problèmes, près d’Opus 5.5. Il indique 55 millions de tokens de sortie et 307 millions d’entrée facturés, sans établir le mécanisme comptable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-83"></a>
### Cas 83: [Trois modèles animent un animal en 3D](https://x.com/leo114119/status/2121054098753785915) (par [@leo114119](https://x.com/leo114119))

**Examinez l’anatomie et le mouvement sur une consigne commune.**

La source compare Hydrogen, GPT-6.1 Terra et Claude Haiku 5.5. L’auteur relève des faiblesses de Hydrogen sur cet exercice.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-84"></a>
### Cas 84: [Hydrogen et Qwen sur ts-bench](https://x.com/gosrum/status/2121058334552060102) (par [@gosrum](https://x.com/gosrum))

**Examinez les erreurs d’appels d’outils avec le résultat global.**

La source compare Hydrogen à Qwen4 Max Preview sur ts-bench et commente la fiabilité des appels. La capture présente les résultats des essais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-85"></a>
### Cas 85: [Une simulation commerciale dans Vending-Bench](https://x.com/andonlabs/status/2121061429889642497) (par [@andonlabs](https://x.com/andonlabs))

**Comparez les revenus simulés avec le coût de fonctionnement de l’agent.**

Andon Labs place Hydrogen troisième dans Vending-Bench 2 et lui attribue davantage de revenus que les modèles de prix comparable dans la simulation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-89"></a>
### Cas 89: [Quatre modèles construisent une île miniature](https://x.com/xKaka1456/status/2121111495358697924) (par [@xKaka1456](https://x.com/xKaka1456))

**Comparez les rendus avec le temps et les coûts dans chaque environnement.**

L’auteur rapporte 4 minutes pour Hydrogen, 20 pour GPT-6.1 Terra, 40 pour Sol et 60 pour DeepSeek. L’absence de coût supplémentaire pour Hydrogen vaut pour sa configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-91"></a>
### Cas 91: [Comparaison de déchirures de tissu en code](https://x.com/MichaelLee009/status/2121126779276402904) (par [@MichaelLee009](https://x.com/MichaelLee009))

**Testez l’étirement, la déchirure et l’interaction avec la fourrure sur une même consigne.**

L’auteur préfère le rendu de Claude Fable 5.2 à celui de Hydrogen. Les réglages et la justesse physique n’ont pas été vérifiés séparément.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-94"></a>
### Cas 94: [Une vérification avec une source introuvable](https://x.com/cagrimbakirci/status/2121130756684886279) (par [@cagrimbakirci](https://x.com/cagrimbakirci))

**Exigez une référence consultable avant d’agir sur un verdict concernant une capture.**

L’auteur rapporte que Hydrogen a validé la publication et invoqué plusieurs fois un outil de vérification sans montrer la source.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-13

---

<a id="case-96"></a>
### Cas 96: [Hydrogen et Sol dessinent un pélican en 2D](https://x.com/YxzRainy/status/2121148582166491164) (par [@YxzRainy](https://x.com/YxzRainy))

**Comparez le délai et le mouvement sur une même animation 2D simple.**

L’auteur indique 28 secondes pour Hydrogen et 6 minutes 51 pour GPT-6.1 Sol. Il montre les deux pélicans à vélo sans établir que les réglages étaient identiques.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-98"></a>
### Cas 98: [Quatre jeux de déplacement à la toile d’araignée](https://x.com/StatsWire/status/2121172215182065807) (par [@StatsWire](https://x.com/StatsWire))

**Comparez déplacement et commandes avec la même contrainte de fichier unique.**

Les quatre Gemini réalisent le même défi 3D dans un HTML autonome sans ressources externes. Hydrogen utilise Extra High, les autres High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-100"></a>
### Cas 100: [Quatre modèles réalisent un diorama architectural](https://x.com/Jackson77li/status/2121172890838352306) (par [@Jackson77li](https://x.com/Jackson77li))

**Comparez les choix d’éclairage sur le même plan architectural.**

L’auteur montre Hydrogen, GPT-6.2, Claude Fable 5.2 et DeepSeek sur la même consigne déclarée. Son classement et ses commentaires de vitesse sont subjectifs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-103"></a>
### Cas 103: [Trois modèles rendent une scène de train](https://x.com/xKaka1456/status/2121193705810104515) (par [@xKaka1456](https://x.com/xKaka1456))

**Comparez le délai d’une même scène avec vos réglages de modèles.**

L’auteur indique environ 3 minutes pour Hydrogen, 20 pour GPT-6.1 Terra et 68 pour Qwen4 Max Preview. La vidéo montre les scènes, sans documenter les itérations et réglages.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-104"></a>
### Cas 104: [Un Chinatown pluvieux avec le réglage Extra](https://x.com/qingzhoucloud/status/2121198911515967952) (par [@qingzhoucloud](https://x.com/qingzhoucloud))

**Chronométrez et inspectez le rendu avant de choisir un niveau de raisonnement pour une animation longue.**

L’auteur annonce presque quatre heures pour son MP4 avec Hydrogen Extra, sur une consigne d’un autre créateur. Les conditions de l’essai Fable 5.2 ne sont pas entièrement comparables.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-106"></a>
### Cas 106: [Trois modèles visualisent des planètes](https://x.com/Stargridcompass/status/2121208957276713181) (par [@Stargridcompass](https://x.com/Stargridcompass))

**Comparez les rendus d’une même consigne d’interface scientifique.**

L’auteur montre Claude Fable 5.2, GPT-6.2 Sol et Hydrogen. Son classement est une appréciation visuelle, sans note objective ni réglages appariés établis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-107"></a>
### Cas 107: [Quatre modèles recréent Chrome Dino](https://x.com/noclipepe/status/2121219775170761044) (par [@noclipepe](https://x.com/noclipepe))

**Mesurez le temps de chaque reproduction et comparez les résultats jouables.**

L’auteur indique 18 minutes 41 pour Hydrogen dans AI Studio et 45 minutes 30 pour Fable 5.2. La vidéo inclut Qwen4-Max-Preview, Carbon et ses notes visuelles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-109"></a>
### Cas 109: [Deux agents de code réalisent des navires différents](https://x.com/marcthecreatorr/status/2121221667619852660) (par [@marcthecreatorr](https://x.com/marcthecreatorr))

**Comparez le premier résultat exploitable et le coût des révisions dans votre environnement.**

L’auteur utilise une même consigne avec Sonnet dans Claude Code et Hydrogen dans Cursor. Hydrogen termine plus vite selon lui, mais nécessite une seconde version.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-111"></a>
### Cas 111: [Un siège au trébuchet testé avec quatre modèles](https://x.com/StatsWire/status/2121226579141386285) (par [@StatsWire](https://x.com/StatsWire))

**Comparez des prototypes de physique jouables et notez les niveaux de raisonnement.**

L’auteur teste quatre Gemini avec des centaines de blocs. Il rapporte 10 minutes 3 pour Hydrogen Extra High, 23 minutes 33 pour Carbon High, et le meilleur délai pour Gemini 3.8 Flash High.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-116"></a>
### Cas 116: [Mémoire persistante dans FrontierMemory](https://x.com/Letta_AI/status/2121255895745351874) (par [@Letta_AI](https://x.com/Letta_AI))

**Comparez le score et le coût par exécution avant de choisir un modèle pour la mémoire d’un agent.**

Letta indique 64,4 % et environ 100 dollars par essai pour Hydrogen, à égalité avec Argon au score. Dans ces réglages, Carbon obtient 71,1 % pour environ 94 dollars.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-117"></a>
### Cas 117: [Hydrogen dans un agent vocal LiveKit défaillant](https://x.com/livekit/status/2121256982023672076) (par [@livekit](https://x.com/livekit))

**Provoquez une panne contrôlée pour voir si l’agent annonce des résultats non vérifiés.**

LiveKit rapporte zéro faux compte rendu lors de son test avec Hydrogen. Le fournisseur compare avec Gemini 3.8 Flash et renvoie vers son compte rendu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-123"></a>
### Cas 123: [Trois Gemini animent un cycliste](https://x.com/AI_Screening/status/2121281026916057443) (par [@AI_Screening](https://x.com/AI_Screening))

**Comparez les mouvements sur la même consigne et mesurez chaque essai.**

L’auteur montre Carbon, Argon et Hydrogen. Il indique environ 90 secondes pour Hydrogen et plus de cinq minutes pour Argon, et préfère le rendu Carbon.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-126"></a>
### Cas 126: [Deux modèles construisent un monde LEGO](https://x.com/kepochnik/status/2121286219669836027) (par [@kepochnik](https://x.com/kepochnik))

**Comparez ce que chaque modèle construit dans le délai indiqué.**

L’auteur présente Fable 5.2 et Hydrogen sur la création d’un monde LEGO, avec 44 et 28 minutes respectivement lors de ses essais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-127"></a>
### Cas 127: [Réparer des bugs réintroduits dans deux dépôts](https://x.com/PawelHuryn/status/2121286545223086302) (par [@PawelHuryn](https://x.com/PawelHuryn))

**Semez des défauts connus pour mesurer les réparations qu’un agent peut effectuer.**

L’évaluateur introduit 105 bugs dans deux dépôts. Hydrogen Extra High se place juste derrière Sonnet 5.5 au même niveau dans cette configuration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-128"></a>
### Cas 128: [Un bonhomme face au curseur avec deux modèles](https://x.com/DanielZambrini/status/2121289822677483740) (par [@DanielZambrini](https://x.com/DanielZambrini))

**Comparez la réaction des deux animations au pointeur.**

L’auteur préfère le résultat de Fable et estime que Hydrogen convient pour une tentative moins coûteuse.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-130"></a>
### Cas 130: [Deux modèles animent un paysage de montagne](https://x.com/ZryMiller/status/2121295750122594440) (par [@ZryMiller](https://x.com/ZryMiller))

**Comparez séparément composition, délai et coût.**

L’auteur montre les résultats de Hydrogen et Opus 5.5. Il annonce 20 minutes 30 et 0,50 dollar contre 11 minutes 23 et 2,50 dollars.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-131"></a>
### Cas 131: [Traduction de l’anglais au persan en environnement personnalisé](https://x.com/MatinSenPai/status/2121296733258887365) (par [@MatinSenPai](https://x.com/MatinSenPai))

**Notez un passage difficile par rapport à une traduction humaine.**

L’auteur donne 94 sur 100 à Hydrogen sur sa propre tâche de traduction. La note subjective dépend de son environnement.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-11-13

---

<a id="case-133"></a>
### Cas 133: [Quatre modèles construisent un navire qui coule](https://x.com/remoteugur/status/2121302956741902451) (par [@remoteugur](https://x.com/remoteugur))

**Évaluez séparément fidélité visuelle, coût et durée pour la même scène.**

L’auteur indique 8,6 minutes et 1,16 dollar pour Hydrogen, contre 10,8 minutes et 1,06 dollar pour Gemini 3.8 Flash. Il teste aussi Carbon et Opus 5.5, qu’il trouve plus réaliste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-135"></a>
### Cas 135: [Comparaison à l’aveugle de quatre textes](https://x.com/quintanilha/status/2121315967447757299) (par [@quintanilha](https://x.com/quintanilha))

**Masquez les noms des modèles avant de choisir le texte à retenir.**

L’auteur préfère Hydrogen dans son test de rédaction à l’aveugle. Il le trouve également plus rapide et moins cher que Carbon dans cet essai.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-11-13

---

<a id="case-136"></a>
### Cas 136: [Détection et lecture selon le niveau de raisonnement](https://x.com/skalskip92/status/2121322414453694489) (par [@skalskip92](https://x.com/skalskip92))

**Mesurez séparément la précision de détection, la lecture de texte, le coût et la latence.**

L’évaluateur indique 29,3 secondes par image et des scores de 64,6 en détection et 87,2 en lecture pour Hydrogen High. Carbon High marque plus aux deux tests, avec plus de coût et de latence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-13

---

<a id="case-137"></a>
### Cas 137: [Quatre modèles recréent la maison de Là-haut](https://x.com/noclipepe/status/2121326233044537688) (par [@noclipepe](https://x.com/noclipepe))

**Comparez les compromis de construction 3D en gardant la même image et la même consigne.**

L’auteur indique que Hydrogen a été le plus rapide et le moins cher des quatre essais, mais préfère Fable. Les réglages et coûts sont rapportés par l’auteur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-144"></a>
### Cas 144: [Un clip de danse à caméra fixe](https://x.com/notoro_ai/status/2121427503952834562) (par [@notoro_ai](https://x.com/notoro_ai))

**Vérifiez que l’animation conserve le personnage, le cadrage et l’angle de caméra.**

L’auteur publie une consigne japonaise et un clip associé à Hydrogen dans Gemini. Le cadre et le style doivent rester fixes. Le modèle de rendu vidéo n’est pas établi.

**Consigne:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-145"></a>
### Cas 145: [Un agent de code bloqué sur son test initial](https://x.com/Its_lakshya_ai/status/2121431788266659919) (par [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**Fixez une durée limite pour les tests de référence et inspectez leur progression.**

La capture montre Hydrogen dans Antigravity encore au test initial après une longue attente. L’auteur demande de l’arrêter et d’enquêter avant de reprendre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-14

---

<a id="case-147"></a>
### Cas 147: [Deux modèles construisent un bras robotisé interactif](https://x.com/gmi_cloud/status/2121467337119588834) (par [@gmi_cloud](https://x.com/gmi_cloud))

**Vérifiez que les articulations Three.js réagissent de façon cohérente.**

GMI Cloud montre Hydrogen et Sonnet 5.5 sur la même tâche. Le fournisseur préfère Sonnet dans ce comparatif et partage les résultats enregistrés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-151"></a>
### Cas 151: [Hydrogen et Sol construisent un village enneigé](https://x.com/badboyfoxy/status/2121501015442669866) (par [@badboyfoxy](https://x.com/badboyfoxy))

**Jugez séparément le délai, le coût et la qualité de la scène.**

L’auteur indique trois minutes et 1,37 dollar pour Hydrogen High, contre quinze minutes et 4,03 dollars pour Sol High. Il préfère le village de Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-152"></a>
### Cas 152: [Une île Three.js aux niveaux High et Ultra](https://x.com/laopai1990/status/2121502334866096160) (par [@laopai1990](https://x.com/laopai1990))

**Notez les niveaux de raisonnement et comparez les visuels et délais sans assimiler les quotas.**

L’auteur rapporte environ 90 secondes pour Hydrogen High et 30 minutes pour GPT-6.1 Sol Ultra. Les coûts sont estimés et les niveaux diffèrent.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-157"></a>
### Cas 157: [Détails d’une manette PS5 en 3D](https://x.com/Stargridcompass/status/2121528563254043015) (par [@Stargridcompass](https://x.com/Stargridcompass))

**Comparez les ombres des boutons et les détails à l’arrière et sur les côtés.**

L’auteur indique environ trois minutes pour Hydrogen High et onze pour GPT-6.2 Sol. Il juge les commandes latérales et arrière plus complètes chez Sol.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-159"></a>
### Cas 159: [CursorBench selon le budget de raisonnement](https://x.com/Beamsters1/status/2121538515909628111) (par [@Beamsters1](https://x.com/Beamsters1))

**Comparez les taux de réussite de plusieurs réglages avant de choisir le plus rapide.**

L’auteur observe une forte hausse de la réussite de Hydrogen sur CursorBench 4.0 lorsque le budget augmente. Le constat concerne les réglages testés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-14

---

<a id="case-160"></a>
### Cas 160: [Trois modèles réalisent un temple stellaire](https://x.com/YxzRainy/status/2121551796766376081) (par [@YxzRainy](https://x.com/YxzRainy))

**Évaluez la stabilité du rendu indépendamment des détails visuels.**

L’auteur compare Hydrogen, DeepSeek V4.1 1017 et Qwen4 Max Preview. Il rapporte un rendu Hydrogen plus rapide, sans écran noir ni scintillement, mais moins détaillé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-162"></a>
### Cas 162: [Remettre en question une stratégie de migration](https://x.com/is_llll/status/2121565725072490559) (par [@is_llll](https://x.com/is_llll))

**Demandez à plusieurs agents si la migration doit remplacer l’architecture en place.**

L’auteur montre Hydrogen et Argon approuvant l’approche existante, alors que Claude Opus propose de la remplacer et de migrer plus tôt. Le jugement concerne un seul projet.

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

Type: Limit | Date: 2026-11-14

---

<a id="case-165"></a>
### Cas 165: [Deux modèles interprètent une évasion d’un temple](https://x.com/runable_hq/status/2121596515474964556) (par [@runable_hq](https://x.com/runable_hq))

**Comparez l’effet de l’éclairage et de l’ambiance sur la lisibilité du même jeu.**

Runable présente les versions Hydrogen et Argon. Le fournisseur décrit un rendu Hydrogen plus sombre et un rendu Argon plus lumineux.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-166"></a>
### Cas 166: [Trois modèles Gemini animent un buggy de rallye](https://x.com/teddyaisi/status/2121604816380010719) (par [@teddyaisi](https://x.com/teddyaisi))

**Évaluez la suspension et l’adhérence dans un virage relevé.**

L’auteur compare Carbon, Argon et Hydrogen sur une animation Three.js dans une carrière. La consigne demande une suspension qui se comprime et une glissade sur terre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-169"></a>
### Cas 169: [Deux modèles animent Chasing Views](https://x.com/VulKan42069/status/2121625271493382166) (par [@VulKan42069](https://x.com/VulKan42069))

**Comparez rendu et durée en tenant compte du niveau de raisonnement.**

L’auteur montre Hydrogen Extra High et Opus 5.5 High et indique respectivement 22 et 18 minutes pour cet essai.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-170"></a>
### Cas 170: [Temps et coût dans Design Creativity Bench](https://x.com/Kombaico/status/2121635837180031129) (par [@Kombaico](https://x.com/Kombaico))

**Comparez délai et coût par création en plus de la note de créativité.**

L’évaluateur indique 49,4 pour Hydrogen avec des médianes de 3,4 minutes et 0,39 dollar. Argon est plus lent et moins cher, Carbon plus lent et plus cher dans cette évaluation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

Type: Benchmark | Date: 2026-11-14

---

<a id="case-172"></a>
### Cas 172: [Quatre modèles animent un galop dans le désert](https://x.com/Marlenuii/status/2121664345818235177) (par [@Marlenuii](https://x.com/Marlenuii))

**Comparez l’appui au sol et le transfert de poids avant l’éclairage ou les détails du maillage.**

L’auteur compare Astra, Carbon, Fable 5.2 et Hydrogen. Il préfère l’allure d’Astra et critique la construction du cheval de Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-174"></a>
### Cas 174: [Des problèmes de recherche dans FrontierCS 2](https://x.com/wenhaocha1/status/2121679887400403308) (par [@wenhaocha1](https://x.com/wenhaocha1))

**Complétez les tests de programmation par un examen orienté recherche et notez l’environnement utilisé.**

La source place Hydrogen septième par taux de réussite sur FrontierCS 2 avec Antigravity, sur des problèmes techniques issus de la recherche en informatique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

Type: Benchmark | Date: 2026-11-14

---

<a id="case-175"></a>
### Cas 175: [Rio Above the Clouds avec quatre modèles](https://x.com/EnvolDev/status/2121701704139956250) (par [@EnvolDev](https://x.com/EnvolDev))

**Comparez durée, coût et qualité perçue à partir du même sujet.**

L’évaluateur indique 6,21 dollars pour Hydrogen Extra High, son rendu le moins apprécié. Astra termine plus tôt. Le compte rendu ne vérifie pas la génération vidéo native.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-176"></a>
### Cas 176: [Hydrogen sur les tâches techniques de GBENCH](https://x.com/leo_linsky/status/2121710421891780864) (par [@leo_linsky](https://x.com/leo_linsky))

**Évaluez des résultats vérifiables avec et sans code, en tenant compte du prix et de la durée.**

L’opérateur publie des résultats GBENCH qui couvrent aussi les circuits et le raisonnement abstrait. Dans ses mesures, Sol se montre plus compétitif à prix et vitesse comparables.

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

Type: Benchmark | Date: 2026-11-14

---

<a id="case-177"></a>
### Cas 177: [Apprendre le créneau à des voitures simulées](https://x.com/noclipepe/status/2121734795738652934) (par [@noclipepe](https://x.com/noclipepe))

**Comparez la progression et le taux de réussite des simulations.**

Sur la même consigne, l’auteur rapporte 5 voitures garées sur 44 avec Hydrogen et 26 sur 40 avec Fable 5.2. Les générations ont pris 5,6 minutes et 24 minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-181"></a>
### Cas 181: [Hydrogen dans Terminal-Bench 4.0](https://x.com/gosrum/status/2121785156273160558) (par [@gosrum](https://x.com/gosrum))

**Examinez à la fois le taux d’achèvement et le coût par tâche pour choisir un modèle de programmation en ligne de commande.**

Cet essai indépendant compare Hydrogen à Claude Opus 5.5 et GPT-6.1 Sol. L’évaluateur rapporte des scores comparables et un coût intermédiaire pour Hydrogen. Il souligne le rôle de la maturité de l’environnement d’exécution.

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

Type: Benchmark | Date: 2026-11-15

---

<a id="case-183"></a>
### Cas 183: [Trois modèles Gemini animent un poulpe](https://x.com/teddyaisi/status/2121800606406885880) (par [@teddyaisi](https://x.com/teddyaisi))

**Vérifiez si la prise sur la roche entraîne un mouvement visible du corps vers l’avant.**

L’auteur montre Carbon, Argon et Hydrogen sur une scène Three.js où un poulpe s’agrippe au rebord d’un récif pour avancer. Il invite à comparer le lien entre prise du tentacule et déplacement du corps.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

Type: Evaluation | Date: 2026-11-15

---

<a id="case-187"></a>
### Cas 187: [Un test de modélisation de château](https://x.com/nemumusitocha/status/2121848375998063012) (par [@nemumusitocha](https://x.com/nemumusitocha))

**Comparez les châteaux et les ressources consommées d’un essai à l’autre.**

L’auteur montre un château en 3D obtenu avec Hydrogen et renvoie aux comparaisons précédentes. Les 3 % du quota hebdomadaire Google AI Pro concernent cet essai.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

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

Type: Evaluation | Date: 2026-11-15

---

<a id="case-191"></a>
### Cas 191: [Le délai estimé change quand le périmètre s’élargit](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (par [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Demandez au modèle quelles hypothèses et fonctionnalités justifient un changement de délai important.**

L’auteur montre un échange où le délai estimé passe d’un mois à un an après une demande de calendrier réaliste avec les fonctionnalités prévues. La durée réelle du projet reste inconnue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-15

---

<a id="case-193"></a>
### Cas 193: [Une conversion calendaire tenant compte des années bissextiles](https://x.com/itsvishaltwt/status/2121891117050589249) (par [@itsvishaltwt](https://x.com/itsvishaltwt))

**Posez une question de conversion simple et vérifiez si la réponse couvre les cas particuliers du calendrier.**

L’auteur demande à Hydrogen High et GPT combien de secondes compte une année. Les deux captures donnent les résultats pour une année ordinaire et une année bissextile. Hydrogen calcule aussi la moyenne grégorienne.

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

Type: Evaluation | Date: 2026-11-15

---

<a id="case-196"></a>
### Cas 196: [Des limites d’abonnement obsolètes dans une réponse](https://x.com/take14262/status/2121934737539514533) (par [@take14262](https://x.com/take14262))

**Confirmez le nom des modèles et les conditions actuelles auprès des sources primaires.**

L’auteur montre que Hydrogen confond des noms proches et donne des durées de validité obsolètes pour un forfait Qwen. Les captures documentent ces erreurs apparentes.

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

Type: Limit | Date: 2026-11-15

---

<a id="case-197"></a>
### Cas 197: [Revoir le récit d’une animation WebGL](https://x.com/snakajima/status/2121939899242996058) (par [@snakajima](https://x.com/snakajima))

**Demandez une progression narrative plus nette quand une première version élaborée manque de structure.**

L’auteur relie la première version WebGL et en montre une deuxième après un retour sur le bruit visuel et le manque de récit. Il préfère la révision à la première version, mais favorise toujours l’essai réalisé dans Claude Code.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

Type: Limit | Date: 2026-11-15

---

<a id="case-199"></a>
### Cas 199: [Deux modèles programment un combat de dragons](https://x.com/DrstaOne/status/2121947540509831302) (par [@DrstaOne](https://x.com/DrstaOne))

**Comparez comment chaque animation coordonne les actions de deux personnages dans une même scène.**

L’auteur compare Qwen-4 Max et Hydrogen pour un combat réalisé en code au-dessus d’un temple de montagne. L’instruction est attribuée à un autre créateur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

Type: Evaluation | Date: 2026-11-15

---

<a id="case-201"></a>
### Cas 201: [Une instruction Three.js reproductible pour animer un pélican](https://x.com/Aki_LIG/status/2121960943361896596) (par [@Aki_LIG](https://x.com/Aki_LIG))

**Vérifiez la coordination des pattes, des roues et de la direction dans une animation cycliste.**

L’auteur publie l’instruction Three.js intégrale en japonais et montre Hydrogen sur une route côtière. Il indique l’avoir aussi soumise à GPT-6.1 Terra. La vidéo associée montre l’essai Hydrogen.

**Consigne:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

Type: Evaluation | Date: 2026-11-15

---

<a id="case-205"></a>
### Cas 205: [La même maison de campagne sur trois plateformes](https://x.com/doe_naps/status/2121999317628330476) (par [@doe_naps](https://x.com/doe_naps))

**Vérifiez le format de sortie quand une tâche visuelle change de configuration ou de plateforme.**

L’auteur rapporte des images fixes avec Hydrogen High dans Antigravity, Hydrogen Extra High dans AI Studio et Carbon High dans Antigravity. Un essai libellé Hydrogen dans Arena a produit un SVG animé, sans identification indépendante de cette version.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

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

Type: Evaluation | Date: 2026-11-15

---

<a id="case-206"></a>
### Cas 206: [Deux tableaux de bord issus de la même instruction](https://x.com/fiapp_pro/status/2122014257667846338) (par [@fiapp_pro](https://x.com/fiapp_pro))

**Comparez la mise en page et la hiérarchie de l’information à partir d’un même brief d’interface.**

L’auteur juxtapose deux captures attribuées à GPT-6.1 Sol et Hydrogen. Elles permettent de comparer le rendu visuel, sans montrer les réglages, l’implémentation ni le fonctionnement.

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

Type: Evaluation | Date: 2026-11-15

---

<a id="case-209"></a>
### Cas 209: [Deux modèles programment une animation à défilement latéral](https://x.com/rubenssoto_ai/status/2122035198728814753) (par [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Comparez la continuité des mouvements et le coût pour une scène d’action.**

L’auteur compare Hydrogen et GPT-6 Astra sur une animation latérale. Il préfère la fluidité des mouvements de Hydrogen et indique un coût inférieur dans ces deux essais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

Type: Evaluation | Date: 2026-11-15

---

<a id="case-212"></a>
### Cas 212: [Des formules sans mise en forme dans une réponse en japonais](https://x.com/ToraMutton/status/2122131489718759930) (par [@ToraMutton](https://x.com/ToraMutton))

**Vérifiez le rendu et l’exactitude des réponses contenant des commandes TeX.**

L’auteur montre une réponse Gemini en japonais qui affiche la notation brute au lieu des équations mises en forme après le passage à Hydrogen. La capture illustre un échec de rendu dans son interface.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

Type: Limit | Date: 2026-11-16

---

<a id="case-214"></a>
### Cas 214: [Tester une consigne de non-réponse](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (par [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Vérifiez si le modèle peut s’abstenir de répondre lorsque le flux de travail l’exige.**

L’auteur partage une capture d’un test de non-réponse et rapporte des différences entre Carbon et Argon. La publication montre une seule série d’essais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

Type: Evaluation | Date: 2026-11-16

---

<a id="case-216"></a>
### Cas 216: [Trois modèles expliquent un moteur électrique](https://x.com/analogalok/status/2122221106304352257) (par [@analogalok](https://x.com/analogalok))

**Comparez la lisibilité et les commandes pédagogiques à partir d’une même demande de simulation.**

L’auteur compare Hydrogen à deux modèles Qwen et préfère son moteur 3D et ses explications de physique. C’est son appréciation dans un seul essai.

**Consigne:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

Type: Evaluation | Date: 2026-11-16

---

<a id="case-217"></a>
### Cas 217: [Deux flux de travail animent une scène de bureau](https://x.com/GeroXBT/status/2122234332102435128) (par [@GeroXBT](https://x.com/GeroXBT))

**Vérifiez les détails, le volume sonore et l’arrêt sur image final par rapport à la demande d’origine.**

L’auteur compare Hydrogen et Astra avec une même instruction dans un environnement API. Selon lui, la version Gemini est plus fluide, mais la scène continue de bouger à la fin et son volume est moindre. Le système de rendu n’est pas précisé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

Type: Evaluation | Date: 2026-11-16

---

<a id="case-221"></a>
### Cas 221: [Un village 2D au son procédural](https://x.com/marcthecreatorr/status/2122266495216459841) (par [@marcthecreatorr](https://x.com/marcthecreatorr))

**Vérifiez si le son réagit à ce qui se passe à l’écran et suivez le temps de création.**

L’auteur compare Qwen 4 Max et Hydrogen au niveau Extra High. Il indique environ 75 minutes et 0,90 USD avec Qwen, contre 12 minutes et 1,70 USD avec Hydrogen. Il préfère la synchronisation musicale de Hydrogen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[Lire la vidéo source](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

Type: Evaluation | Date: 2026-11-16

---

<a id="related-repositories"></a>
## Dépôts associés

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Exemples et comparaisons de Gemini 4 Carbon

<a id="acknowledge"></a>
## 🙏 Remerciements

Merci aux créateurs, développeurs et évaluateurs qui ont partagé publiquement leur travail avec Hydrogen.

**Créateurs des sources:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*L’attribution suit les sources publiques citées et peut ne pas identifier le créateur initial. Pour une correction ou une demande de retrait, ouvrez un ticket avec une source publique.*

Proposez un exemple étayé par une source via un ticket ou une demande de fusion, en suivant la liste de contrôle des contributions.
