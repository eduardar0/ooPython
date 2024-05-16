class Conection: 
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        self.user = user

    def set_password(self, password):
        self.password = password
        #self -METODO DE INSTANCIA

    @classmethod
    def create_with_auth(cls, user, password ):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)


c1 = Conection.create_with_auth('Luiz', '123')
print(c1.user)
# c1.set_user('Luiz')
# c1.set_password('123')
print(c1.user)
print(c1.password)
print(Conection.log('Essa é a mensagem de Log'))

