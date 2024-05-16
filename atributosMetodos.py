#exemplo de codigo oo somente com uma classe com exemplo de uso de atributos e métodos 

class Camera:
    def __init__(self,nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja está filmando')
            return
        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if self.filmando:
            print(f'{self.nome} está parando de filmar')
            self.filmando = False
        else:
            print(f'{self.nome} ja parou de filmar')
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')

        else: 
            print(f'{self.nome} esta fotografando...')


    

    
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
print(c1.filmando)
print(c2.filmando)