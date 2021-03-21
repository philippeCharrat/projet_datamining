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
liste_images_unlike = []
liste_themes = []
orientation_H = 0
orientation_V = 0
orientation_prefere = ""

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

with open('data.json') as json_file :
    data = json.load(json_file)
    data = data["data"]
    for p in data : 
        if (p["nom"] in liste_images) : 
            if (p["theme"] not in liste_themes) : 
                liste_themes.append(p["theme"])
            if(p["orientation"] == "portrait") : 
                orientation_V += 1
            else : 
                orientation_H += 1
        if (p["nom"] in liste_images_unlike) : 
             liste_themes.append(p["theme"])   
if (orientation_V > orientation_H) : 
    orientation_prefere = "portrait"
else :  
    orientation_prefere = "paysage"
        
dico_profil_utilisateur = {"nom_utilisateur":username,"image_like":liste_images,"image_unlike":liste_images_unlike,"theme_test":liste_themes,"orientation_perfere":orientation_prefere}
fichier = open("Profil/profil_"+str(username)+".json","w")
str_dico_profil = str(dico_profil_utilisateur).replace("\'","\"")
fichier.write(str_dico_profil)
fichier.close()
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