#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:09:13 2021

@author: philippe
"""
# Import Bibliothèque ---
import urllib.request
import random
import PIL.Image
import PIL.ExifTags
import os 
from qwikidata.sparql import return_sparql_query_results 
# Suppression des anciennes images 
for filename in os.listdir("Images") : 
    os.remove("Images/"+filename)
    
# Initialisation de la liste contenant les thèmes ---
liste_element = [ ["montagne","Q8502"],["chat","Q146"],["homme","Q5"],["chien","Q144"],["plante","Q756"]]


# Execution d'une requête d'un thème de la liste
element = liste_element[2]
print(element)
query_string = "     SELECT ?item ?itemLabel ?pic   WHERE {         ?item wdt:P31 wd:"+str(element[1])+".        ?item wdt:P18 ?pic} limit 30"
res = return_sparql_query_results(query_string)
for i in range (30) : 
    chaine = "Images/"+str(element[0])+str(i)+".jpg"
    urllib.request.urlretrieve(res["results"]["bindings"][i]["pic"]["value"],chaine)
    descriptionisset = 0
    img = PIL.Image.open(chaine)
    exif_data = img._getexif()
    exif = {}
    try :
        for k,v in img._getexif().items():
            if (k == 270) :
                descriptionisset = 1
    except:
        print("erreur : ",chaine)    
    if (descriptionisset != 1 ) : 
        os.remove(chaine)
    else : 
        print("image sauvée")