aproveitamento = {}
aproveitamento['total'] = 0
aproveitamento['nome'] = input('Nome: ')
aproveitamento['partidas'] = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou: '))

for contador in range(aproveitamento['partidas']):
    aproveitamento['gols'] = int(input(f'Quantos gols na partida {contador}?: '))
    aproveitamento['total'] = aproveitamento['total'] + aproveitamento['gols']


print('=-'*30)

for chave, valores in aproveitamento.items():
    print(f'O campo {chave} tem valor {valores}')

print('=-'*30)
