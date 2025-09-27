def crear_juego(nombre, genero, plataforma, precio):
    return {"nombre": nombre, "genero": genero, "plataforma": plataforma, "precio": precio}

andres_guardia = crear_juego('Minecraft', 'Sandbox', 'PC', 120000)
print(andres_guardia)
