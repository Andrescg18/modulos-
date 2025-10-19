class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def describir(self):
        return f"{self.nombre} cuesta ${self.precio}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)
        return self.precio

p1 = Producto("Camisa", 50000)
print(p1.describir())
print(p1.aplicar_descuento(10))