idade = int(input('Qual a sua idade?: '))

if idade <=9:
    print('Sua categoria é mirim!')
elif idade > 9 and idade <= 14:
    print('Sua categoria é infantil!')
elif idade > 14 and idade <=19:
    print('Sua categoria é Junior!')
elif idade == 20:
    print('Sua categoria é Sênior')
elif idade > 20:
    print('Sua categoria é master')