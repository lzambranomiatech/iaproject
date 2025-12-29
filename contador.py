# Programa para contar palabras en un archivo de texto
# Pedir al usuario que ingrese el nombre del archivo de texto
# Leer el archivo de texto
# Seperar en palabras
# Contar número total de palabras
# Mostrar las 10 palabras mas frecuentes y su conteo
archivo = open("ProcInvoice.txt", "r")
try:
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit(1)

# Seperar en palabras
import re
palabras = re.findall(r'\b\w+\b', contenido)

# Contar número total de palabras
total_palabras = len(palabras)
print("El número total de palabras es:", total_palabras)

# Contar las 10 palabras mas frecuentes y su conteo
from collections import Counter
palabras_mas_frecuentes = Counter(palabras).most_common(10)
print("Las 10 palabras mas frecuentes y su conteo son:", palabras_mas_frecuentes)


