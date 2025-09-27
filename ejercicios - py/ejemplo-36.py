def crear_equipo(nombre, pais, jugadores, liga):
    return {"nombre": nombre, "pais": pais, "jugadores": jugadores, "liga": liga}

andres_guardia = crear_equipo('Barcelona', 'España', 25, 'La Liga')
print(andres_guardia)
