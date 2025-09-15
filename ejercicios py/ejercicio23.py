# Ejercicio 23: Analizador de texto (fijo)
def contar_palabras(texto): return len(texto.split())
def contar_caracteres(texto, incluir_espacios=True):
    return len(texto) if incluir_espacios else len(texto.replace(" ", ""))
def palabra_mas_larga(texto):
    palabras = texto.split()
    return max(palabras, key=len)
frase = "La programación es divertida y educativa"
print("Palabras:", contar_palabras(frase))
print("Caracteres (con espacios):", contar_caracteres(frase))
print("Palabra más larga:", palabra_mas_larga(frase))
