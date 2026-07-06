from tkinter import *
from tkinter import ttk

class JanelaPaint():
    def __init__(self):
        self.root = Tk()  #isso daqui pelo visto tem que ficar ou no main ou no controller
        self.frame = Frame(self.root) #esse tambem

        # Widgets arranjados com Layout grid dentro de frame
        paddings = {'padx': 5, 'pady': 5} 

        # label
        self.label = ttk.Label(self.frame, text='Paint.v0,4')
        self.label.grid(column=0, row=0, sticky=W, **paddings)

        self.label_cor = ttk.Label(self.frame, text='Borda:')
        self.label_cor.grid(column=2, row=0, sticky=W, **paddings)

        self.label_preenchimento = ttk.Label(self.frame, text='Preenchimento:')
        self.label_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

        # option menu das figuras
        self.tipo_figura_var = StringVar(self.root) # Guarda o tipo de figura selecionado no option menu
        self.option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                     'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo')
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        # option menu de cor de borda
        self.tipo_bord_var = StringVar(self.root)
        self.option_menu_bord = ttk.OptionMenu(self.frame, self.tipo_bord_var,
                                          'Preto', 'Preto', 'Azul', 'Verde', 'Vermelho')
        self.option_menu_bord.grid(column=3, row=0, sticky=W, **paddings)

        #option menu cor de preenchiemnto
        self.tipo_preenchimento_var = StringVar(self.root)
        option_menu_preenchimento = ttk.OptionMenu(self.frame, self.tipo_preenchimento_var,
                                                     'Transparente', 'Transparente', 'Preto', 'Azul', 'Verde', 'Vermelho')
        option_menu_preenchimento.grid(column=5, row=0, sticky=W, **paddings)

        # Área de desenho
        self.canvas = Canvas(self.frame, bg='white', width=900, height=600)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

        self.frame.pack()


    def desenhar(self, figura):
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
