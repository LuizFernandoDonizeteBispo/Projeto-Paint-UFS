from tkinter import Tk, Frame, Canvas, W
from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.janelaPaint import JanelaPain
from Controller.Desenhar import Desenho
from Controller.mouse import Mouse
from Controller.arquivos import Arquivos


#******* MAIN *******#

root = Tk()
root.state('zoomed')
arquivos = Arquivos(armazem, desenho)
menu = Menu(root)
menu.montar()
quadro = Quadro(root)
armazem = Armazem()
janela_paint = JanelaPaint(quadro.canvas)
desenho = Desenho(quadro.canvas, janela_paint, menu, armazem)
mouse = Mouse(quadro.canvas, desenho)
mouse.mouse()
root.mainloop()
