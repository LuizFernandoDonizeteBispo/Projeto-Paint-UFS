from Model.figura import Figura
from View.janelaPaint import JanelaPaint
from View.menu import Menu
class Desenho:

    def __init__(self, canvas, Janela_paint, menu):
        self.canvas = canvas
        self.figura_atual = None
        self.menu = menu
        self.janela_paint = Janela_paint
        self.figuras = []
       


    def iniciar_figura(self, event):
        # Pega a cor da borda e converte usando o SeletorCor
        cor_b = self.menu.cor_bord_atual

        cor_p = self.menu.cor_preench_atual
      
        # Pega o tipo da forma selecionada
        tipo = self.menu.tipo_figura_var.get()

        self.figura_atual = Figura.criar(tipo,event.x, event.y, cor_b, cor_p)

        self.redesenhar()

    def atualizar_figura(self, event):
            if self.figura_atual is not None:
                self.figura_atual.atualizar(event.x, event.y)
                self.redesenhar()
    
    def incluir_figura(self, event):
        if not self.figura_atual.incompleta():
            self.figuras.append(self.figura_atual)
        self.redesenhar()

    def redesenhar(self):
        self.limpar()
        for fig in self.figuras:
            self.janela_paint.desenhar(fig)
        if self.figura_atual is not None:
            self.janela_paint.desenhar(self.figura_atual)