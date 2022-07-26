# JOGO DA FORCA

from random import randint
# Criei uma lista de palavras pro jogo
# Lista ou Vetor
'''
continuar = 0

while(continuar):
    menu = int(input(' 1 - Jogar \n 2 - Sair \n R: '))
    if(menu == 1):
        print('Jogar')
    else:
        print('Tchau!!!!')
        continuar = False
'''
palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = randint(0, len(palavras)) # recebe um numero aleatório entre a quantidade total de palavras da lista
palavra_secreta = palavras[indice] # Palavra do jogo
tentativa = []  # Lista da Palavra _ _ _ _ _
chutes = [] # Lista de chutes errados -> W, S, F, G


for i in range(len(palavra_secreta)):
    tentativa.append('_')

print(palavra_secreta)
print(tentativa)

def exibirMsg(msg):
    print(msg)

def encontraLetra(chute):
    temLetra = False
    for i, letra in enumerate(palavra_secreta):
        if (chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra

def jogar():
    while(True):
        chute = input('Digite uma letra R: ')
        tentativas = 5
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        else:
            exibirMsg(f'Letra {chute} não encontrado')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas.')
            exibirMsg(tentativa)
        if(tentativas <= 0):
            exibirMsg('VOCÊ PERDEU; \n JOGUE NOVAMENTE! ')
            exibirMsg(f'A palavra secreta era {palavra_secreta.upper()} !!!')
            break

while(True):
    exibirMsg('**** JOGO DA FORCA ****')
    menu = int(input(' 1 - Jogar \n 2 - Sair \n R: '))
    if(menu == 1):
        jogar()
    else:
        exibirMsg('Tchauu!!!!')        
        break