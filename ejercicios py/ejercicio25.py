# Ejercicio 25: Sistema de registro de estudiantes (simulado con valores fijos)
estudiantes = []
def agregar(nombre, edad, grado):
    estudiantes.append({"nombre": nombre, "edad": edad, "grado": grado, "calificaciones":[]})
def agregar_calificacion(nombre, materia, nota):
    for e in estudiantes:
        if e["nombre"] == nombre:
            e["calificaciones"].append({"materia": materia, "nota": nota})
agregar("Ana García",16,"10°")
agregar("Carlos López",15,"9°")
agregar_calificacion("Ana García","Matemáticas",9.2)
print("Estudiantes registrados:", estudiantes)
