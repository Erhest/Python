class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    def listar_cliente(self):
        print('---' * 10)
        print(f'CLIENTE: {self.__nome} CPF: {self.__cpf}')
        print('---' * 10)        

class Conta:
    def __init__(self, numero, saldo, cliente):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = cliente
        self.__historico = Historico()

    def listar_conta(self):
        print('---' * 15)
        print(f'CONTA: {self.__numero}')
        print(f'TITULAR: {self.__titular.nome} CPF: {self.__titular.cpf} ')
        print(f'SALDO: {self.__saldo}')
        print('---' * 15)

    def sacar(self, valor):
        if not self.verifica_saldo(valor):
            return print('Saldo insuficiente')
        self.__saldo -= valor
        self.__historico.adicionar_transacao(f'Saque de R$ {valor}')
        print(f'Saque de R$ {valor} foi realizado com sucesso')

    def depositar(self, valor):
        self.__saldo += valor
        self.__historico.adicionar_transacao(f'Depósito de R$ {valor}')
        print(f'Deposito de R$ {valor} foi realizado com sucesso')

    def transferir(self, conta, valor):
        self.__saldo -= valor
        conta.depositar(valor)
        self.__historico.adicionar_transacao(f'Transferência de R$ {valor}')
        print(f'Transferência de R$ {valor} foi realizada com sucesso')

    def transacoes(self):
        print('   ***** Transações *****    ')
        self.__historico.listar_historico()

    def verifica_saldo(self, valor):
        if valor > self.__saldo:
            return False
        return True

class Historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, transacao):
        self.__transacoes.append(transacao)

    def listar_historico(self):
        for transacao in self.__transacoes:
            print(f'{transacao}')