from dataclasses import dataclass
from abc import ABC, abstractmethod
#from figura_circulo import FiguraCirculo
#from figura_oval import FiguraOval
#from figura_linha import FiguraLinha
#from figura_rabisco import FiguraRabisco
#from figura_retangulo import FiguraRetangulo


@dataclass
class Figura(ABC):
    """
    Cada Figura recebe:  Tipo, Valores, Cor_Bord e Cor_Preench
    Terá todos os metódos de desenhar uma figura
    """
    tipo: str
    values: list
    cor_bord: str
    cor_preench: str

    @abstractmethod
    def desenhar(self, canvas, tracejado=False):
        """Desenha a figura no canvas recebido."""
        raise NotImplementedError("Subclasse deve implementar o método desenhar")

    @abstractmethod
    def atualizar(self, x, y):
        """Atualiza a figura conforme o mouse se move."""
        raise NotImplementedError("Subclasse deve implementar o método atualizar")

    @abstractmethod
    def incompleta(self):
        """Indica se a figura ainda não tem tamanho válido para ser salva."""
        raise NotImplementedError("Subclasse deve implementar o método incompleta")
