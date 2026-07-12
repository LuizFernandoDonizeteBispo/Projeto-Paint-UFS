from Model.figura import Figura

class Armazem:
    def __init__(self):
        self.__figuras = []

    
    def incluir_figura(self, figura_atual):
        self.__figuras.append(figura_atual)
    def obter_figuras(self):
        return self.__figuras
    def reestruturar_figura(self, figuras_novas):
        self.__figuras = figuras_novas