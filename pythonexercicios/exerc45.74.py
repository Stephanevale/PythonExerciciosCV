import random

numero2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

variavel = random.sample(numero2,5)
print(variavel)
print(f'O maior valor sorteado foi {max(variavel)}')
print(f'O menor valor sorteado foi {min(variavel)}')