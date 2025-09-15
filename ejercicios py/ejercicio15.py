# Ejercicio 15: Juego de adivinanza con intentos fijos (simulado)
numero_secreto = 7
intentos_maximos = 3
intentos = [3, 8, 7]  # intentos simulados
for i, adivinanza in enumerate(intentos, start=1):
    print(f"Intento {i}: {adivinanza}")
    if adivinanza == numero_secreto:
        print("¡GANASTE! El número era", numero_secreto)
        break
    elif adivinanza < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
