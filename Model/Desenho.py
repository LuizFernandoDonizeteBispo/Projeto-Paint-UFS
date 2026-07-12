class Desenho:
    def __init__(self, janela_paint):
        self.figuras = []
        self.janela_paint = janela_paint

    def adiciona_figura(self, figura):
        self.figuras.append(figura)

    def desenha_figuras(self):
        self.janela_paint.limpar()
        for figura in self.figuras:
            self.janela_paint.desenhar(figura)