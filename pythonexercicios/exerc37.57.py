sexo = str(input('Qual seu sexo?(M ou F): ')).upper()
while sexo not in 'MmFf':
        sexo = str(input('Digite novamente:[m/f] ')).upper()
print('Acabou')