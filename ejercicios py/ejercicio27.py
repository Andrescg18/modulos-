# Ejercicio 27: Búsqueda binaria (lista ordenada)
def busqueda_binaria(lista, x):
    izq, der = 0, len(lista)-1
    while izq <= der:
        mid = (izq + der)//2
        if lista[mid] == x:
            return mid
        elif lista[mid] < x:
            izq = mid+1
        else:
            der = mid-1
    return -1
nums = [11,22,25,34,44,55,66,77,88,99]
print("Posición de 55:", busqueda_binaria(nums,55))
