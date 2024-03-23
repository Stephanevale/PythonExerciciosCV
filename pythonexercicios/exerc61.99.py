def maior(*num):
    contador = maior = 0
    print('Analisando os valores passados...') 
    for valor in num:
        print(f' {valor}', end='')
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
             maior = valor
        contador +=1
    
    print(f' Foram informados {contador} valores ao todo.')
    print(f' O maior número informado foi {maior}')
    print('=' * 40)


maior(0,8,5,4,7,6)
maior(0,5,2,6,4)
maior(3)
maior()