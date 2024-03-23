MEDIA_PARA_APROVACAO = 6

dados = []

nome = input('nome: ')
media = float(input('Média: '))

dados.append({'nome': nome, 'media': media})

for dado in dados:
    situacao = "reprovado" if dado['media'] < MEDIA_PARA_APROVACAO else "aprovado"

    print(f'Nome é igual a {dado["nome"]}.')
    print(f'Média é igual a {dado["media"]}.')
    print(f"Situação do aluno {dado['nome']} é {situacao}.")
