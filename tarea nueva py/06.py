

PLUGINS = {}

def plugin(nombre):
    def decorador(func):
        PLUGINS[nombre] = func
        return func
    return decorador

def ejecutar(nombre, *args, **kwargs):
    funcion = PLUGINS.get(nombre)
    if not funcion:
        return f"Plugin '{nombre}' no encontrado."
    return funcion(*args, **kwargs)

@plugin("saludo")
def saludo(nombre):
    return f"¡Hola {nombre}!"

@plugin("despedida")
def despedida(nombre):
    return f"¡Adiós {nombre}!"

print(ejecutar("saludo", "Andrés"))
print(ejecutar("despedida", "Luis"))
