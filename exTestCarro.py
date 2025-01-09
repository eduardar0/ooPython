from exCarro import Carro
from exMotor import Motor
from exFAbricante import Fabricante


carro = Carro('Etios', Motor('v12'), Fabricante('Toyota'))

print(f'Modelo: {carro.carro}')

print(f'Motor:{carro.motor.gMotor}') #agregacção

print(f'Fabricante: {carro.fabricante.gFabricante}')
print('Relação de agregação')