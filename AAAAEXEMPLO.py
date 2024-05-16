#exemplo de estrutura de classe 
class Carro:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} é veloz')
#self é convenção

fusca = Carro('fusca')
fusca.acelerar()
print(fusca.nome)