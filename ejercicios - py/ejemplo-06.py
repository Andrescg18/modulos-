def crear_estudiante(nombre, edad, grado, promedio):
    return {"nombre": nombre, "edad": edad, "grado": grado, "promedio": promedio}

andres_guardia = crear_estudiante("Laura", 15, "10°", 4.2)
print(andres_guardia)