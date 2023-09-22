import os
import sys
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from menus import criar_menu  # Importa a função do arquivo menu.py

positions = ["Trainee", "Intern", "Jr", "Sr", "Manager", "Architect", "Sr Manager"]
salaries = [2000, 2900, 4000, 7000, 10000, 12700, 14500]

root = tk.Tk()
root.minsize(500, 500)
criar_menu(root)
root.title("Regressão polinomial")
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
