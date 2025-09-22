def crear_ensalada(base, proteina, aderezo, precio):
    return {"base": base, "proteina": proteina, "aderezo": aderezo, "precio": precio}

andres_guardia = crear_ensalada("lechuga", "pollo", "ranch", 15000)
print(andres_guardia)