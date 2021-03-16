#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:31:25 2021

@author: philippe
"""

import cgi,cgitb,json

cgitb.enable()
form = cgi.FieldStorage()
liste_images = []
liste_themes = []
orientation_H = 0
orientation_V = 0
orientation_prefere = ""

if form.getvalue("nom_utilisateur"):
    username = form.getvalue("nom_utilisateur")
if form.getvalue("image_0"):
    liste_images.append(form.getvalue("image_0"))
if form.getvalue("image_1"):
    liste_images.append(form.getvalue("image_1"))
if form.getvalue("image_2"):
    liste_images.append(form.getvalue("image_2"))
if form.getvalue("image_3"):
    liste_images.append(form.getvalue("image_3"))
if form.getvalue("image_4"):
    liste_images.append(form.getvalue("image_4"))

with open('data.json') as json_file :
    data = json.load(json_file)
    for p in data : 
        if (p["nom"] in liste_images) : 
            if (p["theme"] not in liste_images) : 
                liste_themes.append(p["theme"])
            if(p["orientation"] == "portrait") : 
                orientation_V += 1
            else : 
                orientation_H += 1
if (orientation_V > orientation_H) : 
    orientation_prefere = "portrait"
else :  
    orientation_prefere = "paysage"
        
dico_profil_utilisateur = {"nom_utilisateur":username,"image_like":liste_images,"theme_like":liste_themes,"orientation_perfere":orientation_prefere}

print("Content-type: text/html; charset=utf-8\n")
html ="""
<html>
    <body>
       <h1> Merci """+str(username)+""", Nous avons créé votre profil. </h1>
       Deux choix possibles : 
           <ul>
               <li> <a href=''>Etiquetage des images </a></li>
               <li> <a href=''>Voir des images </a></li>
           </ul>
    </body>
</html>
"""

print(html)    