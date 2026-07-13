from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_linha import FiguraLinha


@dataclass
class LinhaFerramenta(Ferramenta):
    linha_nova: FiguraLinha = None

    def mouse_pressionado(self, event):
        self.linha_nova = FiguraLinha("linha", [event.x, event.y, event.x, event.y],
                                       self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.linha_nova.values = [self.linha_nova.values[0], self.linha_nova.values[1], event.x, event.y]
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.linha_nova)

    def mouse_solto(self, event):
        if not self.linha_nova.incompleta():
            self.desenho.adiciona_figura(self.linha_nova)
        self.desenho.desenha_figuras()