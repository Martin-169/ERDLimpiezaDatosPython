import pandas as pd

alumnos = pd.DataFrame({
    'Nombre': ['Anna', 'Joan', 'Pau', 'Maria'],
    'Edad': [20, 22, 21, 19],
    'Nota': [8.5, 6.0, 4.5, 9.0]
})

print("🔹 DataFrame de alumnos originales:")
print(alumnos)

alumnos['Resultado'] = alumnos['Nota'].apply(lambda x: 'Aprobado' if x >= 5 else 'Suspendido')

print("\n DataFrame con columna 'Resultado':")
print(alumnos)

ventas = pd.DataFrame({
    'Producto': ['Lapiz', 'Boli', 'Libreta', 'Mochila', 'Carpeta'],
    'Cantidad': [5, 12, 8, 15, 20],
    'Precio': [0.8, 1.2, 3.5, 25.0, 4.0]
})

print("\n🔹 DataFrame de ventas:")
print(ventas)

ventas_filtrado = ventas[ventas['Cantidad'] > 10]

print("\nProductos con más de 10 unidades vendidas:")
print(ventas_filtrado)

alumnos_ordenados = alumnos.sort_values(by='Nota', ascending=False)

print("\nAlumns ordenados por nota (de más alta a más baja):")
print(alumnos_ordenados)