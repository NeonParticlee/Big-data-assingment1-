# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qp7gblVKe-HoSlRbQ623_WEHwhSQ0Ugp
"""

import pandas as pd
import os
#  cleaned dataset
pokeset = pd.read_csv('res_dpre.csv')

# Insight 1: Average base stats of Legendary vs. Non-Legendary
legendary_avg = pokeset.groupby('is_legendary')['base_total'].mean()
with open("eda-in-1.txt", "w") as f:
    f.write(f"Average base stats:\n{legendary_avg}\n")
    f.write("Legendary Pokémon have significantly higher base stats.")

# Insight 2: Most common effectiveness category
against_category_cols = [col for col in pokeset.columns if col.endswith("_category") and col.startswith("against_")]


effectiveness_counts = pokeset[against_category_cols].apply(pd.Series.value_counts).sum(axis=1).sort_values(ascending=False)

# Save to a text file
with open("eda-in-2.txt", "w") as f:
    f.write(f"Most common effectiveness categories:\n{effectiveness_counts}\n")

# Insight 3: Relationship between weight and capture rate
correlation = pokeset[['weight_kg', 'capture_rate']].corr().loc['weight_kg', 'capture_rate']
with open("eda-in-3.txt", "w") as f:
    f.write(f"Correlation between weight and capture rate: {correlation}\n")
    f.write("Heavier Pokémon tend to have lower capture rates.")

print("eda has been finished")

print("EDA has been finished. Running vis.py...")

os.system("python vis.py")