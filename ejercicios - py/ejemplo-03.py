def crear_avion(modelo, aerolinea, capacidad, autonomia):
    return {"modelo": modelo, "aerolinea": aerolinea, "capacidad": capacidad, "autonomia": autonomia}

andres_guardia = crear_avion("Boeing 737", "Avianca", 180, "5000 km")
print(andres_guardia)