# Ejercicio 20: Organizador de lista (ordenar, invertir, mezclar)
import random
numeros = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
print("Original:", numeros)
asc = numeros.copy()
asc.sort()
desc = sorted(numeros, reverse=True)
mezclada = numeros.copy()
random.shuffle(mezclada)
invertida = list(reversed(numeros))
print("Ascendente:", asc)
print("Descendente:", desc)
print("Mezclada:", mezclada)
print("Invertida:", invertida)
