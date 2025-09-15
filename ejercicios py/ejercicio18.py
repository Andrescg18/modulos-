# Ejercicio 18: Calculadora de calificaciones (estadísticas)
calificaciones = [8.5, 9.2, 7.8, 9.5, 6.9, 8.8, 9.1, 7.5]
suma_notas = sum(calificaciones)
promedio = suma_notas / len(calificaciones)
print("Suma de notas:", suma_notas)
print("Promedio:", round(promedio, 2))
print("Nota mayor:", max(calificaciones))
print("Nota menor:", min(calificaciones))
