def duplica(lista):
    contador = 0
    while contador <len(lista):
        lista[contador]*=2
        contador+=1
valores = [7,8,7,6,5,3]
duplica(valores)
print(valores)