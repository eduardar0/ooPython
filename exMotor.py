class Motor:
    def __init__(self, motor):
        self._motor = motor 

    @property
    def gMotor(self):
        return self._motor