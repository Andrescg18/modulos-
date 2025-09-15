# Ejercicio 34: Optimizador de rutas (ejemplo con fuerza bruta para 4 ciudades)
import math, itertools
ciudades = [(0,0),(1,2),(3,1),(2,4)]
def distancia(a,b): return math.hypot(a[0]-b[0], a[1]-b[1])
def distancia_ruta(ciudades, ruta):
    d=0
    for i in range(len(ruta)):
        d += distancia(ciudades[ruta[i]], ciudades[ruta[(i+1)%len(ruta)]])
    return round(d,2)
mejor=None
for perm in itertools.permutations(range(len(ciudades))):
    d = distancia_ruta(ciudades, perm)
    if mejor is None or d<mejor[0]:
        mejor=(d,perm)
print("Mejor distancia:", mejor[0], "Ruta:", mejor[1])
