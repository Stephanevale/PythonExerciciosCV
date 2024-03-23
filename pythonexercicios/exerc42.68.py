from random import randint
print('Vamos jogar par ou impar')
v = 0
while True:
    usuario = int(input('Digite um valor: '))
    sistema = randint(1, 10)
    valor = usuario + sistema
    jogo = ' '
    while jogo not in 'PI':
        jogo = str(input('Você quer par ou impar[P/I]: ')).strip().upper()[0]
    print(f'Você jogou {usuario} e eu joguei {sistema} o total foi {valor}')
    if jogo == 'P':
        if valor %2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif jogo == 'I':
        if valor %2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {v} vezes')




