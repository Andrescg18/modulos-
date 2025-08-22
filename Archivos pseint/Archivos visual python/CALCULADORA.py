def calculadora():
    print(" Calculadora en Python ")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    
    
    num1 = (input("Ingresa el primer número: "))
    num2 = (input("Ingresa el segundo número: "))
    
    
    operacion = input("Elige la operación (+, -, *, /): ")
    
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Operación no válida"
    
    return f"El resultado es: {resultado}"

print(calculadora())