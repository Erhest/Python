class Funcionario:
    _valor_hora_cargo = [189.56, 86.05, 35.48]
    nome_cargo = ['Diretor', 'Gerente', 'Vendedor']

    def __init__(self, nome, cargo, horas_trabalhadas, salario):
        self.nome = nome
        self.cargo = cargo
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = salario

    def exibir_funcionario(self):
        print(f'NOME: {self.nome}')
        print(f'CARGO: {self.nome_cargo[self.cargo]}')
        # print(f'Cargo: {self.cargo}')
        print(f'HORAS TRABALHADAS: {self.horas_trabalhadas} horas')
        print(f'Salário: R${self.salario}')

    def adicionar_horas_trabalhadas(self):
        self.horas_trabalhadas += 1

    def calcular_salario(self):
        self.salario = self.horas_trabalhadas * self._valor_hora_cargo[self.cargo]

    @classmethod # Decorador
    def retornar_cargos(cls):
        return cls.nome_cargo


Funcionario._valor_hora_cargo = [10, 100, 250]
fun = Funcionario('Gabriel', 0, 10, 0)
fun.calcular_salario()
print(fun.exibir_funcionario())


# public int cargo
# protected int cargo = único '_' 'UNDERLINE' 
# private int cargo = duplo '__' 'UNDERLINE' quer dizer que é privado e não mexer 