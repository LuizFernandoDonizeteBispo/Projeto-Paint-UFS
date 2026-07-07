from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.janelaPaint import JanelaPaint
from Controller.Desenhar import Desenho
from Controller.mouse import Mouse


#******* MAIN *******#

root = Tk()
root.state('zoomed')
menu = Menu(root)
menu.montar()
quadro = Quadro(root, menu.tipo_preenchimento_var, menu.tipo_cor_var, menu.tipo_figura_var)
desenho = Desenho(quadro.canvas, menu.tipo_cor_var, menu.tipo_preenchimento_var, menu.tipo_figura_var)
janela_paint = JanelaPaint(quadro.canvas)
mouse = Mouse(quadro.canvas, desenho)
mouse.mouse()
root.mainloop()
