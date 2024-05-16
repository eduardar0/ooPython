#geralmente temos uma associação quando um objeto 
# tem um atributo que referencia outro objeto

class Escritor: 
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

        @property 
        def ferramenta(self): 
            return self._ferramenta 
        
        @ferramenta.setter
        def ferramenta(self, valor):
            self._ferramenta = valor

class Ferramenta: 
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"{self.nome} está escrevendo"

escritor = Escritor('Luiz')

caneta = Ferramenta('Caneta Bic')

escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())