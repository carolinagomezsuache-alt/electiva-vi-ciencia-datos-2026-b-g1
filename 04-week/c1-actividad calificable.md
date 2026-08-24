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
