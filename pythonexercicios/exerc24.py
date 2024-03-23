from random import randint
numero = randint(0,5)
var1 = int(input('Adivinhe qual número eu pensei de 0 a 5: '))
if var1 == numero:
    print('Parabéns você acertou!')
else:
    print('Eu ganhei pensei no número {}!'.format(numero))