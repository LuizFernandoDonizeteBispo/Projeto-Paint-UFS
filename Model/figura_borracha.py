from Model.figura import Figura


class FiguraBorracha(Figura):
    def desenhar(self, canvas, tracejado=False):
        canvas.create_line(self.values, fill="white", width=10, capstyle="round", joinstyle="round")

    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1

    def mover(self, dx, dy):
        self.values = [(x + dx, y + dy) for (x, y) in self.values]

    def contem(self, x, y):
        epsilon = 5
        for i in range(len(self.values) - 1):
            x1, y1 = self.values[i]
            x2, y2 = self.values[i + 1]
            if self.distancia_ponto_segmento(x1, y1, x2, y2, x, y) <= epsilon:
                return True
        return False