from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

tela = Tk()
tela.geometry('300x500+1200+400')
tela.resizable(False, False)

# CheckBox = Caixa de seleção: pode selecionar várias opções

def salvar():
    print('Senha ', valorCheckBox.get())
valorCheckBox = IntVar()
checkSalvar = Checkbutton(tela, text='Deseja salvar a senha?', variable=valorCheckBox, command=salvar)
checkSalvar.select()
checkSalvar.pack()

# RadioButton: só pode selecionar uma opção

valorRadio = IntVar()
valorRadio2 = IntVar()
def radio():
    radio2.config(state=DISABLED)
    radio3.config(state=DISABLED)
    radio4.config(state=DISABLED)
    box.config(state=DISABLED)
    checkSalvar.config(state=DISABLED)
    listaDeAlunos.config(state=DISABLED)
    slide.config(state=DISABLED)

radio1 = Radiobutton(tela, text='Radio 1', variable=valorRadio, value=1, command=radio)
radio2 = Radiobutton(tela, text='Radio 2', variable=valorRadio, value=2)
radio3 = Radiobutton(tela, text='Radio 3', variable=valorRadio, value=3)
radio4 = Radiobutton(tela, text='Radio 4', variable=valorRadio, value=4)
radio3.select()
radio2.focus()
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

radioA = Radiobutton(tela, text='Rio de Janeiro', variable=valorRadio2, value=1)
radioB = Radiobutton(tela, text='São Paulo', variable=valorRadio2, value=2)
radioC = Radiobutton(tela, text='Minas Gerais', variable=valorRadio2, value=3)
radioC.select()
radioA.pack()
radioB.pack()
radioC.pack()

# Escala

def verValor(valor):
    print(valor)
slide = Scale(tela, from_=0.5, to=90.5, orient=HORIZONTAL, resolution=0.2, command=verValor)
slide.pack()

# ComboBox

alunos = ['Selecione o aluno: ', 'Aba', 'Akio','Davi', 'Kenji', 'Sayumi', 'Mateus']
box = Combobox(tela, values=alunos)
box.set(alunos[0]) # choice(alunos)
box.pack()


# Listas

listaDeAlunos = Listbox(tela)
#listaDeAlunos.insert(END, 'Valor 0')
for aluno in alunos:
    listaDeAlunos.insert(END, aluno)
listaDeAlunos.pack()
def retornaIndexSelecionadoNaLista():
    for index in listaDeAlunos.curselection():
        return index


def ver():
    print('Resultados')
    print('Checkbox: ', valorCheckBox.get())
    print('Radio: ', valorRadio.get())
    print('Slide: ', slide.get())
    if box.current() == 0:
        messagebox.showwarning(message='Selecione um aluno')
    else:
        print('Combo: ', box.get())
    print('Lista: ', listaDeAlunos.get(ACTIVE)) # listaDeAlunos.curselection()
    print('Lista Sselecionado: ')
    listaDeAlunos.delete(retornaIndexSelecionadoNaLista())
    listaDeAlunos.insert(END, 'Outro Aluno')

Button(tela, text='Ver', command=ver).pack()
tela.mainloop()