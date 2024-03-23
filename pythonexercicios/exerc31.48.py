soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1 #pode ser tb cont+=1 contador
        soma = soma + c #pode ser tb soma+=c acumulador
print('A soma de todos os {} valores solicitados é {}' .format(cont,soma))