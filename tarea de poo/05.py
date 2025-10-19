from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

class Bus(Transporte):
    def mover(self):
        return "El bus se desplaza por carretera."

class Tren(Transporte):
    def mover(self):
        return "El tren se mueve por rieles."

transportes = [Bus(), Tren()]
for t in transportes:
    print(t.mover())