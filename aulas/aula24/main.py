from classe import *

agua = Produto('Água 500ml', 2.50)
cerveja = Produto('Skola 350ml', 4.00)
refrigerante = Produto('Guaraná 350ml', 3.50)
biscoito = Produto('Biscoito', 6.25)


cc = CarrinhoCompra()
cc.adicionar_produto(agua)
cc.adicionar_produto(cerveja)
cc.adicionar_produto(refrigerante)
cc.adicionar_produto(biscoito)
cc.finalizar_compra()
