

alumnos = {}

def agregar(dic, nombre, nota):
    dic[nombre] = nota
    print(f"Alumno {nombre} agregado con nota {nota}.")

def mostrar(dic):
    print("\nListado de alumnos:")
    for nombre, nota in dic.items():
        print(f"{nombre}: {nota}")

def buscar(dic, nombre):
    return dic.get(nombre, None)

def eliminar(dic, nombre):
    if nombre in dic:
        del dic[nombre]
        print(f"Alumno {nombre} eliminado.")
    else:
        print("Alumno no encontrado.")

def modificar_nota(dic, nombre, nueva_nota):
    if nombre in dic:
        dic[nombre] = nueva_nota
        print(f"Nota de {nombre} actualizada a {nueva_nota}.")
    else:
        print("Alumno no encontrado.")

def filtrar_por_nota(dic, minimo):
    return {n: nota for n, nota in dic.items() if nota >= minimo}

def estadisticas(dic):
    if not dic:
        print("No hay alumnos registrados.")
        return
    notas = dic.values()
    print("\n--- Estadísticas ---")
    print("Total alumnos:", len(dic))
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))
    print("Promedio:", sum(notas)/len(notas))

agregar(alumnos, "Ana", 9)
agregar(alumnos, "Luis", 7)
mostrar(alumnos)
modificar_nota(alumnos, "Luis", 9)
estadisticas(alumnos)
