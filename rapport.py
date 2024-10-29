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

# On tripartie selon les tranches divisées par moyenne- ecart-type et moyenne+ ecart-type

#
#

# 1. les pays les plus pauvres

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

import scipy.stats
df = pd.read_excel('database.xls')

# # Analyses

# ## Quelle est la corrélation entre le bonheur et le malheur ?
# Peut-on être à la fois heureux et malheureux ?

# +
df_notna=df[(df['Negative affect'].notna())&(df['Positive affect'].notna())]

plt.plot(df_notna['Negative affect'],df_notna['Positive affect'], '+', label='valeurs réelles')
x=np.linspace(0.1,0.8, 1000)
plt.plot(x,1-x,color='r',label='courbe théorique')
regression = scipy.stats.linregress(df_notna['Negative affect'],df_notna['Positive affect'])
plt.plot(x,regression[0]*x+regression[1], color='y',label='régression')
plt.xlabel('Negative affect')
plt.ylabel('Positive affect')
plt.legend()
plt.show();
# -

# Ce graphe nous montre que le 'positive affect' ne peut pas être considéré comme une mesure de bonheur suffisante. Si cela correspondrait au bonheur, on aurait 'positive affect'+'negative affect'=1, ce qui correspond à la courbe rouge. On voit qu'effectivement le nuage de point suit la tendance de la droite rouge, mais la pente de la régression n'est pas la même que celle de la droite rouge.
#
# ## Evolution de données (longévité, positive affect, negative affect) sur ces dernières années
# ### Longévité

# +
dfb=df[df['year']>=2006]

life_exp=dfb.groupby(['year'])['Healthy life expectancy at birth'].mean()
plt.plot(life_exp)

regression = scipy.stats.linregress(life_exp.index,life_exp)
plt.plot(range(2006,2023),regression[0]*range(2006,2023)+regression[1], color='r',label='régression')
print("Longévité = {a}*année + {b}".format(a = round(regression[0],3), b=round(regression[1],2)))
plt.title('Longévité en fonction de lannée')
plt.xticks(range(2006,2023,2))
plt.show();

df['Healthy known'] = df['Healthy life expectancy at birth'].notna()
print(df.groupby(['year'])['Healthy known'].sum())
# -

# La longévité a augmenté de 5 ans depuis 2006. La donnée de 2005 n'est pas utilisable, car l'information n'est recensée que pour 27 pays, ce qui ne permet pas de faire une moyenne mondiale fiable.
#
# ### Bonheur

# +
bonh=dfb.groupby(['year'])['Positive affect'].mean()
plt.plot(bonh)

regression = scipy.stats.linregress(bonh.index,bonh)
plt.plot(range(2006,2023),regression[0]*range(2006,2023)+regression[1], color='r',label='régression')
print("Bonheur = {a}*année + {b}".format(a = round(regression[0],3), b=round(regression[1],2)))
plt.title('Bonheur en fonction de lannée')
plt.xticks(range(2006,2023,2))
plt.show();
# -

# ### Malheur

# +
malh=dfb.groupby(['year'])['Negative affect'].mean()
plt.plot(malh)

regression = scipy.stats.linregress(malh.index,malh)
plt.plot(range(2006,2023),regression[0]*range(2006,2023)+regression[1], color='r',label='régression')
print("Malheur = {a}*année + {b}".format(a = round(regression[0],3), b=round(regression[1],2)))
plt.title('Malheur en fonction de lannée')
plt.xticks(range(2006,2023,2))
plt.show();
# -

# Le bonheur reste le même en moyenne, ou en tout cas n'a pas de tendance claire, tandis que le malheur augmente clairement depuis 2006.

# ## Support social, générosité et liberté de faire des choix
# ### Les individus sont-ils plus généreux lorsqu’ils sont bien entourés ?

plt.plot(df['Generosity'],df['Social support'],'+')
plt.xlabel('Generosity')
plt.ylabel('Social support')
plt.title('Support social en fonction de la générosité - tous pays et années')
plt.show();

# Comentaire : Pas de régression linéaire apparente, donc il n'y a pas de fonctions simples permettant de relier le support social et la générosité.
#
# ### Les individus sont-ils plus généreux lorsqu’ils ont plus d’opportunités ?

plt.plot(df['Freedom to make life choices'],df['Generosity'],'+')
plt.ylabel('Generosity')
plt.xlabel('Freedom to make life choices')
plt.title('Générosité en fonction de la liberté de faire des choix - tous pays et années')
plt.show();

# Pas non plus de régressions claires possibles