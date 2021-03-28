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
import pydotplus,json
from IPython.display import Image, display

with open('data.json') as json_file :
        data = json.loads(json_file.read())
        data = data['data']
result = [
              'NotFavorite',
              'Favorite',
              'NotFavorite',
              'NotFavorite',
              'NotFavorite',
              'NotFavorite',
              'NotFavorite',
              'NotFavorite',
              'Favorite',
              'NotFavorite',
              'Favorite'
              ]


#creating dataframes
dataframe = pd.DataFrame(data, columns=['306', 'theme', 'orientation','couleur', 'type'])
resultframe = pd.DataFrame(result, columns=['favorite'])

#generating numerical labels
le1 = LabelEncoder()
dataframe['306'] = le1.fit_transform(dataframe['306'])

le2 = LabelEncoder()
dataframe['theme'] = le2.fit_transform(dataframe['theme'])

print('peinture' in le2.classes_)
le3 = LabelEncoder()
dataframe['orientation'] = le3.fit_transform(dataframe['orientation'])

le4 = LabelEncoder()
dataframe['couleur'] = le4.fit_transform(dataframe['couleur'])
print(le4.classes_)
le5 = LabelEncoder()
dataframe['type'] = le5.fit_transform(dataframe['type'])

le6 = LabelEncoder()
resultframe['favorite'] = le6.fit_transform(resultframe['favorite'])

#Use of decision tree classifiers
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(dataframe, resultframe)

#prediction
prediction = dtc.predict([[le1.transform([2015])[0], le2.transform(['montagne'])[0], 
                           le3.transform(['paysage'])[0], le4.transform([' sienna'])[0],
                           le5.transform(['tres grande image'])[0]]])
print(le6.inverse_transform(prediction))
print(dtc.feature_importances_)





















