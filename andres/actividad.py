class Vehiculo:
    def __init__(self, color, motor, capacidad):
        self.color = color
        self.motor = motor
        self.capacidad = capacidad


moto1 = Vehiculo("negro", 1000, 5)


print(moto1.color)
print(moto1.motor)
print(moto1.capacidad)
