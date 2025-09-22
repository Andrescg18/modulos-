def crear_asignatura(nombre, creditos, profesor, horario):
    return {"nombre": nombre, "creditos": creditos, "profesor": profesor, "horario": horario}

andres_guardia = crear_asignatura("Historia", 3, "Andrés", "Lunes 8am")
print(andres_guardia)