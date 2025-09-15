# Ejercicio 26: Ordenamiento Burbuja (ejemplo)
def burbuja(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
nums = [64,34,25,12,22,11,90]
print("Original:", nums)
print("Ordenada:", burbuja(nums))
