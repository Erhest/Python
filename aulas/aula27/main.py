from funcionario import Gerente, Vendedor
from endereco import *

est1 = Estado('Estado 1', 'SG')
cid1 = Cidade('Cidade 1', est1)
end1 = Endereco('Rua do End 1', 12, 'Bairro Nobre', '12365-789', cid1)


g = Gerente('Nome Completo', '15/02/1995', '123.456.789-00', end1)
print(g.endereco.cidade.estado.sigla)
g.endereco.listar()
g.getSalario()


est2 = Estado('São Paulo', 'SP')
cid2 = Cidade('São Paulo', est2)
end2 = Endereco('AV Paulista', 19, 'Centro', '12365-456', cid2)

v = Vendedor('Vendedor Nome COMpleto', '05/11/1987', '144.789.652-85', end2)
v.endereco.listar()
print(round(v.getSalario(), 2))
print(v.equipe)