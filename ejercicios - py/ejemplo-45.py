def crear_serie(titulo, temporadas, episodios, plataforma):
    return {"titulo": titulo, "temporadas": temporadas, "episodios": episodios, "plataforma": plataforma}

andres_guardia = crear_serie('Breaking Bad', 5, 62, 'Netflix')
print(andres_guardia)
