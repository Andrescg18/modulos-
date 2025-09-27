# ejemplo_64.py
def crear_equipo(nombre, deporte, pais, fundacion):
    return {"nombre": nombre, "deporte": deporte, "pais": pais, "fundacion": fundacion}

andres_guardia = crear_equipo("Barcelona FC", "Fútbol", "España", 1899)
print(andres_guardia)
