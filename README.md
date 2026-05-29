# mercadolibre-funnel-retention-analysis
# Análisis de Embudo de Conversión y Retención de Usuarios (MercadoLibre)

## 📝 Descripción del Proyecto
Este proyecto desarrolla un análisis profundo del comportamiento de los usuarios en la plataforma de MercadoLibre durante el periodo de enero a agosto de 2025. El objetivo principal es identificar fricciones críticas dentro del embudo de conversión (desde la selección de un ítem hasta la compra final) y evaluar la lealtad a largo plazo mediante el análisis de cohortes de retención por país, transformando datos de producto en implicaciones estratégicas de negocio.

## 📊 Estructura de los Datos y Análisis
El análisis se dividió en componentes clave utilizando un modelo dinámico de datos:
1. **Embudo General de Conversión (Funnel):** Evaluación del paso a paso transaccional (`select_item` -> `add_to_cart` -> `begin_checkout` -> `add_shipping_info` -> `add_payment_info` -> `purchase`).
2. **Análisis por Cohortes:** Seguimiento del porcentaje de usuarios que permanecen activos en intervalos clave de tiempo (Días 7, 14, 21 y 28 después del registro).
3. **Segmentación Geográfica:** Comparativa de rendimiento de conversión y retención entre mercados clave de Latinoamérica (México, Brasil, Argentina, Chile, Colombia, Uruguay, Perú, Ecuador, Bolivia y Paraguay).

## 🛠️ Características Técnicas del Reporte
* **Consolidación de Datos:** Uso de funciones de búsqueda y ordenamiento lógico para cruzar métricas de comportamiento temporal por cohortes mensuales.
* **Métricas de Conversión:** Cálculos dinámicos de tasas de caída porcentual (*drop-off*) entre fases consecutivas del embudo.
* **Visualización de Retención:** Construcción de matrices de calor de retención para identificar patrones inusuales en el ciclo de vida del usuario.

## 📈 Conclusiones Clave e Implicaciones de Negocio
* **Optimización del Embudo (Fricción Crítica):** El análisis del embudo general demuestra que la transición entre **"Selección de ítem" (76.9%)** y **"Añadir al carrito" (11.0%)** representa la mayor caída porcentual de usuarios activos. *Implicación:* La etapa prioritaria a mejorar debe ser esta ventana temprana; optimizar la experiencia o los incentivos en esta fase tiene el mayor impacto potencial en la conversión de compra final (la cual se sitúa globalmente en un 1.25%).
* **Comportamiento de la Retención (Ciclo de Vida):** Aunque la retención inicial al Día 7 es sumamente alta y saludable (estable entre el 86% y 87% para casi todas las cohortes), se desploma drásticamente hacia los Días 21 y 28, alcanzando niveles críticos del 2% al 3%. *Implicación:* Si bien la propuesta de valor inicial atrae eficazmente a los usuarios, la plataforma experimenta un reto severo para mantener el compromiso a largo plazo, sugiriendo la necesidad de implementar estrategias de re-engagement y programas de fidelización semanales.
* **Variabilidad por Mercados Regionales:** **México (3.1%)** y **Perú (3.2%)** lideran la retención al Día 28 junto con un desempeño sólido de Brasil, mientras que Bolivia, Ecuador y Paraguay presentan las tasas de retención más bajas. *Implicación:* La experiencia de usuario o la oferta de valor funciona de manera óptima en los mercados principales, pero existen barreras específicas o desafíos de adopción local en los mercados más chicos que requieren una auditoría localizada de UX o logística.
* **Alerta en Cohorte Específica:** Se identificó una caída anómala y severa en la cohorte de **Agosto de 2025**, donde la retención al Día 7 bajó a 70.8% y al Día 28 colapsó a 0.2%. *Implicación:* Esto señala un problema técnico puntual, un cambio drástico no planeado en la interfaz, o una campaña de adquisición de usuarios de baja calidad durante ese mes que requiere investigación inmediata.

## 🚀 Cómo explorar este proyecto
1. Descarga el archivo de análisis ubicado en la carpeta `dashboard/`.
2. Abre el archivo en Microsoft Excel para inspeccionar las hojas de cálculo dinámicas y los resúmenes ejecutivos.
3. Revisa la carpeta `screenshots/` para una previsualización rápida de las matrices de conversión y retención calculadas.
