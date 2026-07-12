from tkinter import Frame, StringVar, X, W
from tkinter import ttk
from View.seletor_cor import SeletorCor


class Menu:
    def __init__(self, root):
        self.frame = Frame(root)  # dois frames separados
        self.frame.pack(fill=X)
        self.tipo_figura_var = StringVar(root)
        self.cor_bord_atual = "Black"
        self.cor_preench_atual = ""
        self.opcoe_var = StringVar(root)

    def montar(self):
        paddings = {'padx': 5, 'pady': 5}

        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                      'Linha', 'Linha', 'Rabisco', 'Circulo', 'Oval', 'Retangulo', 'Borracha')
        option_menu.grid(column=1, row=2, sticky=W, **paddings)

        option_menu_opcao = ttk.OptionMenu(self.frame, self.opcao_var, 'Arquivos', 'Salvar', 'Abrir', 'Fechar',
                                                command=self.escolher_opcao)
        option_menu_opcao.grid(column=1, row=0, sticky=W, **paddings)


        self.botao_cor_bord = ttk.Button(self.frame, text ="◐ Borda", command=self._escolher_borda)
        self.botao_cor_bord.grid(column=3, row=2, sticky=W, **paddings)

        self.botao_cor_preench = ttk.Button(self.frame, text="■ Preench.", command=self._escolher_preench)
        self.botao_cor_preench.grid(column=4, row=2, sticky=W, **paddings)

        self.botao_sem_preench = ttk.Button(self.frame, text="□ Sem Preench.", command=self._sem_preench)
        self.botao_sem_preench.grid(column=5, row=2, sticky=W, **paddings)


    def _escolher_borda(self):
            self.cor_bord_atual = SeletorCor.escolher_cor("Cor da Borda")

    def _escolher_preench(self):
            self.cor_preench_atual = SeletorCor.escolher_cor("Cor do preench.")

    def _sem_preench(self):
            self.cor_preench_atual = ""

    def escolher_opcao(self, opcao_var, caminho, arquivos):
        if opcao_var == 'Salvar':
            arquivos.salvar(caminho)
        elif opcao_var == 'Abrir':
            arquivos.abrir(caminho)
        elif opcao_var == 'Fechar':
             sair