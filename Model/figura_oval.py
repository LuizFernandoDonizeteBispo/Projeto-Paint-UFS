from Model.figura import Figura


class FiguraOval(Figura):

    def desenhar(self, canvas):#, tracejado=False):
        # recebe os pontos centrais (cx, cy) e dois raios, para criar a oval
        cx, cy, raioX, raioY = self.values
        canvas.create_oval(cx - raioX, cy - raioY, cx + raioX, cy + raioY, fill=self.cor_preench, outline=self.cor_bord)

    def atualizar(self, x, y):
        raioX = abs(self.values[0] - x)
        raioY = abs(self.values[1] - y)
        self.values = (self.values[0], self.values[1], raioX, raioY)  # Calcula dois raios, horizontal e vertical

    def incompleta(self):
        return self.values[2] == 0 or self.values[3] == 0
