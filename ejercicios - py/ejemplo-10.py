def crear_nota(materia, valor, porcentaje, observacion):
    return {"materia": materia, "valor": valor, "porcentaje": porcentaje, "observacion": observacion}

andres_guardia = crear_nota("Inglés", 4.5, "30%", "Excelente participación")
print(andres_guardia)