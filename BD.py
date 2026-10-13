import pandas as pd

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


