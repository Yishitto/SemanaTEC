#%%
import numpy as np 
import pandas as pd

# Cargar datos usando Pandas
df = pd.read_csv("insurance.csv")

# Verificar cantidad de datos y columnas
print("Número de filas y columnas:", df.shape)
print("\nNombres de las columnas:", df.columns)

# Mostrar los primeros registros para identificar el contenido de cada columna
print("\nPrimeros 5 registros:\n", df.head())

# Obtener información de tipos de datos y valores nulos
print("\nInformación general del DataFrame:")
print(df.info())

# Analizar estadísticas generales de todas las variables
print("\nDescripción estadística de todas las variables:")
print(df.describe(include="all"))

# Analizar variables categóricas y su distribución
categorical_columns = df.select_dtypes(include="object").columns
print("\nDistribución de las variables categóricas:")
for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Analizar rangos de variables numéricas
numeric_columns = df.select_dtypes(include="number").columns
print("\nRangos de las variables numéricas:")
for col in numeric_columns:
    print(f"{col}: Min={df[col].min()}, Max={df[col].max()}")

# Calcular media, mediana y desviación estándar de cada variable numérica
print("\nEstadísticas detalladas de las variables numéricas:")
for col in numeric_columns:
    mean = df[col].mean()
    median = df[col].median()
    std_dev = df[col].std()
    print(f"{col}: Media={mean}, Mediana={median}, Desviación Estándar={std_dev}")

# Conclusiones basadas en las estadísticas
print("\nConclusiones basadas en las estadísticas de las variables:")
for col in numeric_columns:
    mean = df[col].mean()
    median = df[col].median()
    std_dev = df[col].std()
    print(f"- {col}:")
    print(f"  * Media: {mean:.2f}")
    print(f"  * Mediana: {median:.2f}")
    print(f"  * Desviación Estándar: {std_dev:.2f}")
    print(f"  * Min: {df[col].min()}, Max: {df[col].max()}")
    print(f"  * Rango: {df[col].max() - df[col].min()}")