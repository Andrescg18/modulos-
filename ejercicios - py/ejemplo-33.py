def crear_banda(nombre, miembros, genero, pais):
    return {"nombre": nombre, "miembros": miembros, "genero": genero, "pais": pais}

andres_guardia = crear_banda('Coldplay', 4, 'Rock Alternativo', 'UK')
print(andres_guardia)
