from View.seletor_cor import SeletorCor
from tkinter import Tk, Frame, Canvas, W
from Model import * 
from View.menu import Menu
#from Controller.Desenhar import Desenho


class Quadro:
    def __init__(self, root, tipo_preenchimento_var, tipo_cor_var, tipo_figura_var):      # Guarda o canvas que veio lá de fora
        self.root = root
        self.frame_canvas = Frame(root)
        self.frame_canvas.pack(fill="both", expand=True)
        

        paddings = {'padx': 5, 'pady': 5}

        self.canvas = Canvas(self.frame_canvas, bg='white',width=1200, height=800)  # Área de desenho
        self.canvas.grid(column=0, row=0, sticky="nsew", **paddings)
        
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)

        self.tipo_preenchimento_var = tipo_preenchimento_var
        self.tipo_cor_var = tipo_cor_var
        self.tipo_figura_var = tipo_figura_var
