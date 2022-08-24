from random import randint


class Produto:
    variavelDeClasse = 'Produto'
    def __init__(self):
        self._codigo = self.__gerarCodigoProduto()
        self._nome = ''
        self._preco = 0

    #       METODO ASSESSORES
    #          GET / GETTERS

    @property # DECORARDOR
    def nome(self):
        return self._nome + 'Sobrenome'

    @property
    def preco(self):        
        return f'R$ {self._preco}'
        
    # METODO MODIFICADORES
    #     SET / SETTERS

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    def listarProduto(self):
        print('-' * 20)
        print('Produto')
        print(f' Codigo: {self._codigo} \n Nome: {self._nome} \n R$: {self._preco}')
        print('-' * 20)

    @classmethod
    def metododeClasse(cls):
        print(cls.variavelDeClasse)

    @staticmethod
    def __gerarCodigoProduto():
        return randint(10000, 99999)

    @preco.setter
    def preco(self, valor):
        print(valor)
        valor = valor.replace('R$', '')
        valor = valor.replace(',', '.')
        valor = valor.strip()
        if valor.replace('.', '').isnumeric():
            self._preco = float(valor)
        else:
            self_preco = 0
            print('ERROR: Digite um valor válido.')

    def verificaValorVenda(self, qnt):
        return print(self._preco * qnt)

p = Produto()

print('==== Mercadinho Dinho ====')
while(True):
    menu = input('1 - Cadastrar produto \n2 - Listar produto \n3 - Sair \nR: ')
    if(menu == '1'):
        p.nome = input("Digite o nome do produto: ")
        while(True):
            p.preco = input('Digite o preço do produto: ')
            if not p.preco == 'R$ 0':
                print('Produto cadastrado com sucesso!')
                break
    elif menu == '2':
        p.listarProduto()
    else:
        print('Finalizando programa........')
        break

p.nome = input('Digite o nome do produto: ')
p.preco = (input('Digite o preço do produto: '))
p.listarProduto()
