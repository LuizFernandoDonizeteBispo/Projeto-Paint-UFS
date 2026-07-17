from dataclasses import dataclass


@dataclass
class ControladorSelecao:
    desenho: object
    visao: object

    def __post_init__(self):
        root = self.visao.frame.winfo_toplevel()
        root.bind("<Delete>", self.apagar_selecionada)
        root.bind("<Right>", self.mover_para_frente)
        root.bind("<Left>", self.mover_para_tras)
        root.bind("<Up>", self.mover_para_topo)
        root.bind("<Down>", self.mover_para_fundo)

    def _atualiza_tela(self):
        self.desenho.janela_paint.desenha_figuras(self.desenho.obter_figuras(), self.desenho.obtem_indice_selecionado())

    def apagar_selecionada(self, event):
        self.desenho.apaga_selecionada()
        self._atualiza_tela()

    def mover_para_frente(self, event):
        self.desenho.move_para_frente()
        self._atualiza_tela()

    def mover_para_tras(self, event):
        self.desenho.move_para_tras()
        self._atualiza_tela()

    def mover_para_topo(self, event):
        self.desenho.move_para_topo()
        self._atualiza_tela()

    def mover_para_fundo(self, event):
        self.desenho.move_para_fundo()
        self._atualiza_tela()