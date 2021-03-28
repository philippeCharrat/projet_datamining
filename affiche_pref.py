#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:00:56 2021

@author: philippe
"""

import cgi,cgitb,json

"""Activation de CGI pour les erreurs"""
cgitb.enable()

"Déclaration des variables"
form = cgi.FieldStorage()
fichier_json = "Profil/profil_"+str(profil)+".json" 
try : 
    with open(fichier_json,'r') as f :
        profil_is_set = 1
except :
    profil_is_set = 0
    
if (profil_is_set == 1):
    with open(fichier_json) as json_file :
        dico = json.loads(json_file.read())
        orientation_V = dico
        list_img_like = dico['image_like']
        list_img_unlike = dico['image_unlike']
        
    "Chargement du fichier data.json en remplaçant le nom"
    with open('data.json') as json_file :
            data = json.loads(json_file.read())
            for p in data :
                if (p["nom"] in list_img_like) :
                    if(p["orientation"] == "portrait") : 
                        orientation_V += 1
                    else : 
                        orientation_H += 1
                if (p["nom"] in list_img_unlike) : 
                    list_img_like[p["nom"]] = p
                    
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