Alunos = []
while True:
    nome = input('Nome: ')
    nota1 = (float(input(f'nota: ')))
    nota2 = (float(input(f'nota: '))) 
    media = (nota1 + nota2) / 2

    notas = [nota1, nota2]
    lista_aluno = [nome, notas, media]
    Alunos.append(lista_aluno)
    continuar = (input('Quer continuar?: '))
    if continuar == 'N' or continuar == 'n':
        print()
        break
print('Nº          Nome       Média')
print()
for c, e in enumerate(Alunos):
    print(f'{c}.          {e[0]}          {e[2]}')
print()
while True:
    notas_individuais = int(input(f'Mostrar notas de quais alunos?(100 sai): '))
    if notas_individuais == 100:
        break
    if notas_individuais <= len(Alunos) -1:
        print(f'Notas de {Alunos[notas_individuais][0]} são {Alunos[notas_individuais][1]}')
print()
