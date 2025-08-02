# Objetivo

# Crear un script en Python que imprima información personalizada usando variables y la función print().

# Instrucciones

# 1. Crea un archivo nuevo llamado `mi_script.py` en tu entorno de trabajo (preferiblemente en Visual Studio Code). 
 
# 2. Escribe el siguiente código en el archivo: 
# ```python 
# nombre = "Daniel" 
# edad = 22 
# ciudad = "Bogotá" 
# print("Hola, mi nombre es", nombre) 
# print("Tengo", edad, "años") 
# print("Vivo en", ciudad) 
# ``` 
 
# 3. Guarda el archivo y ejecútalo desde la terminal integrada de Visual Studio Code. Para ello: 
# - Abre la terminal con `Ctrl + ñ` (Windows) o `Ctrl + \\` 
# - Ejecuta el script con el comando: 
# ``` 
# python mi_script.py 
# ``` 
 
# 4. Verifica que el programa imprima en pantalla los datos correctamente, mostrando tres líneas de salida con el nombre, la edad y la ciudad. 

nombre = "Daniel" 
edad = 22 
ciudad = "Bogotá" 
print("Hola, mi nombre es", nombre) 
print("Tengo", edad, "años") 
print("Vivo en", ciudad) 
print( nombre + edad + ciudad)  # Esto generará un error porque no se pueden concatenar tipos diferentes
