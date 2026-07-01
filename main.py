from tkinter import *
from tkinter import ttk

#funçao de preenchimento das figuras
def cor_preenchimento():
    global cor_preench
    if tipo_preenchimento_var.get() == "Preto":
        cor_preench = 'black'
    elif tipo_preenchimento_var.get() == "Vermelho":
        cor_preench = 'red'
    elif tipo_preenchimento_var.get() == "Verde":
        cor_preench = 'green'
    elif tipo_preenchimento_var.get() == "Azul":
        cor_preench = 'blue'
    else:
        cor_preench = ''


#funçao que define a cor das bordas
def cor_borda():
    global cor_bord
    if tipo_cor_var.get() == "Preto":
        cor_bord = 'black'
    elif tipo_cor_var.get() == "Vermelho":
        cor_bord = 'red'
    elif tipo_cor_var.get() == "Verde":
        cor_bord = 'green'
    elif tipo_cor_var.get() == "Azul":
        cor_bord = 'blue'
    else:
        cor_bord = 'black'  # nao existe opcao "transparente" no menu de borda, mas todo caso precisa de um valor


# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova

    cor_preenchimento()  
    cor_borda()           
                           

    if tipo_figura_var.get() == 'Linha':
       
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_bord, cor_preench)

    elif tipo_figura_var.get() == 'Circulo':
        figura_nova = ('circulo', (event.x, event.y, 0), cor_bord, cor_preench)
    
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_bord, cor_preench)

    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ('oval', (event.x, event.y, 0, 0), cor_bord, cor_preench)

    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_bord, cor_preench)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    elif figura_nova[0] == "circulo":
        # Calcula o raio para o circulo
        raio = ( (figura_nova[1][0] - event.x)**2 + (figura_nova[1][1] - event.y)**2 ) ** 0.5
       
        figura_nova = ('circulo', (figura_nova[1][0], figura_nova[1][1], raio), figura_nova[2], figura_nova[3]) 

    elif figura_nova[0] == 'oval':
        # Calcula dois raios, horizontal e vertical
        raioX = abs(figura_nova[1][0] - event.x)
        raioY = abs(figura_nova[1][1] - event.y)
        figura_nova = ('oval', (figura_nova[1][0], figura_nova[1][1], raioX, raioY), figura_nova[2], figura_nova[3])

    elif figura_nova[0] == 'retangulo':
        #a mesma coisa de atualizar linha porque o create_rectangle so precisa de dois pontos, assim como o create_line
        figura_nova = ('retangulo', (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])

    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])

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
    
    for fig, values, cor_borda_fig, cor_preench_fig in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda_fig)
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
            canvas.create_line(values, fill=cor_borda_fig)

# Cria a versao antes dela ser solta, com o efeito do dash
def desenhar_figura_nova(): 
   
    fig, values, cor_borda_fig, cor_preench_fig = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))

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
        canvas.create_line(values, dash=(4, 2))


def incompleta(figura):
    
    fig, values, cor_borda_fig, cor_preench_fig = figura
    if fig == "linha":
       
        return (values[0], values[1]) == (values[2], values[3])
    
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    
    elif fig == 'circulo':
        return values[2] == 0

    elif fig == 'oval':
        return values[2] == 0 or values[3] == 0

    else : # fig == "rabisco"
        return len(values) <= 1


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
label = ttk.Label(frame_menu, text='Paint.v0,3')
label.grid(column=0, row=0, sticky=W, **paddings)

label_cor = ttk.Label(frame_menu, text='Borda:')
label_cor.grid(column=2, row=0, sticky=W, **paddings)

label_preenchimento = ttk.Label(frame_menu, text='Preenchimento:')
label_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
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
