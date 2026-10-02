# C2 Activity - Model, Query, and Data Cleaning

## 1. ERD (Entity-Relationship Diagram)
* **Entities:** `Cliente` (Customer), `Pedido` (Order), `Producto` (Product).
* **Relationships:** 
  * A customer can place multiple orders (`1` to `N`).
  * An order can contain multiple products (`N` to `M` through a detail table).

## 2. Data & Cleaning (English)
This project focuses on data preprocessing and quality enhancement for a transactional database environment. First, a raw dataset containing customer records was loaded using Python and the Pandas library to audit data discrepancies. During the cleaning pipeline, duplicate entries were safely removed, and text fields like names and cities were stripped and standardized. Incorrect data formats and missing numerical values were systematically addressed through median and mean imputation. Finally, analytical queries combining data filtering and grouping aggregations were executed to extract strategic business intelligence from the cleaned dataset.

## 3. Queries and Findings
* **Query 1:** Filtered customers located in Bogotá and Neiva, calculating the average purchase amount per city.
  * **Finding:** Neiva shows a higher average purchase ticket compared to Bogotá, indicating a strong localized market performance.
* **Query 2:** Filtered customers older than 25 years and aggregated the total purchase amount by age.
  * **Finding:** The 30-year-old demographic group generates the highest cumulative revenue stream for the application.
  