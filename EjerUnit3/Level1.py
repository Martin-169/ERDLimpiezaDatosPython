import pandas as pd
import numpy as np


dades = {
    'Nombre': ['Anna', 'Joan', 'Pau', 'Anna', 'Maria', None],
    'Edad': [20, 22, None, 20, 19, 21],
    'Nota': [8.5, None, 7.0, 8.5, 9.0, None],
    'Precio': ['12.5', '8.0', None, '12.5', '10.0', '8.0']
}

df = pd.DataFrame(dades)
print("DataFrame inicial:")
print(df)

df = df.dropna(how='all')

df['Edad'].fillna(df['Edad'].mean(), inplace=True)
df['Nota'].fillna(df['Nota'].mean(), inplace=True)

df = df.drop_duplicates()

df['Precio'] = df['Precio'].astype(float)

media_precio = df['Precio'].mean()

print("\n DataFrame limpio:")
print(df)

print(f"\n Media de los precios: {media_precio:.2f}")
