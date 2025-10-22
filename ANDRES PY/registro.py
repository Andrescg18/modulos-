import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="gestion_cosecha",
        user="postgres",
        password="1234",
        port="5432"
    )

def insertar_cosecha():
    try:
        inicio = int(input("Ingrese el valor de cosecha inicio: "))
        final = int(input("Ingrese el valor de cosecha final: "))
        estado = input("Ingrese el estado (Pendiente / En progreso / Completada): ")

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO cosecha (cosecha_inicio, cosecha_final, estado) VALUES (%s, %s, %s);",
            (inicio, final, estado)
        )
        conexion.commit()
        conexion.close()
        print("Registro insertado correctamente.\n")
    except Exception as e:
        print("Error al insertar la cosecha:", e)

def mostrar_cosechas():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cosecha;")
        registros = cursor.fetchall()

        if not registros:
            print("No hay cosechas registradas.\n")
        else:
            print("\nLista de cosechas:")
            for r in registros:
                print(f"ID: {r[0]}, Fecha: {r[1]}, Inicio: {r[2]}, Final: {r[3]}, Estado: {r[4]}")
        conexion.close()
        print()
    except Exception as e:
        print("Error al mostrar cosechas:", e)

def app():
    while True:
        print("==============")
        print("MENU PRINCIPAL")
        print("==============")
        print("1. Agregar nueva cosecha")
        print("2. Mostrar todas las cosechas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_cosecha()
        elif opcion == "2":
            mostrar_cosechas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.\n")

if __name__ == "__main__":
    app()
