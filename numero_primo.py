primo = int (input("ingresa un numero: "))
if primo < 1:
    print("El numero no es primo")
else:
    for i in range(2, primo):
        if primo % i == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")