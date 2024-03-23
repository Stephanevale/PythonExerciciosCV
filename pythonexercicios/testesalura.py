class Conta:
    def __init__(self, titular, numero, saldo, limite=1000):
      print('Inicializando uma conta')
      self.titular= titular
      self.numero= numero
      self.saldo= saldo
      self.limite= limite

    def deposita(self, valor):
      self.saldo += valor
    def saca(self, valor):
      self.saldo -= valor
    def extrato(self):
        print('numero: {} \nsaldo: {}' .format(self.numero, self.saldo))
    
    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo +=valor 

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite




c1= Conta('123-4', 'João', 120.0, 1000)
c2 = c1
print(c2.saldo)
c1.deposita(100.0)
print(c1.saldo)
c2.deposita(30)
print(c2.saldo)
print(c1.saldo) 

cliente = Cliente ('Maria', 'OLiveira', '1111-1')
minha_conta = Conta ('147-8', cliente, 120, 1000)

print(minha_conta.titular)
print(minha_conta.titular.nome)