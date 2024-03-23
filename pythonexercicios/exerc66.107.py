import moeda

n = int(input('Digite um valor: '))
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'10% de {n} é {moeda.dez(n):.2f}')
print(f'13% de {n} é {moeda.treze(n):.2f}')