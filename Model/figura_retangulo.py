from Model.figura import Figura

class FiguraRetangulo(Figura):
    def atualizar(self, x, y):
        x1, y1, _, _ = self.values
        self.values = (x1, y1, x, y)

    def incompleta(self):
        x1, y1, x2, y2 = self.values
        return (x1, y1) == (x2, y2)

    def contem(self, x, y):
        x1, y1, x2, y2 = self.values
        esquerda, direita = min(x1, x2), max(x1, x2)
        topo, base = min(y1, y2), max(y1, y2)
        return esquerda <= x <= direita and topo <= y <= base
    
    def mover(self, dx, dy):
        x1, y1, x2, y2 = self.values
        self.values = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)