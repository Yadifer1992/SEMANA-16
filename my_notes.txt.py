# ======================================
# TAREA: Trabajo con Archivos de Texto
# Autor: [Yadira Ureña]
# Fecha: [06/04/2025]
# Descripción:
# Este programa crea un archivo de texto, escribe notas personales,
# las lee línea por línea y muestra su contenido.
# ======================================

# ----------- Escritura de Archivo de Texto -----------

# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("1. Recordar estudiar para el examen de Programación el lunes.\n")
archivo.write("2. Terminar el proyecto de físca antes del domingo.\n")
archivo.write("3. Leer el capítulo 4 del libro de estructuras de datos.\n")

# Cerramos el archivo después de escribir
archivo.close()

# ----------- Lectura de Archivo de Texto -----------

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline()
print("Contenido del archivo my_notes.txt:\n")

linea = archivo.readline()  # Lee la primera línea
while linea:
    print(linea.strip())    # Mostramos la línea sin saltos de línea extra
    linea = archivo.readline()  # Lee la siguiente línea

# Cerramos el archivo después de leer
archivo.close()