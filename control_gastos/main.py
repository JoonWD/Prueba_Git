from funciones import (
    registrar_gasto,
    mostrar_gastos,
    calcular_totales,
    filtrar_gastos,
    eliminar_gasto
)

def mostrar_menu():
    print("\n===== CONTROL DE GASTOS PERSONALES =====")
    print("1. Registrar un nuevo gasto")
    print("2. Mostrar todos los gastos")
    print("3. Calcular totales")
    print("4. Filtrar gastos por categoría o mes")
    print("5. Eliminar gasto(s)")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            calcular_totales()
        elif opcion == "4":
            filtrar_gastos()
        elif opcion == "5":
            eliminar_gasto()
        elif opcion == "6":
            print("👋 ¡Hasta luego! Gracias por usar el sistema.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
