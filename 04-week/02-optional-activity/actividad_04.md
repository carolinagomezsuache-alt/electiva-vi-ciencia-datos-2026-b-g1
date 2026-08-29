# Actividad Semana 4: Tipos de Analítica y Ética

**Estudiante:** Wendy Carolina Gómez Suache  
**Asignatura:** Ciencia de Datos | Periodo 2026-B  
**Programa:** Ingeniería Mecatrónica  



## 1. Preguntas por Tipo de Analítica

| Tipo de Analítica | Pregunta Clave del Negocio |
| :--- | :--- |
| **Descriptiva** | ¿Cuántas porciones de cada platillo del menú se vendieron en promedio por día durante el último mes? |
| **Diagnóstica** | ¿Por qué cayó un 30% la venta de sancocho y platos calientes el sábado pasado? *(ej. debido al aumento atípico de temperatura)*. |
| **Predictiva** | ¿Cuántas órdenes de la especialidad de la casa se venderán el próximo viernes considerando que lloverá por la tarde? |
| **Prescriptiva** | ¿Qué cantidad exacta de kg de carne y vegetales perecederos se deben comprar el domingo para minimizar el desperdicio y garantizar un 98% de disponibilidad? |

---

## 2. Enfoque de Machine Learning (Supervisado vs. No Supervisado)

Para las capas **Predictiva** y **Prescriptiva**, se utilizará **Machine Learning Supervisado**:

* **Justificación:** Se cuenta con datos históricos etiquetados (registros del POS con la cantidad exacta de platos vendidos por fecha) junto con variables de entrada conocidas (*features* como día de la semana, clima y si es festivo). 
* **Algoritmos Candidatos:** Regresión Lineal Múltiple, Random Forest Regressor o XGBoost Regressor para predecir la variable continua (cantidad demandada de platillos).

---

## 3. Riesgos Éticos, Sesgos y Mitigación

### Sesgo Identificado: **Sesgo de Selección por Datos Históricos Atípicos**
* **Problema:** Si el modelo se entrena con datos de períodos atípicos (como restricciones pasadas o festividades no recurrentes), asumirá una demanda irreal, generando compras equivocadas y desperdicio masivo de alimentos.

### Estrategia de Mitigación:
1. **Filtrado de Anomalías:** Aplicar reglas de detección de *outliers* para excluir períodos atípicos del entrenamiento.
2. **Supervisión Humana en el Bucle (*Human-in-the-loop*):** El chef o administrador de cocina revisará y validará la recomendación antes de emitir la orden de compra.

## 4. Referencias Bibliográficas

* **Barocas, S., Hardt, M., & Narayanan, A.** (2023). *Fairness and machine learning: Limitations and opportunities*. MIT Press.
* **Kelleher, J. D., Mac Namee, B., & D'Arcy, A.** (2020). *Fundamentals of machine learning for predictive data analytics: Algorithms, worked examples, and case studies* (2nd ed.). MIT Press.
* **Provost, F., & Fawcett, T.** (2013). *Data science for business: What you need to know about data mining and data-analytic thinking*. O'Reilly Media.
* **Shmueli, G., Bruce, P. C., Gedeck, P., & Patel, N. R.** (2020). *Data mining for business analytics: Concepts, techniques and applications in Python*. John Wiley & Sons.