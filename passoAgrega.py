# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome 
#         self.preco = preco

# class Carrinho:
#     def __init__(self):
#         self._produtos = []

#     def adicionar_produtos(self, *produtos):
#         for produto in produtos:
#             self._produtos.append(produto)

#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()
#     def total(self):
#         return sum([produto.preco for produto in self._produtos])


# p1, p2 = Produto('Alface', 1.90), Produto('Azeite', 40)
# carrinho = Carrinho()
# carrinho.adicionar_produtos(p1,p2)
# print('Produtos nos carrinho:')
# carrinho.listar_produtos()
# print('Total do valor: ',carrinho.total())


