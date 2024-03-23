from datetime import date
data_atual = date.today() 
dados = {}

for c in range(0,1):
    dados['nome'] = input('Nome: ')
    dados['ano nascimento'] = int(input('Ano de nascimento: '))
    ano_atual =  data_atual.year
    dados['idade'] = ano_atual - dados['ano nascimento']
    dados['CTPS'] = int(input('carteira de trabalho(0 não se não possuir): '))
    if dados['CTPS'] > 0:
        dados['contratacao'] = int(input('Ano de contratação: '))
        dados['aposentadoria'] = (dados['contratacao'] + 35) - dados['ano nascimento']
        dados['salario'] = float(input('Salário: R$ '))
    elif dados['CTPS'] == 0:
        break

print(dados)
for chave, valor in dados.items():
    print(f'{chave} tem valor {valor}')