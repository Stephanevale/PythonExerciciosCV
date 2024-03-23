from random import randint
número = list()
def sorteio():
    for indice in range(0,5):
        número.append(randint(0,9))

def somaPar(número):
    soma = 0
    for valor in número:
        if valor % 2 == 0:
            soma += valor
    print(f'Sorteando 5 valores da lista: ',end='')
    print(f'{número}')
    print(f'Somando os valores pares de {número} temos {soma}')

sorteio()
somaPar(número)

