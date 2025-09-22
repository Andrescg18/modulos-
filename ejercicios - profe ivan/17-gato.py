def crear_gato(nombre, raza, edad, pelaje):
    return {"nombre": nombre, "raza": raza, "edad": edad, "pelaje": pelaje}

andres_guardia = crear_gato("Michi", "Persa", 2, "blanco")
print(andres_guardia)