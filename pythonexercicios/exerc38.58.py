from random import randint
numero = randint(1,10)
numero_inserido = None
numero_tentivas = 0
while numero_inserido != numero:
    numero_inserido = int(input('Adivinhe qual número eu pensei de 0 a 10: '))
    numero_tentivas += 1
print(f'Você acertou o número {numero} com {numero_tentivas} tentativas')