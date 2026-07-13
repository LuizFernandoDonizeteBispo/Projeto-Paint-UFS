from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_borracha import FiguraBorracha


@dataclass
class BorrachaFerramenta(Ferramenta):
    borracha_atual: FiguraBorracha = None

    def mouse_pressionado(self, event):
        self.borracha_atual = FiguraBorracha("borracha", [[event.x, event.y]], "", "")

    def mouse_arrastado(self, event):
        self.borracha_atual.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.borracha_atual)

    def mouse_solto(self, event):
        if not self.borracha_atual.incompleta():
            self.desenho.adiciona_figura(self.borracha_atual)
        self.desenho.desenha_figuras()