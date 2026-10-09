import pandas as pd

# ==========================================
# FASE 1: CARGA Y LIMPIEZA DE DATOS EN PANDAS
# ==========================================
print("--- 1. CARGANDO Y LIMPIANDO DATOS ---")

# Cargar el dataset
df = pd.read_csv('dataset.csv')

print("Primeras filas del dataset original:")
print(df.head())

# Limpieza de datos: eliminar valores nulos y registros duplicados
df = df.dropna()
df = df.drop_duplicates()

print(f"\nDatos limpios exitosamente. Total de registros válidos: {len(df)}")


# ==========================================
# FASE 2: CONSULTAS Y ANÁLISIS (2 PREGUNTAS)
# ==========================================
print("\n--- 2. RESULTADOS DE LOS ANÁLISIS ---")

# Pregunta 1 (Agregación): ¿Cuál es el promedio del tiempo de entrega agrupado por categoría de comida?
print("\n[Consulta 1] Promedio de tiempo de entrega por categoría:")
analisis_1 = df.groupby('categoria')['tiempo_entrega_min'].mean().reset_index()
analisis_1.columns = ['Categoria', 'Promedio_Tiempo_Min']
print(analisis_1)

# Pregunta 2 (Filtro + Agregación): ¿Cuáles son los pedidos que tienen una calificación mayor o igual a 4 y un tiempo de entrega menor a 35 minutos?
print("\n[Consulta 2] Pedidos eficientes (Calificación >= 4 y Tiempo < 35 min):")
analisis_2 = df[(df['calificacion'] >= 4) & (df['tiempo_entrega_min'] < 35)]
print(analisis_2[['id_pedido', 'cliente', 'categoria', 'tiempo_entrega_min', 'calificacion']])