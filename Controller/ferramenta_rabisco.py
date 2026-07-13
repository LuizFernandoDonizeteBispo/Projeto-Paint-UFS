from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_rabisco import FiguraRabisco


@dataclass
class RabiscoFerramenta(Ferramenta):
    rabisco_atual: FiguraRabisco = None

    def mouse_pressionado(self, event):
        self.rabisco_atual = FiguraRabisco("rabisco", [[event.x, event.y]],
                                            self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.rabisco_atual.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.rabisco_atual)

    def mouse_solto(self, event):
        if not self.rabisco_atual.incompleta():
            self.desenho.adiciona_figura(self.rabisco_atual)
        self.desenho.desenha_figuras()