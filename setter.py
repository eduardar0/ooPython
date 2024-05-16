# precisa de property
# -como getter
# getter = obter valor 
# atributos que começam com unverline NOAO DEVEM SER USADOS fora da classe


class Caneta_dnv:
    def __init__(self, cor):
        self._cor = cor #usa como se fosse um private ou prtected 

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
        print('Estou no setter', valor)

    #continua funcionando como um atributo 

caneta = Caneta_dnv('Rosa')
print(caneta.cor)
caneta.cor = 'Azul'
print(caneta.cor)