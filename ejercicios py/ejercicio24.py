# Ejercicio 24: Generador de contraseñas (fijo ejemplo)
import random, string
def generar_contraseña(longitud=8, mayus=True, nums=True, sims=False):
    chars = string.ascii_lowercase
    if mayus: chars += string.ascii_uppercase
    if nums: chars += string.digits
    if sims: chars += "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(longitud))
print("Contraseña ejemplo:", generar_contraseña(12, True, True, False))
