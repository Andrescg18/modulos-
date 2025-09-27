def crear_concierto(lugar, fecha, artista, asistentes):
    return {"lugar": lugar, "fecha": fecha, "artista": artista, "asistentes": asistentes}

andres_guardia = crear_concierto('Wembley', '2024-07-12', 'Adele', 90000)
print(andres_guardia)
