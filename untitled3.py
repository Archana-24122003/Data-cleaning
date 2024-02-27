# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VUzu2o0Ml4Yleorvuc5TGSG3JSpA6znD
"""

import numpy as np
import pandas as pd
from functools import reduce

df=pd.read_csv('/content/drive/MyDrive/BL-Flickr-Images-Book (1).csv')
df.head()

df.shape

for col in df:
  print(col)

to_drop=["Edition Statement",
         "Corporate Author",
         "Corporate Contributors",
         "Former owner",
         "Engraver",
         "Contributors",
         "Issuance type",
         "Shelfmarks"]
df.drop(to_drop,inplace=True,axis=1)
df.head()

df.shape

for col in df.columns:
  print(col)

df.set_index('Identifier',inplace=True)
df.head()

df["Date of Publication"].head(25)

unwanted_characters=['[',',','-']
def clean_dates(item):
  dop=str(item.loc['Date of Publication'])
  if dop=='nan' or dop[0]=='[':
    return np.NaN
  for character in unwanted_characters:
    if character in dop:
      character_index=dop.find(character)
      dop=dop[:character_index]
  return dop
  df['Date of Publication']=df.apply(clean_data,axis=1)

df['Date of Publication'].head(25)

def Clean_title(Title):
  if Title == "nan":
    return "NaN"
  if Title[0]=='[':
      Title=Title[1:Title.find(']')]
  if 'by' in Title:
      Title=Title[:Title.find('by')]
  elif 'By' in Title:
       Title=Title[:Title.find('By')]
  if '[' in Title:
       Title=Title[:Title.find('[')]
       Title=list(map(str.capitalize,Title.split()))
  return ''.join(Title)
df['Title']=df['Title'].apply(Clean_title)
df.head()

def clean_dates(item):

    dop= str(item.loc['Date of Publication'])

    if dop == 'nan' or dop[0] == '[':
      return np. NaN

    for character in unwanted_characters:
      if character in dop:
        character_index = dop.find(character)
        dop = dop[:character_index]

    return dop

df['Date of Publication'] = df.apply(clean_dates, axis = 1)

def clean_title(title):

    if title == 'nan':
       return 'NaN'

    if title[0] == '[':
       title = title [1: title.find(']')]

    if 'by' in title:
       title = title[:title.find('by')]
    elif 'By' in title:
       title = title[:title.find('By')]

    if '[' in title:
       title = title[:title.find('[')]

    title = title[:-2]


df['Title'] = df['Title'].apply(clean_title)
df.head()

