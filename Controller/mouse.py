from View.quadro import Quadro
from Controller.Desenhar import Desenho

class Mouse:
    def __init__(self, canvas, desenho : Desenho):
        self.canvas = canvas
        self.desenho = desenho


        
    def mouse(self):    # Liga os movimentos do mouse com as funções da classe
        self.canvas.bind('<ButtonPress-1>', self.desenho.iniciar_figura)       # Clicou
        self.canvas.bind('<B1-Motion>', self.desenho.atualizar_figura)         # Arrastou
        self.canvas.bind('<ButtonRelease-1>', self.desenho.incluir_figura)     # Soltou


