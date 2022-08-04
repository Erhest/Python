from conta import Conta
from cliente import Cliente

print('-' * 30)
print(' - - BANCO DOS BANCOS - - ')
print('-' * 30)


cliente1 = Cliente('Sayumi Souza', '123.456.789-11')
conta1 = Conta(cliente1, 1000)
# print(conta1.titular.nome)
# print(conta1.titular.cpf)

# print(cliente1.nome)
# print(cliente1.cpf)

# print(cliente1)
# print(conta1.titular)

if(conta1.sacar(500)):
    print('Saque Efetuado com sucesso!')
else:
    print('Saldo insuficiente!')


cliente2 = Cliente('Igor Oliveira', '987.654.321-94')
conta2 = Conta(cliente2, 1000, 3000.0)

if(not conta2.transferir(conta1, 150)):
    print('Saldo em conta insuficiente para realizar a tranferência!')
else:
    print('Transferência efetuada com sucesso.')

conta2.extrato()
conta1.extrato()

if conta1.transferir(conta2, 50):
    print('Trasferência realizada com sucesso!')
else:
    print('Saldo insuficiente!')

conta2.extrato()
conta1.extrato()
