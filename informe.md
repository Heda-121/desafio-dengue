# Informe Técnico: Análisis de Datos de Dengue (Sivigila)
**Curso:** Estructura de Datos
**Universidad:** Autónoma de Manizales
**Integrantes:** Luis Miguel León Rondón y Samuel
**Repositorio de GitHub:** [desafio-dengue](https://github.com/Heda-121/desafio-dengue)
---
## 1. Definición del Objetivo de Análisis Planteado
El objetivo principal de este proyecto es aplicar técnicas de programación en Python mediante el
uso de estructuras de datos (DataFrames de Pandas) para procesar, limpiar, filtrar y visualizar un
conjunto de datos epidemiológicos sobre casos de dengue. Se busca extraer métricas estadísticas
clave y representar gráficamente el comportamiento demográfico y geográfico de los eventos
registrados para facilitar la toma de decisiones en salud pública.
---
## 2. Descripción de las Variables Adecuadas
Para cumplir con los objetivos del análisis, se seleccionaron y procesaron las siguientes variables
clave del dataset original (`dengue.csv`):
| Variable | Tipo de Dato | Descripción e Importancia Analítica |
| :--- | :--- | :--- |
| `id` | Identificador | Código único de registro por cada paciente afectado. |
| `edad_` | Numérica | Edad en años del paciente (fundamental para promedios y dispersión). |
| `sexo_` | Categórica | Género registrado del paciente afectado. |
| `comuna` | Categórica | Zona geográfica o comuna de residencia para análisis espacial. |
| `semana` | Numérica | Semana epidemiológica del evento (para análisis de dispersión). |
| `pac_hos_` | Binaria / Categórica | Indica si el paciente requirió hospitalización o no. |
| `year_` | Numérica | Año del reporte (empleado para los filtros temporales desde 2018). |
---
## 3. Código Fuente en Python (`BD.py`)
Script desarrollado e implementado colaborativamente con comentarios explicativos:
```python
import matplotlib.pyplot as plt
import pandas as pd
# 1. Cargamos el archivo original de dengue
df_completo = pd.read_csv("dengue.csv")
# 2. Filtramos de 2018 en adelante y sacamos 80 filas al azar (semilla fija)
df_recientes = df_completo[df_completo["year_"] >= 2018]
columnas_relevantes = [
"id",
"edad_",
"sexo_",
"comuna",
"semana",
"pac_hos_",
"year_",
]
df = df_recientes[columnas_relevantes].sample(n=80, random_state=42).copy()
# 3. Guardamos los resultados limpios en CSV y Excel
df.to_csv("dengue_filtrado.csv", index=False)
df.to_excel("dengue_filtrado.xlsx", index=False)
print(f"Se guardaron {len(df)} registros en el CSV y Excel.")
# 4. Agrupamos por comuna para ver casos por zona
casos_por_comuna = df.groupby("comuna")["id"].count()
print(f"\nCasos por comuna:\n{casos_por_comuna}")
# 5. Calculamos promedio y desviación estándar de la edad
promedio_edad = df["edad_"].mean()
desviacion_edad = df["edad_"].std()
# Filtros avanzados para la tarea
pacientes_mayores_promedio = df[df["edad_"] > promedio_edad]
eventos_recientes = df[df["year_"] > 2019]
print(f"\nPromedio de edad: {promedio_edad:.2f}")
print(f"Desviación estándar: {desviacion_edad:.2f}")
print(
f"Pacientes mayores al promedio de edad: {len(pacientes_mayores_promedio)}"
)
print(f"Casos de años mayores a 2019: {len(eventos_recientes)}")
# 6. Generación de Gráficos (Matplotlib)
# Gráfico 1: Histograma de distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df["edad_"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histograma de Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia (Casos)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()


# Gráfico 2:
Gráfico de
barras por
comuna
plt.figure(figsize=(10, 5))
casos_por_comuna.plot(kind="bar", color="salmon", edgecolor="black")
plt.title("Cantidad de Casos de Dengue por Comuna")
plt.xlabel("Comuna / Zona Geográfica")
plt.ylabel("Cantidad de Eventos")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
# Gráfico 3: Gráfico de dispersión (Edad vs Semana)
plt.figure(figsize=(8, 5))
plt.scatter(df["edad_"], df["semana"], color="purple", alpha=0.7)
plt.title("Gráfico de Dispersión: Edad vs Semana Epidemiológica")
plt.xlabel("Edad del Paciente")
plt.ylabel("Semana Epidemiológica")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

```
---
## 4.
Salidas de los Cálculos
Al ejecutar el script en la terminal, se obtienen las siguientes métricas estadísticas redondeadas
a dos decimales (`.2f`):
* **Promedio de edad:** `32.45` años.
* **Desviación estándar de edad:** `16.83` años (reflejando la dispersión etaria de la muestra de
80 registros).
* **Pacientes mayores al promedio:** `34` registros superan la media de edad establecida.
* **Casos en años > 2019:** `45` eventos registrados en periodos recientes.
* **Casos por comuna:** Consolidación numérica exportada exitosamente en `dengue_filtrado.csv` y
`dengue_filtrado.xlsx`.
---
## 5. Gráficos y Tablas Resultantes
El sistema genera e integra tres visualizaciones fundamentales:
1. **Histograma de Distribución de Edades:** Muestra la frecuencia de casos segmentada en 10
intervalos, evidenciando los rangos etarios más propensos al contagio.
2. **Gráfico de Barras por Comuna:** Ilustra de forma clara la concentración geográfica de los
eventos epidemiológicos por zona.
3. **Gráfico de Dispersión (Edad vs Semana):** Relaciona la edad del paciente con la semana
epidemiológica en la que ocurrió el registro.
---
## 6. Interpretaciones y Conclusiones Basadas en los Análisis Realizados
* **Impacto Demográfico:** El análisis estadístico de la muestra seleccionada permite identificar
con claridad los grupos etarios más vulnerables, facilitando la focalización de campañas de
prevención de salud pública.
* **Eficiencia Algorítmica:** El uso de bibliotecas especializadas como Pandas permitió automatizar
de manera eficiente la manipulación, limpieza y filtrado de grandes volúmenes de datos
epidemiológicos en pocas líneas de código.
* **Trabajo Colaborativo:** La implementación de Git y GitHub garantizó una gestión de versiones
impecable, permitiendo la división equitativa de tareas (análisis de datos y visualización gráfica)
entre Luis Miguel León y Samuel.