def crear_mapa(nombre, tamaño, enemigos, clima):
    return {"nombre": nombre, "tamaño": tamaño, "enemigos": enemigos, "clima": clima}

andres_guardia = crear_mapa('Bosque Oscuro', 'Grande', 'Orcos', 'Lluvioso')
print(andres_guardia)
