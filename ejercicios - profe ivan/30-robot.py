def crear_robot(nombre, tipo, funciones, autonomia):
    return {"nombre": nombre, "tipo": tipo, "funciones": funciones, "autonomia": autonomia}

andres_guardia = crear_robot('R2D2', 'Asistente', ['mecánica', 'hologramas'], '12 horas')
print(andres_guardia)
