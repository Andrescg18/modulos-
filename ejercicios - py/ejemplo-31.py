def crear_cancion(titulo, artista, duracion, genero):
    return {"titulo": titulo, "artista": artista, "duracion": duracion, "genero": genero}

andres_guardia = crear_cancion('Imagine', 'John Lennon', '3:05', 'Pop')
print(andres_guardia)
