class Desenho:
    def __init__(self, janela_paint):
        self.figuras = []
        self.janela_paint = janela_paint
        self.selecionada_idx = -1

    def adiciona_figura(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras

    def reestruturar_figura(self, figuras_novas):
        self.figuras = figuras_novas

    def desenha_figuras(self):
        self.janela_paint.limpar()
        for figura in self.figuras:
            self.janela_paint.desenhar(figura)

    def redesenhar(self):
        self.desenha_figuras()

     # ---- Seleção ----

    def limpa_selecao(self):
        self.selecionada_idx = -1

    def seleciona(self, px, py):
        i = len(self.figuras) - 1
        while i >= 0 and not self.figuras[i].contem(px, py):
            i -= 1
        self.selecionada_idx = i

    def selecionada(self):
        if self.selecionada_idx >= 0:
            return self.figuras[self.selecionada_idx]
        else:
            return None

    def apaga_selecionada(self):
        if self.selecionada_idx != -1:
            self.figuras.pop(self.selecionada_idx)
            self.selecionada_idx = -1