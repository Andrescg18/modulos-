# Ejercicio 19: Buscador en lista
animales = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato"]
animal_buscado = "gato"
print("Lista de animales:", animales)
print(animal_buscado, "está en la lista?", animal_buscado in animales)
print("Primera aparición en posición:", animales.index(animal_buscado))
print("Cantidad de apariciones:", animales.count(animal_buscado))
