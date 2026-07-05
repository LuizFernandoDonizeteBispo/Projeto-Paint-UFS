from View.seletor_cor import SeletorCor
from tkinter import Tk, Frame, Canvas, W
from Model import * 


class Quadro:
    def __init__(self, canvas, tipo_preenchimento_var, tipo_bord_var, string_var_figura):         
        self.canvas = canvas       # Guarda o canvas que veio lá de fora
        self.figura_atual = None   # Guarda a figura que está sendo feita na hora
        self.root = Tk()
        self.frame_canvas.pack()
        # Guarda as opções que o usuário escolheu nos menus
        self.tipo_preenchimento_var = tipo_preenchimento_var
        self.tipo_bord_var = tipo_bord_var
        self.string_var_figura = string_var_figura

        # Liga os movimentos do mouse com as funções da classe
        canvas.bind('<ButtonPress-1>', self.iniciar_figura)       # Clicou
        canvas.bind('<B1-Motion>', self.atualizar_figura)         # Arrastou
        canvas.bind('<ButtonRelease-1>', self.incluir_figura)     # Soltou

    def iniciar_figura(self, event):
        # Pega a cor da borda e converte usando o SeletorCor
        cor_b = SeletorCor.converter(self.tipo_bord_var.get())

        # Se for transparente deixa vazio, senão converte a cor
        if self.tipo_preenchimento_var.get() == 'Transparente':
            cor_p = ""
        else:
            cor_p = SeletorCor.converter(self.tipo_preenchimento_var.get())

        # Pega o tipo da forma selecionada
        tipo = self.string_var_figura.get()

        # Cria o objeto certo dependendo do que está selecionado no menu
        if tipo == 'Linha':
            self.figura_atual = FiguraLinha('linha', [event.x, event.y, event.x, event.y], cor_b, cor_p)
        elif tipo == 'Retangulo':
            self.figura_atual = FiguraRetangulo('retangulo', [event.x, event.y, event.x, event.y], cor_b, cor_p)
        elif tipo == 'Rabisco':
            self.figura_atual = FiguraRabisco('rabisco', [(event.x, event.y)], cor_b, cor_p)
        elif tipo == 'Circulo':
            self.figura_atual = FiguraCirculo('circulo', [event.x, event.y, 0], cor_b, cor_p)
        else:
            self.figura_atual = FiguraOval('oval', [event.x, event.y, 0, 0], cor_b, cor_p)

    def montar_quadro(self, root):
        frame_canvas = Frame(root)
        frame_canvas.pack()

        # Widgets arranjados com Layout grid dentro de frame
        paddings = {'padx': 5, 'pady': 5}
        canvas = Canvas(frame_canvas, bg='white', width=900, height=600)  # Área de desenho
        canvas.grid(column=0, row=0, sticky=W, **paddings)

    