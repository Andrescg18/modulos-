def crear_barco(nombre, tipo, eslora, capacidad):
    return {"nombre": nombre, "tipo": tipo, "eslora": eslora, "capacidad": capacidad}

andres_guardia = crear_barco("Titanic", "crucero", "269m", 2200)
print(andres_guardia)