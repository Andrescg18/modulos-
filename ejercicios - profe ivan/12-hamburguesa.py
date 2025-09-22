def crear_hamburguesa(tipo_carne, tamaño, papas, bebida):
    return {"carne": tipo_carne, "tamaño": tamaño, "papas": papas, "bebida": bebida}

andres_guardia = crear_hamburguesa("res", "doble", True, "Coca Cola")
print(andres_guardia)