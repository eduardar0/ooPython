#tentando usar um dicionario json com codigo orientado a objetos

import json

caminho_arquivo = 'arq2.py'

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joana', 18)
p2 = Pessoa('Michele', 11)
p3 = Pessoa('Roberto', 50)
bd = [p1.__dict__, p2.__dict__,p3.__dict__]

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)