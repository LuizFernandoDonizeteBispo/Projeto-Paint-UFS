from Model.figura import Figura


class FiguraRetangulo(Figura):

    def desenhar(self, canvas):#, tracejado=False):
        x1, y1, x2, y2 = self.values
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.cor_preench, outline=self.cor_bord)

    def atualizar(self, x, y):
        x1, y1, x2, y2 = self.values
        # a mesma coisa de atualizar linha porque o create_rectangle so precisa de dois pontos, assim como o create_line
        self.values = (x1, y1, x, y)

    def incompleta(self):
        x1, y1, x2, y2 = self.values
        return (x1, y1) == (x2, y2)
