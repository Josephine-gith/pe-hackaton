import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
# fonction pour charger le contenu en excel

def load_data(filename):
    df = pd.read_excel(filename)
    df = df.rename(columns={"foo": "bar"})
    return df

def clean_data(colonne1, colonne2, colonne3 = None):
    df_notna=(colonne1.notna())&(colonne2.notna())
    return colonne1[df_notna], colonne2[df_notna]

def tracage_regression(colonne1, colonne2, colonne3 = None):
    plt.plot(colonne1,colonne2, '+')
    regression = scipy.stats.linregress(colonne1,colonne2)
    plt.plot(np.linspace(0.4,1,1000), regression[0]*np.linspace(0.4,1,1000)+ regression[1], label='Régression linéaire')
    plt.legend(loc='best')
    plt.xlabel(colonne1.name)
    plt.ylabel(colonne2.name)

def analyse(colonne1, colonne2, colonne3 = None):
    clean = clean_data(colonne1, colonne2)
    tracage_regression(clean[0], clean[1])