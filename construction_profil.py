#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:32:57 2021

@author: philippe
"""
import webbrowser,os,time
import script_prediction_profil

"""Fonction d'initialisation : ce script est appelé après démarrage du frontend"""

if (os.fork()) : 
    password = ""
    commande = 'python3 serveur.py'
    p = os.system('echo %s| sudo -S %s' % (password,commande))
else : 
    time.sleep(10)
    while (True) : 
        print("Que souhaitez vous faire : \n 1 - Créatoin d'un profil \n 2 - Ajout d'une balise \n 3 - Recommendation d'une image")
        choix = input("Saisir le nombre : ")
        if (choix == "1") :
            webbrowser.open("localhost/index.py")
        elif (choix == "2") : 
            webbrowser.open("localhost/ajout_balise.py")
        elif (choix == "3") : 
            profil = input("Saisir votre profil : ")
            script_prediction_profil.verification_profil(profil)
            
            