

def numeros_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

print(numeros_pares([1,2,3,4,5,6,7,8]))


def depurar(func):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__} con args={args} kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@depurar
def sumar(a, b):
    return a + b

sumar(5, 3)
