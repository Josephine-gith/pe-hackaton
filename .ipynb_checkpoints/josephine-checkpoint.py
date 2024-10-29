# # Import et fonctions intermédiaires

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
df = pd.read_excel('database.xls')

df.shape

df.dtypes

df.describe()

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
