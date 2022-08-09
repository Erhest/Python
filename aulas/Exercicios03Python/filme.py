class filmes:
    def __init__(self, filme, alugar, devolver, tema):
        self.self = filme(self)
        self.alugar = alugar
        self.devolver = devolver
        self.tema = tema

    def filme(self):
        self.filme = input('Coloque o nome do filme: ')
        return self.filme

    def alugado(alugar):
        if alugar == True:
            print('Filme ja está alugado.')
        else: 
            print('Filme pode ser alugado.')

    def devolver(devolver):
        if devolver == True:
            print('Filme foi devolvido com sucesso!')
        else: 
            print('Filme não pode ser devolvido!')
