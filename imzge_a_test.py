#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:56:49 2021

@author: philippe
"""

import cgi, random ,json, cgitb

cgitb.enable()
form = cgi.FieldStorage()
if form.getvalue("nom") : 
    nom = form.getvalue("nom") 
    
if form.getvalue("like_image") : 
    like = form.getvalue("like_image") 
    with open("Profil/profil_philippe.json") as json_file :
        data = json.loads(json_file.read())
        if (like == 'oui') :
            data['image_like'].append(nom)
        else :
            data['image_unlike'].append(nom)
    fichier = open("Profil/profil_philippe.json","w")
    fichier.write(str(data).replace("\'","\""))
    fichier.close()
    
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
print(html)