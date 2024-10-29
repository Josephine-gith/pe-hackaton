import pandas as pd

# fonction pour charger le contenu en excel

def load_data(filename):
    df = pd.read_excel(filename)
    df = df.rename(columns={"foo": "bar"})
    return df