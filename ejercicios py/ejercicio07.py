# Ejercicio 7: Calculadora de descuentos
precio_total = 120
descuento = 0
if precio_total > 100:
    descuento = precio_total * 0.10
precio_final = precio_total - descuento
print("Descuento aplicado:", descuento)
print("Precio final:", precio_final)
