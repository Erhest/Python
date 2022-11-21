#from tkinter import *
import tkinter

def verificaEntry():
    if len(txtTelefone.get().strip()) > 0:
        return True
    False

def addTel():
    if verificaEntry():
        ltsTelefone.insert(tkinter.END, txtTelefone.get().strip())
        telefones.append(txtTelefone.get().strip())
    print(telefones)
    funcaoSalvar()

def funcaoSalvar():
    with open(f'{caminho}/chamadasPerdidas.txt', 'w', encoding='utf-8') as arquivo:
        for i in telefones:
            arquivo.write(i + '; ')
    tkinter.message.showinfo(message='Lista Salva com sucesso')

def carregarChamadas():
    with open(f'{caminho}/listaDeCompras.txt', 'r') as arq:
        for linha in arq:
            telefones.append(linha.split('; '))
        for i in telefones:
            ltsTelefone.insert(tkinter.END, i)
    print(telefones)

caminho = './exercicios08Python'
telefones = []
run = tkinter.Tk()
run.geometry('300x500+1490+100')
run.title('Chamadas perdidas')
run.resizable(False, False)

txtTelefone = tkinter.Entry(run, font='Arial 25')
txtTelefone.place(x=10, y=10, width=280, height=50)
tkinter.Button(run, text='Adicionar', command=addTel).place(x=10, y=70, width=280, height=50)
ltsTelefone = tkinter.Listbox(run)
ltsTelefone.place(x=10, y=140, width=280, height=250)
carregarChamadas()

run.mainloop()