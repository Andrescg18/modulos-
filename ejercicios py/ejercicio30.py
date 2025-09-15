# Ejercicio 30: Sistema de recomendaciones (simplificado)
usuarios = {
    "Ana":{"accion":True,"comedia":True},
    "Carlos":{"accion":True,"comedia":False},
    "Pedro":{"accion":True,"comedia":True}
}
def similitud(u1,u2):
    comunes=0; iguales=0
    for k in u1:
        if k in u2:
            comunes+=1
            if u1[k]==u2[k]: iguales+=1
    return iguales/comunes if comunes else 0
print("Similitud Ana-Carlos:", similitud(usuarios["Ana"], usuarios["Carlos"]))
