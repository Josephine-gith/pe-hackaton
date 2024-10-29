import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
df = pd.read_excel('database.xls')

df.shape

df.dtypes

df.describe()

plt.scatter(df['Generosity'],df['Social support'])
plt.xlabel('Generosity')
plt.ylabel('Social support')
plt.title('Support social en fonction de la générosité - tous pays et années')
plt.show();

# Analyse du graphe :
#
# Pas de régression linéaire apparente, donc il n'y a pas de fonctions simples permettant de relier le support social et la générosité.

plt.scatter(df['Freedom to make life choices'],df['Generosity'])
plt.ylabel('Generosity')
plt.xlabel('Freedom to make life choices')
plt.title('Générosité en fonction de la liberté de faire des choix - tous pays et années')
plt.show();

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

life_exp=df.groupby(['year'])['Healthy life expectancy at birth'].mean()
plt.plot(life_exp)
plt.title('Longévité en fonction de lannée')
plt.show();
df['Healthy known'] = df['Healthy life expectancy at birth'].notna()
print(df.groupby(['year'])['Healthy known'].sum())

len(df['Country name'].unique())


