def crear_tablet(marca, modelo, tamaño, bateria):
    return {"marca": marca, "modelo": modelo, "tamaño": tamaño, "bateria": bateria}

andres_guardia = crear_tablet('Apple', 'iPad Pro', '12 pulgadas', '10000mAh')
print(andres_guardia)
