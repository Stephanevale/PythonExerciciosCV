idade = int(input('Qual o ano que você nasceu: '))
calculo = 2024 - idade

if calculo <18:
    print('Você ainda vai precisar se alistar ao exército!')
    print('Falta {} ano(s) para se alistar'.format(18 - calculo))
elif calculo > 18:
    print('Já passou do tempo de se alistar ao exército!')
    print('Passou {} anos(s) do alistamento'.format(calculo - 18))
elif calculo == 18:
    print('Está na hora de se alistar ao exército!')

