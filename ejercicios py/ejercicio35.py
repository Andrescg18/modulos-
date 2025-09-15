# Ejercicio 35: Compresión simple (repetición simple)
def comprimir_repeticion_simple(texto):
    if not texto: return ""
    resultado = ""
    contador = 1
    for i in range(1,len(texto)):
        if texto[i]==texto[i-1]:
            contador += 1
        else:
            resultado += str(contador) + texto[i-1]
            contador = 1
    resultado += str(contador) + texto[-1]
    return resultado
print(comprimir_repeticion_simple("aaaaabbbccaa"))
