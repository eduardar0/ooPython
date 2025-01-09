class Fabricante:
    def __init__(self, fabricante):
        self._fabricante = fabricante

    @property
    def gFabricante(self):
        return self._fabricante