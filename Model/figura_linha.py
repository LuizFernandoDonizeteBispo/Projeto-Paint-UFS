from Model.figura import Figura


class FiguraLinha(Figura):
    def atualizar(self, x, y):
        x1, y1, _, _ = self.values
        self.values = (x1, y1, x, y)

    def incompleta(self):
        return self.values[0:2] == self.values[2:4]
    
    def contem(self, x, y):
        x1, y1, x2, y2 = self.values
        epsilon = 3
        return self.distancia_ponto_segmento(x1, y1, x2, y2, x, y) <= epsilon
    
    def mover(self, dx, dy):
        x1, y1, x2, y2 = self.values
        self.values = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)