class Humano:
    def __init__(self, nome):
        self.nome = nome

class Professor(Humano):    
    __materias = ['Matemática', 'Português', 'História', 'Quyímica', 'Física', 'Geografia']
    def __init__(self, nome, cpf, materia):
        super().__init__(nome)
        self.cpf = cpf
        self.materia = materia
    
    def listar_professor(self):
        print(f'{self.nome} \n{self.cpf} \n{self.__materias[self.materia]}')

p = Professor('Godofredo', 'xxx-xxx-xxx-xx', 0)
p.listar_professor()

class Aluno(Humano):
    def __init__(self, nome, ano_nascimento, ano_escolar):
        super().__init__(nome)
        self.ano_nascimento = ano_nascimento
        self.ano_escolar = ano_escolar

    def listar_aluno(self):
        print(f'Aluno: {self.nome} \nNascido em: {self.ano_nascimento} \nO aluno está no {self.ano_escolar}° ano/série')

    def alterar_ano_escolar(self, valor):
        self.ano_escolar = valor

    def idade_aluno(self, idade):
        self.idade = idade
        print(f'A idade do aluno é {self.idade}')

a = Aluno('Churi', 1994, 5)
a.listar_aluno()
a.alterar_ano_escolar(15)
a.listar_aluno()
a.idade_aluno(17)