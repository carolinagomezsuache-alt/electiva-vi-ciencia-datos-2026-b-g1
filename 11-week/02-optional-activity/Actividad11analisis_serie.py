import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Crear una serie de tiempo simulada (ej. producción o ventas diarias) con fecha como índice
np.random.seed(42)
fechas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
valores = 100 + 15 * np.sin(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 10, len(fechas))

# Cargar en DataFrame de pandas con la fecha como índice
df = pd.DataFrame({"valor": valores}, index=fechas)

# 2. Agregación por mes (resample) usando el promedio mensual
df_mensual = df.resample("ME").mean()

# Calcular la media móvil (rolling) con una ventana de 3 meses
df_mensual["media_movil"] = df_mensual["valor"].rolling(window=3).mean()

# 3. Visualización de la serie temporal y su media móvil
plt.figure(figsize=(10, 6))
plt.plot(df_mensual.index, df_mensual["valor"], marker='o', linestyle='--', label="Promedio Mensual", color='#1976d2')
plt.plot(df_mensual.index, df_mensual["media_movil"], marker='s', linewidth=2.5, label="Media Móvil (3 Meses)", color='#d32f2f')

plt.title("Análisis de Serie Temporal: Agregación Mensual y Media Móvil", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Mes", fontsize=11)
plt.ylabel("Valor de la Serie", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()

# Guardar el gráfico para la entrega en el repositorio
plt.savefig("serie_tiempo_grafico.png", dpi=300)
plt.show()
