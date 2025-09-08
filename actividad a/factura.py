

margen = "--------------factura-------------"
nombre = "Andres el chamoloco"
fecha = "fecha 01-09-2025"
margen2 = "--------------productos-------------"
productos = ("pan","salchichas", "Huevos", "Cocacola")
precios = (1000, 1500, 1600, 6500)
margen3 = "--------------sus productos-------------"
comprados = """
1. Pan = 1000
2. Salchichas = 1500
3. Huevos = 1600
"""
margen4 = "--------------Total-------------"
subtotal = int(1000 + 1500 + 1600)
iva = int(subtotal * 0.15)
total = int(subtotal + iva)
margen5 = "---------------------------------"
gracias = """
GACIAS POR SU COMPRA, VUELVA PRONTO
"""


with open("factura.txt", "w") as archivo:
    
    archivo.write(f"{margen}\n")
    archivo.write(f"{nombre} {fecha}\n")
    archivo.write(f"{margen2}\n")

    for i in range(len(productos)):
        archivo.write(f"{i+1}. {productos[i]} = {precios[i]}\n")

    archivo.write(f"{margen3}\n")
    archivo.write(f"{comprados}\n")
    
    archivo.write(f"{margen4}\n")
    archivo.write(f"Subtotal= {subtotal}\n")
    archivo.write(f"iva= {iva}\n")
    archivo.write(f"total= {total}\n")
    
    archivo.write(f"{margen5}\n")
    archivo.write(f"{gracias}\n")

print("Queridos compañeros aqui esta su factura")
print (margen)
print (nombre, fecha)
print (margen2)
print (productos)
print (precios)
print (margen3)
print (comprados)
print (margen4)
print (subtotal)
print (iva)
print (total)
print (margen5)
print (gracias)
