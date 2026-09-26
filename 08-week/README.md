# Taller guiado · Primeros pasos con cuadernos y pandas

**Ciencia de Datos · Semana 8 · Cargar, graficar y limpiar datos con Python**

| Programa | Ingeniería Industrial |
|---|---|
| Asignatura | Electiva · Ciencia de Datos |
| Unidad | Unidad 2 · Conexión de datos |
| Semana / Corte | 8 · Corte 2 |
| Periodo | 2026‑B |
| Estudiante | Wendy Carolina Gómez Suache |

## Objetivos

- Reconocer qué es un cuaderno (.ipynb) y ejecutarlo celda por celda.
- Entender qué es una librería y para qué sirven pandas y matplotlib.
- Cargar un archivo CSV y explorarlo antes de usarlo.
- Graficar los datos tal como llegan y descubrir en el gráfico sus problemas de calidad.
- Hacer una limpieza mínima y comparar el antes y el después.

## El caso

Una planta de empaques registra cada día cuántas unidades produjo cada una de sus **3 máquinas**, cuántas salieron defectuosas y a qué temperatura trabajó la máquina, durante la primera quincena de septiembre. Los datos son **ficticios** y traen, a propósito, los errores típicos de un registro real.

## Qué se hizo

Se ejecutó el cuaderno `taller-primeros-pasos.ipynb` completo, en orden, de principio a fin (Ejecutar todo), sin modificar ni agregar ninguna celda de código: todo el código ejecutado es el que ya venía escrito en el cuaderno. Solo se completaron las celdas de texto marcadas con 🧠 con lo observado en las salidas reales.

## Puntos de control — resultado obtenido al ejecutar

| Dónde | Debe obtener (según la guía) | Obtenido |
|---|---|---|
| Parte 3 | La tabla carga y muestra 5 columnas | ✅ `fecha`, `maquina`, `unidades_producidas`, `unidades_defectuosas`, `temperatura_c` |
| Parte 4 | `df.shape` = (47, 5) · `value_counts()` muestra 7 nombres de máquina | ✅ `(47, 5)` · 7 nombres: `M-01`, `M-02`, `M-03`, `m-02`, ` M-03`, `M01`, `m-03` |
| Parte 5 | 3 gráficos: líneas con un pico, barras con 7 barras e histograma de temperatura | ✅ generados en el cuaderno |
| Parte 6.1 | Quedan exactamente 3 máquinas: M-01, M-02 y M-03 | ✅ `M-01: 16`, `M-02: 16`, `M-03: 15` |
| Parte 6.2 | 2 filas repetidas eliminadas | ✅ 2 |
| Parte 6.3 | 2 temperaturas vacías antes y 0 después | ✅ 2 → 0 |
| Parte 6.4 | 44 filas al terminar la limpieza | ✅ 44 (se retiró la fila del 2026-09-07, M-01, 11.600 unidades) |
| Parte 9 | Archivo `produccion_septiembre_limpio.csv` con 44 filas | ✅ generado |

## Resultado del análisis (Parte 8)

Promedio de `% defectos` y `temperatura_c` por máquina, sobre los datos ya limpios:

| Máquina | % defectos promedio | Temperatura promedio (°C) |
|---|---|---|
| M-01 | 1.92 | 33.06 |
| M-02 | 1.17 | 31.49 |
| M-03 | 5.82 | 37.13 |

M-03 es la máquina con más defectos y también la de mayor temperatura promedio. Esto es una **correlación**, no una prueba de que la temperatura **cause** los defectos.

## Entrega

1. Preguntas 🧠 respondidas en las celdas de texto del cuaderno.
2. Cuaderno ejecutado completo, sin errores.
3. Subir a fork del repositorio de la clase, en la carpeta `08-week/01-session/`.
4. `git add .` · `git commit -m "Taller primeros pasos semana 08"` · `git push`.
