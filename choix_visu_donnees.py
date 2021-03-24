#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:37:59 2021

@author: eremix
"""

import json
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
    <center><h2> Visualisation des données </h2></center>
    <form method="post" action="visu_donnees.py">
    <h3>Veuillez sélectionner les images que vous appréciez le plus : </h3>
        <table>
            <tr>
    """
with open('data.json') as json_file :
    data = json.loads(json_file.read())
    data = data['data']
    liste = [x for x in range(len(data))]
    for i in liste: 
        image = image +"<td><img src='"+str(data[i]["nom"])+"'></td>"
        checbox =  checbox+"<td><input type='checkbox' name='image_"+str(i)+"' value='"+str(data[i]["nom"])+"'></td>"
        hidden = hidden+"<input type='hidden' name='invisible_"+str(i)+"' value='"+str(data[i]["nom"])+"'>"
html = html + image + "</tr><tr>"+checbox+"</tr></table>"+hidden
radio_btn = """<input type = "radio" name = "visu_type" value = "bar_graph" /> Graphe en barres <br>
<input type = "radio" name = "visu_type" value = "compo" /> Composition de la photo <br>
<input type = "radio" name = "visu_type" value = "clusters" /> Couleurs prédominantes <br>"""
html = html + radio_btn +"""
        <input type='submit' value='Je confirme mon choix'>
    </form>
    </body>
</html>
"""
print(html)