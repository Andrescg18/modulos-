def crear_galaxia(nombre, tipo, estrellas, tamaño):
    return {"nombre": nombre, "tipo": tipo, "estrellas": estrellas, "tamaño": tamaño}

andres_guardia = crear_galaxia('Vía Láctea', 'Espiral', '100B', '105000 ly')
print(andres_guardia)
