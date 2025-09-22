def crear_celular(marca, modelo, ram, almacenamiento):
    return {"marca": marca, "modelo": modelo, "ram": ram, "almacenamiento": almacenamiento}

andres_guardia = crear_celular('Samsung', 'S23', '12GB', '256GB')
print(andres_guardia)
