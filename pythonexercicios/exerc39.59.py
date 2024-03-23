numero1 = None
numero2 = None
c = None

while c != 5:
    if c == 1:
        print('A soma dos dois números é: {}'.format(numero1 + numero2))
    elif c == 2:
        print('A multiplicação dos dois números é {}'.format(numero1 * numero2))
    elif c == 3 and numero1 > numero2:
        print('O primeiro número é maior que o segundo')
    elif c == 3 and numero2 > numero1:
        print('O segundo número é maior que o primeiro')
    elif c == 3 and numero1 == numero2:
        print('Os dois números são iguais')
    elif c == 4:
        numero1
        numero2

    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    c = (float(input(
        '''Você pode: \n1. Somar \n2. Multiplicar\n3. Saber qual o maior\n4. Digitar novos números\n5. Sair do programa \nO que deseja fazer: 
''')))

print('Obrigada, o programa acabou')
