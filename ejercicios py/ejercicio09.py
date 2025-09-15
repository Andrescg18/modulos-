# Ejercicio 9: Adivinanza de números (fijo)
numero_secreto = 7
adivinanza = 5
print("El número secreto es:", numero_secreto)
print("Tu adivinanza es:", adivinanza)
if adivinanza == numero_secreto:
    print("¡FELICIDADES! Adivinaste el número")
elif adivinanza < numero_secreto:
    print("Tu número es menor. Intenta con uno más grande")
else:
    print("Tu número es mayor. Intenta con uno más pequeño")
