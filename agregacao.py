#agregação é uma forma mais especializada eespecializada
#de associacao entre dois ou mais objetos
#cada objeto terá seu ciclo de vida independente 
#é um tipo de associação 
#relação fraca

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

class Carrinho:
    def __init__(self):
        self._produtos = []  #uma lista vazia

    def adicionar_produtos(self, *produtos): #recebe os produtos empacotados da classe produto
        for produto in produtos:
            self._produtos.append(produto) #adiciona os produtos pegados na classe Produto, e desempacota eles com um for, e coloca na lista _produtos

    def listar_produtos(self): 
        print()
        for produto in self._produtos:                #pega cada produto e preço na lista _produtos
            print(produto.nome, produto.preco)
        print()
    def total(self):
        return sum([produto.preco for produto in self._produtos])       #soma os precos dos produtos 


p1, p2 = Produto('Alface', 1.90), Produto('Azeite', 40)
carrinho = Carrinho()
carrinho.adicionar_produtos(p1,p2)
print('Produtos nos carrinho:')
carrinho.listar_produtos()
print('Total do valor: ',carrinho.total())




