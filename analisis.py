# leer un archivo csv y calcular la media, mediana, desviacion estandar de cada columna
# genera una grafica de dispersion de cada columna
import pandas as pd
import matplotlib.pyplot as plt

# leer el archivo csv
df = pd.read_csv('DATA_ANALISIS.csv')

# calcular la media, mediana, desviacion estandar de cada columna e imprimir los resultados
media = df.mean()
mediana = df.median()
desviacion = df.std()
print("Media:", media)
print("Mediana:", mediana)
print("Desviacion estandar:", desviacion)

# generar una grafica de dispersion de una columna vs otra columna, traza un scatter plot de col1 vs col2
plt.scatter(df['col1'], df['col2'])
plt.show()
