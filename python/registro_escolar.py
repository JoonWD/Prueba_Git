# 1. Crea un archivo llamado `registro_escolar.py`. 

# 2. El programa debe permitir registrar los siguientes datos de varios estudiantes: 

# Nombre (texto)
# Edad (entero)
# Curso (texto) 
# 3. Usa una lista para almacenar múltiples diccionarios, donde cada diccionario representa un estudiante. 

 
# 4. Permite que el usuario ingrese tantos estudiantes como desee hasta que decida finalizar. 

 
# 5. Al final, muestra en pantalla todos los registros capturados. 
 
# Ejemplo básico de estructura esperada: 
# ```python 
# estudiantes = [] 
# while True: 
#     nombre = input("Nombre: ") 
#     edad = int(input("Edad: ")) 
#     curso = input("Curso: ") 
#     estudiantes.append({"nombre": nombre, "edad": edad, "curso": curso}) 
#     continuar = input("¿Deseas agregar otro estudiante? (s/n): ") 
#     if continuar.lower() != 's': 
#         break 
# print("\nListado de estudiantes:") 
# for est in estudiantes: 
#     print(est) 
# ``` 

estudiantes = [] 
while True: 
    nombre = input("Nombre: ") 
    edad = int(input("Edad: ")) 
    curso = input("Curso: ") 
    estudiantes.append({"nombre": nombre, "edad": edad, "curso": curso}) 
    continuar = input("¿Deseas agregar otro estudiante? (s/n): ") 
    if continuar.lower() != 's': 
        break 
print("\nListado de estudiantes:") 
for est in estudiantes: 
    print(est) 