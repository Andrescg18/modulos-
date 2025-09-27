# ejemplo_62.py
def crear_videojuego(nombre, plataforma, genero, jugadores):
    return {"nombre": nombre, "plataforma": plataforma, "genero": genero, "jugadores": jugadores}

andres_guardia = crear_videojuego("The Legend of Zelda", "Nintendo Switch", "Aventura", 1)
print(andres_guardia)
