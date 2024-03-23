lista = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input(f'digite um número para a posição {c}º: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else: 
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]} e os ímpares são {lista[1]}')