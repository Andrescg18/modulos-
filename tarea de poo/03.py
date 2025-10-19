class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        return f"{self.nombre} está siendo tocado."

class Guitarra(Instrumento):
    def tocar(self):
        return f"La guitarra {self.nombre} suena con acordes."

class Piano(Instrumento):
    def tocar(self):
        return f"El piano {self.nombre} produce notas suaves."

i1 = Guitarra("Fender")
i2 = Piano("Yamaha")
print(i1.tocar())
print(i2.tocar())