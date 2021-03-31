# Projet Data Mining 
###### Auteurs : Philippe CHARRAT et Clément CORNU
###### Version : 1.1
###### Date : 31/03/2021

## Objectif
Création d'un système de recommendation d'images via des profils, dans le cadre du module Data Mining de CPE Lyon. 

## Langages utilisés
- Python
- Sparql
- HTML/CSS

## Pré-requis à l'utilisation de ce programme
- Bibliothèques appelées :
  - cgi
  - cgitb
  - json
  - numpy
  - sickit-learn
  - pandas
  - urllib.request
  - qwikidata.sparql
  - Pillow
  - webbrowser
  - webcolors
  - graphviz
  - http.server
  - matplotlib
- Le mot de passe administrateur est à renseigner dans le script `main.py`.
- Le port 80 doit être libre. Sinon, modifier le port dans `serveur.py`

## Fonctionnement
- Un script principal (`main.py`) qui va effectuer les étapes suivantes :
  - Création d'un deuxième processus, pour exécuter en administrateur un serveur web sur le port 80.
  - Début d'une boucle infinie où l'utilisateur a le choix entre 7 actions différentes :
      - Création de profil via `index.py` : initialisation d'un profil utilisateur en .json ;
      - Ajout d'une balise via `ajout_balise.py` : lancement d'une page web proposant une photo à l'utilisateur et l'invitant à renseigner une balise pour celle-ci
      - Recommendation d'une image via `script_prediction_profil.py` : arbre de décision initialisé selon les préférences de l'utilisateur et lui proposant une image en fonction de ces dernières ;
      - Effacer le terminal via l'exécution de la commande `clear` du shell ;
      - Visualiser des donnees via `choix_visu_donnees.py` : lancement d'une page web invitant l'utilisateur à choisir les données qu'il souhaite visualiser et lui permettant dans un second temps de les visualiser ;
      - Lancer l'extraction et le pré-traitement des données via `extraction.py`, `pre_traitement_donnees.py` et `visu_donnees.py` : lancement de l'extraction des images, de leurs métadonnées et de leur analyse à des fins d'affichage ;
      - Connaitre vos préférences profil via `affiche_pref.py` : lancement d'une page web affichant les préférences de l'utilisateur


