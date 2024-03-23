valores = []
cont = 0
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'O maior número foi {max(valores)} e esta na posição: {i}')
    if v == min(valores):
        print(f'o menor foi {min(valores)} na posição: {i}')

print(valores)

