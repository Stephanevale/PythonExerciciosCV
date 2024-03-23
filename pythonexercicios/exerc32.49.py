numero = int(input('Digite o número da tabuada que você quer ver: '))
for c in range(1,11):
    print('{} * {} = {}' .format(numero, c, numero *c))