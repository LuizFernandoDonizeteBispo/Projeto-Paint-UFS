from figura import Figura


class FiguraLinha(Figura):

    def desenhar(self, canvas, tracejado=False):
        x1, y1, x2, y2 = self.values
        canvas.create_line(x1, y1, x2, y2, fill=self.cor_bord)

    def atualizar(self, x, y):
        x1, y1, x2, y2 = self.values
        self.values = (x1, y1, x, y)

    def incompleta(self):
        return self.values[0:2] == self.values[2:4]
