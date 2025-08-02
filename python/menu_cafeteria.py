# Instrucciones

# 1. Abre Visual Studio Code y crea un archivo llamado `menu_cafeteria.py` 
 
# 2. Escribe el siguiente código o uno similar adaptado a tus preferencias: 
# ```python 
# print("Bienvenido a la cafetería") 
# print("Menú:") 
# print("1. Café - $4.000") 
# print("2. Té - $3.000") 
# print("3. Chocolate - $4.500") 
# opcion = input("Seleccione una opción (1-3): ") 
 
# if opcion == "1": 
#     print("Has elegido Café. Precio: $4.000") 
# elif opcion == "2": 
#     print("Has elegido Té. Precio: $3.000") 
# elif opcion == "3": 
#     print("Has elegido Chocolate. Precio: $4.500") 
# else: 
#     print("Opción no válida. Por favor, selecciona una bebida del menú.") 
# ``` 
# 3. Guarda y ejecuta el script desde la terminal. Prueba con diferentes opciones para verificar que el programa funcione correctamente

errores = 0  # Contador de errores

while True:
    print("Bienvenido a la cafetería") 
    print("Menú:") 
    print("1. Café - $4.000") 
    print("2. Té - $3.000") 
    print("3. Chocolate - $4.500") 
    
    opcion = input("Seleccione una opción (1-3): ") 

    if opcion == "1": 
        print("Has elegido Café. Precio: $4.000") 
        break
    elif opcion == "2": 
        print("Has elegido Té. Precio: $3.000") 
        break
    elif opcion == "3": 
        print("Has elegido Chocolate. Precio: $4.500") 
        break
    else: 
        errores += 1
        print(f"Opción no válida. Intento {errores}/3\n")
        
        if errores == 3:
            print("Has superado el número máximo de intentos. Saliendo del programa.")
            break
