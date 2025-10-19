

import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ Tiempo de ejecución de '{func.__name__}': {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso_lento(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

print(proceso_lento(1000000))
