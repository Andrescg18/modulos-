def crear_album(titulo, artista, año, canciones):
    return {"titulo": titulo, "artista": artista, "año": año, "canciones": canciones}

andres_guardia = crear_album('Thriller', 'Michael Jackson', 1982, 9)
print(andres_guardia)
