from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo ==0:
        passo= 1
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo} ')
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
        print('FIM')
    

        
contador(1,10,1)
contador(10,0,2)
i = (int(input('Inicio: ')))
f = (int(input('Fim: '))) 
p = (int(input('Passo: ')))
contador(i,f,p)