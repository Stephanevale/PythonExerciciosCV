tabela = ('Corinthians', 'Santos', 'Avaí', 'América - MG', 'Bragantino',\
         'Atlético -MG', 'São Paulo', 'Botafogo', 'Internacional', \
         'Coritiba', 'Cuiabá', 'Atlético - PR', 'Palmeiras','Flamengo','Fluminense', 'Goiás', 'Ceará - SC',\
         'Juventude', 'Atlético -GO','Fortaleza')

print('=' * 40)
print('Tabela Campeonato Brasileiro')
print('=' * 40)
print(f'Os times são: {tabela}')
print('=' * 40)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('=' * 40)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('=' * 40)
print(f'Time em ordem alfabética:{sorted(tabela)}')
print('=' * 40)
print(f'Quem está na 8º posição é: {tabela[7]}')
print('=' * 40)
