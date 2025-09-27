def crear_atomo(elemento, protones, neutrones, electrones):
    return {"elemento": elemento, "protones": protones, "neutrones": neutrones, "electrones": electrones}

andres_guardia = crear_atomo('Oxígeno', 8, 8, 8)
print(andres_guardia)
