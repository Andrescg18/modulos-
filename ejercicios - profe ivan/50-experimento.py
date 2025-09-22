def crear_experimento(nombre, lugar, objetivo, costo):
    return {"nombre": nombre, "lugar": lugar, "objetivo": objetivo, "costo": costo}

andres_guardia = crear_experimento('LHC', 'CERN', 'Partículas subatómicas', '9 mil millones USD')
print(andres_guardia)
