maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input('Peso da {} pessoa?: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi {} e o maior foi {}'. format(menor, maior))
