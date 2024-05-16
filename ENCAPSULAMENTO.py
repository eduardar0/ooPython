# python não te modificadores de acesso 
#public: nenhum underline no nome do metodo ou ...
#protected: dentro da classe e das subclasses(self._protected): um underline 
#private: .__ - somene dentro da classe que foi criado 


class Foo: 

    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

        def metodo_publico(self):
            return 'Metodo Publico'
        
        def _metodo_protected(self):
            print('_metodo_protected')
            return '_metodo_protected'
        
        def __metodo_private(self):
            print('__metodo_private')
            return '__metodo_private' #feito pra não acessar fora da classe 
#python muda o nome do metodo//atriburo 

