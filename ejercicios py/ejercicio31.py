# Ejercicio 31: Simulador simple de ecosistema (resumen)
import random
class Animal:
    def __init__(self,nombre,tipo,energia=50):
        self.nombre=nombre; self.tipo=tipo; self.energia=energia; self.vivo=True
    def mover(self):
        self.energia -= 5
        if self.energia <=0: self.vivo=False
a1 = Animal("Liebre","herbívoro")
for _ in range(3):
    a1.mover()
print("Energía final:", a1.energia, "Vivo?", a1.vivo)
