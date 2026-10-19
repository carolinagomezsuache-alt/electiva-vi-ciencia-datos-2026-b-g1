# Actividad Semana 12: Rediseño de un Gráfico

##  1. Diagnóstico del Problema (Antes)
* **Problema detectado:** El gráfico original utilizaba un gráfico de torta con más de 6 categorías y un diseño en 3D, lo que distorsionaba gravemente las proporciones visuales de los datos. Además, carecía de un título descriptivo con conclusión y utilizaba una paleta de colores saturada sin ningún propósito analítico.

---

##  2. Solución y Rediseño Aplicado (Después)
* **Tipo de gráfico correcto:** Se cambió a un **gráfico de barras verticales**, ideal para comparar magnitudes discretas entre categorías.
* **Escala honesta:** Se configuró el eje Y partiendo estrictamente desde cero (`0`), evitando la exageración artificial de las diferencias entre líneas.
* **Color con propósito:** Se utilizó una paleta neutra (gris) para la mayoría de las barras y un color focal (azul institucional) únicamente para resaltar la **Línea D**, que es el objeto de atención principal.
* **Título con conclusión:** Se reemplazó un título genérico por uno analítico que comunica directamente el hallazgo principal: *"La Línea D lidera el rendimiento productivo con 480 u/h"*.

---

## 3. Archivos de la Entrega
* `script_rediseño.py`: Código fuente en Python con la generación del gráfico mediante Matplotlib.
* `grafico_rediseñado.png`: Imagen final optimizada.