def crear_cafe(tipo, tamaño, leche, azucar):
    return {"tipo": tipo, "tamaño": tamaño, "leche": leche, "azucar": azucar}

andres_guardia = crear_cafe("capuchino", "mediano", True, 2)
print(andres_guardia)