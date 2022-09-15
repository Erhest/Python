from random import randint

class Pessoa:
    def __init__(self, nome, nascimento):
        self.__codigo = self.__gerarCodigo()
        self.__nome = nome
        self.__nascimento = nascimento

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @staticmethod
    def __gerarCodigo():
        return randint(10000, 99999)    

    def exibirPessoa(self):
        print(f'Código: {self.codigo}\nNome: {self.nome}\nNascimento {self.nascimento}')

class Funcinario(Pessoa):    
    def __init__(self, nome, nascimento, veiculo):
        super().__init__(nome, nascimento)
        self.__matricula = self.__gerarMatricula()
        self.__veiculo = Veiculo        
        self.__dependentes = []

    @property
    def matricula(self):
        return self.__matricula

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def dependentes(self):
        for dep in self.__dependentes:
            print(f'Codigo: {dep.codigo}')
            print(f'NOME: {dep.nome}')
            print(f'Nacimento: {dep.nascimento}')
            print(f'Parentesco: {dep.parentesco}')

    @staticmethod
    def __gerarMatricula():
        return randint(100000, 999999)

    def addDepen(self, nome, nascimento, parentesco):
        dep = Dependentes(nome, nascimento, self.nome, parentesco)
        self.__dependentes.append(dep)

    def exibirFuncionario(self):
        super().exibirPessoa()
        print(f'Matricula: {self.matricula}')
        print('Dependentes')
        
        self.veiculo

class Dependentes(Pessoa):
    def __init__(self, nome, nascimento, parentesco):
        super().__init__(nome, nascimento)
        self.__funcionario = Funcinario
        self.__parentesco = parentesco

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def parentesco(self):
        return self.__parentesco

    def exibirDependente(self):
        super().exibirPessoa()
        print(f'Parentesco: {self.parentesco}')


class Veiculo:
    def __init__(self, modelo, placa):
        self.__codigo = self.__gerarCodigo()
        self.__modelo = modelo
        self.__placa = placa

    @property
    def codigo(self):
        return self.__codigo

    @property
    def modelo(self):
        return self.__modelo

    @property
    def placa(self):
        return self.__placa

    @staticmethod
    def __gerarCodigo():
        return randint(10, 99)

    def exibirVeiculo(self):
        print(f'Codigo: {self.codigo}\nModelo: {self.modelo}\nPlaca: {self.placa}')