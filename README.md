# Análisis del rendimiento académico

Proyecto de la materia de Big Data. Es un análisis exploratorio de las calificaciones de 1000 estudiantes usando Python, pandas y matplotlib. También sirve para practicar Git, GitHub y la reproducibilidad de un proyecto.

## Dataset

- **Nombre:** Students Performance
- **Fuente:** Kaggle (https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Descripción:** tiene 1000 estudiantes y 8 columnas: género, grupo, nivel educativo de los padres, tipo de comida, curso de preparación y las calificaciones de matemáticas, lectura y escritura.
- El archivo está en `data/StudentsPerformance.csv`.

## Objetivo

Ver como se comporta el rendimiento de los estudiantes y que factores estan relacinados con tener mejores calificaciones, por ejemplo el curso de preparación o el nivel educativo de los padres.

## Requisitos

- Python 3
- Git
- Las librerías que están en `requirements.txt` (pandas y matplotlib con sus dependencias)

## Instalación

1. Clonar el repositorio:

```
git clone https://github.com/manuurc12-hash/Students_performance
```

2. Entrar a la carpeta del proyecto:

```
cd Students_performance
```

3. Crear el entorno virtual:

```
python -m venv .venv
```

4. Activar el entorno.

Windows:

```
.venv\Scripts\activate
```

macOS/Linux:

```
source .venv/bin/activate
```

5. Instalar las dependencias:

```
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta principal del proyecto:

```
python src/analysis.py
```

El script imprime los resultados en la terminal y guarda las gráficas y un CSV limpio en `outputs/resultados/`.

## Estructura del proyecto

```
Students_performance/
├── data/
│   └── StudentsPerformance.csv
├── src/
│   └── analysis.py
├── outputs/
│   └── resultados/
├── README.md
├── requirements.txt
└── .gitignore
```

## Limpieza y preprocesamiento

- Se revisaron los valores faltantes y los registros duplicados. El dataset tiene 0 nulos y 0 duplicados, así que no se eliminó ninguna fila.
- Se renombraron las columnas para quitar espacios y diagonales (por ejemplo `math score` quedó como `math_score`).
- La columna del curso de preparación se cambió a `no lo hizo` y `lo completo` para que las gráficas se lean mejor.

## Variables nuevas

- `average_score`: promedio de matemáticas, lectura y escritura de cada estudiante.
- `nivel`: clasificación del rendimiento según el promedio.

| Nivel | Criterio |
|---|---|
| Bajo | promedio de 60 o menos |
| Medio | promedio mayor a 60 y hasta 80 |
| Alto | promedio mayor a 80 |

Se eligieron estos cortes porque 60 es un límite común para aprobar y 80 se considera un buen desempeño.

## Análisis realizados

1. Promedio por materia.
2. Promedio según el curso de preparación.
3. Promedio según el nivel educativo de los padres.
4. Porcentaje de estudiantes en cada nivel de rendimiento.
5. Promedio por grupo.

## Resultados y conclusiones

**Promedio por materia**

| Materia | Promedio |
|---|---|
| Matemáticas | 66.09 |
| Lectura | 69.17 |
| Escritura | 68.05 |

**Promedio según el curso de preparación**

| Curso | Promedio |
|---|---|
| Lo completó | 72.67 |
| No lo hizo | 65.04 |

**Promedio según el nivel educativo de los padres**

| Nivel educativo | Promedio |
|---|---|
| Maestría | 73.60 |
| Licenciatura | 71.92 |
| Carrera técnica (associate's) | 69.57 |
| Algo de universidad | 68.48 |
| Algo de preparatoria | 65.11 |
| Preparatoria | 63.10 |

**Porcentaje de estudiantes por nivel**

| Nivel | Porcentaje |
|---|---|
| Medio | 51.3% |
| Bajo | 29.3% |
| Alto | 19.4% |

**Promedio por grupo**

| Grupo | Promedio |
|---|---|
| E | 72.75 |
| D | 69.18 |
| C | 67.13 |
| B | 65.47 |
| A | 62.99 |

**Conclusiones**

- Lectura es la materia con mejor promedio y matemáticas es la más baja.
- Los estudiantes que completaron el curso de preparación tienen un promedio de casi 7.6 puntos más que los que no lo hicieron.
- Mientras mayor es el nivel educativo de los padres, mayor tiende a ser el promedio de los estudiantes. La diferencia entre maestría y preparatoria es de más de 10 puntos.
- Más de la mitad de los estudiantes está en nivel Medio y solo 1 de cada 5 llega a Alto.
- El grupo E tiene el mejor promedio y el grupo A el más bajo.
- Estos resultados muestran relaciones entre variables, pero no prueban que una cause a la otra. Por ejemplo, el curso de preparación parece ayudar, pero también pueden influir otros factores que el dataset no tiene.

## Gráficas

Se guardan en `outputs/resultados/`:

- `grafica_materias.png`
- `grafica_curso.png`
- `grafica_padres.png`
- `grafica_histograma.png`
