from tkinter import *

tela = Tk()
tela.title('Primeira aula de Grid')
tela.geometry('+1200+100')



lbl1 = Label(tela, width=30, justify='right', text='Label',)
lbl2 = Label(tela, width=30, justify='right', text='E-mail',)
lbl3 = Label(tela, width=30, justify='right', text='Senha',)

btnCadastrar = Button(tela, text='Cadatrar')

txtNome = Entry(tela)
txtEmail = Entry(tela)
txtSenha = Entry(tela, show='*')


lbl1.grid(row=0, column=0, sticky=W,)
lbl2.grid(row=1, column=0, sticky=W,)
lbl3.grid(row=2, column=0, sticky=W,)

txtNome.grid(row=0, column=1)
txtEmail.grid(row=1, column=1)
txtSenha.grid(row=2, column=1)

btnCadastrar.grid(columnspan=2, sticky='we')

tela.mainloop()

'''
        0 -> 0  |  1  |  2
        1 -> 0  |  1  |  2
        2 -> 0  |  1  |  2
        3 -> 0  |  1  |  2
        3 -> Button   |  2

'''

