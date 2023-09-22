import tkinter as tk
from tkinter import messagebox
import logging

# Configuração do logger
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def newLog(log_type, message, showmessage):
    if log_type == "INFO":
        logging.info(message)
        show_message("INFO", message, showmessage)
    elif log_type == "ERROR":
        logging.error(message)
        show_message("ERROR", message, showmessage)
    elif log_type == "WARNING":
        logging.warning(message)
        show_message("WARNING", message, showmessage)

def show_message(log_type, message, showmessage):
    if (showmessage == True):
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        if log_type == "INFO":
            messagebox.showinfo("Informação", message)
        elif log_type == "ERROR":
            messagebox.showerror("Erro", message)
        elif log_type == "WARNING":
            messagebox.showwarning("Aviso", message)

        root.destroy()

# Exemplo de uso:
#try:
    # Simulando um erro
#    num1 = 10
#    num2 = 0
#    resultado = num1 / num2
#except ZeroDivisionError as e:
#    error_message = f"Erro de divisão: {e}"
#    registrar("ERROR", error_message)

# Exemplo de uso:
#info_message = "Isso é uma mensagem de informação."
#registrar("INFO", info_message)

# Exemplo de uso:
#warning_message = "Isso é um aviso."
#registrar("WARNING", warning_message)
