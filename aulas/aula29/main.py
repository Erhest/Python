from empresa import Chefe, Comissionado

c = Chefe()
c.adicionarEmpregado('    Gabriel Silva    ','Rua abc, Centro, São Paulo - SP')
c.adicionarSalario('2000.00')
c.adicionarSalario('345.00')
c.exibirEmpregado()
c.calcularSalario()

com = Comissionado(2000, 68, 12)
com.adicionarEmpregado('Calco P.', 'Rua asdp, 46, JOAIUSDF')
com.exibirEmpregado()
com.calcularSalario()
print(f'Salário: R$ {com.calcularSalario()}')