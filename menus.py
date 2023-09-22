import tkinter as tk
def criar_menu(root):
    # Cria um menu superior
    menu = tk.Menu(root)
    root.config(menu=menu)

    # Cria um submenu "Arquivo"
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="Arquivo", menu=file_menu)
    file_menu.add_command(label="Sair", command=root.quit)
