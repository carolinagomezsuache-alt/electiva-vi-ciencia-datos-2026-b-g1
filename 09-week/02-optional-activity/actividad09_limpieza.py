import pandas as pd
import numpy as np

# 1. CREAR UN DATASET "SUCIO" DE PRUEBA
data = {
    'id': [1, 2, 2, 3, 4, 5, 6],
    'nombre': ['  ana gómez ', 'JUAN PÉREZ', 'JUAN PÉREZ', None, 'carlos ruiz', 'maria lopez', 'ana gómez'],
    'edad': [25, 30, 30, None, 45, '28', 25], # '28' es texto y hay un nulo
    'salario': [1200.5, 1500.0, 1500.0, 1100.0, np.nan, 2000.0, 1200.5],
    'fecha_registro': ['2023-01-10', '2023-05-12', '2023-05-12', 'fecha_invalida', '2023-02-20', '2023-03-15', '2023-01-10']
}

df = pd.DataFrame(data)

print("=========================================")
print("          INFORME ANTES DE LA LIMPIEZA    ")
print("=========================================")
print(f"Total de filas: {len(df)}")
print(f"Valores nulos por columna:\n{df.isnull().sum()}")
print(f"Filas duplicadas: {df.duplicated().sum()}")
print("\nPrimeras filas del dataset sucio:")
print(df)
print("-" * 45)

# 2. PROCESO DE LIMPIEZA CON PANDAS

# A. Eliminar registros duplicados
df = df.drop_duplicates()

# B. Corregir tipos de datos (edad a numérico, fecha a datetime)
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')

# C. Tratar valores nulos (imputar o rellenar)
df['nombre'] = df['nombre'].fillna('Desconocido')
df['edad'] = df['edad'].fillna(df['edad'].median())

# D. Normalizar formatos de texto (quitar espacios sobrantes y estandarizar mayúsculas/minúsculas)
df['nombre'] = df['nombre'].str.strip().str.title()

print("\n=========================================")
print("          INFORME DESPUÉS DE LA LIMPIEZA  ")
print("=========================================")
print(f"Total de filas: {len(df)}")
print(f"Valores nulos por columna:\n{df.isnull().sum()}")
print(f"Filas duplicadas: {df.duplicated().sum()}")
print("\nPrimeras filas del dataset limpio:")
print(df)
print("=========================================")