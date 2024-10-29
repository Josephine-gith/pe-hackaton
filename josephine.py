import pandas as pd
import matplotlib.pyplot as plt
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


