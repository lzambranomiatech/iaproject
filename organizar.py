# 1. Definir categorías de extensiones (por ejemplo: imágenes = [".png", ".jpg", ".gif"], documentos = [".pdf", ".docx", ".txt"], etc.)
# 2. Crear un diccionario para almacenar archivos por categoría
# 3. Leer el contenido del directorio actual
# 4. Para cada archivo, determinar su extensión y moverlo a la categoría correspondiente
# 5. Si la categoría no existe, crearla
# 6. Mostrar un resumen de los archivos movidos

import os
from pathlib import Path

# Definir categorías de extensiones
categorias = {
    "imagenes": [".png", ".jpg", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "otros": []
}

# Crear un diccionario para almacenar archivos por categoría
archivos = {nombre: [] for nombre in categorias.keys()}

# Leer el contenido del directorio actual
for archivo in os.listdir("."):
    if os.path.isfile(archivo):
        # Obtener la extensión del archivo usando pathlib
        extension = Path(archivo).suffix.lower()
        
        # Determinar a qué categoría pertenece
        categoria_encontrada = False
        for nombre_categoria, extensiones in categorias.items():
            if extension in extensiones:
                archivos[nombre_categoria].append(archivo)
                categoria_encontrada = True
                break
        
        # Si no se encontró categoría, agregar a "otros"
        if not categoria_encontrada:
            archivos["otros"].append(archivo)

# Para cada archivo, determinar su extensión y moverlo a la categoría correspondiente
for nombre_categoria, lista_archivos in archivos.items():
    # 5. Si la categoría no existe, crearla
    if not os.path.exists(nombre_categoria):
        os.makedirs(nombre_categoria)
        print(f"Directorio '{nombre_categoria}' creado.")
    
    # Mover archivos a la categoría correspondiente
    for archivo in lista_archivos:
        destino = os.path.join(nombre_categoria, archivo)
        os.rename(archivo, destino)

# Mostrar un resumen de los archivos movidos
print("\nResumen de archivos movidos:")
for nombre_categoria, lista_archivos in archivos.items():
    print(f"{nombre_categoria}: {len(lista_archivos)} archivos")
    
