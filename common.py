import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

# fonction pour charger le contenu en excel


def load_data(filename):
    df = pd.read_excel(filename)
    df = df.rename(columns={"foo": "bar"})
    return df


def clean_data(colonne1, colonne2=None, colonne3=None):
    if colonne2 is None:
        return colonne1[colonne1.notna()]
    df_notna = (colonne1.notna()) & (colonne2.notna())
    return colonne1[df_notna], colonne2[df_notna]


def remove_outliers(colonne1, marge=0.05):
    return colonne1[
        (colonne1 > colonne1.quantile(marge))
        & (colonne1 < colonne1.quantile(1 - marge))
    ]


def tracage_regression(colonne1, colonne2, colonne3=None):
    plt.plot(colonne1, colonne2, "+")
    regression = scipy.stats.linregress(colonne1, colonne2)
    plt.plot(
        np.linspace(0.4, 1, 1000),
        regression[0] * np.linspace(0.4, 1, 1000) + regression[1],
        label="Régression linéaire",
    )
    plt.legend(loc="best")
    plt.xlabel(colonne1.name)
    plt.ylabel(colonne2.name)


def analyse(colonne1, colonne2, marge=0.05, colonne3=None):
    clean = clean_data(colonne1, colonne2)
    totally_clean = remove_outliers(clean[0]), remove_outliers(clean[1])
    tracage_regression(totally_clean[0], totally_clean[1])
