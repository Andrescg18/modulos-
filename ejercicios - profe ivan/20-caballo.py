def crear_caballo(nombre, raza, edad, velocidad):
    return {"nombre": nombre, "raza": raza, "edad": edad, "velocidad": velocidad}

andres_guardia = crear_caballo("Tornado", "Pura Sangre", 5, "60 km/h")
print(andres_guardia)