# Ejercicio 17: Lista de compras (operaciones)
compras = ["pan", "leche", "huevos"]
compras.append("queso")
compras.insert(1, "mantequilla")
compras.remove("huevos")
elemento_eliminado = compras.pop(0)
print("Lista final:", compras)
print("Elemento eliminado:", elemento_eliminado)
