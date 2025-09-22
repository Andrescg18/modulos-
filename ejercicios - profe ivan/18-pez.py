def crear_pez(nombre, especie, tamaño, color):
    return {"nombre": nombre, "especie": especie, "tamaño": tamaño, "color": color}

andres_guardia = crear_pez("Nemo", "Payaso", "pequeño", "naranja")
print(andres_guardia)