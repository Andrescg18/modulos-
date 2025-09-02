numerosdivisiblespor2= []

for i in range(1, 25): 
    if i % 2 == 0:
        numerosdivisiblespor2.append(i)
        if len(numerosdivisiblespor2) == 20:
            break

print(numerosdivisiblespor2)
