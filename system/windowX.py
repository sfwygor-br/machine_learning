import tkinter as tk
import sysWindowFunctions
import loggerX

#def on_close():
#    root.quit()
#    loggerX.newLog("INFO", "Destroying screen", False)

def configureWindow(root, title):
    #root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
    root.title(title)
    root.minsize(500, 500)
    #label = tk.Label(root, text="")
    #label.pack()

def configureMenu(root):
    # Cria um menu superior
    menu = tk.Menu(root)
    root.config(menu=menu)

    # Cria um submenu "Arquivo"
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="Arquivo", menu=file_menu)
    file_menu.add_command(label="Visualizar datasets", command=sysWindowFunctions.datasetView)
    file_menu.add_command(label="Sair", command=root.quit)

def configureSubMenu(root):
    # Cria um menu superior
    menu = tk.Menu(root)
    root.config(menu=menu)

    # Cria um submenu "Arquivo"
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="Arquivo", menu=file_menu)
    file_menu.add_command(label="Sair", command=root.quit)