from dataclasses import dataclass
from Controller.Ferramenta import Ferramenta


@dataclass
class SelecaoFerramenta(Ferramenta):
    ult_x: int = 0
    ult_y: int = 0

    def mouse_pressionado(self, event):
        self.ult_x = event.x
        self.ult_y = event.y
        self.desenho.limpa_selecao()
        self.desenho.seleciona(event.x, event.y)
        self.desenho.desenha_figuras()
        self.desenho.janela_paint.canvas.focus_set()  

    def mouse_arrastado(self, event):
        fig_sel = self.desenho.selecionada()
        if fig_sel is not None:
            fig_sel.mover(event.x - self.ult_x, event.y - self.ult_y)
            self.ult_x = event.x
            self.ult_y = event.y
            self.desenho.desenha_figuras()

    def mouse_solto(self, event):
        pass