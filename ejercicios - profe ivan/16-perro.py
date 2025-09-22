def crear_perro(nombre, raza, edad, color):
    return {"nombre": nombre, "raza": raza, "edad": edad, "color": color}

andres_guardia = crear_perro("Firulais", "Labrador", 3, "marrón")
print(andres_guardia)