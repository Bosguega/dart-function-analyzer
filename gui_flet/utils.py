import os
import webbrowser
from tkinter import Tk, filedialog


def selecionar_diretorio():
    root = Tk()
    root.withdraw()
    pasta = filedialog.askdirectory()
    root.destroy()
    return pasta or None


def salvar_arquivo():
    root = Tk()
    root.withdraw()
    caminho = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown files", "*.md"), ("Todos os arquivos", "*.*")]
    )
    root.destroy()
    return caminho or None


def abrir_no_navegador(caminho):
    webbrowser.open(f'file://{os.path.abspath(caminho)}')
