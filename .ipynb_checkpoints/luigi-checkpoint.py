import pandas as pd
import matplotlib.pyplot as plt
import common

# # Bienvenue dans mon document ^^ !!! uwu

df = common.load_data("database.xls")
df.head()
# On va virer les outliers
social = df[df['Social support'] > 0.4]
healthy = df[df['Healthy life expectancy at birth']> 35]
plt.scatter(social, healthy)


