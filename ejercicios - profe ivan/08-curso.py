def crear_curso(nombre, duracion, modalidad, precio):
    return {"nombre": nombre, "duracion": duracion, "modalidad": modalidad, "precio": precio}

andres_guardia = crear_curso("Python Básico", "40 horas", "virtual", 120000)
print(andres_guardia)