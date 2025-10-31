import pandas as pd
import numpy as np

# ==============================================
#         ANÀLISI DE NOTES D’UNA CLASSE
# ==============================================

notas = pd.DataFrame({
    'Nombre': ['Anna', 'Joan', 'Pau', 'Maria', 'Carla', 'Toni'],
    'Nota': [9.5, 8.0, 6.0, 4.5, 7.5, 10.0]
})

notas.to_csv('notas_clase.csv', index=False)

notas_df = pd.read_csv('notas_clase.csv')

print("Notas de los alumnos:")
print(notas_df)

media = notas_df['Nota'].mean()
maximo = notas_df['Nota'].max()
minimo = notas_df['Nota'].min()

print(f"\nEstadisticas de las notas:")
print(f"Media: {media:.2f}")
print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")

def categoria(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Bien"
    else:
        return "Suspendido"

notas_df['Categoria'] = notas_df['Nota'].apply(categoria)

print("\nDataFrame con categorias:")
print(notas_df)

# ==============================================
#          NETEJA DE DADES DE VENDES
# ==============================================

ventas = pd.DataFrame({
    'Producto': ['Lapiz', 'Boli', 'Libreta', 'Mochila', 'Carpeta', 'Boli'],
    'Cantidad': [10, -5, 8, 15, 0, 12],
    'Precio': [0.8, 1.2, 3.5, 25.0, 4.0, 1.2],
    'Fecha': ['2025-01-10', '', '2025-02-01', '2025-02-10', '2025-02-12', None]
})

ventas.to_csv('ventas.csv', index=False)

ventas_df = pd.read_csv('ventas.csv')

print("\nDatos originales de ventas:")
print(ventas_df)

ventas_df = ventas_df[ventas_df['Fecha'].notnull() & (ventas_df['Fecha'] != '')]

ventas_df = ventas_df[ventas_df['Cantidad'] >= 0]

ventas_df['Total'] = ventas_df['Cantidad'] * ventas_df['Precio']
total_producto = ventas_df.groupby('Producto')['Total'].sum().reset_index()

print("\nDatos limpios de ventas:")
print(ventas_df)

print("\nTotal de ventas por producto:")
print(total_producto)