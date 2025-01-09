#composição é uma especialidade da agregação
#uma classe depende da outra

class Cliente:
    def __init__(self, nome):
        self.nome = nome 
        self.enderecos = [] #lista de enderecos

    def inserir_enderecos(self, rua, numero): 
        # self.rua = rua
        # self.numero = numero
        self.enderecos.append(Endereco(rua, numero))#coloca na lista
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Av Brasil', 54)
cliente1.inserir_enderecos('Samambaia', 3)

# print(cliente1.enderecos[0].numero)
# print(cliente1.enderecos[1].numero)
cliente1.listar_enderecos()
del cliente1
print('AQUI TERMINA MEU CODIGO')