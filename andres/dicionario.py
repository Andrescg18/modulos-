#lista1=["juan"]
#lista=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#print(lista1)
#print(lista[2])

#diccionario={
 #   "computador": {"cantidad": 10, "precio":150},
  #  "teclado": {"cantidad":15, "precio":50}
#}

#print(diccionario["computador"])

diccionario = {
    "computador": {"cantidad": 10, "precio": 150},
    "teclado": {"cantidad": 15, "precio": 50}
}

for i in diccionario:
    if i == "teclado":
        print(diccionario[i])
