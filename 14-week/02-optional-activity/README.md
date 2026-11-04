# Semana 14 — Optimiza una consulta (opción A: SQL)

**Autor:** FULL_NAME · **GitHub:** carolinagomezsuache-alt

## Consulta ANTES (lenta)
```sql
SELECT *
FROM ventas
WHERE YEAR(fecha) = 2025
  AND MONTH(fecha) = 3;
```

**Problemas:**
1. `SELECT *` lee todas las columnas, aunque solo se necesiten algunas.
2. `YEAR(fecha)` y `MONTH(fecha)` aplican una función a la columna, así que el motor tiene que calcularla fila por fila y **no puede usar un índice** (full table scan).
3. No hay índice sobre `fecha`.

## Consulta DESPUÉS (optimizada)
```sql
CREATE INDEX idx_ventas_fecha ON ventas (fecha);

SELECT fecha, cliente_id, producto_id, monto
FROM ventas
WHERE fecha >= '2025-03-01'
  AND fecha <  '2025-04-01';
```

## Por qué mejora
| Cambio | Efecto |
|---|---|
| Filtro por **rango** en vez de funciones sobre la columna (condición *sargable*) | El motor puede usar el índice y saltar directo a las filas del mes |
| **Índice** en `fecha` | Pasa de un *full scan* a un *range scan*: lee solo las filas necesarias |
| **Solo las columnas necesarias** | Menos datos leídos y transferidos; menos memoria y red |
| Límite superior **exclusivo** (`< '2025-04-01'`) | Cubre todo marzo, incluidas las horas del último día, sin errores de borde |

Para verificar la mejora se usa `EXPLAIN` en ambas consultas: antes muestra un barrido completo de la tabla (`type = ALL`) y después un barrido por rango con el índice (`type = range`).

## Buenas prácticas aplicadas
- Evitar `SELECT *`.
- No usar funciones sobre columnas en el `WHERE`.
- Crear índices en las columnas que se filtran con frecuencia.
- Medir con `EXPLAIN` antes y después de optimizar.
- Considerar un índice cubriente si la consulta se ejecuta mucho (ver el `.sql`).
