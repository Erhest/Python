from random import randint

class Conta:

    def __init__(self, cliente, saldo, limite = 1000):
        self.numero = self.gerar_numero_aleatorio()
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def gerar_numero_aleatorio(self):
        numero = str(randint(10000, 99999)) + '-1'
        return numero

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        self.saldo += valor
        print('Deposito efetuado com sucesso')

    def extrato(self):
        print(f'{self.numero}\n{self.titular.nome}\nSaldo R$ {self.saldo} \nlimite R$ {self.limite}\n')
        
    def transferir(self, contaDestinatario, valor):
        transferiu = self.sacar(valor)
        if not transferiu:
            return False
        else:
            contaDestinatario.depositar(valor)
            return True