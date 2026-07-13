import pickle
from Model.desenho import Desenho

class Arquivos:

    def __init__(self, desenho : Desenho):
        self.desenho = desenho

    def salvar(self, caminho):
        with open(caminho, "wb") as arquivo:
            pickle.dump(self.desenho.obter_figuras(), arquivo, protocol=3)

    def abrir(self, caminho):
        with open(caminho, "rb") as arquivo:
            self.desenho.reestruturar_figura(pickle.load(arquivo))
        self.desenho.redesenhar()


