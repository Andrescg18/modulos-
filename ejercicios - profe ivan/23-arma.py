def crear_arma(nombre, tipo, daño, durabilidad):
    return {"nombre": nombre, "tipo": tipo, "daño": daño, "durabilidad": durabilidad}

andres_guardia = crear_arma('Excalibur', 'Espada', 90, 100)
print(andres_guardia)
