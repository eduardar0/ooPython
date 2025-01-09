

class MinhaString(str):
    def upper(self):
        print('Chamou Upper')
        retorno = super().upper()
        print('Saiu do Upper')

        return retorno  #pega o metodo da superclasse
    



nome = MinhaString('Luiz')
print(nome.upper())

