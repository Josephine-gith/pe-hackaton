import pandas as pd
import matplotlib.pyplot as plt
import common
import numpy as np
import scipy.stats

# # Bienvenue dans mon document ^^ !!! uwu

df = common.load_data("database.xls")
df.head()
# On va virer les outliers
social = df['Social support'][(df['Social support'] > 0.4) & (df['Healthy life expectancy at birth']> 35)]
healthy = df['Healthy life expectancy at birth'][(df['Social support'] > 0.4) & (df['Healthy life expectancy at birth']> 35)]
plt.plot(social,healthy, '+')
regression = scipy.stats.linregress(social,healthy)
plt.plot(np.linspace(0.4,1,1000), regression[0]*np.linspace(0.4,1,1000)+ regression[1])
plt.xlabel('Social support')
plt.ylabel('Healthy life expectancy')

