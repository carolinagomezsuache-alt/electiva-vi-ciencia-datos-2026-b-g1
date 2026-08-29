# Actividad Semana 3: Diseño de una Arquitectura de Datos

**Estudiante:** Wendy Carolina Gómez Suache  
**Asignatura:** Ciencia de Datos | Periodo 2026-B  
**Programa:** Ingeniería Mecatrónica  

---

## 1. Diagrama de Arquitectura de Datos (ASCII)

El flujo de datos diseñado desde las fuentes de origen hasta la capa de inteligencia de negocios (BI) se representa a continuación:

```text
+-------------------------------------------------------------------------------------------------------+
|                                        FUENTES DE DATOS                                               |
|  +--------------------+      +---------------------------+      +----------------------------------+  |
|  | Base POS (Postgres)|      | API Clima (OpenWeather)   |      | Reseñas (Google / Redes)         |  |
|  +---------+----------+      +-------------+-------------+      +----------------+-----------------+  |
+------------|-------------------------------|-----------------------------------|----------------------+
             |                               |                                   |
             v                               v                                   v
+-------------------------------------------------------------------------------------------------------+
|                                    1. CAPA DE INGESTA DE DATOS                                        |
|  +-------------------------------------------------------------------------------------------------+  |
|  | Apache Kafka (Ingesta en tiempo real) / Apache NiFi (Extracción programada)                    |  |
|  +-------------------------------------+-----------------------------------------------------------+  |
+----------------------------------------|--------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|                                 2. CAPA DE ALMACENAMIENTO CRUDO                                       |
|  +-------------------------------------------------------------------------------------------------+  |
|  | Data Lake (Amazon S3 / MinIO) - Archivos Parquet, JSON y RAW                                    |  |
|  +-------------------------------------+-----------------------------------------------------------+  |
+----------------------------------------|--------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|                                3. CAPA DE PROCESAMIENTO Y TRANSFORMACIÓN                              |
|  +-------------------------------------------------------------------------------------------------+  |
|  | Apache Spark / PySpark (Limpieza, agregación, modelado dimensional)                             |  |
|  +-------------------------------------+-----------------------------------------------------------+  |
+----------------------------------------|--------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|                                4. CAPA DE ALMACENAMIENTO ANALÍTICO                                    |
|  +-------------------------------------------------------------------------------------------------+  |
|  | Data Warehouse (PostgreSQL / Snowflake) - Modelo Estrella (Hechos y Dimensiones)                |  |
|  +-------------------------------------+-----------------------------------------------------------+  |
+----------------------------------------|--------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|                                    5. CAPA DE ANÁLISIS Y BI                                           |
|  +-------------------------------------------------------------------------------------------------+  |
|  | Power BI / Metabase (Dashboards de predicción de demanda y control de inventario)              |  |
|  +-------------------------------------------------------------------------------------------------+  |
+-------------------------------------------------------------------------------------------------------+

2. Justificación de Decisiones Técnicas
¿Data Lake o Data Warehouse?
Se adopta una arquitectura híbrida (Data Lakehouse):

Data Lake (S3 / MinIO): Necesario en la fase inicial para recibir y almacenar datos en bruto (JSON de clima, texto de reseñas de clientes, transacciones sin procesar) de manera económica y flexible sin requerir un esquema previo.

Data Warehouse (PostgreSQL / Snowflake): Esencial para consolidar los datos una vez limpios y estructurados bajo un modelo dimensional (Tablas de Hechos de Ventas y Dimensiones de Tiempo, Menú y Clima). Esto garantiza consultas rápidas y precisas para la toma de decisiones gerenciales.

¿Batch o Streaming?
Se utiliza un enfoque mixto (Arquitectura Lambda):

Streaming (Tiempo Real): Aplicado a las transacciones del sistema POS y alertas de stock de la cocina para actualizar tableros en tiempo real durante las horas pico de atención.

Batch (Por Lotes): Procesamiento nocturno programado para consolidar históricos de clima, calcular promedios semanales y reentrenar el modelo predictivo de demanda de insumos para los siguientes 7 días.

## 3. Herramientas Candidatas por Etapa

| Etapa | Herramienta Candidata | Justificación de Selección |
| :--- | :--- | :--- |
| **Ingesta** | `Apache Kafka` | Permite transmitir e ingerir eventos de ventas del POS y cambios de estado en cocina con muy baja latencia y alta tolerancia a fallas. |
| **Almacenamiento Crudo** | `Amazon S3` / `MinIO` | Proporciona almacenamiento de objetos escalable y de bajo costo para guardar archivos JSON, CSV y backups en su formato nativo. |
| **Procesamiento** | `Apache Spark` (`PySpark`) | Motor distribuido ideal para realizar transformaciones pesadas, limpieza de datos, uniones de grandes volúmenes y ejecuciones de algoritmos de Machine Learning. |
| **Almacenamiento Analítico** | `PostgreSQL` / `Snowflake` | Ofrece un motor relacional robusto con soporte optimizado para consultas SQL complejas necesarias en reportes gerenciales. |
| **Análisis / BI** | `Power BI` / `Metabase` | Facilita la creación de paneles interactivos e intuitivos para que el equipo de cocina y administración visualice la demanda proyectada de insumos.

## 4. Referencias Bibliográficas

* **Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M.** (2021). Lakehouse: A new generation of open platforms that unify data warehousing and advanced analytics. *Proceedings of Conference on Innovative Data Systems Research (CIDR)*.
* **Kleppmann, M.** (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.
* **Marz, N., & Warren, J.** (2015). *Big Data: Principles and best practices of scalable realtime data systems*. Manning Publications.
* **White, T.** (2015). *Hadoop: The definitive guide: Storage and analysis at Internet scale* (4th ed.). O'Reilly Media.