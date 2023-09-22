import tkinter as tk
import loggerX
import constants as c

root    = tk.Tk()
windows = {}

global root
global windows

def on_close(window, title):
    # Fecha a janela específica passada como argumento
    window.destroy()
    print(c.show_log_info_display)
    loggerX.newLog("INFO", "About to destroy screen :" + title, c.show_log_info_display)

# Dicionário para rastrear as janelas e suas funções de fechamento


def create_window(title):
    # Cria uma nova janela
    window = tk.Toplevel(root)
    window.minsize(500, 500)
    window.title(title)

    # Associa o evento de fechamento da janela à função on_close
    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, title))

    # Adiciona a janela ao dicionário
    windows[window] = on_close


def main():
    # Cria a janela principal
    root.minsize(500, 500)
    root.title("Sistema")

    # Botão para criar uma nova janela
    button = tk.Button(root, text="Nova Janela", command = lambda: create_window("abc"))
    button.pack()

    # Inicie o loop principal da interface gráfica
    root.mainloop()
