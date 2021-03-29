#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script pour la gestion d'ajout d'informations dans les balises via formulaire HTML
Remarque : Impératif d'exécuter l'haromnisation des Exifs, sinon plantage.
"""
# Import des bibliothèques
import cgi, random ,json
print("Content-type: text/html; charset=utf-8\n")

"""Récupération des informations du formulaire"""
form = cgi.FieldStorage()
if form.getvalue("nom_image") : 
    ajout_balise = 1
else : 
    ajout_balise = 0

"""Si une balise a été saisie alors elle est ajoutée dans data["balise_supp"]"""
if (ajout_balise == 1) :
    with open('data.json') as json_file :
        data = json.loads(json_file.read())
        chaine_json = "{ \"data\" :["
        data = data['data']
        for p in data: 
            if p["nom"] == form.getvalue("nom_image") :
                p["balise_supp"] = form.getvalue("balise_supp")
            chaine_json = chaine_json + str(p)+","
        chaine_json = chaine_json[:-1]
        chaine_json += "]}"    
        chaine_json = chaine_json.replace("\'","\"")
    fichier = open("data.json","w")
    fichier.write(chaine_json)
    fichier.close()

# Afifchage d'une nouvelle images
with open('data.json') as json_file :
    data = json.loads(json_file.read())
    data = data['data']
    image = data[random.randint(0,len(data)-1)]
    nom = image["nom"]
    theme = image["theme"]

html ="""
<html>
    <body>
        <style>
            img { width:300px; } 
        </style>
    <center><h2> Formulaire d'ajout de balise</h2></center>
    <form method="post" action="ajout_balise.py">
    <h3>La balise supplémentaire : </h3>
    <input type='text' name="balise_supp" required>
        <input type='submit' value='Soumettre'>
    <h3>Image issue du thème : """+ theme +""": </h3>
        <center>
    """
dynamique = "<input type='hidden' name='nom_image' value='"+str(nom) +"'><img src='"+str(nom) +"'>"    
html = html + dynamique + """
        </center>
    </form>
    </body>
</html>
"""                
print(html)    