from conexion import conn


cursor = conn.cursor()

cursor.execute("SELECT * FROM personas ORDER BY id")


registros = cursor.fetchall()


if len(registros) == 0:
    print("No hay registros")
else:
    print(f"Se encontraron {len(registros)} registros:\n")

    # Recorrer y mostrar los registros
    for registro in registros:
        print(f"ID: {registro[0]}")
        print(f"Nombre: {registro[1]}")
        print("------------------------")

cursor.close()
conn.close()