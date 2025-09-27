def crear_carro(marca, modelo, color, puertas):
    return {"marca": marca, "modelo": modelo, "color": color, "puertas": puertas}

andres_guardia = crear_carro("Toyota", "Corolla", "negro", 4)
print(andres_guardia)