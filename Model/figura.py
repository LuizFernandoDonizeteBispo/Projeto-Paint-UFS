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

    @staticmethod
    def criar(tipo, x, y, cor_bord, cor_preench):
        from Model.figura_linha import FiguraLinha
        from Model.figura_circulo import FiguraCirculo
        from Model.figura_retangulo import FiguraRetangulo
        from Model.figura_oval import FiguraOval
        from Model.figura_rabisco import FiguraRabisco
        from Model.figura_borracha import FiguraBorracha

        if tipo == "Linha":
            return FiguraLinha("linha", [x, y, x, y], cor_bord, cor_preench)
        elif tipo == "Circulo":
            return FiguraCirculo("circulo", [x, y, 0], cor_bord, cor_preench)
        elif tipo == "Retangulo":
            return FiguraRetangulo("retangulo", [x, y, x, y], cor_bord, cor_preench)
        elif tipo == "Oval":
            return FiguraOval("oval", [x, y, 0, 0], cor_bord, cor_preench)
        elif tipo == "Borracha":
            return FiguraBorracha("borracha", [[x, y]], "", "")
        else:  # Rabisco
            return FiguraRabisco("rabisco", [[x, y]], cor_bord, cor_preench)
