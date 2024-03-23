pessoas = []
dado = []
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = (input('Quer continuar?[s/n]: '))
    if continuar == 'n' or continuar == 'N':
        break   

maior_peso = max(pessoas, key=lambda v: v[1])
nome_pessoa_maior_peso = maior_peso[0]
valor_maior_peso = maior_peso[1]

menor_peso = min(pessoas, key=lambda v: v[1])
valor_menor_peso  = menor_peso[1]
nome_pessoa_menor = menor_peso[0]

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {valor_maior_peso} da {nome_pessoa_maior_peso}')
print(f'O menor peso foi de {valor_menor_peso} da {nome_pessoa_menor}')