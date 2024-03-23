def voto(ano):
    from datetime import date
    ano_atual =  date.today().year
    data_nascimento = ano_atual - ano
    if data_nascimento < 16:
        return f'{data_nascimento} anos, sem idade para votar'
    elif data_nascimento <= 16 or data_nascimento > 65:
        return f'Com {data_nascimento} o voto é opcional'
    else:
        return 'Voto obrigatório'
    
nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))
