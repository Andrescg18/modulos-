def crear_personaje(nombre, rol, nivel, poder):
    return {"nombre": nombre, "rol": rol, "nivel": nivel, "poder": poder}

andres_guardia = crear_personaje('Link', 'Héroe', 20, 'Espada Maestra')
print(andres_guardia)
