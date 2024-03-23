soma = 0
for c in range(1,7):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
       soma += numeros
print('A soma dos números pares digitados é: {}' .format(soma))