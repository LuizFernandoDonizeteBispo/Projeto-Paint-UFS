from tkinter import *
from tkinter import ttk
from dataclasses import dataclass
from abc import ABC, abstractmethod

#####################################################################################################################################################

'''
Falta adicionar a classe Quadro(canvas)
class Quadro:
    def __init__(self, figura_nova):
    self.figura_nova = figura_nova

    def iniciar_figura_nova():
        pass
        
    def atualizar_figura_nova():
        pass

    def incluir_figura_nova ():
        pass

'''
#####################################################################################################################################################


class Menu:
    def __init__(self, root):
        self.frame = Frame(root) # dois frames separados
        self.frame.pack(fill=X)

        self.tipo_figura_var = StringVar(root)
        self.tipo_cor_var = StringVar(root)
        self.tipo_preenchimento_var = StringVar(root)

    def montar(self):
        paddings = {'padx': 5, 'pady': 5}

        label = ttk.Label(self.frame, text='Paint.v0,4')
        label.grid(column=0, row=0, sticky=W, **paddings)

        label_cor = ttk.Label(self.frame, text='Borda:')
        label_cor.grid(column=2, row=0, sticky=W, **paddings)

        label_preenchimento = ttk.Label(self.frame, text='Preenchimento:')
        label_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                      'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo')
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        option_menu_cor = ttk.OptionMenu(self.frame, self.tipo_cor_var,
                                          'Preto', 'Preto', 'Azul', 'Verde', 'Vermelho')
        option_menu_cor.grid(column=3, row=0, sticky=W, **paddings)

        option_menu_preenchimento = ttk.OptionMenu(self.frame, self.tipo_preenchimento_var,
                                                     'Transparente', 'Transparente', 'Preto', 'Azul', 'Verde', 'Vermelho')
        option_menu_preenchimento.grid(column=5, row=0, sticky=W, **paddings)


#####################################################################################################################################################
#classe super
@dataclass
class Figura:
    """
    Cada Figura recebe:  Tipo, Valores, Cor_Bord e Cor_Preench
    Terá todos os metódos de desenhar uma figura
    """
    tipo: str
    values: list
    cor_bord: str
    cor_preench: str


    def desenhar(self, canvas, tracejado=False): # Juntei as duas funçoes desenhar() em 1, puxando o canvas(chamar os create_) e recebendo o dash ou nao. <-- vai ser na Classe Quadro
        raise NotImplementedError("Subclasse deve implementar o método desenhar") # Impede de utilizar o metodo diretamente (Será usado atravez do Quadro)


    def atualizar(self, x, y): # Metodo para atualizar a figura conforme o mouse se move
        raise NotImplementedError("Subclasse deve implementar o método atualizar")


    def incompleta(self): # Metodo para o caso de uma figura incompleta ser feita
        raise NotImplementedError("Subclasse deve implementar o método incompleta")


#####################################################################################################################################################

class FiguraLinha(Figura):


    def desenhar(self, canvas, tracejado=False): 
        x1, y1, x2, y2 = self.values
        canvas.create_line(x1, y1, x2, y2, fill=self.cor_preench)


    def atualizar(self, x, y):
        x1, y1, x2, y2 = self.values
        self.values = (x1, y1, x, y)


    def incompleta(self):
        return self.values[0:2] == self.values[2:4]


#####################################################################################################################################################

class FiguraRabisco(Figura):


    def desenhar(self, canvas, tracejado=False):
        canvas.create_line(self.values, fill=self.cor_preench)


    def atualizar(self, x, y):
        self.values.append((x, y))


    def incompleta(self):
        return len(self.values) <= 1
        
#####################################################################################################################################################

class FiguraRetangulo(Figura):


    def desenhar(self, canvas, tracejado=False):
        x1, y1, x2, y2 = self.values
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.cor_preench, outline=self.cor_bord)


    def atualizar(self, x, y):
        x1, y1, x2, y2 = self.values
        #a mesma coisa de atualizar linha porque o create_rectangle so precisa de dois pontos, assim como o create_line
        self.values = (x1, y1, x, y)


    def incompleta(self):
        x1, y1, x2, y2 = self.values
        return (x1, y1) == (x2, y2)


#####################################################################################################################################################

class FiguraCirculo(Figura):


    def desenhar(self, canvas, tracejado=False):
        cx, cy, raio = self.values # recebe os pontos centrais (cx, cy) e o raio e cria o circulo com base neles
        canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, fill=self.cor_preench, outline=self.cor_bord)


    def atualizar(self, x, y):
        self.raio = ( (self.values[0] - x)**2 + (self.values[1] - y)**2 ) ** 0.5  # Calcula o raio para o circulo
        self.values = (self.values[0], self.values[1], self.raio)  # figura_nova Recebe o nome, os dois primeiros pontos e o raio calculado)


    def incompleta(self):
        return self.values[2] == 0

#####################################################################################################################################################

class FiguraOval(Figura):


    def desenhar(self, canvas, tracejado=False):
            # recebe os pontos centrais (cx, cy) e dois raios, para criar a oval
                cx, cy, raioX, raioY = self.values
                canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, fill=self.cor_preench, outline=self.cor_bord)   

    def atualizar(self, x, y):
        raioX = abs(self.values[0] - x)
        raioY = abs(self.values[1] - y)
        self.values =  (self.values[0], self.values[1], raioX, raioY)     # Calcula dois raios, horizontal e vertical


    def incompleta(self):
        return self.values[2] == 0 or self.values[3] == 0

#####################################################################################################################################################


class SeletorCor:


   _CORES = {
       "Preto": "black",
       "Vermelho": "red",
       "Verde": "green",
       "Azul": "blue",
       "Amarelo": "yellow",
       "Cinza": "gray",
       "Roxo": "purple",
   }
   @staticmethod
   def converter(nome):
       return SeletorCor._CORES.get(nome, "black")


cor_bord = SeletorCor.converter(tipo_cor_var.get())
cor_preench = SeletorCor.converter(tipo_preenchimento_var.get())


#####################################################################################################################################################


#******* MAIN *******#


root = Tk()


frame_canvas = Frame(root)
frame_canvas.pack()

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 
canvas = Canvas(frame_canvas, bg='white', width=900, height=600) # Área de desenho
canvas.grid(column=0, row=0, sticky=W, **paddings)


menu = Menu(root)
menu.montar()


quadro = Quadro(canvas, menu.tipo_figura_var, menu.tipo_cor_var, menu.tipo_preenchimento_var)


root.mainloop()
