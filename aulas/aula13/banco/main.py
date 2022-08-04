from conta import Conta

conta1 = Conta('1234', 'Akio', 1000, 5000)
print(conta1.numero)
print('Banco dos Bancos')

conta1.depositar(500)
conta1.sacar(300)
conta1.extrato()


conta2 = Conta('4321', 'Emerson', 1000, 3000)
conta2.extrato()
