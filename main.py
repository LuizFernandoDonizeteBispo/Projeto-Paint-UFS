from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.janelaPaint import JanelaPaint
from Model.Desenho import Desenho
from Controller.controlador_paint import ControladorPaint


#******* MAIN *******#

root = Tk()
root.state('zoomed')
menu = Menu(root)
menu.montar()
quadro = Quadro(root)
janela_paint = JanelaPaint(quadro.canvas)
desenho = Desenho(janela_paint)
controlador = ControladorPaint(desenho, menu)
root.mainloop()
