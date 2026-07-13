from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_quadrado import FiguraQuadrado


@dataclass
class QuadradoFerramenta(Ferramenta):
    quadrado_novo: FiguraQuadrado = None

    def mouse_pressionado(self, event):
        self.quadrado_novo = FiguraQuadrado("quadrado", [event.x, event.y, event.x, event.y],
                                               self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.quadrado_novo.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.quadrado_novo)

    def mouse_solto(self, event):
        if not self.quadrado_novo.incompleta():
            self.desenho.adiciona_figura(self.quadrado_novo)
        self.desenho.desenha_figuras()