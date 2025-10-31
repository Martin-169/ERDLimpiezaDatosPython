import pandas as pd

df = pd.read_csv(
    r"C:\Users\marti\Downloads\sales_data_sample.csv",
    encoding='Windows-1252'
)


print("Primeras 5 filas:")
print(df.head())

print("\nValores nulos antes:")
print(df.isnull().sum())

df_clean = df.dropna(subset=['QUANTITYORDERED','PRICEEACH'])

print("\nValores nulos despues de la limpieza:")
print(df_clean.isnull().sum())

df_clean['QUANTITYORDERED'] = df_clean['QUANTITYORDERED'].astype(int)
df_clean['PRICEEACH'] = df_clean['PRICEEACH'].astype(float)

df_clean['ORDERDATE'] = pd.to_datetime(df_clean['ORDERDATE'], errors='coerce')

df_clean['TotalVenta'] = df_clean['QUANTITYORDERED'] * df_clean['PRICEEACH']

def categoria_total(x):
    if x >= 1000:
        return 'Gran venta'
    elif x >= 100:
        return 'Venta media'
    else:
        return 'Venta pequeña'

df_clean['CategoriaVenta'] = df_clean['TotalVenta'].apply(categoria_total)

df_clean.to_csv('sales_data_limpio.csv', index=False)
print("\nFichero exportado: sales_data_limpio.csv")