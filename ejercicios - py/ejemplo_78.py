# ejemplo_78.py
def crear_computador(marca, procesador, ram, almacenamiento):
    return {"marca": marca, "procesador": procesador, "ram": ram, "almacenamiento": almacenamiento}

andres_guardia = crear_computador("Dell", "Intel i7", "16GB", "512GB SSD")
print(andres_guardia)
