from Model.figura import Figura


class FiguraRabisco(Figura):
    def atualizar(self, x, y):
        self.values.append((x, y))

    def incompleta(self):
        return len(self.values) <= 1

    def contem(self, x, y):
        epsilon = 3
        for i in range(len(self.values) - 1):
            x1, y1 = self.values[i]
            x2, y2 = self.values[i + 1]
            if self.distancia_ponto_segmento(x1, y1, x2, y2, x, y) <= epsilon:
                return True
        return False
    
    def mover(self, dx, dy):
        self.values = [(x + dx, y + dy) for (x, y) in self.values]