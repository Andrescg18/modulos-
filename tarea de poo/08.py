class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def cambiar_estado(self, estado):
        self.disponible = estado

class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        return self.habitacion.precio * self.dias

h1 = Habitacion(101, "Suite", 300000)
c1 = Cliente("Laura", "CC1234")
r1 = Reserva(c1, h1, 3)
print(r1.calcular_total())