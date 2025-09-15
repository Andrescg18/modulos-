# Ejercicio 32: Analizador de patrones de texto (ejemplo)
import re
texto = "Contacte a info@example.com o llame al 123-456-7890."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', texto)
telefonos = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', texto)
print("Emails encontrados:", emails)
print("Teléfonos encontrados:", telefonos)
