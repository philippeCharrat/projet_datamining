#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:37:30 2021

@author: philippe
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:36:17 2021

@author: philippe
"""

from sklearn import tree
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus,json,random,webbrowser
from IPython.display import Image, display

with open('Profil/profil_philippe.json') as json_file :
        dico = json.loads(json_file.read())
        list_img_like = dico['image_like']
        list_img_unlike = dico['image_unlike']
        data = [x for x in list_img_like ]
        data = data + [x for x in list_img_unlike ]
        result = ['Favorite' for x in list_img_like]
        result = result + ['NotFavorite' for x in list_img_unlike ]

with open('data.json') as json_file :
        array = json.loads(json_file.read())
        reference_label = array['data']
        for p in reference_label :
            if (p["nom"] in data) : 
                data[data.index(p["nom"])] = p

#creating dataframes
dataframe = pd.DataFrame(data, columns=['306', 'theme', 'orientation','couleur', 'type'])
resultframe = pd.DataFrame(result, columns=['favorite'])

reference_labels = pd.DataFrame(reference_label, columns=['306', 'theme', 'orientation','couleur', 'type'])

#generating numerical labels
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
le5.fit(reference_labels['type'])
dataframe['type'] = le5.transform(dataframe['type'])

le6 = LabelEncoder()
resultframe['favorite'] = le6.fit_transform(resultframe['favorite'])

#Use of decision tree classifiers
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(dataframe, resultframe)


#prediction
while(True) : 
    image_testee = reference_label[random.randint(0,len(reference_label)-1)]
    if(image_testee not in data) :     
        prediction = dtc.predict([[le1.transform([image_testee['306']])[0], le2.transform([image_testee['theme']])[0], 
                               le3.transform([image_testee['orientation']])[0], le4.transform([image_testee['couleur']])[0],
                               le5.transform([image_testee['type']])[0]]])
        if (le6.inverse_transform(prediction) == 'Favorite') :
            webbrowser.open("localhost/imzge_a_test.py?nom="+image_testee['nom'])
            break
