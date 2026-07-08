from tkinter import colorchooser

class SeletorCor:
    @staticmethod
    def escolher_cor(titulo="Escolha uma cor"):
        cor = colorchooser.askcolor(title=titulo)
        return  cor[1] if cor[1] else "black"