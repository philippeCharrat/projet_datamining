
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
query_string = "     SELECT ?item ?itemLabel ?pic         WHERE {         ?item wdt:P31 wd:"+str(element[1])+".        ?item wdt:P18 ?pic} limit 10"
res = return_sparql_query_results(query_string)
#print(res["results"]["bindings"][0]["pic"])
for i in range (4) : 
    chaine = "Images/"+str(element[0])+str(i)+".jpg"
    urllib.request.urlretrieve(res["results"]["bindings"][i]["pic"]["value"],chaine)
    
    img = PIL.Image.open(chaine)
