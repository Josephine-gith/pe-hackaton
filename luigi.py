import pandas as pd
import matplotlib.pyplot as plt
import common
import numpy as np
import scipy.stats

# # Quelques éléments de sociologie
# Voici quelques exemples de données étudiées à partir du dataset.
#

df = common.load_data("database.xls")

<<<<<<< HEAD
# ## Corrélation entre santé et entourage
# Une première question que l'on peut se poser est sur un possible lien entre espérance de vie et entourage social : en effet, on peut s'attendre non seulement à un effet positif sur la santé mentale, mais aussi sur la santé physique des individus lorsque l'on sait par exemple qu'un stress prolongé augmente la probabilité d'apparition de nombreuses maladies.
=======
<<<<<<< HEAD

=======
>>>>>>> 3c9f6eb6c99ee91e1525c34a040b6f41827f7964
"""def clean_data(colonne1, colonne2, colonne3 = None):
    df_notna=(colonne1.notna())&(colonne2.notna())
    return colonne1[df_notna], colonne2[df_notna]
>>>>>>> 076a3ace13ff47aeeb762147636f27aaf2eccee3

common.analyse(df['Social support'],df['Healthy life expectancy at birth'])

# On obtient un résultat cohérent avec notre intition initiale.


