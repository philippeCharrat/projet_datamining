#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:43:53 2021

@author: philippe
"""
from PIL import Image
import json, numpy, math, webcolors
from scipy.spatial import KDTree
from sklearn.cluster import KMeans
import os

def reharmonisation_date(fichier)  :
    """
        But : Réharmonisation des dates, les exifs sont "2010:03:08 13:33:40". La fonction va 
        récupérer l'année. Sans années spécifiés, on ajoute l'année 2021. 
        Remarque : A n'exécuter qu'une fois.  
        Input : 
            - fichier : string contenant le nom du fichier
        Output : 
            - int : 0
    """
    with open(fichier) as json_file :
        data = json.loads(json_file.read())
        datas = data['data']
        chaine_json = "{ \"data\" :["
        for p in datas:
            try : 
                data_inco = p["306"].split(":")
                p["306"] = int(data_inco[0]) 
                chaine_json = chaine_json + str(p)+","
            except : 
                p["306"] = 2021
        chaine_json = chaine_json[:-1]
        chaine_json += "]}"    
        chaine_json = chaine_json.replace("\'","\"")
    fichier = open("data.json","w")
    fichier.write(chaine_json)
    fichier.close()
    return 0

def convert_rgb_to_names(rgb_tuple):
    """
    But : Fonction qui retourne la couleur la couleur html la plus proche en fonction de 
    l'intensité rgb
    Input : 
        - rgb_tuple : tuple de longueur 3 contenant les intensités des pixels rouge, vert et bleu
    Output:
        - f' {names[index]}' : string de la couleur html la plus proche du tuple rgb fourni
    """  
    # a dictionary of all the hex and their respective names in css3
    css3_db = webcolors.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f' {names[index]}'


def etiquetage_couleur(image):
    """
    But : Fonction qui retourne la couleur en fonction des clusters
    Input : 
        - image : string contenant le chemin relatif de l'image (ex : "Images/nom_image.jpg")
    Output:
        - couleur_predominante : string contenant la couleur (ex : "orange")
    """    
    imgfile = Image.open(image)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters = 4)
    clusters.fit(numarray)
    npbins = numpy.arange(0, 5)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)
    classement_couleur = numpy.argsort(histogram[0])#Couleur prédominante en derniere position
    couleur_predominante = classement_couleur[-1] #Là on la récup
    couleur_predominante = convert_rgb_to_names(webcolors.hex_to_rgb('#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[couleur_predominante][0]), 
            math.ceil(clusters.cluster_centers_[couleur_predominante][1]),
        math.ceil(clusters.cluster_centers_[couleur_predominante][2])))) #On récup la couleur à l'aide de webcolors
    return couleur_predominante
    

def reharmonisation_exif(fichier)  :
    """
        But : Réharmonisation des exifs. La fonction va tester leurs présences
        et sinon les ajouter.
        Remarque : A n'exécuter qu'une fois.  
        Input : 
            - fichier : string contenant le nom du fichier
        Output : 
            - int : 0
    """
    with open(fichier) as json_file :
        data = json.loads(json_file.read())
        datas = data['data']
        chaine_json = "{ \"data\" :["
        for p in datas:
            try : 
                atest = p["305"] 
            except : 
                p["305"] = ""
            try : 
                atest = p["270"] 
            except : 
                p["270"] = ""  
            p["balise_supp"] = ""
            chaine_json = chaine_json + str(p)+","
        chaine_json = chaine_json[:-1]
        chaine_json += "]}"    
        chaine_json = chaine_json.replace("\'","\"")
    fichier = open("data.json","w")
    fichier.write(chaine_json)
    fichier.close()
    return 0
reharmonisation_date('data.json')

with open('data.json') as json_file :
        data = json.loads(json_file.read())
        datas = data['data']
        for i in os.listdir("Images"):
            couleur_predominante = etiquetage_couleur("Images/"+i)
            datas["couleur_predominante"] = couleur_predominante