#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script pour la gestion des likes sur les images recomamndées.
"""
# Import des bibliothèque
import cgi, json, cgitb

"""Utilisation de CGI pour formulaire HTML"""
cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("nom") : 
    nom = form.getvalue("nom") 
"""Affichage du code HTML"""  
print("Content-type: text/html; charset=utf-8\n")
html ="""
    <html>
        <body>
            <style>
                img { width:300px; } 
            </style>
        <center><h2> Proposition d'image</h2></center>
        <form method="post" action="">
        <h3>Vous likez la photo ?</h3>
            <input type='submit' name='like_image' value='oui'>
            <input type='submit' name='like_image' value='non'>
            <center>
        """
dynamique = "<input type='hidden' name='nom_image' value='"+str(nom) +"'><img src='"+str(nom) +"'>"    
html = html + dynamique + """
            </center>
        </form>
        </body>
    </html>
    """
"""
Récupération du choix de l'utilisateur et ajout dans les dicos d'images 
likées/unlikées afin d'affiner la future proposition
"""

if form.getvalue("like_image") : 
    like = form.getvalue("like_image") 
    with open(form.getvalue("profil")) as json_file :
        data = json.loads(json_file.read())
        if (like == 'oui') :
            data['image_like'].append(nom)
        else :
            data['image_unlike'].append(nom)
    fichier = open(form.getvalue("profil"),"w")
    fichier.write(str(data).replace("\'","\""))
    fichier.close()

    """Affichage du code HTML"""  
    html ="""
        <html>
            <body>
                <style>
                    img { width:300px; } 
                </style>
            <center> <h1> Votre choix a été pris en compte. Vous pouvez fermer la page </h1>
            </body>
        </html>
        """

print(html)