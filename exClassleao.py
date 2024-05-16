class Animal:
    def __init__(self,nome):
        self.nome = nome

    def acao(self):
        return f'{self.nome} está execultando'
    
    def comendo(self, alimento):
        return f'{self.acao()} um {alimento} para comer'


leao = Animal('leão')
#print(leao.acao())
print(leao.comendo('zebra'))
        