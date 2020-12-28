# Bienvenue sur mon projet PrestaShop !
Il s'agit d'un projet réalisé en Novembre-Décembre 2020 dans le cadre de ma formation "Expert DevOps" chez OpenClassRooms.

## Ca fait quoi ?
Ca fait de l'Intégration Continue ( CI ) à l'aide de Jenkins, à l'attention d'une équipe de QA qui a en charge de vérifier le bon fonctionnement des développements réalisés sur PrestaShop, et qui souahite automatiser ses tests unitaires et fonctionnels

## Ca ressemble à quoi ?
J'ai utilisé les plugins Blue Ocean pour obtenir un affichage plutôt sympa : 
![Vue globale du Pipeline de CI](https://github.com/alinuxien/PrestaShop/raw/develop/pipeline.png)
![Résultats des Tests](https://github.com/alinuxien/PrestaShop/raw/develop/tests.png)

## Contenu ?
Le dépôt est basé sur la branche `develop` du dépôt officiel de [PrestaShop](https://github.com/PrestaShop/PrestaShop)

Les fichiers spécifiques que j'ai préparés/personnalisés sont : 
- Jenkinsfile
- docker-compose.yml
- le répertoire .docker qui contient entre autre le Dockerfile pour "packager" l'application 
- le répertoire tests/Functional

## J'ai besoin de quoi ?
D'un environnement de travail Jenkins, dont 1 VM est [disponible ici](https://github.com/alinuxien/jenkins)

## Comment ça s'utilise ?
Il suffit de cloner ce dépôt, paramétrer un "projet" Jenkins pour scanner ce dépôt cloné, et le reste est automatique.

# Et après ?
Il suffit de créer des tests de QA automatisés par Selenium, en Python ou autre, sur Chrome, Firefox..., en s'inspirant des fichiers contenus dans tests/Functional

