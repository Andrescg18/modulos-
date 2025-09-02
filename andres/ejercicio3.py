def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b != 0:
            return a / b
        else:
            return "Error: división por cero"
    else:
        return "Operación no válida"
    
