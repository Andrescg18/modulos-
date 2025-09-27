def crear_instrumento(nombre, tipo, precio, marca):
    return {"nombre": nombre, "tipo": tipo, "precio": precio, "marca": marca}

andres_guardia = crear_instrumento('Guitarra', 'Cuerda', 1200, 'Fender')
print(andres_guardia)
