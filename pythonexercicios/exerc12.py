valor_original = float(input('Qual o valor do produto? R$'))
valor_desconto = int(input('Qual o valor do desconto?' ))

operacao = valor_original - (valor_original * valor_desconto) / 100

print('O valor do produto será de:{:.2f}'.format(operacao))
