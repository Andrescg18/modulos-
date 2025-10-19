class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def listar_profesores(self):
        return [p.nombre for p in self.profesores]

u = Universidad("Nacional")
u.agregar_profesor(Profesor("Andrés"))
u.agregar_profesor(Profesor("Lucía"))
print(u.listar_profesores())