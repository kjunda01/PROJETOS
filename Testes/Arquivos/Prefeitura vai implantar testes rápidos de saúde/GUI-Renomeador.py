import tkinter as tk
from tkinter import filedialog
import glob
import shutil
import os

# Funções do programa

def selecionarPasta():
   abrirPasta = filedialog.askdirectory()
   if abrirPasta:
      diretorio = os.path.abspath(abrirPasta)
      tk.Label(window, text="Pasta selecionada: " + str(diretorio).split("/")[-1]).pack()


def zip_extract():
    zip_list = glob.glob1('*.zip')
    for zips in zip_list:
        shutil.unpack_archive(zips)


window = tk.Tk()

# ********** Propriedades da janela principal **********

# Título
window.title("Renomeador Python")

# Tamanho da tela
window.geometry("800x600")


# ********** Começo dos itens na tela **********

msgInicial = tk.Label(window, text="Selecione uma pasta para começar", )
msgInicial.pack(padx=10, pady=10)

botao_selectFolder = tk.Button(window, text="Pasta", command=selecionarPasta)
botao_selectFolder.pack(padx=10, pady=10)


window.mainloop()
