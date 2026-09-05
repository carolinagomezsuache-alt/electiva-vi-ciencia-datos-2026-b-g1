PARCIAL-C1 
NOMBRE: Wendy Carolina Gomez Suache

Caso: Cafetería "El Aroma"

# Contexto
"El Aroma" es una cafetería de barrio que combina la venta de café de especialidad, bebidas frías y postres artesanales. El negocio opera bajo tres canales principales: atención en el local físico (mesas y venta en mostrador), pedidos a domicilio gestionados a través de una aplicación de delivery, y una presencia activa en redes sociales (Instagram y Google Maps), donde los clientes publican fotos de los productos y dejan reseñas sobre su experiencia.

Debido a esta combinación de canales, la cafetería genera información de distinta naturaleza: registros de ventas con estructura fija provenientes del sistema de punto de venta (POS), pedidos con formato semiestructurado enviados por la app de domicilios, y contenido no estructurado como comentarios de clientes y fotografías compartidas en redes. Esta diversidad de datos representa tanto un reto como una oportunidad: si se integran y analizan correctamente, pueden ayudar al dueño del negocio a entender qué productos se venden más, identificar tendencias de consumo, anticipar la demanda futura y mejorar la toma de decisiones sobre inventario, personal y estrategias de marketing.

1. Tipos de datos y clasificación


## 1. Tipos de datos y clasificación

| # | Dato | Fuente | Clasificación |
|---|------|--------|----------------|
| 1 | Registro de ventas diarias (fecha, producto, cantidad, precio) en el sistema POS | Base de datos del punto de venta | Estructurado (tablas con filas y columnas fijas) |
| 2 | Pedidos recibidos por la app de domicilios (JSON con cliente, productos, dirección, notas) | App de delivery | Semiestructurado (tiene etiquetas/campos, pero estructura flexible, ej. JSON o XML) |
| 3 | Comentarios y reseñas de clientes en Google Maps o redes sociales | Redes sociales / reseñas | No estructurado (texto libre, sin formato fijo) |
| 4 | Fotos de los productos publicadas por clientes en Instagram | Redes sociales | No estructurado (imágenes) |

2. Preguntas de analítica
Descriptiva: ¿Cuál fue el producto más vendido en la cafetería durante el último mes?
Predictiva: ¿Cuántas unidades de café se venderán la próxima semana, según la tendencia histórica de ventas y factores como el clima o los días festivos?

3. Diagrama del flujo de datos
+-----------+     +------------------+     +-------------+     +----------------+
|  Fuente   | --> | Almacenamiento   | --> |  Análisis   | --> | Visualización  |
+-----------+     +------------------+     +-------------+     +----------------+
POS, app de       Base de datos /            Modelos y BI       Dashboard con
domicilios,        data warehouse en          (Power BI, Excel   gráficos de
reseñas             la nube                    avanzado)          ventas/tendencias

Detalle:

Fuente: sistema POS, app de domicilios, reseñas en Google.
Almacenamiento: base de datos en la nube (data warehouse).
Análisis: herramientas de BI (Power BI, Excel avanzado) o modelos estadísticos.
Visualización: dashboard con gráficos de ventas y tendencias.

4. English sentences

- Descriptive analytics summarizes historical data to explain what has already happened in the business, such as which products sold best last month. 

- Predictive analytics goes a step further, using statistical models and past patterns to forecast what is likely to happen in the future, such as next week's demand.

5. Referencias bibliográficas

- IBM. (2025). What is unstructured data? IBM Think. https://www.ibm.com/think/topics/unstructured-data

- IBM. (2026). Structured vs. unstructured data: What's the difference? IBM Think. https://www.ibm.com/think/topics/structured-vs-unstructured-data

- IBM. (2026). What is predictive analytics? IBM Think. https://www.ibm.com/think/topics/predictive-analytics

- IBM. (2025). What is prescriptive analytics? IBM Think. https://www.ibm.com/think/topics/prescriptive-analytics

- UNSW Online. (2025). Descriptive, predictive and prescriptive analytics: What are the differences? https://studyonline.unsw.edu.au/blog/descriptive-predictive-prescriptive-analytics

- Wikipedia contributors. (s.f.). Semi-structured data. Wikipedia. https://en.wikipedia.org/wiki/Semi-structured_data
