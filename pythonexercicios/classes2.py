class Planta:
    def __init__(self, nome, cor, porte, decorativa, eh_de_sol):
        self.nome = nome
        self.cor = cor
        self.porte = porte
        self.decorativa = decorativa
        self.eh_de_sol = eh_de_sol

    def fotosintese(self):
        if self.decorativa:
            print(f'Não faço fotossíntese')
        else:
            print(f'Sou real  e estou fazendo fotossíntese')

    def absorve_CO2(self):
        if not self.decorativa:
            print(f'Além disso, absorvo O2')
        else:
            print(f'Não sou real, portanto não absorvo O2')

    def libera_O2(self):
        if not self.decorativa:
            print(f'Também libero O2')
        else:
            print(f'Assim, não libero O2')

class PlantaCarnivora(Planta):
    def complementa_nutricao(self):
        print(f'Complementa nutrição com seres vivos, por exemplo, insetos.')


planta_um = Planta('Sigonio', 'verde e branco', 'médio', False, True)
planta_dois = Planta('Suculenta', 'Verde','pequeno', True, False)
planta_tres = PlantaCarnivora('Planta carnívora', 'verde', 'pequena', False, False)


print(f'Eu sou a', planta_um.nome, 'minha cor é', planta_um.cor, 'tenho o porte', planta_um.porte)
planta_um.fotosintese(),
planta_um.absorve_CO2(),
planta_um.libera_O2() 


print(f'Eu sou a', planta_dois.nome,'minha cor é',planta_dois.cor,'meu porte é', planta_dois.porte,'sou decorativa e não sou de sol')
planta_dois.fotosintese(),
planta_dois.absorve_CO2(),
planta_dois.libera_O2()


print('Eu sou a', planta_tres.nome,'minha cor é',planta_tres.cor,'meu porte é', planta_tres.porte)
planta_tres.fotosintese()
planta_tres.absorve_CO2()
planta_tres.libera_O2()