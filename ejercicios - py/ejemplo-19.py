def crear_ave(nombre, especie, alas, color):
    return {"nombre": nombre, "especie": especie, "alas": alas, "color": color}

andres_guardia = crear_ave("Piolín", "Canario", True, "amarillo")
print(andres_guardia)