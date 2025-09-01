diccionario={
    "nombre1":"juan", "edad1":89, "ciudad1":"colombia",
    "nombre2":"andres", "edad2":9, "ciudad2":"españa",
    "nombre3":"sebastian", "edad3":8, "ciudad3":"venezuela",
    "nombre4":"diego", "edad4":70, "ciudad4":"francia",
    "nombre5":"martin", "edad5":15, "ciudad5":"inglaterra"}

#print(diccionario["edad5"])
archivo=open("dic.txt", "a")
archivo.write(diccionario["nombre1"]+ "," + str(diccionario["edad1"]) +"\n" )
archivo.close()