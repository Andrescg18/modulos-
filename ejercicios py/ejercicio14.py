# Ejercicio 14: Detector de números pares entre 1 y 20
pares = []
for numero in range(1, 21):
    if numero % 2 == 0:
        pares.append(numero)
print("Números pares entre 1 y 20:", pares)
