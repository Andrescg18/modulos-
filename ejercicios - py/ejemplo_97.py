# ejemplo_97.py
def crear_lugar(nombre, pais, tipo, atractivo):
    return {"nombre": nombre, "pais": pais, "tipo": tipo, "atractivo": atractivo}

andres_guardia = crear_lugar("Machu Picchu", "Perú", "Ruinas", "Patrimonio de la Humanidad")
print(andres_guardia)
