from Dado import *

class Ficha:

    dado = Dado(6)
    color = ""
    posicion = 0

    def __init__(self, color):
        self.color = color
        self.posicion = 0
    
    def avanzar(self):
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.posicion)
    


