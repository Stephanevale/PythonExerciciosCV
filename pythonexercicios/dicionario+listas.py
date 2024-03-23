brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print(brasil[0])

#adicionar dicionarios nas litas
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Uf: '))
    estado['sigla'] = str(input('sigla: '))
    brasil.append(estado.copy()) 
    #método interno do dicionário para fazer uma cópia
print(brasil)
#usando laços
for e in brasil:
    print(e)
#ou
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}') 
#ou
for e in brasil:
    for v in e.values():
        print(v)