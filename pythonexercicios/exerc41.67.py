while True:
    print('-'*20)
    numero = int(input('Digite o número da tabuada que você quer ver: '))
    if numero <0:
        break
    print('-'*20)
    for c in range(1,11):
        print('{} * {} = {}'.format(numero,c, numero * c))
print('Acabou!')

