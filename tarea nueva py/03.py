

def promedio(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def mostrar_info_completa(nombre, edad, **kwargs):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

print(promedio(2, 4, 6))
mostrar_info_completa("Ana", 22, ciudad="Bogotá", curso="Python")
