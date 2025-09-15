# Ejercicio 33: Juego de la vida (creación simple de tablero)
import random
def crear_tablero(filas,cols,densidad=0.3):
    return [[1 if random.random()<densidad else 0 for _ in range(cols)] for _ in range(filas)]
tab = crear_tablero(5,5,0.2)
print("Tablero inicial (5x5):")
for fila in tab: print(fila)
