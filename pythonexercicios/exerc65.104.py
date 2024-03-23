def leiaint():
    valor = 0
    while True:
        n = input("numero: ")
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Digite um número inteiro')
    return valor
n = leiaint()
print(f'Você digitou {n}')
