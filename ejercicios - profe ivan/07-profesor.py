def crear_profesor(nombre, materia, experiencia, universidad):
    return {"nombre": nombre, "materia": materia, "experiencia": experiencia, "universidad": universidad}

andres_guardia = crear_profesor("Carlos", "Matemáticas", 12, "Nacional")
print(andres_guardia)