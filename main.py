from tkinter import *
from tkinter import ttk
from dataclasses import dataclass
from abc import ABC, abstractmethod

#####################################################################################################################################################

'''
Falta adicionar a classe Menu(option_menu)
class Menu
    nao pensei o que usar nessa classe, pensem ai


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


""" # Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova

    cor_borda() 
    cor_preenchimento()  

    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_preench)

    elif tipo_figura_var.get() == 'Circulo':
        figura_nova = ('circulo', (event.x, event.y, 0))
    
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_preench)

    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ('oval', (event.x, event.y, 0, 0), cor_preench)

    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_preench)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    elif figura_nova[0] == "circulo":
        # Calcula o raio para o circulo
        raio = ( (figura_nova[1][0] - event.x)**2 + (figura_nova[1][1] - event.y)**2 ) ** 0.5
        # figura_nova Recebe o nome, os dois primeiros pontos e o raio calculado)
        figura_nova = ('circulo', (figura_nova[1][0], figura_nova[1][1], raio)) 

    elif figura_nova[0] == 'oval':
        # Calcula dois raios, horizontal e vertical
        raioX = abs(figura_nova[1][0] - event.x)
        raioY = abs(figura_nova[1][1] - event.y)
        figura_nova = ('oval', (figura_nova[1][0], figura_nova[1][1], raioX, raioY))

    elif figura_nova[0] == 'retangulo':
        #a mesma coisa de atualizar linha porque o create_rectangle so precisa de dois pontos, assim como o create_line
        figura_nova = ('retangulo', (figura_nova[1][0], figura_nova[1][1], event.x, event.y))

    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))

    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) # salva as figuras na tela
    desenhar_figuras()

# Cria a imagem na tela, sem deixar as versoes depois de soltar o mouse
def desenhar_figuras():
    canvas.delete("all")
    for fig, values in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_preench)
        # recebe os pontos x e y do inicio e x e y do fim e cria o retangulo com base nesses pontos
        elif fig == "retangulo":
            if cor_preench_fig == '':
                canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_borda_fig, width=3)
            else:
                canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_borda_fig,width=3, fill=cor_preench_fig)

        # recebe os pontos centrais (cx, cy) e o raio e cria o circulo com base neles
        elif fig == 'circulo':
            cx, cy, raio = values
            if cor_preench_fig == '':
                canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, outline=cor_borda_fig, width=3)
            else:
                canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, outline=cor_borda_fig,width=3, fill=cor_preench_fig)

        # recebe os pontos centrais (cx, cy) e dois raios, para criar a oval
        elif fig == 'oval':
            cx, cy, raioX, raioY = values
            if cor_preench_fig == '':
                canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, outline=cor_borda_fig,width=3)
            else:
                canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, outline=cor_borda_fig,width=3, fill=cor_preench_fig)    

        else : # fig == "rabisco"
            canvas.create_line(values, fill=cor_preench)

# Cria a versao antes dela ser solta, com o efeito do dash
def desenhar_figura_nova(): 
    fig, values = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_preench)

    elif fig == 'retangulo':
        if cor_preench_fig == '':
            canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4,2))
        else:
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cor_preench_fig, dash=(4,2))

    # Utiliza de um raio e dois pontos centrais para o circulo
    elif fig == 'circulo':
        cx, cy, raio = values
        if cor_preench_fig == '':
            canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, dash=(4, 2))
        else:
            canvas.create_oval(cx-raio, cy-raio, cx+raio, cy+raio, fill=cor_preench_fig, dash=(4, 2))

    # Utiliza de dois raios e dois pontos centrais para a criação da oval
    elif fig == 'oval':
        cx, cy, raioX, raioY = values
        if cor_preench_fig == '':
            canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, dash=(4,2))
        else:
            canvas.create_oval(cx-raioX, cy-raioY, cx+raioX, cy+raioY, fill=cor_preench_fig, dash=(4,2))

    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2), fill=cor_preench)


def incompleta(figura):
    fig, values = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[1], values[0])
    
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    
    elif fig == 'circulo':
        return values[2] == 0

    elif fig == 'oval':
        return values[2] == 0 or values[3] == 0

    else : # fig == "rabisco"
        return len(values) <= 1 """


#******* MAIN *******#
cor_preench = None
cor_bord = None
figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

raioX = 0
raioY = 0

root = Tk()

# dois frames separados
frame_menu = Frame(root)
frame_menu.pack(fill=X)

frame_canvas = Frame(root)
frame_canvas.pack()

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame_menu, text='Paint.v0,4')
label.grid(column=0, row=0, sticky=W, **paddings)

label_cor = ttk.Label(frame_menu, text='Borda:')
label_cor.grid(column=2, row=0, sticky=W, **paddings)

label_preenchimento = ttk.Label(frame_menu, text='Preenchimento:')
label_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu
option_menu = ttk.OptionMenu(frame_menu, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

tipo_cor_var = StringVar(root)
option_menu_cor = ttk.OptionMenu(frame_menu, tipo_cor_var,
                                 'Preto', 'Preto', 'Azul', 'Verde', 'Vermelho')
option_menu_cor.grid(column=3, row=0, sticky=W, **paddings)

tipo_preenchimento_var = StringVar(root)
option_menu_preenchimento = ttk.OptionMenu(frame_menu, tipo_preenchimento_var,
                                           'Transparente', 'Transparente', 'Preto', 'Azul', 'Verde', 'Vermelho')
option_menu_preenchimento.grid(column=5, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame_canvas, bg='white', width=900, height=600)
canvas.grid(column=0, row=0, sticky=W, **paddings)

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
