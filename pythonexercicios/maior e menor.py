l = [5,2,96,7]
maximo = l[0]
menor = l[0]
for e in l:
    if e > maximo:
        maximo = e
    if e < menor:
        menor = e
print(maximo)
print(menor)
