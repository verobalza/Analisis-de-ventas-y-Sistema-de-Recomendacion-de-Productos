 # Análisis de Ventas y Sistema de Recomendación de Productos

## Descripción  
Este proyecto surge como respuesta a una problemática detectada en el análisis de ventas de una tienda ficticia de alimentos saludables. A través de un dashboard interactivo, se observó un descenso progresivo en las ventas mes a mes. Tras evaluar posibles causas, se concluyó que la ausencia de un apartado de recomendaciones en la web representaba una oportunidad clave para mejorar la conversión comercial.

El objetivo fue desarrollar un sistema que, a partir del historial de compras, pudiera sugerir productos complementarios a los clientes, aumentando así el ticket promedio y la fidelización.

## Objetivos  
- Analizar el comportamiento de compra de los clientes  
- Identificar asociaciones entre productos mediante métricas como soporte, confianza y lift  
- Visualizar métricas clave en dashboards interactivos  
- Integrar recomendaciones en la web para mejorar la conversión comercial

## Componentes del proyecto  
- Base de datos: Estructura en Excel con registros de ventas simuladas  
- Consultas: Exploración de datos según problemáticas comerciales (`consultas_bd.sql`)  
- Requerimientos: Documento funcional ampliado con necesidades del sistema (`Requerimientos.pdf`)  
- Dashboard: Visualización de KPIs en Excel (`dashboard_sanofood.pbix`)  
- Modelo de recomendación: Script en Python con cálculo de soporte, confianza y lift (`market_basket_A.py`)  
- Resultados: Archivo CSV con asociaciones entre productos (`asociaciones.csv`)  
- Informe final: Documento de conclusiones del análisis (`conclusiones.pdf`)

## Herramientas utilizadas  
- Python (Pandas, SQLite3, itertools)  
- Excel  
- SQL  
- Documentación técnica en Word

## Notas  
Este proyecto utiliza datos simulados. El nombre del establecimiento ha sido modificado por motivos de privacidad. La base de datos completa no se incluye por tamaño, pero se proporciona una muestra estructural para referencia.


## Estructura del repositorio
- `consultas_sql/`: Archivo con las consultas SQL utilizadas para el análisis de ventas e insights.
- `requerimientos/`: Documento funcional con los requerimientos del sistema de recomendación.
- `market_basket_analysis/`: Script en Python para generar reglas de asociación entre productos.
- `asociacion_productos/`: Resultados del modelo, incluyendo métricas como lift, soporte y confianza.
- `dashboards/`: Capturas de los dashboards desarrollados en Power BI.
- `conclusiones/`: Informe final con hallazgos clave y recomendaciones estratégicas.


## Documentación adicional

- [Requerimientos](requirements/Requerimientos.pdf) 
- [Consultas SQL - análisis de ventas](consultas/consultas_bd.sql)
- [Market basket analisis](market_basket_analisis/market_Basket_A.py)
- [asociaciones de productos](asociacion_productos/asociaciones.csv)
- [conclusiones](conclusiones/conclusiones.pdf)
## Dashboards del proyecto

Este proyecto incluye dos dashboards desarrollados en Power BI:

- **Dashboard de ventas**: Visualiza ingresos, unidades vendidas y evolución mensual.
- **Dashboard de recomendaciones**: Muestra asociaciones entre productos mediante métricas como lift, soporte y confianza.

- [Capturas de los dashboards](dashboard/Capturas_dashboard.pdf)
> Nota: El archivo original del dashboard en Power BI (.pbix) no se incluye por limitaciones de tamaño en GitHub. Si deseas revisarlo, puedes solicitarlo directamente.
## Autora  
Verónica Balza Herrera  
Analista de Datos | Ingeniería Civil | Python | Estrategia de Negocio  
Castellón de la Plana, España  
LinkedIn: https://linkedin.com/in/veronicabalza  
GitHub: https://github.com/veronicabalza

