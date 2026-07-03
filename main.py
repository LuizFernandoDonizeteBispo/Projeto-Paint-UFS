from tkinter import Tk, Frame, Canvas, W

from figura import Figura
from menu import Menu
from quadro import Quadro
from seletor_cor import SeletorCor


#******* MAIN *******#

root = Tk()

frame_canvas = Frame(root)
frame_canvas.pack()

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5}
canvas = Canvas(frame_canvas, bg='white', width=900, height=600)  # Área de desenho
canvas.grid(column=0, row=0, sticky=W, **paddings)

menu = Menu(root)
menu.montar()

quadro = Quadro(canvas, menu.tipo_preenchimento_var, menu.tipo_cor_var, menu.tipo_figura_var)

root.mainloop()
