Dossier de Fundamentos — Cierre C1
Predicción de demanda en un restaurante mediante Ciencia de Datos

Estudiante: Wendy Carolina Gómez Suache Programa: Ingeniería Mecatrónica Asignatura: Ciencia de Datos | Periodo 2026-B Semana: 5 · Corte 1

Resumen del proyecto

Un restaurante presenta variaciones altas e imprevistas en la demanda diaria de platillos del menú. Esto genera dos problemas simultáneos: desperdicio de insumos perecederos en días de baja venta y desabastecimiento o pérdida de clientes en días de alta concurrencia. Este dossier reúne, de forma coherente y mejorada, el encuadre del problema, las fuentes de datos, la arquitectura propuesta y el tipo de analítica que se aplicará para resolverlo.

1. Pregunta de negocio y decisión esperada

Pregunta de negocio: ¿Cuál será la demanda estimada de cada platillo del menú para los próximos 7 días, considerando el histórico de ventas, el día de la semana y las condiciones climáticas locales?

Decisión / acción esperada: Con base en la demanda proyectada, cada domingo se ajustará la planificación de compras de ingredientes perecederos: se reducirá el inventario de los platillos con baja demanda estimada y se reforzará el de aquellos con alta demanda proyectada.

Impacto esperado: Reducción estimada del 15% en el desperdicio de materia prima perecedera y optimización del costo operativo de inventario.

2. Fuentes de datos, clasificación y "V" del Big Data
2.1 Inventario de fuentes
Fuente de datos	Descripción / formato	Clasificación
Histórico de ventas (Sistema POS)	Base de datos relacional (PostgreSQL) con fecha, hora, platillo, cantidad y precio	Estructurado
Datos meteorológicos (OpenWeatherMap API)	Respuestas en JSON con temperatura, humedad y precipitación	Semiestructurado
Calendario de festivos y eventos locales	Dataset oficial de festivos nacionales y eventos especiales (CSV)	Semiestructurado
Comentarios de clientes (Google Reviews / redes)	Opiniones y texto libre sobre la experiencia	No estructurado
Fotos de platillos servidos	Imágenes para control de calidad antes de salir a mesa	No estructurado
Inventario de insumos y proveedores	Archivos XML/CSV de stock, proveedores y caducidad	Semiestructurado
Pedidos a domicilio (apps de delivery)	Registros tabulados de fechas, direcciones y tiempos de entrega	Estructurado
2.2 "V" del Big Data más críticas
Veracidad — Si el POS registra mal una venta o la API del clima entrega datos desactualizados, el modelo predictivo generará estimaciones erróneas, y comprar insumos perecederos con base en pronósticos imprecisos produce pérdidas económicas directas o desabastecimiento.
Variedad — Predecir bien la demanda exige fusionar datos estructurados (POS), semiestructurados (clima, festivos, inventario) y no estructurados (reseñas de clientes sobre platillos de temporada).
Valor — Todo el esfuerzo analítico se traduce en una acción concreta: reducir el desperdicio de insumos en un 15% y mejorar el margen operativo semanal de la cocina.
2.3 Reto de veracidad detectado

Problema: registros duplicados o incoherentes cuando el POS local pierde conexión, acumula ventas offline y las envía en bloque con el mismo timestamp, o cuando el personal registra mal una anulación.

Detección: reglas de validación en el pipeline de datos que identifiquen outliers (p. ej., 50 platillos vendidos en el mismo segundo) y transacciones con IDs duplicados.

Mitigación: limpiar las marcas de tiempo usando la hora real de impresión de la comanda en cocina antes de alimentar los modelos.

3. Arquitectura de datos propuesta
text
+-------------------------------------------------------------------------------------------------------+
|                                        FUENTES DE DATOS                                                 |
|  Base POS (Postgres)      API Clima (OpenWeather)      Reseñas (Google / Redes)      Inventario (CSV)  |
+-------------------------------------------------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|  1. INGESTA        Apache Kafka (tiempo real) / Apache NiFi (extracción programada)                    |
+-------------------------------------------------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|  2. ALMACENAMIENTO CRUDO   Data Lake (Amazon S3 / MinIO) — archivos Parquet, JSON y RAW                 |
+-------------------------------------------------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|  3. PROCESAMIENTO   Apache Spark / PySpark — limpieza, agregación, modelado dimensional                 |
+-------------------------------------------------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|  4. ALMACENAMIENTO ANALÍTICO   Data Warehouse (PostgreSQL / Snowflake) — modelo estrella                |
+-------------------------------------------------------------------------------------------------------+
                                         |
                                         v
+-------------------------------------------------------------------------------------------------------+
|  5. ANÁLISIS Y BI   Power BI / Metabase — dashboards de demanda y control de inventario                 |
+-------------------------------------------------------------------------------------------------------+
3.1 Decisiones técnicas

¿Data Lake o Data Warehouse? Se adopta una arquitectura híbrida (Lakehouse):

Data Lake (S3/MinIO) para recibir datos crudos (JSON de clima, texto de reseñas, transacciones sin procesar) de forma económica y flexible, sin esquema previo.
Data Warehouse (PostgreSQL/Snowflake) para consolidar los datos limpios en un modelo dimensional (hechos de ventas; dimensiones de tiempo, menú y clima), garantizando consultas rápidas para la gerencia.

¿Batch o Streaming? Se usa un enfoque mixto (arquitectura Lambda):

Streaming para las transacciones del POS y alertas de stock en horas pico.
Batch nocturno para consolidar históricos de clima, calcular promedios semanales y reentrenar el modelo predictivo.
3.2 Herramientas por etapa
Etapa	Herramienta	Justificación
Ingesta	Apache Kafka	Baja latencia y alta tolerancia a fallas para eventos de venta y cocina
Almacenamiento crudo	Amazon S3 / MinIO	Almacenamiento de objetos escalable y de bajo costo
Procesamiento	Apache Spark (PySpark)	Motor distribuido para limpieza, uniones y ML sobre grandes volúmenes
Almacenamiento analítico	PostgreSQL / Snowflake	Motor relacional robusto para consultas SQL complejas
Análisis / BI	Power BI / Metabase	Paneles interactivos para cocina y administración
4. Tipos de analítica y riesgo ético
4.1 Preguntas por tipo de analítica
Tipo	Pregunta clave
Descriptiva	¿Cuántas porciones de cada platillo se vendieron en promedio por día el último mes?
Diagnóstica	¿Por qué cayó un 30% la venta de sancocho el sábado pasado?
Predictiva (objetivo principal)	¿Cuántas órdenes de la especialidad de la casa se venderán el próximo viernes si lloverá por la tarde?
Prescriptiva (objetivo complementario)	¿Qué cantidad de kg de carne y vegetales perecederos se debe comprar el domingo para minimizar el desperdicio y garantizar 98% de disponibilidad?

El proyecto se centra en analítica predictiva, con un componente de analítica prescriptiva que traduce la predicción en una recomendación de compra.

Enfoque de Machine Learning: supervisado, porque se cuenta con datos históricos etiquetados (cantidad vendida por fecha) y variables de entrada conocidas (día de la semana, clima, festivos). Algoritmos candidatos: Regresión Lineal Múltiple, Random Forest Regressor o XGBoost Regressor.

4.2 Riesgo ético identificado

Sesgo de selección por datos históricos atípicos: si el modelo se entrena incluyendo periodos atípicos (restricciones pasadas, festividades no recurrentes), asumirá una demanda irreal y generará compras equivocadas y desperdicio masivo.

Mitigación:

Filtrado de anomalías: excluir periodos atípicos del entrenamiento mediante detección de outliers.
Supervisión humana en el bucle (human-in-the-loop): el chef o administrador de cocina valida la recomendación antes de emitir la orden de compra.
5. Ciclo de vida del proyecto
text
[1. Pregunta]   -> ¿Cuál será la demanda estimada de platillos para los próximos 7 días?
       |
       v
[2. Obtener]    -> Extracción de datos POS, consumo de la API de clima, lectura de inventario
       |
       v
[3. Limpiar]    -> Eliminación de duplicados, imputación de nulos, formateo de fechas
       |
       v
[4. Analizar]   -> Entrenamiento del modelo predictivo (clima + demanda)
       |
       v
[5. Visualizar] -> Dashboard con demanda estimada y sugerencia de compra
       |
       v
[6. Decidir]    -> Ajuste semanal (cada domingo) de la orden de compra de insumos perecederos
6. Referencias bibliográficas
Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2021). Lakehouse: A new generation of open platforms that unify data warehousing and advanced analytics. Proceedings of CIDR.
Barocas, S., Hardt, M., & Narayanan, A. (2023). Fairness and machine learning: Limitations and opportunities. MIT Press.
Cai, L., & Zhu, Y. (2015). The challenges of data quality and data quality assessment in the big data era. Data Science Journal, 14, 2.
Davenport, T. H., & Harris, J. (2017). Competing on analytics: Updated, with a new introduction. Harvard Business Press.
Kelleher, J. D., Mac Namee, B., & D'Arcy, A. (2020). Fundamentals of machine learning for predictive data analytics (2nd ed.). MIT Press.
Kleppmann, M. (2017). Designing data-intensive applications. O'Reilly Media.
Marz, N., & Warren, J. (2015). Big Data: Principles and best practices of scalable realtime data systems. Manning Publications.
Provost, F., & Fawcett, T. (2013). Data science for business. O'Reilly Media.
Shmueli, G., Bruce, P. C., Gedeck, P., & Patel, N. R. (2020). Data mining for business analytics. John Wiley & Sons.
White, T. (2015). Hadoop: The definitive guide (4th ed.). O'Reilly Media.
Zikopoulos, P., DeRoos, D., Bienko, K., Buglio, R., & Eaton, C. (2015). Big data analytics: Beyond the hype. McGraw-Hill Education.
