import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/resultados", exist_ok=True)

datos = pd.read_csv("data/StudentsPerformance.csv")

print("EXPLORACION INICIAL")
print("Numero de registors:", datos.shape[0])
print("Numero de columnas:", datos.shape[1])
print("Nombre de las variables:")
print(list(datos.columns))
print("Tipos de datos:")
print(datos.dtypes)
print("Valores faltnates:")
print(datos.isnull().sum())
print("Registros duplicados:", datos.duplicated().sum())
print("Estadisticas descriptivas:")
print(datos.describe())

datos = datos.drop_duplicates()
datos = datos.dropna()

datos = datos.rename(columns={
    "race/ethnicity": "group",
    "parental level of education": "parent_education",
    "test preparation course": "prep_course",
    "math score": "math_score",
    "reading score": "reading_score",
    "writing score": "writing_score"
})

datos["prep_course"] = datos["prep_course"].replace({"none": "no lo hizo", "completed": "lo completo"})


datos["average_score"] = (datos["math_score"] + datos["reading_score"] + datos["writing_score"]) / 3
datos["average_score"] = datos["average_score"].round(2)

datos["nivel"] = pd.cut(
    datos["average_score"],
    bins=[0, 60, 80, 100],
    labels=["Bajo", "Medio", "Alto"],
    include_lowest=True
)

print("")
print("CRITERIOS DE LAS CATEGORIAS")
print("Bajo: promedio de 60 o menos")
print("Medio: promedio mayor a 60 y hasta 80")
print("Alto: promedio mayor a 80")

print("")
print("ANALISIS 1: promedio por materia")
promedios_matreias = datos[["math_score", "reading_score", "writing_score"]].mean().round(2)
print(promedios_matreias)
print("La materia con mayor promedio es:", promedios_matreias.idxmax())

print("")
print("ANALISIS 2: curso de preparacion")
prom_cruso = datos.groupby("prep_course")["average_score"].mean().round(2)
print(prom_cruso)

print("")
print("ANALISIS 3: nivel educativo de los padres")
prom_padres = datos.groupby("parent_education")["average_score"].mean().round(2).sort_values(ascending=False)
print(prom_padres)

print("")
print("ANALISIS 4: porcentaje de estudiantes por nivel")
porcentjaes = (datos["nivel"].value_counts(normalize=True) * 100).round(2)
print(porcentjaes)

print("")
print("ANALISIS 5: promedio por grupo")
prom_grupos = datos.groupby("group")["average_score"].mean().round(2).sort_values(ascending=False)
print(prom_grupos)
print("Grupo con mejor promedio:", prom_grupos.index[0])
print("Grupo con menor promedio:", prom_grupos.index[-1])