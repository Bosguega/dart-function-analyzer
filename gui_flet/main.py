import flet as ft
from ui_components import (
    criar_cabecalho,
    criar_selecao_projeto,
    criar_configuracoes,
    criar_status,
    criar_resultados,
    criar_rodape
)
from utils import selecionar_diretorio, salvar_arquivo, abrir_no_navegador
from analysis_service import run_analysis_stream
from theme import THEME_LIGHT, THEME_DARK
import threading
import os


def main(page: ft.Page):
    tema_escuro = False
    theme = THEME_LIGHT

    page.title = "Dart Function Analyzer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    project_path = ft.Text(value="Nenhum projeto selecionado", color=ft.Colors.GREY_700)
    progress_bar = ft.ProgressBar(width=400, visible=False)
    results_field = ft.TextField(
        value="Selecione um projeto e configure as opções para iniciar",
        multiline=True,
        read_only=True,
        expand=True,
        height=400,
        text_style=ft.TextStyle(font_family="monospace", size=12)
    )
    status_text = ft.Text(value="", color=ft.Colors.GREY_600)

    modo_avancado = ft.Switch(label="Modo Avançado", value=True)
    agrupar_por = ft.Dropdown(
        label="Agrupar por",
        options=[
            ft.dropdown.Option("modulo"),
            ft.dropdown.Option("funcao"),
        ],
        value="modulo",
        width=200
    )
    funcao_especifica = ft.TextField(
        label="Função específica (opcional)",
        hint_text="Deixe em branco para analisar todas",
        width=300
    )
    output_file = ft.TextField(
        label="Arquivo de saída",
        value="mapa_funcional.md",
        width=300
    )

    def alternar_tema(_):
        nonlocal tema_escuro, theme
        tema_escuro = not tema_escuro
        theme = THEME_DARK if tema_escuro else THEME_LIGHT
        page.theme_mode = ft.ThemeMode.DARK if tema_escuro else ft.ThemeMode.LIGHT
        page.update()

    def on_selecionar_projeto(_):
        pasta = selecionar_diretorio()
        if pasta:
            project_path.value = pasta
            page.update()

    def on_analisar(_):
        if project_path.value == "Nenhum projeto selecionado":
            status_text.value = "Selecione um projeto primeiro!"
            page.update()
            return

        progress_bar.visible = True
        results_field.value = ""
        status_text.value = "Analisando projeto..."
        page.update()

        def append_log(line):
            results_field.value += line + "\n"
            page.update()

        def task():
            ok = run_analysis_stream(
                project_path.value,
                modo_avancado.value,
                funcao_especifica.value,
                output_file.value,
                agrupar_por.value,
                append_log
            )
            progress_bar.visible = False
            status_text.value = "Análise concluída!" if ok else "Erro na análise"
            page.update()

        threading.Thread(target=task, daemon=True).start()

    def on_abrir_resultado(_):
        if os.path.exists(output_file.value):
            abrir_no_navegador(output_file.value)
        else:
            status_text.value = "Arquivo de resultado não encontrado!"
            page.update()

    def on_salvar_resultado(_):
        caminho = salvar_arquivo()
        if caminho:
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(results_field.value)
            status_text.value = f"Resultado salvo em: {caminho}"
            page.update()

    page.add(
        ft.Column(
            [
                ft.Row([
                    criar_cabecalho(theme),
                    ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=alternar_tema, tooltip="Alternar tema")
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                criar_selecao_projeto(on_selecionar_projeto, project_path, theme),
                criar_configuracoes(modo_avancado, agrupar_por, funcao_especifica, output_file, on_analisar, theme),
                criar_status(status_text, progress_bar),
                criar_resultados(results_field, on_abrir_resultado, on_salvar_resultado, theme),
                criar_rodape()
            ],
            width=800,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
