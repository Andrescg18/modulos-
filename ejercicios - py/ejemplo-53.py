# ejemplo_53.py
def crear_cancion(titulo, artista, genero, duracion):
    return {"titulo": titulo, "artista": artista, "genero": genero, "duracion": duracion}

andres_guardia = crear_cancion("Shape of You", "Ed Sheeran", "Pop", "3:53")
print(andres_guardia)
