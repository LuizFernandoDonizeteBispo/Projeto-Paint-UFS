from dataclasses import dataclass


@dataclass
class ControladorSelecao:
    desenho: object
    visao: object

    def __post_init__(self):
        root = self.visao.frame.winfo_toplevel()
        root.bind("<Delete>", self.apagar_selecionada)

    def apagar_selecionada(self, event):
        self.desenho.apaga_selecionada()
        self.desenho.desenha_figuras()