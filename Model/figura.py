from dataclasses import dataclass
from abc import ABC, abstractmethod




@dataclass
class Figura(ABC):
    """
    Cada Figura recebe: Tipo, Valores, Cor_Bord e Cor_Preench
    """
    tipo: str
    values: list
    cor_bord: str
    cor_preench: str

    @abstractmethod
    def atualizar(self, x, y):
        pass

    @abstractmethod
    def incompleta(self):
        pass

    