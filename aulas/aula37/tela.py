from tkinter import *
from tkinter import messagebox


# Funções
def limparCampo():
    txtItem.delete(0, END)
    txtItem.focus()

def verificaEntry():
    if len(txtItem.get().strip()) > 0:
        return True
    False

def adicionar():
    if verificaEntry():
        lista.insert(END, txtItem.get().strip())
        itens.append(txtItem.get().strip())
    limparCampo()
    print(itens)

def remover():
    indice = retornaIndex()
    if not indice == None:
        lista.delete(indice)
        del itens[indice]
    print(itens)

def retornaIndex():
    for indice in lista.curselection():        
        return indice

def salvar():
    with open(f'{caminho}/listaDeCompras.txt', 'w') as arquivo:
        for i in itens:
            arquivo.write(i + '\n')
    messagebox.showinfo(message='Lista Salva com sucesso')
    
def carregarArquivo():
    with open(f'{caminho}/listaDeCompras.txt', 'r') as arq:
        for linha in arq:
            itens.append(str(linha).replace('\n', ''))
            lista.insert(END, linha)
    print(itens)

# Variaveis
itens = []
caminho = './aula37'

run = Tk()
run.geometry('300x400+1520+100')
run.title('Lista de Compras')
run.resizable(False, False)

Label(run, text='Lista de Compras', font='Calibri 24').pack()

txtItem = Entry(run)
txtItem.pack()

Button(run, text='ADICIONAR', font='Arial 14', command=adicionar). pack()

lista = Listbox(run)
Label(run, font='Calibri 10').pack()
lista.pack()

Button(run, text='Deletar', font='Arial 12', command=remover). pack()
Button(run, text='Salvar', font='Arial 12', command=salvar). pack()
carregarArquivo()

run.mainloop()