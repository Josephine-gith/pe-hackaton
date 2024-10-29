import common
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = common.load_data('database.xls')
df.head()

# # 1. Étude du vide #
# Il s'agit d'étudier le vide
# ## Résulats ##
# Voici les résulats : 

df.isna().sum()

# ## Analyse des résultats ##
# On remarque qu'il y a beaucoup de NaN dans la colonne *'Perception of corruption'*, car Poutine empêche aux gens de poucave
#
# ## Conclusion ##
# cheese NaN

# # 2. Étude de la corruption #
# Il s'agit d'étudier la corruption en 2022.

mask1 = (df['year']==2022)
mask2 = ~(df['Freedom to make life choices'].isna())
mask3 = ~(df['Social support'].isna())
df = df[mask1 & mask2 & mask3]
df

plt.scatter(df['Social support'],df['Freedom to make life choices'])
plt.xlabel('Social support')
plt.ylabel('Freedom to make life choices')
a,b = np.polyfit(df['Social support'],df['Freedom to make life choices'],1)
X = np.linspace(0,1,100)
Y = a*X + b
plt.plot(X,Y,color='red')
plt.show()


