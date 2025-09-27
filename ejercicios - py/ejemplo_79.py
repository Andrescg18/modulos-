# ejemplo_79.py
def crear_telefono(marca, modelo, pantalla, bateria):
    return {"marca": marca, "modelo": modelo, "pantalla": pantalla, "bateria": bateria}

andres_guardia = crear_telefono("Samsung", "Galaxy S23", "6.5 pulgadas", "5000mAh")
print(andres_guardia)
