#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:43:53 2021

@author: philippe
"""
import json 

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
reharmonisation_date('data.json')            
