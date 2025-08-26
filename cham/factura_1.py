
nombre_cliente = "Juan Pérez"
productos = [
    {"nombre": "Producto A", "cantidad": 2, "precio_unitario": 10.00},
    {"nombre": "Producto B", "cantidad": 1, "precio_unitario": 20.00},
]


factura = f"""
Factura de Compra
==========================
Cliente: {nombre_cliente}


Productos:
--------------------------
"""


total = 0
for producto in productos:
    total_producto = producto["cantidad"] * producto["precio_unitario"]
    factura += f"{producto['nombre']} (x{producto['cantidad']}): ${total_producto:.2f}\n"
    total += total_producto

factura += f"""
--------------------------
Total a pagar: ${total:.2f}

Gracias por su compra.
"""


print(factura)
