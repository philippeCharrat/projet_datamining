#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script permettant de calculer/afficher les préférences de l'utilisateur
"""
import cgi,cgitb,json
# Récupération du profil à test 
try : 
    form = cgi.FieldStorage()
    profil = form.getvalue("nom_utilisateur")
    fichier_json = "Profil/profil_"+str(profil)+".json" 
    with open(fichier_json,'r') as f :
        profil_is_set = 1
 #Sinon profil inexistant ou non envoyé
except :
    profil_is_set = 0

# Traitement du profil    
if (profil_is_set == 1):
    theme_pref = ""
    iteration_theme_pref =0
    i  =0
    couleur_pref = ""
    iteration_couleur_pref =0
    type_pref = ""
    iteration_type_pref =0
    
    # Récupération de son dictionnaire 
    with open(fichier_json) as json_file :
        dico = json.loads(json_file.read())
        orientation_V = 0
        orientation_H = 0
        list_img_like = dico['image_like']
        list_img_unlike = dico['image_unlike']
        dico_themes = {}
        dico_couleur = {}
        dico_type = {}
        
    #Chargement du fichier data.json en remplaçant le nom
    with open('data.json') as json_file :
        data = json.loads(json_file.read())
        data = data["data"]
        for p in data :
            # Si l'image est dans la liste like 
            if (p["nom"] in list_img_like) :
                i += 1
                # Ajout du mode 
                if(p["orientation"] == "portrait") : 
                    orientation_V += 1
                else : 
                    orientation_H += 1
            
                if (p["theme"] not in dico_themes.keys()) : 
                    dico_themes[p["theme"]] = 1
                else :
                    dico_themes[p["theme"]] = dico_themes[p["theme"]]+ 1
                
                if (p["couleur"] not in dico_themes.keys()) : 
                    dico_couleur[p["couleur"]] = 1
                else :
                    dico_couleur[p["couleur"]] = dico_themes[p["couleur"]]+ 1                    
                
                if (p["type"] not in dico_type.keys()) : 
                    dico_type[p["type"]] = 1
                else :
                    dico_type[p["type"]] = dico_type[p["type"]]+ 1                    
                      
    
    if (orientation_V > orientation_H) : 
        orientation_prefere = "portrait"
    else :  
        orientation_prefere = "paysage"
    for p in dico_themes.keys() : 
        if (dico_themes[p] > iteration_theme_pref) :
            theme_pref = p
            iteration_theme_pref = dico_themes[p]
            
    for p in dico_couleur.keys() : 
        if (dico_couleur[p] > iteration_couleur_pref) :
            couleur_pref = p
            iteration_couleur_pref = dico_couleur[p] 
            
    for p in dico_type.keys() : 
        if (dico_type[p] > iteration_type_pref) :
            type_pref = p
            iteration_type_pref = dico_type[p]    
        
    "Stockage des informations de l'utilisateur"        
    dico_profil_utilisateur = {"nom_utilisateur":profil,"image_like":list_img_like,"image_unlike":list_img_unlike,"theme":dico_themes,"orientation_perfere":orientation_prefere,"orientation_V":orientation_V,"orientation_H":orientation_H}
    fichier = open("Profil/profil_"+str(profil)+".json","w")
    str_dico_profil = str(dico_profil_utilisateur).replace("\'","\"")
    fichier.write(str_dico_profil)
    fichier.close()
    
    "Affichage d'autres options après création profil"
    print("Content-type: text/html; charset=utf-8\n")
    html ="""
    <html>
        <style>
         td { border: 1px solid black; width:200px;}
        </style>
        <body>
           <h1> Bonjour """+str(profil)+"""</h1>
           <p> Nous pouvons vous dire que vous avez liké """+str(i)+""" 
           photos sur les """ +str(len(list_img_unlike)+i) +""" 
           proposées. Soit un poucrentage de : """+str(int(100*(i/(len(list_img_unlike)+i)))) +"""% </p></br>
           <table><tr><td>Theme : </td><td> Couleur : </td><td> Orientation :</td><td> Type :</td></tr><tr><td>"""+theme_pref+"</td><td>"+couleur_pref+"</td><td>"+orientation_prefere+"</td><td>"+type_pref+"""
           </td></tr></table></br>
           Liste de thèmes likées : </br>"""+str(dico_themes)+"""</br></br>
           Liste de couleurs likées : </br>"""+str(dico_couleur)+"""</br></br>
           Liste des types: </br>"""+str(dico_type)+"""</br></br>
           Images likées : </br>"""+str(list_img_like)+"""</br></br>
           Images unlike : </br>"""+str(list_img_unlike)+"""</br></br>
           Images à l'horizontale : """+str(orientation_H)+"""</br></br>
           Images à la verticale : """+str(orientation_V)+"""</br></br>
        </body>
    </html>
    """
    print(html)   
    
else :
    print("Content-type: text/html; charset=utf-8\n")
    html ="""
    <html>
        <style>
        </style>
        <body>
           <h1> Bonjour Erreur, votre profil n'est pas enregistré.</h1>
        </body>
    </html>
    """
    print(html)   
