from exMotor import Motor
from exFAbricante import Fabricante

class Carro:
    def __init__(self, carro, motor, fabricante):
        self.__carro = carro 
        self._motor = motor
        self._fabricante = fabricante

    @property
    def carro(self):
        return self.__carro
    
    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    





    