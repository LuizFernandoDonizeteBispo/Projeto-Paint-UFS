from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_circulo import FiguraCirculo


@dataclass
class CirculoFerramenta(Ferramenta):
    circulo_novo: FiguraCirculo = None

    def mouse_pressionado(self, event):
        self.circulo_novo = FiguraCirculo("circulo", [event.x, event.y, 0],
                                           self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.circulo_novo.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.circulo_novo)

    def mouse_solto(self, event):
        if not self.circulo_novo.incompleta():
            self.desenho.adiciona_figura(self.circulo_novo)
        self.desenho.desenha_figuras()