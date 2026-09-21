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