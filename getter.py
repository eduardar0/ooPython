#@property é um metdo que se comporta como um atributo
#geralmente usada como: 
# um getter 
# para evitar quebra de codigo cliente 
# para habilitar um setter 
# para execultar ações ao obter um atributo 
#codigo cliente é o codigo que usa seu codigo


class Caneta: 
    def __init__(self, cor):
        self.cor_tampa = cor

    @property
    def cor(self): 
        print('PROPRETY')
        return self.cor_tampa
    
    @property 
    def cor_tampa_2(self):
        return 'Mesma cor da caneta'
    
    

    

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa_2)
