# Informe Técnico: Análisis de Datos de Dengue (Sivigila)
**Curso:** Estructura de Datos  
**Universidad:** Autónoma de Manizales  
**Integrantes:** Luis Miguel León Rondón y Samuel  

---

## 1. Introducción
En este proyecto se realiza un análisis y visualización de datos utilizando un conjunto de registros de salud pública (Sivigila/Dengue). El objetivo es aplicar herramientas de programación en Python mediante Pandas y Matplotlib para la limpieza, filtrado, cálculos estadísticos y representación gráfica de variables epidemiológicas clave.

## 2. Metodología y Procesamiento de Datos
* Se cargó el archivo original `dengue.csv`.
* Se aplicó un filtro temporal para seleccionar registros a partir del año 2018 (`year_ >= 2018`).
* Se extrajo una muestra aleatoria de **80 registros** utilizando una semilla fija (`random_state=42`) para garantizar la reproducibilidad de los datos.
* Se seleccionaron las columnas relevantes: `id`, `edad_`, `sexo_`, `comuna`, `semana`, `pac_hos_` y `year_`.
* Los datos procesados se exportaron a nuevos archivos limpios en formato CSV y Excel (`dengue_filtrado.csv` y `dengue_filtrado.xlsx`).

## 3. Análisis Estadístico y Filtros Avanzados
* **Promedio de edad:** Calculado mediante la función `.mean()` sobre la columna de edades.
* **Desviación estándar:** Calculada mediante `.std()` para medir la dispersión de las edades.
* **Filtros avanzados:** Se segmentaron los pacientes cuyas edades superan el promedio general y aquellos correspondientes a eventos de años recientes.

## 4. Visualización de Resultados
El script genera tres gráficos principales para interpretar el comportamiento de los datos:
1. **Histograma de Edades:** Permite observar la frecuencia de los casos de dengue según los rangos de edad de los pacientes.
2. **Gráfico de Barras por Comuna:** Muestra la distribución geográfica de los eventos registrados por zona.
3. **Gráfico de Dispersión (Edad vs Semana):** Relaciona la edad de los afectados con la semana epidemiológica en la que ocurrió el caso.

## 5. Conclusiones
El uso de estructuras de datos en Python facilitó la automatización del procesamiento de información en salud pública. La implementación de control de versiones con Git y GitHub permitió un trabajo colaborativo eficiente entre los integrantes del equipo.