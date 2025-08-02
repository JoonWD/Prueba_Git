# Objetivo: 
# Esta actividad tiene como objetivo aplicar funciones de ordenamiento (`sorted`) y comprensión de listas en Python para organizar una lista de estudiantes por edad.

# Pasos sugeridos: 
# 1. Crea un archivo llamado `ordenar_estudiantes.py`. 

# 2. Define una lista con varios estudiantes, donde cada estudiante esté representado como un diccionario con las claves: 
#  'nombre' 
#  'edad' 
# 3. Usa la función `sorted()` para ordenar la lista por edad. 
# 4. Usa una comprensión de listas para mostrar los resultados de manera legible.
# Ejemplo básico de estructura esperada: 
# ```python 
# estudiantes = [ 
#     {"nombre": "Ana", "edad": 22}, 
#     {"nombre": "Luis", "edad": 20}, 
#     {"nombre": "Carla", "edad": 23}, 
#     {"nombre": "Pedro", "edad": 21}, 
# ] 
# estudiantes_ordenados = sorted(estudiantes, key=lambda e: e["edad"]) 
# resultado = [f'{e["nombre"]} - {e["edad"]} años' for e in estudiantes_ordenados] 
# for r in resultado: 
#     print(r) 
# ```


estudiantes = [ 
    {"nombre": "Ana", "edad": 22}, 
    {"nombre": "Luis", "edad": 20}, 
    {"nombre": "Carla", "edad": 23}, 
    {"nombre": "Pedro", "edad": 21}, 
] 
estudiantes_ordenados = sorted(estudiantes, key=lambda e: e["edad"]) 
resultado = [f'{e["nombre"]} - {e["edad"]} años' for e in estudiantes_ordenados] 
for r in resultado: 
    print(r) 