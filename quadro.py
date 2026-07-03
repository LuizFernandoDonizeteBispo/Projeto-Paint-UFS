from figura_linha import FiguraLinha
from figura_retangulo import FiguraRetangulo
from figura_rabisco import FiguraRabisco
from figura_circulo import FiguraCirculo
from figura_oval import FiguraOval
from seletor_cor import SeletorCor
from figura import Figura


class Quadro:
    def __init__(self, canvas, tipo_preenchimento_var, tipo_bord_var, string_var_figura):
        self.figuras = []          # Lista para guardar todos os desenhos prontos
        self.canvas = canvas       # Guarda o canvas que veio lá de fora
        self.figura_atual = None   # Guarda a figura que está sendo feita na hora

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

    def atualizar_figura(self, event):
        if self.figura_atual is not None:
            self.figura_atual.atualizar(event.x, event.y)
            self.redesenhar()

    def incluir_figura(self, event):
        if self.figura_atual is not None:
            if not self.figura_atual.incompleta():
                self.figuras.append(self.figura_atual)

            self.figura_atual = None
            self.redesenhar()

    def redesenhar(self):
        self.canvas.delete('all')

        for fig in self.figuras:
            fig.desenhar(self.canvas)

        if self.figura_atual is not None:
            self.figura_atual.desenhar(self.canvas, tracejado=True)
