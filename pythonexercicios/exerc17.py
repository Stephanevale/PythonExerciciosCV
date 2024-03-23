import random
aluno1 = input('Insira o nome do primerio aluno: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)

print('O aluno escolhido foi {}'.format(sorteado))