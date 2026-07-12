from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Ferramenta(ABC):
    visao: object
    desenho: object

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    @abstractmethod
    def mouse_arrastado(self, event):
        pass

    @abstractmethod
    def mouse_solto(self, event):
        pass