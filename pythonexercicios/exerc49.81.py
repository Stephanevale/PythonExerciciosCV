lista = []
while True:
    inserir = int(input('Digite um valor (0) sai: '))
    if inserir == 0:
        break
    lista.append(inserir) 
if 5 in lista:
    print(f'O número 5 está na lista!')
lista.reverse()
print(f'Foram digitados {len(lista)} números')
print(lista)
