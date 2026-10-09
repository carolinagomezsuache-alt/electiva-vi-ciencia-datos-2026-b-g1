# Mini-proyecto de Datos - Semana 10 (Corte 2)

## 1. Modelo de Datos (ERD)
El diagrama entidad-relación (ERD) se encuentra adjunto en la carpeta bajo el nombre `erd.png`. Este modelo define la estructura relacional entre las entidades de Clientes, Pedidos y Categorías de servicio.

## 2. Extracción, Limpieza y Transformación
- **Extracción:** Se importó el conjunto de datos transaccionales desde el archivo tabular `dataset.csv`.
- **Limpieza:** Se procesó el DataFrame mediante la librería Pandas aplicando los métodos `.dropna()` para suprimir valores vacíos y `.drop_duplicates()` para garantizar la unicidad de los registros, dejando el set listo para la fase analítica.

## 3. Análisis y Consultas
Se resolvieron dos interrogantes clave mediante operaciones de filtrado y agregación:
1. **Promedio de tiempo de entrega por categoría:** Permitió evaluar el rendimiento operativo y detectar cuáles categorías de servicio presentan mayores demoras.
2. **Filtrado de calidad y eficiencia:** Extracción de los pedidos que cumplen simultáneamente con estándares altos de satisfacción ($\text{calificación} \ge 4$) y tiempos óptimos de entrega ($< 35$ minutos).