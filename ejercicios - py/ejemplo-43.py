def crear_director(nombre, peliculas, oscars, pais):
    return {"nombre": nombre, "peliculas": peliculas, "oscars": oscars, "pais": pais}

andres_guardia = crear_director('Spielberg', 35, 3, 'EE.UU')
print(andres_guardia)
