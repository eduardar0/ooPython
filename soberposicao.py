class A:
    atributo_a = 'valor a'
    def __init__(self, atributo):
        self.atributo = atributo 


    def metodo(self):
        print('A')

class B(A): #a calsse B herdou de A, mas s vai ter um metodo, pq ja ta definido na propria classe 
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        super(C, self).metodo()
        #A partir desso objeto, procure o proximo metodo....
        super(B, self).metodo()
        #A paritr de B, procura o proximo metodo, ou seja, B herda de A, então a saida será 'A
        print('C')

c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
print()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.metodo())