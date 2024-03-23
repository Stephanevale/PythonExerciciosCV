dados = []
informacao = {}
informacao['nome'] = input('nome: ')
informacao['media'] = float(input('Média: '))
dados.append(informacao.copy())
print(f'Nome é igual a {dados[0]["nome"]}')
print(f'Média é igual a {dados[0]["media"]}')
if informacao['media'] < 6:
    print('Situação do aluno é reprovado')
else:
    print('Situação do aluno é aprovado')
    