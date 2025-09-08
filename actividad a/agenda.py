
import os
#funcion para agregar contactos a la agenda
def agregar_contacto():
    print("Agregar contacto:")
    nombre = input("Ingresa el nombre de tu contacto: ")
    telefono = input("Ingresa el número de teléfono: ")
    fecha_de_llamado = input("Ingresa la fecha del llamado: ")

    with open("agenda.txt", "a", encoding="utf-8") as archivo:
        archivo.write("=====================\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Fecha del llamado: {fecha_de_llamado}\n")
        archivo.write("=====================\n")

    print("Contacto agregado correctamente.")

#funcion para mostrar los contactos 
def mostrar_contactos():
    print("Mostrando todos los contactos:")
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print(contenido)
            else:
                print("No hay contactos guardados.")
    else:
        print("No hay contactos guardados.")

#funcion para modificar contactos
def modificar_contacto():
    nombre_buscar = input("Ingresa el nombre del contacto que deseas modificar: ")
    encontrado = False
    with open("agenda.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    with open("agenda.txt", "w", encoding="utf-8") as archivo:
        for linea in lineas:
            if nombre_buscar in linea and not encontrado:
                print(f"Se ha encontrado el contacto: {linea.strip()}")
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                nuevo_telefono = input("Ingresa el nuevo número de teléfono: ")
                nueva_fecha = input("Ingresa la nueva fecha del llamado: ")
                archivo.write(f"Nombre: {nuevo_nombre}\n")
                archivo.write(f"Teléfono: {nuevo_telefono}\n")
                archivo.write(f"Fecha del llamado: {nueva_fecha}\n")
                archivo.write("=====================\n")
                encontrado = True
            else:
                archivo.write(linea)

    if not encontrado:
        print("No se encontró el contacto.")
    else:
        print("Contacto modificado correctamente.")

#funcion para eliminar contactos
def eliminar_contacto():
    nombre_buscar = input("Ingresa el nombre del contacto que deseas eliminar: ")
    encontrado = False
    with open("agenda.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    with open("agenda.txt", "w", encoding="utf-8") as archivo:
        for linea in lineas:
            if nombre_buscar in linea and not encontrado:
                print(f"Se ha encontrado y eliminado el contacto: {linea.strip()}")
                encontrado = True
            else:
                archivo.write(linea)

    if not encontrado:
        print("No se encontró el contacto.")
    else:
        print("Contacto eliminado correctamente.")

#funcion para mostrar el menu
def mostrar_menu():
    print("\nMenu de la Agenda")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("elige una opcion: ")
    return opcion

#funcion principal de la agenda
def agenda():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            mostrar_contactos()
        elif opcion == '3':
            modificar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("Agenda creada correctamente ahora puedes llamar a tus contactos")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


agenda()
