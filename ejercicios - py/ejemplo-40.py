def crear_trofeo(nombre, organizacion, año, ganador):
    return {"nombre": nombre, "organizacion": organizacion, "año": año, "ganador": ganador}

andres_guardia = crear_trofeo('Balón de Oro', 'France Football', 2023, 'Messi')
print(andres_guardia)
