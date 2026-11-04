"""c3-activity - Corte 3: Análisis temporal y visualización
Serie temporal (resample + media móvil) y 2 visualizaciones.

NOTA: si existe datos.csv (columnas: fecha, ventas) se usa ese archivo.
Si no existe, se genera una serie sintética de ventas diarias para demostrar el análisis.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------- 1. Datos ----------
if os.path.exists("datos.csv"):
    df = pd.read_csv("datos.csv", parse_dates=["fecha"])
else:
    rng = np.random.default_rng(42)
    dias = pd.date_range("2022-01-01", "2025-12-31", freq="D")
    t = np.arange(len(dias))
    estacional = 1 + 0.35 * np.sin(2 * np.pi * (dias.dayofyear - 80) / 365) \
                   + 0.25 * (dias.month == 12)
    ventas = (200 + 0.15 * t) * estacional + rng.normal(0, 15, len(dias))
    df = pd.DataFrame({"fecha": dias, "ventas": np.clip(np.asarray(ventas), 0, None)})
    df.to_csv("datos.csv", index=False)

df = df.set_index("fecha").sort_index()

# ---------- 2. Serie temporal: resample + media móvil ----------
try:
    mensual = df["ventas"].resample("ME").sum()
except ValueError:          # pandas < 2.2
    mensual = df["ventas"].resample("M").sum()
mm3 = mensual.rolling(window=3).mean()

# Tendencia (pendiente lineal) y estacionalidad
x = np.arange(len(mensual))
pendiente = np.polyfit(x, mensual.values, 1)[0]
por_mes = mensual.groupby(mensual.index.month).mean()
crec = (mensual.iloc[-12:].sum() / mensual.iloc[:12].sum() - 1) * 100
print(f"Pendiente: {pendiente:,.0f} por mes | Crecimiento ultimo vs primer anio: {crec:.1f}%")
print(f"Mes pico: {por_mes.idxmax()} ({por_mes.max():,.0f}) | Mes valle: {por_mes.idxmin()} ({por_mes.min():,.0f})")

# ---------- 3. Visualización 1: evolución ----------
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(mensual.index, mensual.values, color="#9ecae1", label="Ventas mensuales")
ax.plot(mm3.index, mm3.values, color="#08519c", linewidth=2.5, label="Media móvil (3 meses)")
ax.set_title(f"Las ventas mensuales crecieron {crec:.0f}% entre el primer y el último año")
ax.set_ylabel("Ventas por mes"); ax.set_ylim(bottom=0)
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("evolucion.png", dpi=150); plt.close()

# ---------- 4. Visualización 2: comparación ----------
meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
colores = ["#08519c" if m in (por_mes.idxmax(), por_mes.idxmin()) else "#9ecae1" for m in por_mes.index]
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.bar([meses[m-1] for m in por_mes.index], por_mes.values, color=colores)
ax.set_title(f"{meses[por_mes.idxmax()-1]} es el mes más fuerte y {meses[por_mes.idxmin()-1]} el más débil")
ax.set_ylabel("Ventas promedio por mes"); ax.set_ylim(bottom=0)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout(); plt.savefig("comparacion.png", dpi=150); plt.close()
print("Listo: evolucion.png y comparacion.png")
