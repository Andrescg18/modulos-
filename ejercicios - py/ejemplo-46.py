def crear_planeta(nombre, tipo, distancia, lunas):
    return {"nombre": nombre, "tipo": tipo, "distancia": distancia, "lunas": lunas}

andres_guardia = crear_planeta('Marte', 'rocoso', '225M km', 2)
print(andres_guardia)
