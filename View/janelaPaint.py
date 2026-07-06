from tkinter import *
from tkinter import ttk
from Model import *


class JanelaPaint():
    def __init__(self, canvas):
       self.canvas = canvas
    def desenhar(self, figura): #desenha figuras çiteralmente, esta no view porque mexe na parte visual. o controller e responsavel por puxar esse metodo
        tipo = figura.tipo
        coords = figura.values
        cor_bord = figura.cor_bord
        cor_preench = figura.cor_preench

        if tipo == 'linha':
            x1, y1, x2, y2 = coords
            self.canvas.create_line(x1, y1, x2, y2, fill= cor_preench, outline= cor_bord)
        
        elif tipo == 'retangulo':
            x1, y1, x2, y2 = coords
            self.canvas.create_rectangle(x1, y1, x2, y2, fill= cor_preench, outline= cor_bord)
        
        elif tipo == 'rabisco':
            pontos = [valor for ponto in coords for valor in ponto]
            self.canvas.create_line(*pontos, fill=cor_bord)
        
        elif tipo == 'circulo':
            cx, cy, raio = coords  # recebe os pontos centrais (cx, cy) e o raio e cria o circulo com base neles
            self.canvas.create_oval(cx - raio, cy - raio, cx + raio, cy + raio, fill=cor_preench, outline=cor_bord)

        elif tipo == 'oval':
            cx, cy, raioX, raioY = coords
            self.canvas.create_oval(cx - raioX, cy - raioY, cx + raioX, cy + raioY, fill=cor_preench, outline=cor_bord)
    
    def redesenhar(self):
        self.canvas.delete('all')

        for fig in self.figuras:
            fig.desenhar(self.canvas)

        if self.figura_atual is not None:
            self.figura_atual.desenhar(self.canvas, tracejado=True)
