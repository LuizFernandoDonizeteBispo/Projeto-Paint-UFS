from Model.figura import Figura

class FiguraCirculo(Figura):


#    def desenhar(self, canvas):#, tracejado=False):
#        cx, cy, raio = self.values  # recebe os pontos centrais (cx, cy) e o raio e cria o circulo com base neles
#        canvas.create_oval(cx - raio, cy - raio, cx + raio, cy + raio, fill=self.cor_preench, outline=self.cor_bord)

    def circulo(self, x, y):
        cx, cy, x, y, raio = self.values
        self.raio = ((self.values[0] - x) ** 2 + (self.values[1] - y) ** 2) ** 0.5


#    def atualizar(self, x, y):
#        self.raio = ((self.values[0] - x) ** 2 + (self.values[1] - y) ** 2) ** 0.5  # Calcula o raio para o circulo
#        self.values = (self.values[0], self.values[1], self.raio)  # figura_nova Recebe o nome, os dois primeiros pontos e o raio calculado)


    def incompleta(self):
        return self.values[2] == 0
