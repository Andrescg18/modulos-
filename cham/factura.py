margen4 = "--------------Total-------------"
margen5 = "---------------------------------"
gracias = """
GRACIAS POR SU COMPRA, FELIZ DIA
"""

def calcular_total():
    subtotal = 1500 + 15000 + 16000
    iva = int(subtotal * 0.15)
    total = subtotal + iva

    print(margen4)
    print("Subtotal =", subtotal)
    print("IVA =", iva)
    print("Total =", total)
    print(margen5)
    print(gracias)