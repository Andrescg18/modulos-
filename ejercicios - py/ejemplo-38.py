def crear_partido(equipo1, equipo2, resultado, torneo):
    return {"equipo1": equipo1, "equipo2": equipo2, "resultado": resultado, "torneo": torneo}

andres_guardia = crear_partido('Colombia', 'Brasil', '1-1', 'Copa América')
print(andres_guardia)
