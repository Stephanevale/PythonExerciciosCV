def ficha(a, b):
    return f'O jogador {a} fez {b} gols'

a = input('Nome do jogador: ')
b = input('Quantos gols: ')
if a == '':
    a = 'desconhecido'
if b == '':
    b = '0'
variavel = ficha(a, b)
print(variavel)
