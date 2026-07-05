from Model import *
from View.menu import Menu
from View.quadro import Quadro
from View.seletor_cor import SeletorCor


#******* MAIN *******#
menu = Menu(root)
menu.montar()

quadro = Quadro(canvas, menu.tipo_preenchimento_var, menu.tipo_cor_var, menu.tipo_figura_var)
quadro.montar_quadro()
root.mainloop()
