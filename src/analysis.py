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
