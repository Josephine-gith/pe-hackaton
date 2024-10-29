import pandas as pd
import matplotlib.pyplot as plt
import common
import numpy as np
import scipy.stats

# # Quelques éléments de sociologie
# Voici quelques exemples de données étudiées à partir du dataset.
#

df = common.load_data("database.xls")

# ## Corrélation entre santé et entourage
# Une première question que l'on peut se poser est sur un possible lien entre espérance de vie et entourage social : en effet, on peut s'attendre non seulement à un effet positif sur la santé mentale, mais aussi sur la santé physique des individus lorsque l'on sait par exemple qu'un stress prolongé augmente la probabilité d'apparition de nombreuses maladies.

common.analyse(df['Social support'],df['Healthy life expectancy at birth'])

# On obtient un résultat cohérent avec notre intition initiale.


