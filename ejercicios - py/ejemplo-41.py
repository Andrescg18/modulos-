def crear_pelicula(titulo, director, año, genero):
    return {"titulo": titulo, "director": director, "año": año, "genero": genero}

andres_guardia = crear_pelicula('Inception', 'Christopher Nolan', 2010, 'Ciencia ficción')
print(andres_guardia)
