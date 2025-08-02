import csv
from datetime import datetime
from collections import defaultdict

ARCHIVO = 'gastos.csv'
CATEGORIAS = ['Alimentación', 'Transporte', 'Salud', 'Ocio', 'Otros']

def registrar_gasto():
    print("\n--- REGISTRAR GASTO(S) ---")

    while True:
        nombre = input("Nombre del gasto: ")

        while True:
            monto = input("Monto ($, solo números enteros sin puntos, comas ni espacios): ").strip()
            if not monto.isdigit():
                print("❌ Por favor, ingrese una cantidad válida: solo números enteros, sin espacios, comas ni puntos.")
            else:
                monto = int(monto)
                break

        print("Categorías disponibles:")
        for i, cat in enumerate(CATEGORIAS, 1):
            print(f"{i}. {cat}")
        while True:
            try:
                cat_index = int(input("Selecciona la categoría (1-5): ")) - 1
                if 0 <= cat_index < len(CATEGORIAS):
                    categoria = CATEGORIAS[cat_index]
                    break
                else:
                    print("❌ Selección fuera de rango.")
            except ValueError:
                print("❌ Ingresa un número válido.")

        fecha = datetime.now().strftime("%Y-%m-%d")

        with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, monto, categoria, fecha])

        print("✅ Gasto registrado con éxito.")

        continuar = input("¿Deseas registrar otro gasto? (s/n): ").strip().lower()
        if continuar != 's':
            break

def mostrar_gastos():
    print("\n--- LISTA DE GASTOS ---")
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("{:<20} {:<10} {:<15} {:<12}".format("Nombre", "Monto", "Categoría", "Fecha"))
            print("-" * 60)
            for fila in reader:
                print("{:<20} ${:<9} {:<15} {:<12}".format(*fila))
    except FileNotFoundError:
        print("⚠️ No hay gastos registrados aún.")

def calcular_totales():
    print("\n--- TOTALES ---")
    total = 0
    por_categoria = defaultdict(float)

    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for nombre, monto, categoria, fecha in reader:
                monto = float(monto)
                total += monto
                por_categoria[categoria] += monto

        print(f"Total gastado: ${total:.2f}")
        print("Gasto por categoría:")
        for cat, val in por_categoria.items():
            print(f"  - {cat}: ${val:.2f}")
    except FileNotFoundError:
        print("⚠️ No hay datos para calcular.")

def filtrar_gastos():
    print("\n--- FILTRAR GASTOS ---")
    print("1. Filtrar por categoría")
    print("2. Filtrar por mes y año (YYYY-MM)")

    opcion = input("Selecciona una opción (1 o 2): ").strip()

    if opcion == "1":
        print("Categorías disponibles:")
        for i, cat in enumerate(CATEGORIAS, 1):
            print(f"{i}. {cat}")
        try:
            cat_index = int(input("Selecciona la categoría (1-5): ")) - 1
            if 0 <= cat_index < len(CATEGORIAS):
                categoria = CATEGORIAS[cat_index]
            else:
                print("❌ Categoría fuera de rango.")
                return
        except ValueError:
            print("❌ Entrada inválida.")
            return
        criterio = "categoría"

    elif opcion == "2":
        fecha_mes = input("Ingresa el mes y año a filtrar (formato: YYYY-MM): ").strip()
        if not fecha_mes or len(fecha_mes) != 7 or fecha_mes[4] != '-' or not fecha_mes.replace("-", "").isdigit():
            print("❌ Formato inválido. Usa el formato YYYY-MM.")
            return
        criterio = "fecha"

    else:
        print("❌ Opción inválida.")
        return

    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            resultados = []

            for fila in reader:
                nombre, monto, cat, fecha_gasto = fila
                if criterio == "categoría" and cat.lower() == categoria.lower():
                    resultados.append(fila)
                elif criterio == "fecha" and fecha_gasto.startswith(fecha_mes):
                    resultados.append(fila)

            if resultados:
                print("\n--- RESULTADOS FILTRADOS ---")
                print("{:<20} {:<10} {:<15} {:<12}".format("Nombre", "Monto", "Categoría", "Fecha"))
                print("-" * 60)
                total = 0
                for fila in resultados:
                    nombre, monto, categoria, fecha = fila
                    monto = int(monto)
                    total += monto
                    print("{:<20} ${:<9} {:<15} {:<12}".format(nombre, monto, categoria, fecha))
                print("-" * 60)
                print(f"🔢 Total filtrado: ${total}")
            else:
                print("⚠️ No se encontraron gastos que coincidan.")
    except FileNotFoundError:
        print("⚠️ No hay datos para filtrar.")

def eliminar_gasto():
    print("\n--- ELIMINAR GASTO(S) ---")

    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as file:
            gastos = list(csv.reader(file))
    except FileNotFoundError:
        print("⚠️ No hay datos para eliminar.")
        return

    if not gastos:
        print("⚠️ No hay registros en el archivo.")
        return

    print("\nListado de gastos:")
    print("{:<4} {:<20} {:<10} {:<15} {:<12}".format("ID", "Nombre", "Monto", "Categoría", "Fecha"))
    print("-" * 65)
    for idx, fila in enumerate(gastos, start=1):
        print("{:<4} {:<20} ${:<9} {:<15} {:<12}".format(idx, *fila))

    print("\nOpciones:")
    print("1. Eliminar un gasto específico")
    print("2. Eliminar todos los gastos")
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        try:
            id_eliminar = int(input("Ingresa el ID del gasto a eliminar: "))
            if 1 <= id_eliminar <= len(gastos):
                eliminado = gastos.pop(id_eliminar - 1)
                with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(gastos)
                print(f"✅ Gasto '{eliminado[0]}' eliminado con éxito.")
            else:
                print("❌ ID fuera de rango.")
        except ValueError:
            print("❌ Ingresa un número válido.")
    elif opcion == "2":
        confirmar = input("⚠️ ¿Estás seguro de que deseas eliminar TODOS los gastos? (s/n): ").strip().lower()
        if confirmar == 's':
            with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as file:
                pass  # Borra todo el contenido
            print("✅ Todos los gastos han sido eliminados.")
        else:
            print("❌ Acción cancelada.")
    else:
        print("❌ Opción inválida.")
