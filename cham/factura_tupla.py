margen=("--------------factura-------------")

nombre=("Andres el chamoloco")
fecha=("fecha 01-09-2025")

print(margen)
print(f"{nombre} {fecha}")
margen2=("--------------productos-------------")
print(margen2)

productos=("Arroz","Carne","Huevos","Cocacola")
precios=(1500,15000,16000,8500)

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} = ${precios[i]}")
margen3=("--------------sus productos-------------")
print(margen3)
comprados=""""
1.Arroz = 1500
2.Carne = 15000
3.Huevos = 16000
"""

print(margen3)
print(comprados)
margen4=("--------------Total-------------")
subtotal=(int(1500+15000+16000))
iva=(int(subtotal*0.15))
total=(int(subtotal+iva))
print(margen4)
print("Subtotal=", subtotal)
print("iva=", iva)
print("total=", total)
margen5=("---------------------------------")
gracias=""""
GRACIAS POR SU COMPRA, FELIZ DIA
"""
print(margen5)
print(gracias)



