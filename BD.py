import pandas as pd
import matplotlib.pyplot as plt
# 1. Cargamos el archivo original de dengue
df_completo = pd.read_csv("dengue.csv")

# 2. Filtramos de 2018 en adelante y sacamos 80 filas al azar con una semilla fija
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

# El random_state hace que salgan siempre los mismos datos al ejecutar
df = df_recientes[columnas_relevantes].sample(n=80, random_state=42).copy()

# 3. Guardamos el resultado en un nuevo CSV limpio
df.to_csv("dengue_filtrado.csv", index=False)
print(f"Se guardaron {len(df)} registros en el CSV.")

# 4. Agrupamos por comuna para ver cuántos casos hay en cada zona
casos_por_comuna = df.groupby("comuna")["id"].count()
print(f"\nCasos por comuna:\n{casos_por_comuna}")

# Guardamos también en Excel como pide la profe
df.to_excel("dengue_filtrado.xlsx", index=False)
print("Archivo Excel creado con éxito.")

# 5. Calculamos promedio y desviación estándar de la edad
promedio_edad = df["edad_"].mean()
desviacion_edad = df["edad_"].std()

# 6. Filtros avanzados para la tarea
pacientes_mayores_promedio = df[df["edad_"] > promedio_edad]
eventos_recientes = df[df["year_"] > 2019]

print(f"\nPromedio de edad: {promedio_edad:.2f}")
print(f"Desviación estándar: {desviacion_edad:.2f}") 
print(f"Pacientes mayores al promedio de edad: {len(pacientes_mayores_promedio)}")
print(f"Casos de años mayores a 2019: {len(eventos_recientes)}")

# Gráfico 1: Histograma de distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df["edad_"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histograma de Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia (Casos)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# Gráfico 2: Gráfico de barras por comuna
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
