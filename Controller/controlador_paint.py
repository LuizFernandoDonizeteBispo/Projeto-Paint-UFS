from dataclasses import dataclass
from Model.Desenho import Desenho
from Controller.ferramenta_linha import LinhaFerramenta
from Controller.ferramenta_circulo import CirculoFerramenta
from Controller.ferramenta_retangulo import RetanguloFerramenta
from Controller.ferramenta_oval import OvalFerramenta
from Controller.ferramenta_rabisco import RabiscoFerramenta
from Controller.ferramenta_borracha import BorrachaFerramenta


@dataclass
class ControladorPaint:
    desenho: Desenho
    visao: object

    def __post_init__(self):
        self.ferramentas = {
            "Linha": LinhaFerramenta(self.visao, self.desenho),
            "Circulo": CirculoFerramenta(self.visao, self.desenho),
            "Retangulo": RetanguloFerramenta(self.visao, self.desenho),
            "Oval": OvalFerramenta(self.visao, self.desenho),
            "Rabisco": RabiscoFerramenta(self.visao, self.desenho),
            "Borracha": BorrachaFerramenta(self.visao, self.desenho),
        }
        self.ferramenta_atual = self.ferramentas["Linha"]

        self.visao.tipo_figura_var.trace('w', self.muda_ferramenta)

        self.desenho.janela_paint.ativar_mouse(
            self.mouse_pressionado,
            self.mouse_arrastado,
            self.mouse_solto
        )

    def muda_ferramenta(self, *args):
        tipo = self.visao.tipo_figura_var.get()
        self.ferramenta_atual = self.ferramentas[tipo]

    def mouse_pressionado(self, event):
        self.ferramenta_atual.mouse_pressionado(event)

    def mouse_arrastado(self, event):
        self.ferramenta_atual.mouse_arrastado(event)

    def mouse_solto(self, event):
        self.ferramenta_atual.mouse_solto(event)