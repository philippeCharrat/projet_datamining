#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:17:00 2021

@author: clementcornu
"""
import sys
sys.path.insert(0,"/lib/python3/dist-packages/numpy")
import json,numpy,math,cgitb,cgi
from pandas import json_normalize
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

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
    
def clusters_image(image,n):
    imgfile = Image.open(image)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters = n)
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
    plot.savefig("Donnees_visualisees/"+str(n)+"_clusters_"+juste_le_nom)
    plot.clf()
    
def get_name(image):
    nom = image.split("/",1)[1]
    nom = nom.split(".",1)[0]
    nom = nom+".png"
    return nom
    
cgitb.enable()
form = cgi.FieldStorage()
images_choisies = []
affichage_images = ""

for i in range(10):
    if form.getvalue("image_"+str(i)):
        images_choisies.append(form.getvalue("image_"+str(i)))
if form.getvalue("visu_type"):
    visu_type = form.getvalue("visu_type")
else:
    visu_type = "compo"

if visu_type == "compo":
    for i in len(images_choisies)-1:
        composition_image(images_choisies[i])
        nom = get_name(images_choisies[i])
        affichage_images = affichage_images +"<img src='Donnees_visualisees/"+nom+"'>"
elif visu_type == "clusters":
    for i in len(images_choisies)-1:
        clusters_image(images_choisies[i],2)
        nom = get_name(images_choisies[i])
        affichage_images = affichage_images +"<img src='Donnees_visualisees/"+nom+"'>"
else:
    x_en_fonction_de_y("theme","nom")
        
"Affichage du code HTML"   
print("Content-type: text/html; charset=utf-8\n")
html ="""
    <html>
        <body>
        
        """   
html = html + affichage_images + """
        <body>
    </html>
    """
print(html)