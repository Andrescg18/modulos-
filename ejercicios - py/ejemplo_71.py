# ejemplo_71.py
def crear_libro(titulo, autor, año, genero):
    return {"titulo": titulo, "autor": autor, "año": año, "genero": genero}

andres_guardia = crear_libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico")
print(andres_guardia)
