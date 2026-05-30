# mercadolibre-funnel-retention-analysis
# Product Analytics: Análisis de Embudo y Retención de Usuarios en MercadoLibre

## 📝 Descripción del Proyecto
Este proyecto implementa un análisis técnico de **Growth & Product Analytics** utilizando Python para evaluar el comportamiento transaccional y la lealtad de los usuarios de MercadoLibre en Latinoamérica (periodo enero - agosto de 2025). 

A través del modelado de datos con Pandas y la creación de visualizaciones avanzadas con Matplotlib, el análisis diagnostica de manera cuantitativa las tasas de caída (*drop-off*) en el embudo de conversión y mide la retención de usuarios mediante matrices temporales de cohortes y segmentación por países.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3**
* **Pandas:** Para la estructuración y manipulación de DataFrames con métricas analíticas complejas.
* **Matplotlib:** Para el diseño personalizado de gráficos de líneas, barras y visualizaciones ejecutivas de retención.

## 📊 Estructura del Código Analítico
El script principal `scripts/mercadolibre_resumen.py` procesa de forma estructurada los siguientes bloques de datos:
1. **Embudo General:** Métricas continuas de conversión desde el inicio (`select_item`) hasta el éxito del negocio (`purchase`).
2. **Embudo por País:** Desglose comparativo de conversión en 10 mercados regionales de LATAM.
3. **Retención por País:** Análisis del ciclo de vida del usuario a los 7, 14, 21 y 28 días del registro inicial.
4. **Retención por Cohortes Mensuales:** Diagnóstico cronológico de permanencia para evaluar la estabilidad del engagement mes a mes.

## 📈 Hallazgos Clave e Implicaciones de Negocio (Basado en Datos Reales)

* **Fricción Crítica en la Conversión Early-Stage:** El embudo general revela una caída drástica e inmediata en el primer paso: de los usuarios que seleccionan un ítem (**76.90%**), solo el **11.01%** llega a agregarlo al carrito de compras. La conversión final de compra se sitúa en un **1.25%**. 
  * *Implicación:* La fuga masiva ocurre antes de iniciar la intención de pago. Los esfuerzos de optimización de UX/UI deben centrarse prioritariamente en la experiencia de la página de producto y los disparadores de decisión para "Añadir al carrito".

* **El Desafío de la Retención a Largo Plazo:** Si bien la plataforma muestra un excelente interés y adopción inicial con una retención al Día 7 muy sólida y estable (entre el **85% y 87%** en la mayoría de las cohortes), el compromiso colapsa sistemáticamente hacia el Día 28, alcanzando niveles críticos de apenas el **2% al 3%**.
  * *Implicación:* MercadoLibre es sumamente eficiente atrayendo y entregando valor la primera semana, pero experimenta dificultades severas para retener orgánicamente. Se requieren campañas automatizadas de re-engagement, personalización de ofertas o programas de fidelización para mitigar este abandono del ciclo de vida rápido.

* **Alerta Técnica y Operacional en la Cohorte de Agosto:** Los datos de la cohorte de agosto de 2025 muestran una anomalía severa: la retención al Día 7 cae inusualmente a un **70.8%** y se desintegra por completo para el Día 28, llegando a un **0.2%**.
  * *Implicación:* Este comportamiento fuera de la tendencia histórica apunta directamente a un fallo técnico crítico (ej. caída de la app/web, bugs en el registro) o a un canal de adquisición de tráfico masivo de muy baja calidad durante ese mes específico. Requiere auditoría inmediata del equipo de ingeniería de producto.

* **Desempeño Geográfico Variable:** Mercados líderes como **México (3.10%)** y **Perú (3.20%)** registran los mejores índices de retención terminal al Día 28, mientras que países de menor escala como Bolivia, Ecuador y Paraguay muestran los rendimientos más bajos. En conversión, mercados como Uruguay alcanzan picos excepcionales de éxito en compras de hasta el **4.54%**.

## 🚀 Ejecución y Visualizaciones
El script incluye funciones automáticas para exportar gráficos en alta definición que apoyan el proceso de toma de decisiones. Para ejecutar el pipeline analítico:

1. Clona el repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
