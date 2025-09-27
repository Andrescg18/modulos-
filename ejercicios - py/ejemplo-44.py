def crear_cine(nombre, ciudad, salas, is_3D):
    return {"nombre": nombre, "ciudad": ciudad, "salas": salas, "3D": is_3D}

andres_guardia = crear_cine('Cine Colombia', 'Bogotá', 10, True)
print(andres_guardia)
