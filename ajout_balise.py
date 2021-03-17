#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021

@author: philippe
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:48:41 2021

@author: philippe
"""
import cgi, random ,json,random

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
if form.getvalue("nom_image") : 
    ajout_balise = 1
else : 
    ajout_balise = 0

if (ajout_balise == 0) :
    with open('data.json') as json_file :
        data = json.loads(json_file.read())
        data = data['data']
        image = data[random.randint(0,len(data)-1)]
        nom = image["nom"]
        theme = image["theme"]
    
    html ="""
    <html>
        <body>
            <style>
                img { width:300px; } 
            </style>
        <center><h2> Formulaire d'ajout de balise</h2></center>
        <form method="post" action="ajout_balise.py">
        <h3>La balise supplémentarie : </h3>
        <input type='text' name="balise_supp" required>
            <input type='submit' value='Soumettre'>
        <h3>Image issue du thème : """+ theme +""": </h3>
            <center>
        """
    dynamique = "<input type='hidden' name='nom_image' value='"+str(nom) +"'><img src='"+str(nom) +"'>"    
    html = html + dynamique + """
            </center>
        </form>
        </body>
    </html>
    """
else :
    html = "<html><body><center><h1> Merci de votre ajout </h1></center></body></html>"
print(html)    