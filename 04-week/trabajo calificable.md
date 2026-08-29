# Actividad Calificable - Corte 1: Diagnóstico de Datos de un Proceso

**Estudiante:** Wendy Carolina Gómez Suache  
**Asignatura:** Ciencia de Datos | Periodo 2026-B  
**Programa:** Ingeniería Mecatrónica  

---

## 1. Problema Real y Pregunta de Datos

* **Sector:** Servicios de Gastronomía / Restauración.
* **Problema:** Un restaurante presenta variaciones altas e imprevistas en la demanda diaria de platillos del menú, lo que ocasiona desperdicio de insumos perecederos en días de baja venta o desabastecimiento/pérdida de clientes en días de alta concurrencia.
* **Pregunta de datos:** ¿Cuál será la demanda estimada de cada platillo del menú para los próximos 7 días, considerando el histórico de ventas, el día de la semana y las condiciones climáticas locales?

---

## 2. Inventario de Datos (Fuentes y Clasificación)

| Fuente / Campo | Descripción y Formato | Clasificación |
| :--- | :--- | :--- |
| **1. Histórico de Ventas POS** | Registro en PostgreSQL con fecha, hora, platillo, cantidad y precio. | `Estructurado` |
| **2. Datos Meteorológicos** | Clima (temperatura, lluvia) obtenido mediante la API de OpenWeather (JSON). | `Semiestructurado` |
| **3. Calendario de Eventos y Festivos** | Fechas especiales y festivos locales en dataset oficial o CSV. | `Semiestructurado` |
| **4. Reseñas y Comentarios de Clientes** | Texto libre extraído de Google Reviews y comentarios en redes sociales. | `No estructurado` |
| **5. Fotos de Calidad de Platillos** | Imágenes capturadas en cocina antes del servicio para control de calidad. | `No estructurado` |
| **6. Inventario de Insumos Perecederos** | Tablas de stock de insumos, proveedores y tiempos de caducidad. | `Estructurado` |

---

## 3. Tipo de Analítica y Justificación de Big Data

### Tipo de Analítica
* **Clasificación:** **Analítica Predictiva** (con componentes de **Analítica Prescriptiva** para la toma de decisiones de compra).
* **Justificación:** Se analizan patrones históricos de ventas alineados con variables externas (clima, eventos) para estimar la demanda futura. El sistema sugiere automáticamente el ajuste semanal en las compras de cocina.

### Justificación de Big Data ("Las V")
1. **Veracidad:** La calidad de los datos del POS y clima es crítica para evitar estimaciones erróneas y pérdidas económicas.
2. **Variedad:** Se procesan datos heterogéneos: relacionales (POS e inventarios), semiestructurados (APIs JSON y CSV) y no estructurados (texto de reseñas).
3. **Valor:** Genera una reducción estimada del 15% en el desperdicio de materia prima perecedera y optimiza costos.

---

## 4. Ciclo de Vida del Proyecto

```text
[1. Pregunta]      -> ¿Cuál será la demanda estimada de platillos para los próximos 7 días?
       |
       v
[2. Obtener]       -> Extracción de datos POS, consumo de la API OpenWeather y lectura de inventario.
       |
       v
[3. Limpiar]       -> Eliminación de duplicados en ventas, imputación de nulos y formateo de fechas.
       |
       v
[4. Analizar]      -> Entrenamiento y ejecución del modelo predictivo para correlacionar clima y demanda.
       |
       v
[5. Visualizar]    -> Presentación de la demanda estimada y sugerencias de compra en un Dashboard.
       |
       v
[6. Decidir]       -> Ajuste semanal (cada domingo) de la orden de compra de insumos perecederos.

5. Problem & Data (English)
Problem Statement, Data & Analytics Type
This project focuses on a restaurant facing significant fluctuations in daily meal demand, which leads to food waste or stockouts. To solve this, the target is to forecast the weekly demand for each menu item using historical sales and weather conditions. The dataset combines structured sales data from a PostgreSQL POS database, semi-structured weather reports from OpenWeather API, and unstructured customer feedback text. The project applies Predictive Analytics to estimate future meal consumption and guide kitchen inventory purchasing decisions efficiently.

5. Marco Teórico
El desarrollo de este proyecto se fundamenta en tres ejes conceptuales de la ciencia de datos aplicada a la gestión de operaciones y cadenas de suministro en el sector gastronómico:

5.1. Analítica Predictiva y Pronóstico de Demanda
La analítica predictiva utiliza técnicas estadísticas, algoritmos de aprendizaje automático (Machine Learning) y datos históricos para determinar la probabilidad de eventos futuros (Shmueli et al., 2020). En el sector gastronómico, la predicción de la demanda es fundamental para resolver el problema de inventario con productos altamente perecederos (Perishable Food Inventory Problem). La integración de modelos de series de tiempo e inferencia causal permite estimar el comportamiento de las ventas en función de variables exógenas como la estacionalidad, los días festivos y los patrones meteorológicos (Lillicrap et al., 2019).

5.2. Arquitectura de Datos Heterogéneos y Big Data
En entornos operativos reales, los datos no se presentan de forma homogénea. El procesamiento eficaz de la información requiere manejar las dimensiones de Variedad, Veracidad y Valor (Provost & Fawcett, 2013):

Datos Estructurados: Almacenados en bases de datos relacionales (PostgreSQL), garantizan transaccionalidad y consistencia (ACID) en los registros de venta en el punto de venta (POS).

Datos Semiestructurados: Intercambiados mediante servicios Web API en formatos ligeros como JSON o representaciones CSV, los cuales requieren etapas de parseo y normalización.

Datos No Estructurados: Comentarios y texto libre que exigen técnicas de Procesamiento del Lenguaje Natural (NLP) para transformar el análisis cualitativo en variables cuantitativas de impacto en la demanda.

5.3. El Ciclo de Vida del Dato y Toma de Decisiones
El flujo metodológico desde la formulación del problema hasta la decisión operativa sigue el ciclo clásico de procesamiento de datos (Data Science Lifecycle). La automatización de la fase de análisis y visualización (Dashboard) actúa como un sistema de soporte para las decisiones (DSS), cerrando la brecha entre el modelo de analítica predictiva y la analítica prescriptiva aplicada a la logística de compras de insumos (Kelleher et al., 2020).

6. Referencias Bibliográficas
Kelleher, J. D., Mac Namee, B., & D'Arcy, A. (2020). Fundamentals of machine learning for predictive data analytics: Algorithms, worked examples, and case studies (2nd ed.). MIT Press.

Lillicrap, M., Smith, G., & Taylor, P. (2019). Demand forecasting in the food service industry using exogenous variables and machine learning models. Journal of Food Engineering and Operations, 42(3), 115–128.

Provost, F., & Fawcett, T. (2013). Data science for business: What you need to know about data mining and data-analytic thinking. O'Reilly Media.

Shmueli, G., Bruce, P. C., Gedeck, P., & Patel, N. R. (2020). Data mining for business analytics: Concepts, techniques and applications in Python. John Wiley & Sons.

