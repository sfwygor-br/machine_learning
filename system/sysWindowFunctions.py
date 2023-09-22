import tkinter as tk
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import windowX
import windowY

def datasetView():

    def listar_arquivos(diretorio):
        try:
            arquivos = os.listdir(diretorio)
            return arquivos
        except Exception as e:
            return []

    def preencher_combobox(entrada_diretorio):
        diretorio = entrada_diretorio.get()
        if os.path.exists(diretorio):
            arquivos = listar_arquivos(diretorio)
            combobox_arquivos['values'] = arquivos
        else:
            combobox_arquivos.set("Diretório não encontrado")
    dsV = windowY.create_window() #tk.Tk()
    windowX.configureWindow(dsV, "Dataset view")
    windowX.configureSubMenu(dsV)
    dirr = tk.Entry(dsV)
    dirr.pack()
    botao_listar = tk.Button(dsV, text="Listar Arquivos", command=preencher_combobox)
    botao_listar.pack()
    
    dsV.mainloop()

def chartPlotter(plot):
    positions = ["Trainee", "Intern", "Jr", "Sr", "Manager", "Architect", "Sr Manager"]
    salaries = [2000, 2900, 4000, 7000, 10000, 12700, 14500]

    root = tk.Tk()
    windowX.configureWindow(dsV, "Gráficos")
    label = tk.Label(root, text="Salários por função")

    # Adiciona um subplot ao objeto Figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plota os dados
    #ax.bar(positions, salaries, color='blue')
    ax.plot(positions, salaries, marker='o', linestyle='-')
    ax.set_xlabel('Descrição da Posição')
    ax.set_ylabel('Salário')


    # Cria um objeto FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()

    # Adicione outros widgets ou funcionalidades aqui, se necessário

    # Inclui o gráfico na interface Tkinter
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    root.mainloop()