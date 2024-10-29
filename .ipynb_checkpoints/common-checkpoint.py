import pandas as pd

# fonction pour charger le contenu en excel

def load_data(filename):
    df = pd.read_excel(filename)
    df = df.rename(columns={"foo": "bar"})
<<<<<<< HEAD
    return df

=======
    return df
>>>>>>> dabe45f86af70a73aeca14648ef5855eb5ec5209
