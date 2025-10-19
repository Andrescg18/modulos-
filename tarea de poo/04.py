class Empleado:
    def trabajar(self):
        return "El empleado está trabajando."

class Desarrollador(Empleado):
    def trabajar(self):
        return "El desarrollador está escribiendo código."

class Disenador(Empleado):
    def trabajar(self):
        return "El diseñador está creando interfaces."

empleados = [Desarrollador(), Disenador()]
for e in empleados:
    print(e.trabajar())