def encabezado(nombre, fecha):
    print("------------- FACTURA -------------")
    print(f"Nombre: {nombre}  Fecha: {fecha}")

def mostrar_productos(productos, precios):
    print("--------- PRODUCTOS DISPONIBLES ---------")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} = ${precios[i]}")

def mostrar_comprados(compras):
    print("--------- SUS PRODUCTOS ---------")
    for i, (producto, precio) in enumerate(compras.items(), 1):
        print(f"{i}. {producto} = ${precio}")

def calcular_total(compras):
    subtotal = sum(compras.values())
    iva = int(subtotal * 0.15)
    total = subtotal + iva
    return subtotal, iva, total

def factura(nombre, fecha, compras):
    encabezado(nombre, fecha)
    mostrar_comprados(compras)

    print("----------- TOTAL -----------")
    subtotal, iva, total_final = calcular_total(compras)
    print(f"Subtotal: ${subtotal}")
    print(f"IVA (15%): ${iva}")
    print(f"Total: ${total_final}")
    print("-----------------------------")
    print("🤗 GRACIAS POR SU COMPRA, FELIZ DÍA 🤗")


nombre = "Andres el chamoloco"
fecha = "01-09-2025"

productos = ["Arroz", "Carne", "Huevos", "Cocacola"]
precios = [1500, 15000, 16000, 8500]


mostrar_productos(productos, precios)


compras = {
    "Arroz": 1500,
    "Carne": 15000,
    "Huevos": 16000
}


factura(nombre, fecha, compras)

