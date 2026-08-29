# Actividad Semana 2: Clasificación de Datos y las "V" del Big Data

**Estudiante:** Wendy Carolina Gómez Suache  
**Asignatura:** Ciencia de Datos | Periodo 2026-B  
**Programa:** Ingeniería Mecatrónica  

---

## 1. Clasificación de Fuentes de Datos (6+ Fuentes)

Para el sistema de predicción de demanda en nuestro restaurante, se identifican las siguientes fuentes de datos organizadas según su estructura:

| Fuente de Datos | Descripción / Formato | Clasificación |
| :--- | :--- | :--- |
| **1. Transacciones del Sistema POS** | Base de datos PostgreSQL con tablas de ventas, horarios, precios e ítems. | **Estructurado** |
| **2. Datos Meteorológicos (OpenWeather API)** | Respuestas en formato JSON con temperatura, humedad y precipitación. | **Semiestructurado** |
| **3. Comentarios de Clientes (Google Reviews / Redes)** | Opiniones y resúmenes de experiencia en texto libre. | **No estructurado** |
| **4. Fotos e Imágenes de Platos Servidos** | Fotografías tomadas para control de calidad antes de salir a mesa. | **No estructurado** |
| **5. Registros de Inventario y Proveedores** | Archivos XML / CSV exportados de insumos e ingredientes. | **Semiestructurado** |
| **6. Histórico de Pedidos a Domicilio (Apps)** | Registros tabulados de fechas, direcciones y tiempos de entrega. | **Estructurado** |

---

## 2. "V" del Big Data Relevantes y Críticas

Las tres **V** más críticas para nuestro caso de estudio son:

1. **Veracidad:**  
   * *Justificación:* Si los datos del POS registran mal un platillo, o la API del clima reporta datos desactualizados, los modelos predictivos generarán estimaciones erróneas. Comprar insumos perecederos con base en pronósticos imprecisos genera pérdidas económicas directas o desabastecimiento.
2. **Variedad:**  
   * *Justificación:* Para predecir correctamente la demanda no basta con ver ventas pasadas (tablas). Necesitamos fusionar datos estructurados (tablas POS), semiestructurados (JSON de clima/festivos) y no estructurados (reseñas de clientes sobre platos de temporada).
3. **Valor:**  
   * *Justificación:* Todo el esfuerzo analítico debe traducirse en acciones concretas: reducir el desperdicio de insumos perecederos en un 15% y mejorar el margen operativo semanal de la cocina.

---

## 3. Reto de Veracidad (Calidad de Datos) y Detección

* **Problema de veracidad detectado:**  
  **Registros duplicados o incoherentes por fallas de conexión:** Ocurre cuando el sistema POS local se queda sin internet y acumula ventas offline, enviándolas en bloque más tarde con la misma marca de tiempo (*timestamp*), o cuando los meseros registran anulaciones de pedidos incorrectamente.
* **Cómo detectarlo y solucionarlo:**
  * **Detección:** Implementar reglas de validación en la canalización de datos (*data pipeline*), verificando *outliers* o picos atípicos (por ejemplo, 50 platillos vendidos exactamente al mismo segundo) e identificando registros con IDs de transacción duplicados.
  * **Acción:** Filtrar y limpiar las marcas de tiempo usando la hora real de impresión de comanda en cocina antes de alimentar los modelos de predicción.
  
  ## 4. Referencias Bibliográficas

* **Cai, L., & Zhu, Y.** (2015). The challenges of data quality and data quality assessment in the big data era. *Data Science Journal*, 14, 2. https://doi.org/10.5334/dsj-2015-002
* **Kelleher, J. D., Mac Namee, B., & D'Arcy, A.** (2020). *Fundamentals of machine learning for predictive data analytics: Algorithms, worked examples, and case studies* (2nd ed.). MIT Press.
* **Provost, F., & Fawcett, T.** (2013). *Data science for business: What you need to know about data mining and data-analytic thinking*. O'Reilly Media.
* **Zikopoulos, P., DeRoos, D., Bienko, K., Buglio, R., & Eaton, C.** (2015). *Big data analytics: Beyond the hype*. McGraw-Hill Education.

  