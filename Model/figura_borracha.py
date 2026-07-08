from Model.figura import Figura


class Borracha(Figura):
    def desenhar(self, canvas, tracejado=False):
        pontos = [valor for ponto in self.values for valor in ponto]
        canvas.create_line(*pontos, fill="white", width=10, capstyle="round", joinstyle="round")

    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1