import flet as ft
from ui import criar_tela_principal

def main(page: ft.Page):
    criar_tela_principal(page)

if __name__ == "__main__":
    ft.app(target=main)
