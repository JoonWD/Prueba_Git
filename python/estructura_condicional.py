# Crear una estructura condicional que evalúe un valor numérico y un valor booleano.
# Usar `if`, `else`, y `else if` para ejecutar diferentes bloques de código.
# Imprimir el resultado en la consola.
numero = input("Ingresa un número: ")
buleano = input("Ingresa un valor booleano (True/False): ")
try:
    if buleano.lower() == 'true':
        buleano = True
        print(f"El valor booleano {buleano} es verdadero.")
    elif buleano.lower() == 'false':
        buleano = False
        print(f"El valor booleano {buleano} es falso.")
    else:
        print("Entrada inválida. Por favor ingresa True o False.")
        buleano = None
except AttributeError:
    print("Entrada inválida. Por favor ingresa True o False.")
    buleano = None

if buleano is not None:
    try:
        numero = float(numero.strip())
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entero.")
        numero = None

    if numero is not None:
        if numero > 0:
            print(f"El número {numero} es positivo.")
        elif numero < 0:
            print(f"El número {numero} es negativo.")
        else:
            print(f"El número {numero} es cero.")
