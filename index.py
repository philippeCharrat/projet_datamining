#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:48:41 2021

@author: philippe
"""
import cgi, random ,json,random

print("Content-type: text/html; charset=utf-8\n")
image = ""
checbox = ""
hidden = ""
html ="""
<html>
    <body>
        <style>
            img { width:100px; } 
        </style>
    <center><h2> Formulaire de création </h2></center>
    <form method="post" action="creation_profil.py">
    <h3>Votre nom : </h3>
    <input type='text' name="nom_utilisateur" required>
    <h3>Veuillez sélectionner les images que vous appréciez le plus : </h3>
        <table>
            <tr>
    """
with open('data.json') as json_file :
    data = json.loads(json_file.read())
    data = data['data']
    liste = [x for x in range(len(data))]
    for i in range(5) : 
        j = random.randint(0,len(liste)-2)
        increment = liste[j]
        image = image+"<td><img src='"+str(data[increment]["nom"])+"'></td>"
        checbox =  checbox+"<td><input type='checkbox' name='image_"+str(i)+"' value='"+str(data[increment]["nom"])+"'></td>"
        hidden = hidden+"<input type='hidden' name='invisible_"+str(i)+"' value='"+str(data[increment]["nom"])+"'>"
        del liste[j]
html = html + image + "</tr><tr>"+checbox+"</tr></table>"+hidden+"""
        <input type='submit' value='Soumettre'>
    </form>
    </body>
</html>
"""

print(html)    