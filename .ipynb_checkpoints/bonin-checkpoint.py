import common
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
df = common.load_data('database.xls')

# # Étude du vide #
# Il s'agit d'étudier le vide
# ## Résulats ##
# Voici les résulats : 

df.isna().sum()

# ## Analyse des résultats ##
# On remarque qu'il y a beaucoup de NaN dans la colonne *'Perception of corruption'*, car Poutine empêche aux gens de poucave
#
# ## Conclusion ##
# cheese NaN


