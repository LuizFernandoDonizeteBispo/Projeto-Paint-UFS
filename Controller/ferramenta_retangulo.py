from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta
from Model.figura_retangulo import FiguraRetangulo


@dataclass
class RetanguloFerramenta(Ferramenta):
    retangulo_novo: FiguraRetangulo = None

    def mouse_pressionado(self, event):
        self.retangulo_novo = FiguraRetangulo("retangulo", [event.x, event.y, event.x, event.y],
                                               self.visao.cor_bord_atual, self.visao.cor_preench_atual)

    def mouse_arrastado(self, event):
        self.retangulo_novo.atualizar(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.desenhar(self.retangulo_novo)

    def mouse_solto(self, event):
        if not self.retangulo_novo.incompleta():
            self.desenho.adiciona_figura(self.retangulo_novo)
        self.desenho.desenha_figuras()