cateto = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do cateto adjacente: '))

calculo = (cateto ** 2 + cateto_adj** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(calculo))


#ou pode utilizar a função math

#import.math
#cateto = float(input('Digite o valor do cateto oposto: '))
#cateto_adj = float(input('Digite o valor do cateto adjacente: '))
#calculo = math.hypot (cateto, cateto_adj)
#print('A hipotenusa vai medir {:.2f}'.format(calculo))
#hypot é a função da hipotenusa