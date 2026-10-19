import matplotlib.pyplot as plt
import pandas as pd

# 1. Datos de ejemplo: Productividad por línea de producción (unidades/hora)
# Supongamos un gráfico mal hecho anterior donde se truncaba el eje Y para exagerar diferencias.
datos = {
    "Línea de Producción": [
        "Línea A",
        "Línea B",
        "Línea C",
        "Línea D",
        "Línea E",
    ],
    "Productividad (u/h)": [420, 450, 310, 480, 390],
}

df = pd.DataFrame(datos)

# 2. Configuración de la visualización optimizada
plt.figure(figsize=(10, 6))

# Color con propósito: Destacamos la línea con mayor desempeño en un color llamativo y el resto en gris neutro
colores = ["#b0bec5", "#b0bec5", "#b0bec5", "#1976d2", "#b0bec5"]

barras = plt.bar(
    df["Línea de Producción"],
    df["Productividad (u/h)"],
    color=colores,
    width=0.6,
)

# Eje Y honesto que empieza obligatoriamente en 0 para no distorsionar proporciones
plt.ylim(0, 600)

# Título con conclusión y subtítulo explicativo
plt.title(
    "La Línea D lidera el rendimiento productivo con 480 u/h",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.suptitle(
    "Comparativa de productividad horaria por línea de ensamblaje",
    fontsize=10,
    color="gray",
    y=0.92,
)

plt.xlabel("Líneas de Producción", fontsize=11, labelpad=10)
plt.ylabel("Unidades por Hora (u/h)", fontsize=11, labelpad=10)

# Añadir las etiquetas de valor exacto sobre cada barra para evitar fatiga visual
for barra in barras:
  altura = barra.get_height()
  plt.text(
      barra.get_x() + barra.get_width() / 2.0,
      altura + 15,
      f"{altura}",
      ha="center",
      va="bottom",
      fontsize=10,
      fontweight="bold",
  )

# Limpiar diseño (quitar bordes innecesarios)
sns_style = plt.gca()
sns_style.spines["top"].set_visible(False)
sns_style.spines["right"].set_visible(False)

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Guardar la imagen para el repositorio
plt.savefig("grafico_rediseñado.png", dpi=300)
plt.show()
