-- Semana 14: Optimiza una consulta (opción A: SQL)
-- Tabla de ejemplo: ventas(id, fecha, cliente_id, producto_id, monto, observaciones, ...)

-- =========================
-- ANTES (consulta lenta)
-- =========================
SELECT *
FROM ventas
WHERE YEAR(fecha) = 2025
  AND MONTH(fecha) = 3;

-- =========================
-- DESPUÉS (consulta optimizada)
-- =========================
-- 1) Índice sobre la columna de filtro.
CREATE INDEX idx_ventas_fecha ON ventas (fecha);

-- 2) Filtro por rango (sin funciones sobre la columna) y solo las columnas necesarias.
SELECT fecha, cliente_id, producto_id, monto
FROM ventas
WHERE fecha >= '2025-03-01'
  AND fecha <  '2025-04-01';

-- 3) (Opcional) Índice cubriente: contiene las columnas que se leen y evita ir a la tabla.
-- CREATE INDEX idx_ventas_fecha_cubriente ON ventas (fecha, cliente_id, producto_id, monto);

-- Para comprobar la mejora, compara los planes de ejecución:
-- EXPLAIN SELECT ...;   (antes: type = ALL / full scan;  después: type = range usando idx_ventas_fecha)
