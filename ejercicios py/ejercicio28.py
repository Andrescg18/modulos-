# Ejercicio 28: Contador de frecuencias
def contar_frecuencias(lista):
    frec = {}
    for e in lista:
        frec[e] = frec.get(e,0) + 1
    return frec
numeros = [1,2,3,2,1,4,2,5,2,1,3,2]
print("Frecuencias:", contar_frecuencias(numeros))
