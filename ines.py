import pandas as pd
import common
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = common.load_data('database.xls')

columns = list(df.columns)
columns

argent_bonheur = df[['Country name',
 'year',
 'Log GDP per capita',
 'Freedom to make life choices',
 'Generosity',
 'Positive affect',
 'Negative affect']]

argent_bonheur

# +
# l'argent fait-il le bonheur ? quelques pays européens

dfa = df[
df["Country name"].isin(["France", "Germany", "Italy", "Spain", "Switzerland"])

]

sns.relplot(data=dfa, x="Log GDP per capita", y='Positive affect', 
            hue='year',   
           );

# +
# l'argent fait-il le bonheur ? les 10 pays les plus pauvres 

dfp = df[
df["Country name"].isin([
'South Sudan',
'Burundi',
'Central African Republic',
'DR Congo',
'Mozambique',
'Malawi',
'Niger',
'Chad',
'Liberia',])

]

sns.relplot(data=dfp, x="Log GDP per capita", y='Positive affect',    
                       hue='year',);

# +
df2022 = df[df["year"]== 2022]

df_clean = df[~df["Log GDP per capita"].isna()]

moy = df["Log GDP per capita"].mean()
sigma = df["Log GDP per capita"].std()
maxi = df["Log GDP per capita"].max()

df_clean["categorie"] = pd.cut(df_clean['Log GDP per capita'],
       bins=[0,moy-sigma, moy+sigma, maxi],
       labels=['pauvre', 'moyen', 'riche'])
# -

df_clean

# +
# l'argent fait-il le bonheur ? les pays les plus pauvres (moyenne-ecart type)

sns.relplot(data=df_clean[df_clean["categorie"]=="pauvre"], x="Log GDP per capita", y='Positive affect',    
                       hue='year',);

# +
# l'argent fait-il le bonheur ? les pays moyens (moyenne +- ecart-type)

sns.relplot(data=df_clean[df_clean["categorie"]=="moyen"], x="Log GDP per capita", y='Positive affect',    
                       hue='year',);

# +
# l'argent fait-il le bonheur ? les pays les plus riches (moyenne+ecart type)

sns.relplot(data=df_clean[df_clean["categorie"]=="riche"], x="Log GDP per capita", y='Positive affect',    
                       hue='year',);
# -




