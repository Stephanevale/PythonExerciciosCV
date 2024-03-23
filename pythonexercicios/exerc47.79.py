lista = []
while True:
    inserir = int(input('Digite um número: '))
    continuar = (input('Quer continuar? [S/N]: '))
    if inserir not in lista:
        lista.append(inserir)
    if continuar in 'nN':
        break
print('Os números duplicados não foram adicionados na lista')
lista.sort()
print(lista) 