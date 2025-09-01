margen2 = "--------------productos-------------"
productos = ("Arroz", "Carne", "Huevos", "Cocacola")
precios = (1500, 15000, 16000, 8500)

def mostrar_productos():
    print(margen2)
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} = ${precios[i]}")