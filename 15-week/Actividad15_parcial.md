# Semana 5 del corte (sem 15) - parcial

**Nombre:** Wendy Carolina Gomez Suache

---

## Problema 1 - Serie de tiempo (1.5)

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar con la fecha como índice
df = pd.read_csv("ventas.csv", parse_dates=["fecha_venta"], index_col="fecha_venta")

# 2. Agregar por periodo (mensual). En pandas < 2.2 usar "M" en vez de "ME"
mensual = df["total"].resample("ME").sum()

# 3. Media móvil de 3 meses
mm3 = mensual.rolling(window=3).mean()

# 4. Graficar
plt.figure(figsize=(10, 4))
plt.plot(mensual, label="Ventas mensuales", alpha=0.6)
plt.plot(mm3, label="Media móvil (3 meses)", linewidth=2)
plt.title("Ventas mensuales y tendencia")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.legend()
plt.show()
```

**Interpretación**

- **Tendencia:** la media móvil suaviza el ruido y muestra la dirección general de la serie a largo plazo. Si sube de forma sostenida, la tendencia es creciente; si baja, decreciente.
- **Estacionalidad:** son patrones que se repiten en periodos fijos (por ejemplo, picos cada diciembre o cada trimestre). Se ven como oscilaciones regulares alrededor de la tendencia.

---

## Problema 2 - Visualización (1.5)

| Pregunta | Gráfico correcto | Justificación |
|---|---|---|
| **Evolución** (¿cómo cambió en el tiempo?) | Gráfico de líneas | Muestra continuidad y tendencia temporal. |
| **Comparación** (¿qué categoría es mayor?) | Barras ordenadas | La longitud se compara con precisión. |
| **Proporción** (¿qué parte del total?) | Barras apiladas al 100 % o torta con pocas categorías (≤ 5) | Muestra la parte frente al todo. |

**Error de diseño detectado: eje Y truncado**

- **Problema:** si un gráfico de barras empieza en 90 en vez de 0, una diferencia pequeña parece enorme y engaña al lector.
- **Corrección:** iniciar el eje en 0 en gráficos de barras (o usar líneas si se quiere resaltar la variación), y agregar título claro y etiquetas de datos.

**Otro error posible: torta saturada**

- **Problema:** con más de 6 categorías es ilegible y no se pueden comparar los ángulos.
- **Corrección:** usar barras horizontales ordenadas o agrupar las categorías pequeñas en "Otros".

---

## Problema 3 - Optimización y métricas (2.0)

**Consulta lenta (antes)**

```sql
SELECT *
FROM ventas
WHERE YEAR(fecha_venta) = 2025;
```

**Consulta optimizada (después)**

```sql
CREATE INDEX idx_ventas_fecha_venta ON ventas(fecha_venta);

SELECT id_venta, cliente_id, total, fecha_venta
FROM ventas
WHERE fecha_venta >= '2025-01-01' AND fecha_venta < '2026-01-01';
```

**Por qué mejora**

1. Se piden solo las **columnas necesarias** en vez de `SELECT *`, lo que reduce la cantidad de datos leídos.
2. Se elimina la **función sobre la columna** (`YEAR(fecha_venta)`), que impide usar el índice. Con un **filtro por rango** el motor sí puede usarlo.
3. El **índice** sobre `fecha_venta` evita recorrer toda la tabla (full scan).

**Dos medidas DAX**

```DAX
Total Ventas = SUM(Ventas[total])

% del Total =
DIVIDE(
    [Total Ventas],
    CALCULATE([Total Ventas], ALL(Ventas))
)
```

Opcional, comparación entre periodos:

```DAX
Ventas Año Anterior =
CALCULATE([Total Ventas], SAMEPERIODLASTYEAR(Calendario[Fecha]))
```

**Medida vs. columna calculada**

| | Medida | Columna calculada |
|---|---|---|
| Cuándo se calcula | En tiempo de consulta, según el contexto de filtro | Al cargar o actualizar el modelo, fila por fila |
| Almacenamiento | No ocupa espacio en el modelo | Ocupa memoria |
| Uso típico | Totales, porcentajes, KPIs | Categorías o etiquetas por fila, usadas en filtros o ejes |

---

## English requirement (20%)

An **index** speeds up a query because the database can find rows directly, like using a book's index, instead of scanning the entire table. A **measure** in Power BI is a calculation, written in DAX, that is evaluated dynamically based on the filters applied in a report, such as total sales by region or year.