import pandas as pd

alumnos = pd.read_csv('alumnos.csv')

print("Primeras 5 filas del CSV:")
print(alumnos.head())

alumnos_limpio = alumnos.dropna()

alumnos_limpio.to_csv('limpio.csv', index=False)

print("\Fichero 'limpio.csv' creado sin valores nulos:")
print(alumnos_limpio)

notes = pd.read_csv('notas.csv')

fusionat = pd.merge(alumnos_limpio, notes, on='Nombre')

print("\nDataFrame fusionado:")
print(fusionat)