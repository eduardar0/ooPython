#Polimorfismo é o principio que permite que classes derivadas 
#de uma mesma superclasse tenham metodos iguais (com mesma assinatura), 
#mas com comportamentos difrentes.
#assinatra de metodo = mesmo nome e qualidade  
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

class PessoaA:
    def se_apresentar(self) ->None:
        pass
        print('Ola sou a pessoa A')

class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse metodo')

    
class PessoaC(PessoaB):
    def __init__(self):
        super().__init__()

pessoa1 = PessoaA()
pessoa1.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()