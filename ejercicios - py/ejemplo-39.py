def crear_estadio(nombre, ciudad, capacidad, año):
    return {"nombre": nombre, "ciudad": ciudad, "capacidad": capacidad, "año": año}

andres_guardia = crear_estadio('Camp Nou', 'Barcelona', 99354, 1957)
print(andres_guardia)
