def crear_pizza(sabor, tamaño, extra_queso, precio):
    return {"sabor": sabor, "tamaño": tamaño, "extra_queso": extra_queso, "precio": precio}

andres_guardia = crear_pizza("Hawaiana", "mediana", True, 35000)
print(andres_guardia)