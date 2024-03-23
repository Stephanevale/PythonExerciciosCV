soma = 0
mais = 0
while True:
    numero = int(input('Digite um número(999 para parar): '))
    if numero == 999:
        break
    mais += 1
    soma += numero
print(f'A soma dos números foi {soma}')
print(f'Foram digitados {mais} números')
