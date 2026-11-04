-- c3-activity: optimización de consulta SQL

-- ANTES: la función YEAR() sobre la columna impide usar un índice (full table scan)
-- y SELECT * lee columnas innecesarias.
SELECT *
FROM ventas
WHERE YEAR(fecha) = 2025;

-- DESPUÉS: filtro por rango (sargable), solo columnas necesarias e índice en fecha.
CREATE INDEX idx_ventas_fecha ON ventas (fecha);

SELECT fecha, monto
FROM ventas
WHERE fecha >= '2025-01-01'
  AND fecha <  '2026-01-01';

-- Mejora: el motor usa un index range scan en lugar de leer toda la tabla,
-- y se reduce la cantidad de datos transferidos al leer solo 2 columnas.
