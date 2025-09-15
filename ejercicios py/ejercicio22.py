# Ejercicio 22: Calculadora con funciones
def sumar(a,b): return a+b
def restar(a,b): return a-b
def multiplicar(a,b): return a*b
def dividir(a,b): return a/b if b != 0 else "Error: división por cero"
num1, num2 = 15, 3
print("Sumar:", sumar(num1,num2))
print("Restar:", restar(num1,num2))
print("Multiplicar:", multiplicar(num1,num2))
print("Dividir:", dividir(num1,num2))
