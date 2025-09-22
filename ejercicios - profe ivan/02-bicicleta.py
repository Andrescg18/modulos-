def crear_bicicleta(tipo, marca, color, cambios):
    return {"tipo": tipo, "marca": marca, "color": color, "cambios": cambios}

andres_guardia = crear_bicicleta("montaña", "GW", "azul", 18)
print(andres_guardia)