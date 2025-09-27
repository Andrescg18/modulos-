def crear_helado(sabor, tamaño, topping, precio):
    return {"sabor": sabor, "tamaño": tamaño, "topping": topping, "precio": precio}

andres_guardia = crear_helado("chocolate", "grande", "oreo", 8000)
print(andres_guardia)