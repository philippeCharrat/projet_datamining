#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script pour la prédiction d'image recommandées.
"""


import cgi,cgitb,json

"""Activation de CGI pour les erreurs"""
cgitb.enable()

"Déclaration des variables"
form = cgi.FieldStorage()
liste_images = []
liste_images_unlike = []
dico_themes = {}
orientation_H = 0
orientation_V = 0
orientation_prefere = ""

""""
Récupération des informations de l'utilisateur
Stockage dans des listes
"""
if form.getvalue("nom_utilisateur"):
    username = form.getvalue("nom_utilisateur")
if form.getvalue("image_0"):
    liste_images.append(form.getvalue("image_0"))
else:
    liste_images_unlike.append(form.getvalue("invisible_0"))
if form.getvalue("image_1"):
    liste_images.append(form.getvalue("image_1"))
else:
    liste_images_unlike.append(form.getvalue("invisible_1"))
if form.getvalue("image_2"):
    liste_images.append(form.getvalue("image_2"))
else:
    liste_images_unlike.append(form.getvalue("invisible_2"))
if form.getvalue("image_3"):
    liste_images.append(form.getvalue("image_3"))
else:
    liste_images_unlike.append(form.getvalue("invisible_3"))
if form.getvalue("image_4"):
    liste_images.append(form.getvalue("image_4"))
else:
    liste_images_unlike.append(form.getvalue("invisible_4"))

"""
Comparaison entre data.json et formulaire pour déterminer les préférences de 
l'utilisateur.
"""
with open('data.json') as json_file :
    data = json.load(json_file)
    data = data["data"]
    for p in data : 
        if (p["nom"] in liste_images) : 
            if (p["theme"] not in dico_themes.keys()) : 
                dico_themes[p["theme"]] = 1
            else :
                dico_themes[p["theme"]] = dico_themes[p["theme"]]+ 1
            if(p["orientation"] == "portrait") : 
                orientation_V += 1
            else : 
                orientation_H += 1
                
if (orientation_V > orientation_H) : 
    orientation_prefere = "portrait"
else :  
    orientation_prefere = "paysage"

"Stockage des informations de l'utilisateur"        
dico_profil_utilisateur = {"nom_utilisateur":username,"image_like":liste_images,"image_unlike":liste_images_unlike,"theme":dico_themes,"orientation_perfere":orientation_prefere,"orientation_V":orientation_V,"orientation_H":orientation_H}
fichier = open("Profil/profil_"+str(username)+".json","w")
str_dico_profil = str(dico_profil_utilisateur).replace("\'","\"")
fichier.write(str_dico_profil)
fichier.close()

"Affichage d'autres options après création profil"
print("Content-type: text/html; charset=utf-8\n")
html ="""
<html>
    <body>
       <h1> Merci """+str(username)+""", Nous avons créé votre profil. Vous pouvez fermer cette page</h1>
    </body>
</html>
"""
print(html)    