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
#os.remove("data.json")


# Initialisation de la liste contenant les thèmes ---
chaine_json = "["
liste_element = [["montagne","Q8502"],["chat","Q146"],["homme","Q5"],["chien","Q144"],["plante","Q756"],["Q31629","sport"],["Q11424","film"],["Q838948","art"],["Q11629","peinture"]]
for a in range(len(liste_element)-1):
    # Execution d'une requête d'un thème de la liste
    element = liste_element[a]
    query_string = "SELECT ?item ?itemLabel ?pic WHERE { ?item wdt:P31 wd:"+str(element[1])+". ?item wdt:P18 ?pic} limit 5"
    res = return_sparql_query_results(query_string)
    nb_elements = str(res).count("item")
    for i in range (nb_elements-2) :
        chaine = "Images/"+str(element[0])+str(i)+".jpg"
        try :
            urllib.request.urlretrieve(res["results"]["bindings"][i]["pic"]["value"],chaine)
            descriptionisset = 0
            img = PIL.Image.open(chaine)
            exif_data = img._getexif()
            dico_image = {"nom":chaine}
            for k,v in img._getexif().items():
                if (k in [270,40962,40963,306,305]):
                    v = str(v).replace("\""," ")
                    descriptionisset = 1
                    dico_image[str(k)] = v
            dico_image["theme"] = element[0]
            if int(dico_image["40962"]) >= int(dico_image["40963"]):
                dico_image["orientation"] = "paysage"
            else:
                dico_image["orientation"] = "portrait" 
        except:
            print("erreur : ",chaine)
        if (descriptionisset != 1 ) : 
            os.remove(chaine)
        else : 
            print("image sauvée")
            chaine_json += str(dico_image) + ","
chaine_json = chaine_json[:-1]
chaine_json += "]"
chaine_json = chaine_json.replace("\'","\"")
fichier = open("data.json","a")
fichier.write(chaine_json)
fichier.close()