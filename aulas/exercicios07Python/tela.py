from tkinter import *

'''
Casa
1 - Criar um conversor de temperatura
 1.1 - Converter celsius fahrenheit e kelvin (Converter  da  temperatura desejada para a outra temperatura desejada)
 1.2 - Tratar e evitar todos os possíveis erros

2 - Criar uma lista de compras
 2.1 - O programa deve adicionar um item desejado e toda vez que adicionar um item, exibir a lista atualizada
 2.2 - Podem ser inseridos inúmeros itens
 2.3 - Tratar e evitar todos os possíveis erros 
    exe
    1 - Arroz
     2 - Feijão
'''

tela = Tk()
tela.title('Conversor de temperaturas')
Label(tela, text='Conversor', font='Arial 18').grid(row=0, columnspan=4)
Label(tela, text='Temperatura').grid(row=1, columnspan=0, sticky=W)

temperatura = Entry(tela)
temperatura.grid(row=2, columnspan=3, sticky=W+E)

def limparCampo():
    temperatura.delete(0, END)
    temperatura.focus()
def celFah():
    # C x 1.8 + 32
    calc = float(temperatura.get()) * 1.8 + 32
    lblExibir.config(text=calc)
    limparCampo()

Button(tela, text='Celsius > Fahrenheit', command=celFah).grid(row=3, column=0)
Button(tela, text='Fahrenheit > Celsius').grid(row=3, column=1)
Button(tela, text='Celsius > Kelvin').grid(row=3, column=2)
Button(tela, text='Kelvin > Celsius').grid(row=4, column=0)
Button(tela, text='Kelvin > Fahrenheit').grid(row=4, column=1)
Button(tela, text='Fahrenheit > Kelvin').grid(row=4, column=2)

lblExibir = Label(tela, font='Arial 14')
lblExibir.pack()

tela.mainloop()