def crear_actor(nombre, edad, nacionalidad, premios):
    return {"nombre": nombre, "edad": edad, "nacionalidad": nacionalidad, "premios": premios}

andres_guardia = crear_actor('Leonardo DiCaprio', 49, 'EE.UU', 3)
print(andres_guardia)
