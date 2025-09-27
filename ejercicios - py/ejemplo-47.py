def crear_estrella(nombre, tipo, masa, edad):
    return {"nombre": nombre, "tipo": tipo, "masa": masa, "edad": edad}

andres_guardia = crear_estrella('Sol', 'Enana amarilla', '1.989e30 kg', '4.6B años')
print(andres_guardia)
