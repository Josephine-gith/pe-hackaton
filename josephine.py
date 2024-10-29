import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

plt.plot(df['Negative affect'],df['Positive affect'], '+', label='valeurs réelles')
x=np.linspace(0.1,0.8, 100)
plt.plot(x,1-x,color='r',label='courbe théorique')
plt.xlabel('Negative affect')
plt.ylabel('Positive affect')
plt.legend()
plt.show();

# Cette courbe nous montre que le 'positive affect' ne peut pas être considéré comme une mesure de bonheur suffisante. Si cela correspondrait au bonheur, on aurait 'positive affect'+'negative affect'=1, ce qui correspond à la courbe rouge. On voit qu'effectivement le nuage de point suit la tendance de la courbe rouge, mais pas de façon précise.
