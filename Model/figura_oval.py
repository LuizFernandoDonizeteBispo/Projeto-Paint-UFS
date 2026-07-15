from Model.figura import Figura


class FiguraOval(Figura):
    def atualizar(self, x, y):
        cx, cy, _, _ = self.values
        raioX = abs(cx - x)
        raioY = abs(cy - y)
        self.values = (cx, cy, raioX, raioY)

    def incompleta(self):
        return self.values[2] == 0 or self.values[3] == 0
    
    def contem(self, x, y):
        cx, cy, raioX, raioY = self.values
        if raioX == 0 or raioY == 0:
            return False
        valor = ((x - cx) / raioX) ** 2 + ((y - cy) / raioY) ** 2
        return valor <= 1
    
    def mover(self, dx, dy):
        cx, cy, raioX, raioY = self.values
        self.values = (cx + dx, cy + dy, raioX, raioY)
