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

indice = '' # recebe um numero aleatório entre a quantidade total de palavras da lista
palavra_secreta = [] # Palavra do jogo
tentativa = []  # Lista da Palavra _ _ _ _ _
chutes = [] # Lista de chutes errados -> W, S, F, G


def exibirMsg(msg):
    print(msg)

def encontraLetra(chute):
    temLetra = False
    for i, letra in enumerate(palavra_secreta):
        if(chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra

def jogar():
    tentativas = 5
    while(True):
        chute = input('Digite uma letra R: ')        
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        else:
            exibirMsg(f'Letra {chute} não encontrado')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas.')
            exibirMsg(tentativa)
        if(verificaVitoria()):
            exibirMsg('Parabéns você VENCEU!!!')
            break
        if(tentativas <= 0):
            exibirMsg('VOCÊ PERDEU; \n JOGUE NOVAMENTE! ')
            exibirMsg(f'A palavra secreta era {palavra_secreta.upper()} !!!')
            break

def verificaVitoria():
    if('_' in tentativa):
        return False
    else:
        return True

def iniciaJogo():
    global indice
    indice = randint(0, len(palavras)) # recebe um numero aleatório entre a quantidade total de palavras da lista
    global palavra_secreta
    palavra_secreta = palavras[indice] # Palavra do jogo
    global tentativa
    tentativa = []  # Lista da Palavra _ _ _ _ _
    global chutes
    chutes = [] # Lista de chutes errados -> W, S, F, G

    for i in range(len(palavra_secreta)):
        tentativa.append('_')
        
def escolha():
    while(True):
        iniciaJogo()
        exibirMsg('**** JOGO DA FORCA ****')
        menu = int(input(' 1 - Jogar \n 2 - Sair \n R: '))
        if(menu == 1):
            jogar()
        else:
            exibirMsg('Tchauu!!!!')        
            break
escolha()