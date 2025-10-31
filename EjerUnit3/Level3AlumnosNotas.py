import pandas as pd

datos_alumnos = {
    'Nombre': ['Anna', 'Joan', 'Pau', 'Maria', 'Carla'],
    'Edad': [20, 22, None, 19, 21],
    'Clase': ['A', 'B', 'A', 'B', 'A']
}

alumnos = pd.DataFrame(datos_alumnos)
alumnos.to_csv('alumnos.csv', index=False)
print("Fichero 'alumnos.csv' creado")

datos_notas = {
    'Nombre': ['Anna', 'Joan', 'Pau', 'Maria', 'Carla'],
    'Nota': [8.5, 6.0, 4.5, 9.0, 7.0]
}

notas = pd.DataFrame(datos_notas)
notas.to_csv('notas.csv', index=False)
print("Fichero 'notas.csv' creado")

print("\nContenido de 'alumnos.csv':")
print(alumnos)

print("\Contenido de 'notas.csv':")
print(notas)