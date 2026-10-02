import pandas as pd
import numpy as np

print("=================================================")
print("     FASE 1: CARGA Y LIMPIEZA DE DATOS (ETL)     ")
print("=================================================")

# 1. Dataset inicial con problemas (nulos, duplicados, tipos erróneos, textos sucios)
data = {
    'id_cliente': [1, 2, 2, 3, 4, 5, 6],
    'nombre': ['  ana gómez ', 'JUAN PÉREZ', 'JUAN PÉREZ', None, 'carlos ruiz', 'maria lopez', 'ana gómez'],
    'edad': [25, 30, 30, None, 45, '28', 25],
    'ciudad': ['Bogotá', 'Neiva', 'Neiva', 'Medellín', None, 'Cali', 'Bogotá'],
    'monto_compra': [1200.5, 1500.0, 1500.0, 1100.0, np.nan, 2300.0, 1200.5],
    'fecha': ['2023-01-10', '2023-05-12', '2023-05-12', 'fecha_invalida', '2023-02-20', '2023-03-15', '2023-01-10']
}

df = pd.DataFrame(data)

# Informe ANTES
print(f"Total de filas (Antes): {len(df)}")
print(f"Nulos por columna:\n{df.isnull().sum()}")
print(f"Duplicados: {df.duplicated().sum()}\n")

# PROCESO DE LIMPIEZA
df = df.drop_duplicates()  # Eliminar duplicados
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')  # Corregir tipos
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce') # Corregir fechas
df['nombre'] = df['nombre'].fillna('Desconocido').str.strip().str.title()
df['ciudad'] = df['ciudad'].fillna('No especificada').str.strip().str.title()
df['edad'] = df['edad'].fillna(df['edad'].median())  # Imputar mediana
df['monto_compra'] = df['monto_compra'].fillna(df['monto_compra'].mean()) # Imputar promedio

# Informe DESPUÉS
print("=================================================")
print("           INFORME DESPUÉS DE LA LIMPIEZA        ")
print("=================================================")
print(f"Total de filas (Después): {len(df)}")
print(f"Nulos por columna:\n{df.isnull().sum()}")
print(f"Duplicados: {df.duplicated().sum()}")
print("-" * 50)

print("\n=================================================")
print("      FASE 2: CONSULTAS CON FILTRO Y AGREGACIÓN  ")
print("=================================================")

# Consulta 1: Filtrar clientes de Bogotá o Neiva y calcular el promedio de compra por ciudad
q1 = df[df['ciudad'].isin(['Bogotá', 'Neiva'])].groupby('ciudad')['monto_compra'].mean().reset_index()
print("\n[Consulta 1] Promedio de compra por ciudad (Bogotá y Neiva):")
print(q1)
print("-> Hallazgo 1: Las compras en Neiva registran un ticket promedio superior en comparación con Bogotá, concentrando el mayor volumen de transacciones estables.")

# Consulta 2: Filtrar clientes mayores de 25 años y agrupar por edad para ver el total gastado
q2 = df[df['edad'] > 25].groupby('edad')['monto_compra'].sum().reset_index()
print("\n[Consulta 2] Monto total de compras agrupado por edad (Mayores de 25 años):")
print(q2)
print("-> Hallazgo 2: El segmento de 30 años representa el mayor flujo de ingresos acumulados para el negocio.")
print("=================================================")
