from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('João')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever()
maquina.escrever()

#associação: 
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
escritor.ferramenta.lala()

#ENTENDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
