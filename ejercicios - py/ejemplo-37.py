def crear_jugador(nombre, edad, posicion, goles):
    return {"nombre": nombre, "edad": edad, "posicion": posicion, "goles": goles}

andres_guardia = crear_jugador('Messi', 36, 'Delantero', 800)
print(andres_guardia)
