# Ejercicio 29: Generador de primos (Criba de Eratóstenes)
def criba(limite):
    es_primo = [True]*(limite+1)
    es_primo[0]=es_primo[1]=False
    for i in range(2,int(limite**0.5)+1):
        if es_primo[i]:
            for j in range(i*i, limite+1, i):
                es_primo[j]=False
    return [i for i,pr in enumerate(es_primo) if pr]
print("Primos hasta 30:", criba(30))
