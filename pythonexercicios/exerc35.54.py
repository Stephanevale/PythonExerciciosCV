maior = 0
menor = 0

for c in range(0,7):
    nasc = int(input('Qual o ano do seu nascimento?: '))
    conta = 2022 - nasc
    if conta >=18:
        maior +=1
    else:
        menor +=1

print('{} pessoas são maiores de idade e {} são menores de idade'. format(maior, menor))