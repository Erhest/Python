from tkinter import *

telaInicial = Tk() # Instanciar
telaInicial['bg'] = '#cccccc' # cor do fundo
telaInicial.title('Home') # ALterar titulo

largura = 850 #altura do programa
altura = 650 #largura do programa
larguraUser = telaInicial.winfo_screenwidth()
alturaUser = telaInicial.winfo_screenheight()
larguraX = int((larguraUser - largura)/2)
alturaY = int(alturaUser - altura/2)
telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(True, True) #
telaInicial.minsize(850, 650)
telaInicial.maxsize(1920, 1080)
# telaInicial.state('zoomed') # 'zoomed' abre em tela cheia e 'iconic' abre a tela minimizado

def entrar():
    print('Olá, Mundo')
btnEntrar = Button(telaInicial, text='Entrar', command=entrar) # cria instância do botão
btnEntrar.pack()


telaInicial.mainloop() # abre a tela