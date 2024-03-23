from random import randint
jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
print('-' * 20)

for c in jogo:
    print(f'O {c}. tirou: {jogo[c]} no dado .')

print('-' * 20)
print('Ranking dos jogadores')
print('-' * 20)

for i, v in enumerate(sorted(jogo, key = jogo.get, reverse =True)):
     print(f'{i+1}º lugar: {v} com {jogo[v]}.')

print()
