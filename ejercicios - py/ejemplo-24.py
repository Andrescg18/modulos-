def crear_mision(nombre, dificultad, recompensa, tiempo):
    return {"nombre": nombre, "dificultad": dificultad, "recompensa": recompensa, "tiempo": tiempo}

andres_guardia = crear_mision('Salvar al reino', 'Alta', '500 monedas', '3 horas')
print(andres_guardia)
