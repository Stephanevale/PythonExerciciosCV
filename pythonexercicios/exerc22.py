nome = input('Digite sua frase?: ').upper() .strip()
print('Seu nome tem {} letras a'.format(nome.count('A')))
print('A letra a aparece primeira vez na posição {}'.format(nome.find('A')+1))
print('A letra a aparece última vez na posição {}'.format(nome.rfind('A')+1))
