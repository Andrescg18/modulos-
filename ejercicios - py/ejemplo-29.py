def crear_smartwatch(marca, modelo, resistencia, precio):
    return {"marca": marca, "modelo": modelo, "resistencia": resistencia, "precio": precio}

andres_guardia = crear_smartwatch('Xiaomi', 'Mi Watch', '50m agua', 800000)
print(andres_guardia)
