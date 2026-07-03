from figura import Figura


class FiguraRabisco(Figura):

    def desenhar(self, canvas, tracejado=False):
        canvas.create_line(self.values, fill=self.cor_bord)

    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1
