def crear_computador(marca, procesador, ram, gpu):
    return {"marca": marca, "procesador": procesador, "ram": ram, "gpu": gpu}

andres_guardia = crear_computador('Dell', 'i7', '16GB', 'RTX 3060')
print(andres_guardia)
