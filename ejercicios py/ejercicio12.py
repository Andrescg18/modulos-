# Ejercicio 12: Tabla de multiplicar (numero fijo=5)
numero = 5
multiplicador = 1
print("Tabla de multiplicar del", numero, ":")
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)
    multiplicador += 1
