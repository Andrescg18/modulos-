def crear_tren(compañia, tipo, vagones, velocidad):
    return {"compañia": compañia, "tipo": tipo, "vagones": vagones, "velocidad": velocidad}

andres_guardia = crear_tren("Renfe", "alta velocidad", 10, "300 km/h")
print(andres_guardia)