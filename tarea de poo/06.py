class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f"Rectángulo {self.ancho}x{self.alto}"

    def __eq__(self, otro):
        return self.area() == otro.area()

    def __lt__(self, otro):
        return self.area() < otro.area()

r1 = Rectangulo(5, 10)
r2 = Rectangulo(4, 12)
print(r1)
print(r1 == r2)
print(r1 < r2)