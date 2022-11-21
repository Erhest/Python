# .txt

'''

    r -> Ler
    w -> Escrever
    a -> Acrescentar
    r+ -> Ler e escraver

'''
caminho = './aula37'

# Escrever
'''
with open(f'{caminho}/teste.txt', 'w') as arq:
    arq.write('Primeiro arquivo externo')
'''

# Acrescentar
'''with open(f'{caminho}/teste.txt', 'a') as arq:
    arq.write('\n Linhas')'''

# Ler
'''
with open(f'{caminho}/teste.txt', 'r') as arq:
    texto = []
    for linha in arq:
        texto.append(linha)
    texto[0] = 'Linha 1 \n'
    print(texto)

for i in texto:
    print(i)
'''
'''
with open(f'{caminho}/teste.txt', 'w') as arq:
    for linha in arq:
        arq.write(linha)
'''
'''
# Ler e Acrescentar
with open(f'{caminho}/teste.txt', 'r+') as arq:
    for linha in arq:
        arq.write(linha)
'''
