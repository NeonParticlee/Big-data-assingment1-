# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pr6OTyev-Mm2cZUM1W93AxUkvW7n70UQ

-	dpre.py: This file should perform Data Cleaning, Data Transformation, Data Reduction, and Data Discretization steps. Save the resulting data frame as a new CSV file named res_dpre.csv. [2 MARKS]
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import sys
import os
csv_path = sys.argv[1]
pokeset = pd.read_csv(csv_path)
pokeset.head()

pokeset.info()

pokeset.describe()

pokeset.columns

pokeset['against_fairy'].unique()

pokeset.isnull().sum()

pokeset[pokeset['is_legendary'] == 1]['percentage_male'].isna().sum()

genderless_pokemon = pokeset[pokeset['percentage_male'].isna()]
non_legendary_genderless = genderless_pokemon[genderless_pokemon['is_legendary'] == 0]
non_legendary_genderless['name']

pokeset["height_m"].fillna(pokeset["height_m"].median(), inplace=True)
pokeset["weight_kg"].fillna(pokeset["weight_kg"].median(), inplace=True)

drop_cols = ['base_happiness', 'japanese_name', 'pokedex_number']
pokeset.drop(columns=drop_cols, inplace=True)  # Modify pokeset directly

# Proceed as normal
pokeset["height_m"].fillna(pokeset["height_m"].median(), inplace=True)
pokeset["weight_kg"].fillna(pokeset["weight_kg"].median(), inplace=True)

# descretization
bins = [0, 300, 450, 600, 780, float('inf')]
labels = ['Weak', 'Average', 'Strong', 'Very Strong', 'Legendary']
pokeset['base_total_category'] = pd.cut(pokeset['base_total'], bins=bins, labels=labels)

for stat in ['attack', 'defense', 'speed']:
    pokeset[f'{stat}_category'] = pd.cut(pokeset[stat], bins=[0, 50, 100, 150, 255], labels=['Low', 'Medium', 'High', 'Very High'])

pokeset['weight_category'] = pd.cut(pokeset['weight_kg'], bins=[0, 10, 50, 200, float('inf')], labels=['Small', 'Medium', 'Large', 'Giant'])
pokeset['height_category'] = pd.cut(pokeset['height_m'], bins=[0, 0.5, 1.5, 3, float('inf')], labels=['Tiny', 'Short', 'Tall', 'Giant'])

pokeset['capture_rate'] = pd.to_numeric(pokeset['capture_rate'], errors='coerce')
pokeset['capture_rate_category'] = pd.cut(pokeset['capture_rate'], bins=[0, 50, 150, 255], labels=['Hard', 'Moderate', 'Easy'])

def gender_category(row):
    if pd.isna(row['percentage_male']):
        return 'Genderless'
    elif row['percentage_male'] > 75:
        return 'Mostly Male'
    elif row['percentage_male'] < 25:
        return 'Mostly Female'
    else:
        return 'Balanced'

pokeset['gender_category'] = pokeset.apply(gender_category, axis=1)

pokeset.to_csv('res_dpre.csv', index=False)

against_cols = [col for col in pokeset.columns if col.startswith("against_")]

unique_values = {col: pokeset[col].unique() for col in against_cols}

for col, values in unique_values.items():
    print(f"{col}: {sorted(values)}")

def categorize_effectiveness(value):
    if value == 0.0:
        return "Not Effective"
    elif value in [0.25, 0.5]:
        return "Resistant"
    elif value == 1.0:
        return "Normal"
    elif value == 2.0:
        return "Effective"
    elif value == 4.0:
        return "Very Effective"

for col in against_cols:
    pokeset[col + "_category"] = pokeset[col].apply(categorize_effectiveness)

pokeset

pokeset.to_csv("res_dpre.csv", index=False)  
print("Data preprocessing complete. Running eda.py...")


os.system("python eda.py")