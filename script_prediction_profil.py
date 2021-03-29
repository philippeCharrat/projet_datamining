#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script pour la prédiction d'image recommandées.
"""

from sklearn import tree
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus,json,random,webbrowser
from IPython.display import Image, display

def prediction_dune_image_pour(profil) : 
    "Utilisation du fichier des préférences utilisateur"
    with open(profil) as json_file :
            dico = json.loads(json_file.read())
            list_img_like = dico['image_like']
            list_img_unlike = dico['image_unlike']
            data = [x for x in list_img_like ]
            data = data + [x for x in list_img_unlike ]
            #Attribution balise Favorite/NotFavorite en fonction de like/dislike
            result = ['Favorite' for x in list_img_like] 
            result = result + ['NotFavorite' for x in list_img_unlike ]
    
    "Chargement du fichier data.json en remplaçant le nom"
    with open('data.json') as json_file :
            array = json.loads(json_file.read())
            reference_label = array['data']
            for p in reference_label :
                if (p["nom"] in data) : 
                    data[data.index(p["nom"])] = p
    
    "Création des dataframes"
    dataframe = pd.DataFrame(data, columns=['306', 'theme', 'orientation','couleur','305', 'type','balise_supp'])
    resultframe = pd.DataFrame(result, columns=['favorite'])
    
    """
    Ajout de labels de référence pour les labels encoders, afin d'éviter 
    les problèmes lorsqu'un des labels n'est pas présent pour l'image
    """
    reference_labels = pd.DataFrame(reference_label, columns=['306', 'theme', 'orientation','couleur','305', 'type','balise_supp'])
    
    "Génération de labels numériques"
    le1 = LabelEncoder()
    le1.fit(reference_labels['306'])
    dataframe['306'] = le1.transform(dataframe['306'])
    
    le2 = LabelEncoder()
    le2.fit(reference_labels['theme'])
    dataframe['theme'] = le2.transform(dataframe['theme'])
    
    le3 = LabelEncoder()
    le3.fit(reference_labels['orientation'])
    dataframe['orientation'] = le3.transform(dataframe['orientation'])
    
    le4 = LabelEncoder()
    le4.fit(reference_labels['couleur'])
    dataframe['couleur'] = le4.transform(dataframe['couleur'])
    
    le5 = LabelEncoder()
    le5.fit(reference_labels['305'])
    dataframe['305'] = le5.transform(dataframe['305'])
    
    le6 = LabelEncoder()
    le6.fit(reference_labels['type'])
    dataframe['type'] = le6.transform(dataframe['type'])
    
    le7 = LabelEncoder()
    le7.fit(reference_labels['balise_supp'])
    dataframe['balise_supp'] = le7.transform(dataframe['balise_supp'])
    
    le8 = LabelEncoder()
    resultframe['favorite'] = le8.fit_transform(resultframe['favorite'])
    
    
    
    "Prédiction d'image à l'aide des labels et de l'arbre de décisions"
    i=0
    while(True) : 
        
        #Use of decision tree classifiers
        dtc = tree.DecisionTreeClassifier()
        dtc = dtc.fit(dataframe, resultframe)
        image_testee = reference_label[random.randint(0,len(reference_label)-1)]
        i +=1
        if i > 100 : 
            print("Aucune photo")
            break
        if(image_testee not in data) :     
            prediction = dtc.predict([[le1.transform([image_testee['306']])[0], le2.transform([image_testee['theme']])[0], 
                                   le3.transform([image_testee['orientation']])[0], le4.transform([image_testee['couleur']])[0],
                                   le5.transform([image_testee['305']])[0],le6.transform([image_testee['type']])[0], le7.transform([image_testee['balise_supp']])[0]]])
            print(le8.inverse_transform(prediction))
            print(dtc.feature_importances_)
            if (le8.inverse_transform(prediction) == 'Favorite') :
                webbrowser.open("localhost/image_a_tester.py?nom="+image_testee['nom']+"&profil="+profil)
                break

def verification_profil(profil) : 
    fichier_json = "Profil/profil_"+str(profil)+".json" 
    try : 
        with open(fichier_json,'r') as f :
            profil_is_set = 1
    except :
        profil_is_set = 0
    if (profil_is_set == 1) :
        prediction_dune_image_pour(fichier_json)
    else : 
        print("Vous n'avez pas encore de compte")

        