# # Hackathon P24 #
#
# Groupe : MIMOUNI Ines, PERONNE Joséphine, ROMAIN Luigi, BONIN Aurélien 
#
# Thème : _Le bonheur_
#
# ## Objectifs de l'étude ##
#
# Notre objectif ici est de manipuler la base de donnée mise à disposition par le _World happiness report_ afin de mettre
# certaines affirmations présupposées à l'épreuve des faits.
#
# Plus précisement, les hyopthèses que nous avons cherché à confirmer ou infirmer sont les suivantes :
# - L'argent fait-il le bonheur ?
# - L'argent fait-il le malheur ? 
# - L'argent fait-il la liberté ?
# - Le soutien de notre entourage améliore-t-il notre santé ?
# - Les individus sont-ils plus généreux lorsqu'ils sont bien entourés ?
# - Les individus sont-ils plus généreux lorsqu'ils ont plus d'opportunités ?
# - Peut-on à la fois être heureux et malheureux ?
# - Être bien soutenu par ses proches contribue-t-il à notre sentiment de liberté ?
#
# ## Méthodologie ##
#
# Pour répondre à ces interrogations, la méthode générale que nous avons adopté est la suivante :
# - Nettoyer les données à utiliser (suppression des NaN...)
# - Étudier les liens entre différentes grandeurs (regression linéaires)
#
# ## Analyse des Résultats ##

# +
import pandas as pd
import common
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = common.load_data('database.xls')
# -

# ### L'argent fait-il le bonheur ?
#
# On commence par étudier quelques cas particuliers : 

# 1. Quelques pays européens :

# +
# l'argent fait-il le bonheur ? quelques pays européens

dfa = df[
df["Country name"].isin(["France", "Germany", "Italy", "Spain", "Switzerland"])

]

sns.relplot(data=dfa, x="Log GDP per capita", y='Positive affect', 
            hue='year',   
           );
# -

# Ce que nous indique ce graphique, c'est que (quoique l'écart du PIB se soit dilaté entre le début des années 2000 et aujourd'hui), l'argent semble faire le bonheur à chaque période temporelle (fonction croissante du PIB)

# 2. Les 10 pays les plus pauvres : 

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
# -

# Pour les 10 pays les plus pauvres, cette affirmation n'est plus vraie : dispersion trop grande des données, voire même, on serait tenté.e.s de dire que plus le temps avance, plus être riche dans les pays les plus pauvres rend malheureux...?

# 3. Étude en tripartition selon le PIB 

# +
df_clean = df[~df["Log GDP per capita"].isna()]

moy = df["Log GDP per capita"].mean()
sigma = df["Log GDP per capita"].std()
maxi = df["Log GDP per capita"].max()
mini = df["Log GDP per capita"].min()

df_clean["categorie"] = pd.cut(df_clean['Log GDP per capita'],
       bins=[0,moy-sigma, moy+sigma, maxi],
       labels=['pauvre', 'moyen', 'riche'])
# -

On 





# +
# l'argent fait-il le bonheur ? les pays les plus pauvres (moyenne-ecart type)

ax = sns.relplot(data=df_clean[df_clean["categorie"]=="pauvre"], x="Log GDP per capita", y='Positive affect',    
                       hue='year',);
ax2= sns.relplot(data=df_clean[df_clean["categorie"]=="pauvre"], x="Log GDP per capita", y='Positive affect',    
                       hue='year' );
ax2.set(xlim=(mini, maxi))
ax.set(title = "en relatif : " )
ax2.set(title = "à l'échelle PIBmin/PIBmax : " )

# +
# l'argent fait-il le bonheur ? les pays moyens (moyenne +- ecart-type)

ax = sns.relplot(data=df_clean[df_clean["categorie"]=="moyen"], x="Log GDP per capita", y='Positive affect',    
                       hue='year',);
ax2= sns.relplot(data=df_clean[df_clean["categorie"]=="moyen"], x="Log GDP per capita", y='Positive affect',    
                       hue='year' );
ax2.set(xlim=(mini, maxi))
ax.set(title = "en relatif : " )
ax2.set(title = "à l'échelle PIBmin/PIBmax : " )
# -


