from Model.armazem_figuras import Armazem
import pickle
from .Desenhar import Desenho

class Arquivos:

    def __init__(self, armazem, desenho : Desenho):
        self.armazem = armazem
        self.desenho = desenho

    def salvar(self, caminho):
        with open(caminho, "wb") as arquivo:
            pickle.dump(self.armazem.obter_figuras(), arquivo, protocol=3)

    def abrir(self, caminho):
        with open(caminho, "rb") as arquivo:
            self.armazem.reestruturar_figura(pickle.load(arquivo))
        self.desenho.redesenhar()


