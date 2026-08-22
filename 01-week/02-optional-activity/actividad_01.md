# Actividad Semana 1: Encuadre de un Proyecto de Datos

**Estudiante:** Wendy Carolina Gómez Suache  
**Asignatura:** Ciencia de Datos | Periodo 2026-B  
**Programa:** Ingeniería Mecatrónica  


## 1. Problema Real y Pregunta de Negocio
* **Sector:** Servicios de Gastronomía / Restauración.
* **Problema:** Un restaurante presenta variaciones altas e imprevistas en la demanda diaria de platillos del menú, lo que ocasiona desperdicio de insumos perecederos en días de baja venta o desabastecimiento/pérdida de clientes en días de alta concurrencia.
* **Pregunta de negocio:** ¿Cuál será la demanda estimada de cada platillo del menú para los próximos 7 días, considerando el histórico de ventas, el día de la semana y las condiciones climáticas locales?

## 2. Datos Necesarios y Fuentes
1. **Histórico de ventas diarias por platillo:** 
   * *Fuente:* Sistema POS (Point of Sale) del restaurante mediante base de datos relacional (PostgreSQL / MySQL).
2. **Datos meteorológicos locales (temperatura y lluvia):** 
   * *Fuente:* API pública de clima (ej. OpenWeatherMap API).
3. **Calendario de festivos y eventos locales:** 
   * *Fuente:* Dataset oficial de días festivos nacionales y eventos especiales.

## 3. Decisión o Acción Esperada
* **Acción concreta:** Ajustar semanalmente (cada domingo) la planificación de compras de ingredientes perecederos en la cocina, reduciendo el inventario de platillos con baja demanda estimada y reforzando los insumos para aquellos de alta demanda proyectada.
* **Impacto esperado:** Reducción estimada del 15% en el desperdicio de materia prima perecedera y optimización del costo operativo de inventario.

## 4. Tipo de Analítica
* **Clasificación:** **Analítica Predictiva** (con componentes de analítica prescriptiva para la toma de decisiones de compra).