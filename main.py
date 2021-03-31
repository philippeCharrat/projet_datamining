#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Fonction principale executée dans le terminal, permettant à l'utilisateur de décider ce qu'il souhaite faire
"""
import webbrowser,os,time
import script_prediction_profil
import pre_traitement_donnees
import extraction_images_et_donnees as extraction
import visu_donnees

"""Fonction d'initialisation : ce script est appelé après démarrage du frontend"""

if (os.fork()) : 
    try : 
        password = "VotreMotDePasse"
        commande = 'python3 serveur.py'
        p = os.system('echo %s| sudo -S %s' % (password,commande))
    except :
        exit()
else : 
    
    while (True) :
        time.sleep(2) 
        print("Que souhaitez-vous faire : \n 1 - Création d'un profil \n 2 - Ajout d'une balise \n 3 - Recommendation d'une image \n 4 -  Effacer le terminal \n 5 - Visualiser des donnees \n 6 - Lancer l'extraction et le pré-traitement des données\n 7 - Connaitre vos préférences profil")
        choix = input("Saisir le nombre : ")
        if (choix == "1") :
            webbrowser.open("localhost/index.py")
        elif (choix == "2") : 
            webbrowser.open("localhost/ajout_balise.py")
        elif (choix == "3") : 
            profil = input("Saisir votre profil : ")
            script_prediction_profil.verification_profil(profil)
        elif (choix == "4") : 
            os.system("clear")
        elif (choix == "5"):
            webbrowser.open("localhost/choix_visu_donnees.py")
        elif (choix == "6"):
            extraction.extraction_brute()
            pre_traitement_donnees.pre_traitement()
            visu_donnees.images_visu_donnees()
        elif (choix == "7") :
            profil = input("Saisir votre profil : ")
            webbrowser.open("localhost/affiche_pref.py?nom_utilisateur="+profil)
            