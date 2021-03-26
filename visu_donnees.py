#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:17:00 2021

@author: clementcornu
"""

import json,numpy,math,os,time
from pandas import json_normalize
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

def get_name(image):
    nom = image.split("/",1)[1]
    nom = nom.split(".",1)[0]
    nom = nom+".png"
    return nom

def x_en_fonction_de_y(x,y):
    data = json.load(open('data.json'))
    dataframe = json_normalize(data["data"])
    dataframe = pd.DataFrame(dataframe, columns=[x, y])
    grouped = dataframe.groupby(x).count()
    grouped = grouped.rename(
      columns={'languageLabel':'count'}).reset_index()
    img = grouped.plot(x=0, kind='bar', title= x+" en fonction de "+y).get_figure()
    img.savefig("Donnees_visualisees/"+x+"_fct_de_"+y+".png")

def composition_image(image):
    imgfile = Image.open(image)
    histogram = imgfile.histogram()
    
    # we have three bands (for this image)
    red = histogram[0:255]
    green = histogram[256:511]
    blue = histogram[512:767]
    x=range(255)
    y = []
    for i in x:
        y.append((red[i],green[i],blue[i]))
    plot.plot(x,y)
    juste_le_nom = get_name(image)
    plot.savefig("Donnees_visualisees/Composition_"+juste_le_nom)
    plot.clf()
    imgfile.close()
    
def clusters_image(image):
    imgfile = Image.open(image)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters = 4)
    clusters.fit(numarray)
    npbins = numpy.arange(0, 5)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)
    labels = numpy.unique(clusters.labels_)
    barlist = plot.bar(labels, histogram[0])
    for i in range(4):
        barlist[i].set_color('#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[i][0]), 
            math.ceil(clusters.cluster_centers_[i][1]),
        math.ceil(clusters.cluster_centers_[i][2])))
    juste_le_nom = get_name(image)
    plot.savefig("Donnees_visualisees/clusters_"+juste_le_nom)
    plot.clf()

def donnees_profil_utilisateur(data):
    print("Fonction pas encore mise en place")

start = time.time()   
for i in os.listdir("Images"):
    composition_image("Images/"+i)
    clusters_image("Images/"+i)
    print("Infos "+i+" synthétisées")
    
print("Fin de synthétisation des images")
print("Début mise en place des graphiques")
data = json.load(open('data.json'))
for i in data["data"].keys():
    for j in data["data"].keys():
        if i != j:
            x_en_fonction_de_y(i,j)
finish = time.time()
temps_exec = finish-start
print("Fin de synthétisation des données")
print("Le temps de calcul par image était de "+str(temps_exec/10)+" secondes")




            