import common
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = common.load_data('database.xls')
df.head()

# # Étude du lien 'soutien/liberté' #
# Il s'agit d'étudier ici le lien entre le soutien qu'un individu reçoit via ses proches, et le sentiment de liberté pour
# faire des choix.

# Dans un premier lieu, on commence par nettoyer les données

mask1 = (df['year']==2022)
mask2 = ~(df['Freedom to make life choices'].isna())
mask3 = ~(df['Social support'].isna())
df = df[mask1 & mask2 & mask3]

# Ensuite, on étudie la correlation entre les deux grandeurs mesurées

plt.scatter(df['Social support'],df['Freedom to make life choices'])
plt.xlabel('Social support')
plt.ylabel('Freedom to make life choices')
a,b = np.polyfit(df['Social support'],df['Freedom to make life choices'],1)
X = np.linspace(0,1,100)
Y = a*X + b
plt.plot(X,Y,color='red')
plt.show()

# ## Analyse des résultats ##
#
# On observe une nette correlation entre les deux grandeurs, bien que la régression linéaire ne soit pas d'une grande qualité.


