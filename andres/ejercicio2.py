def verificar_edad(edad):
    if edad == 0:
        return "dato no válido"
    elif edad < 18:
        return "es menor de edad"
    elif edad == 18:
        return "tiene exactamente 18 años"
    elif edad > 18:
        return "es mayor de edad"
    
edad=int(input("ingresa edad"))
print(verificar_edad(edad)) 