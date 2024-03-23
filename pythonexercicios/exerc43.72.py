numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze',
           'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = None
while True:
    mensagem = int(input('Digite um numero entre 0 e 20: '))
    if mensagem <0 or mensagem >20:
        print('Tente novamente, digite um numero entre 0 e 20. ')
    if 0 <= mensagem <=20:
        print(f'Você digitou o número {numeros[mensagem]}')
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'S':
        mensagem
    if continuar == 'N':
        break
print('Obrigada!')