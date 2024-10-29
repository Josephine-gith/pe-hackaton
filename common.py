import pandas as pd

# fonction pour charger le contenu

def load_data(filename):
    df = pd.read_xls(filename)
    df = df.rename(columns={"foo": "bar"})
    return df