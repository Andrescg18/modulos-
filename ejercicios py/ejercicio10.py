# Ejercicio 10: Validador de contraseñas (simple)
contraseña = "MiClave123"
longitud_minima = 8
print("Contraseña a validar:", contraseña)
if len(contraseña) >= longitud_minima:
    print("La contraseña tiene la longitud correcta")
else:
    print("La contraseña es demasiado corta")
