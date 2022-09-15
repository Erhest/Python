from banco import Cliente, Conta, Historico

c1 = Cliente('Mateus F.', '111.222.333-44')
cc1 = Conta(4321, 100, c1)



c2 = Cliente('Igor F.', '555.666.777-88')
cc2 = Conta(1234, 400, c2)


cc1.transferir(cc2, 1000)
cc1.listar_conta()
cc2.listar_conta()

cc1.transacoes()
