#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script d'extraction des images depuis Wikidata ainsi que de leurs données (Exif).
"""
# Import Bibliothèque ---
from PIL import Image
import urllib.request, random, os, time
from qwikidata.sparql import return_sparql_query_results 


def etiquetage_taille(dico_image_hauteur,dico_image_largeur):
    """
    But : Fonction qui retourne le type d'une image
    Input : 
        - dico_image_hauteur : entier équivalent à la hauteur en pixels
        - dico_image_largeur : entier équivalent à la largeur en pixels
    Output:
        - type_image : string contenant le type de l'image (ex : "icone")
    """
    taille = dico_image_hauteur*dico_image_largeur #Taille en pixels
    if taille < 1000000:
        type_image = "icone"
    elif taille < 2000000 & taille > 1000000:
        type_image = "image de taille moyenne"
    elif taille < 3000000 & taille > 2000000:
        type_image = "grande image"
    else:
        type_image = "tres grande image"
    return type_image

def extraction_brute():
    # Initialisation de la liste contenant les thèmes ---
    # Suppression des anciennes images 
    for filename in os.listdir("Images") : #Suppression des anciennes images
        os.remove("Images/"+filename)
    #os.remove("data.json")
    chaine_json = "{ \"data\" :["
    liste_element = [["montagne","Q8502"],["chat","Q146"],["manga","Q8724"],["homme","Q5"],["chien","Q144"],["plante","Q756"],["sport","Q31629"],["film","Q11424"],["art","Q838948"],["peinture","Q11629"]]
    images = 0

    start = time.time()
    while(images<100) :
        # Execution d'une requête d'un thème de la liste
        
        "Choix d'un thème dans la liste d'éléments"
        a = random.randint(0,len(liste_element)-1)
        element = liste_element[a]
        
        "Préparation requête SQL avec le code wikidata du thème et exécution"
        query_string = "SELECT ?item ?itemLabel ?pic WHERE { ?item wdt:P31 wd:"+str(element[1])+". ?item wdt:P18 ?pic} limit 30"
        res = return_sparql_query_results(query_string)
        
        "Etiquetage à l'aide des ExifTags et des fonctions de ce script"
        nb_elements = str(res).count("item")
        for i in range (nb_elements-2) :
            chaine = "Images/"+str(element[0])+str(i)+".jpg"
            try :
                urllib.request.urlretrieve(res["results"]["bindings"][i]["pic"]["value"],chaine)
                descriptionisset = 0
                img = Image.open(chaine)
                exif_data = img._getexif()
                dico_image = {"nom":chaine}
                for k,v in img._getexif().items():
                    """
                    Etiquetages pris en compte : description, largeur, hauteurs (en pixels), logiciel et date de prise de vue.
                    Si une image ne contient pas un de ces tags, elle ne sera pas prise en compte.
                    """
                    if (k in [270,40962,40963,306,305]):
                        v = str(v).replace("\x00",".")
                        v = str(v).replace("\""," ")
                        v = str(v).replace("\'"," ")
                        descriptionisset = 1
                        dico_image[str(k)] = v
                dico_image["theme"] = element[0]
                try : 
                    "Etiquetage paysage ou portrait, en fonction de la largeur et de la hauteur"
                    if int(dico_image["40962"]) >= int(dico_image["40963"]): #Largeur > Hauteur
                        dico_image["orientation"] = "paysage"
                    else:
                        dico_image["orientation"] = "portrait"
                    "Etiquetage de la couleur"
                    #dico_image["couleur"] = etiquetage_couleur(chaine) #ajout de la couleur
                except:
                    descriptionisset = 0
            except:
                print("erreur : ",chaine)
            if (descriptionisset != 1 ) : 
                #Aucun des tags attendus, suppression de l'image
                os.remove(chaine)
            else : 
                print("image sauvée")
                "Etiquetage type à l'aide de la fonction préprogrammée"
                dico_image["type"]= etiquetage_taille(int(dico_image["40962"]),int(dico_image["40963"]))
                images += 1
                chaine_json += str(dico_image) +","
        
        liste_element.remove(element)
        print(element)

    "Encodage des tags dans un fichier JSON"
    chaine_json = chaine_json[:-1]
    chaine_json += "]}"
    chaine_json = chaine_json.replace("\'","\"")
    fichier = open("data.json","w") #Réécriture du fichier : les données précédentes sont effacées
    fichier.write(chaine_json)
    fichier.close()

    finish = time.time()
    duree = finish - start
    print("L'extraction des images a pris "+str(duree/60)+" minutes")
