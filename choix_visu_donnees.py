#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script permettant la visualisation des données des images
"""

import json,cgi,os

print("Content-type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
image = ""
checbox = ""
hidden = ""

"""On entre ici si l'utilisateur a fait son choix"""
if form.getvalue("visu_type"):
    html ="""
    <html>
        <body>
            <style>
                img { width:500px; } 
            </style>
        <center><h2> Visualisation des données </h2></center>
            <table>
                <tr>"""
    choix = form.getvalue("visu_type")
    if choix == "bar_graph":
        for i in os.listdir("Donnees_visualisees"):
            """Affichage de tous les graphes"""
            if "_fct_de_" in i:
                image = image + "<td><img src='Donnees_visualisees/"+i+"'></td>"
    else:
        print("1")
        """Affichage des infos de la/les images sélectionnées"""
        with open('data.json') as json_file :
            #3 lignes ici sont pour récupérer le nombre d'images et garantir la bonne exécution de la boucle
            data = json.loads(json_file.read())
            data = data['data']
            liste = [x for x in range(len(data))]
            print(liste)
            for i in liste:
                #Récupération de l'image dont le bouton a été coché
                if form.getvalue("image_"+str(i)):
                    image_choisie = form.getvalue("image_"+str(i)).split("/",1)[1].split(".",1)[0]
                    image_choisie = image_choisie + ".png"
                    print(image_choisie)
                    for j in os.listdir("Donnees_visualisees"):
                        #Récupération du choix de l'utilisateur pour afficher la bonne image
                        if choix == "compo" and "Compo" in j and image_choisie in j:
                            image = image + "<td><img src='Donnees_visualisees/"+j+"'></td>"
                        if choix == "clusters" and "clusters" in j and image_choisie in j:
                            image = image + "<td><img src='Donnees_visualisees/"+j+"'></td>"
    html = html + image +"""</body>
    </html>
    """


else:
    """Choix de l'utilisateur pour affichage"""
    html ="""
    <html>
        <body>
            <style>
                img { width:100px; } 
            </style>
        <center><h2> Visualisation des données </h2></center>
        <form method="post" action="choix_visu_donnees.py">
        <h3>Veuillez sélectionner les images dont vous souhaitez voir les données: </h3>
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