class Desenho:
    def __init__(self, janela_paint):
        self.figuras = []
        self.janela_paint = janela_paint
        self.selecionada_idx = -1

    def adiciona_figura(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras

    def reestruturar_figura(self, figuras_novas):
        self.figuras = figuras_novas

     # ---- Seleção ----

    def limpa_selecao(self):
        self.selecionada_idx = -1

    def seleciona(self, px, py):
        i = len(self.figuras) - 1
        while i >= 0 and not self.figuras[i].contem(px, py):
            i -= 1
        self.selecionada_idx = i

    def selecionada(self):
        if self.selecionada_idx >= 0:
            return self.figuras[self.selecionada_idx]
        else:
            return None

    def obtem_indice_selecionado(self):
        return self.selecionada_idx

    def apaga_selecionada(self):
        if self.selecionada_idx != -1:
            self.figuras.pop(self.selecionada_idx)
            self.selecionada_idx = -1


    #Ordem de empilhamento (z-order
    # A posição na lista é a ordem de desenho: índice 0 é desenhado primeiro
    # (fica no fundo), e o último índice é desenhado por último (fica no topo).
    def move_para_frente(self):
        """Troca a selecionada com a próxima da lista (sobe 1 posição = fica mais na frente)."""
        i = self.selecionada_idx
        if i == -1 or i == len(self.figuras) - 1: #se a figura selecionada nao existir(ate porque nao existe indice -1) ou se a figura selecionada for a ultima da lista de figuras(ai nao da mais pra avançar)
            return # nada selecionado, ou já está no topo: não há o que fazer
        self.figuras[i], self.figuras[i+1] = self.figuras[i+1], self.figuras[i]
        self.selecionada_idx = i+1
    
    def move_para_tras(self):
        i = self.selecionada_idx
        if i <=0:
            return
        self.figuras[i-1], self.figuras[i] = self.figuras[i], self.figuras[i-1]
        self.selecionada_idx = i - 1
    
    def move_para_topo(self):
        i = self.selecionada_idx
        if i ==-1 or i == len(self.figuras)-1:
            return
        figura = self.figuras.pop(i)
        self.figuras.append(figura)
        self.selecionada_idx = len(self.figuras)-1

    def move_para_fundo(self):
        """Tira a selecionada da posição atual e coloca no início da lista (fundo)."""
        i = self.selecionada_idx
        if i <= 0:
            return
        figura = self.figuras.pop(i)
        self.figuras.insert(0, figura)
        self.selecionada_idx = 0