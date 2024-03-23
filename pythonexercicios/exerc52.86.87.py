lista = [[0,0,0], [0,0, 0], [0,0,0]]
pares = soma_coluna = seg_linha = 0
for l in range(0, 3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor para {[l],[c]}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] %2 == 0:
            pares +=lista[l][c]
    print()    
for c in range(0,3):
    soma_coluna += lista[c][2]

print(f'O maior valor da segunda linha é: {max(lista[1])}')
print(f'A soma dos números pares é: {pares}')
print(f'A soma_da terceira coluna é: {soma_coluna}')
