from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_oval import FiguraOval



@dataclass
class OvalFerramenta(Ferramenta):
    oval_novo: FiguraOval = None

    def mouse_pressionado(self, event):
        self.oval_novo = FiguraOval("oval", [event.x, event.y, 0, 0],
                                     self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.oval_novo.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.oval_novo)

    def mouse_solto(self, event):
        if not self.oval_novo.incompleta():
            self.desenho.adiciona_figura(self.oval_novo)
        self.desenho.desenha_figuras()