soma_idades = 0
media_idade = 0
idade_maisvelho = 0
mais_velho = ''
total_mulheres = 0
for c in range(1,5):
    print(f'{c} Pessoa')
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? ')).upper()
    soma_idades += idade
    if sexo in 'Mm' and idade > idade_maisvelho:
        idade_maisvelho = idade
        mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres +=1
media_idade = soma_idades / 4
print(f'O homem mais velho é {mais_velho} e ele tem {idade_maisvelho} anos')
print(f'Tem {total_mulheres} mulheres com menos de 20 anos')
print(f'A média de idade de todos é {media_idade}')
print()