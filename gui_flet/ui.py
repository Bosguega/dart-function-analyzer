import flet as ft
import asyncio
import threading
from tkinter import Tk, filedialog
from async_tasks import executar_analise_async

def run_async(coro, callback):
    def runner():
        result = asyncio.run(coro)
        callback(result)
    threading.Thread(target=runner).start()

async def selecionar_pasta_async():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder_selected = filedialog.askdirectory()
    root.destroy()
    return folder_selected

def criar_tela_principal(page: ft.Page):
    page.title = "Dart Function Analyzer"
    page.scroll = ft.ScrollMode.AUTO

    project_path = ft.Text(value="Nenhum projeto selecionado", selectable=True)

    checkbox_avancado = ft.Checkbox(label="Avançado", value=True)
    dropdown_agrupamento = ft.Dropdown(
        width=150,
        label="Agrupar por",
        value="modulo",
        options=[
            ft.dropdown.Option("modulo"),
            ft.dropdown.Option("arquivo"),
            ft.dropdown.Option("função"),
        ],
    )

    resultados_field = ft.TextField(
        value="Aqui aparecerão os resultados da análise",
        multiline=True,
        read_only=True,
        expand=True,
        height=400,
    )

    status_bar = ft.Text("Pronto", color=ft.Colors.GREEN)

    def on_selecionar_pasta(e):
        def callback(result):
            if result:
                project_path.value = result
                page.update()
        run_async(selecionar_pasta_async(), callback)

    def on_analisar(e):
        if not project_path.value or project_path.value == "Nenhum projeto selecionado":
            resultados_field.value = "Selecione um projeto primeiro!"
            status_bar.value = "Erro: projeto não selecionado."
            status_bar.color = ft.Colors.RED
            page.update()
            return

        status_bar.value = "Analisando..."
        status_bar.color = ft.Colors.ORANGE
        resultados_field.value = ""
        page.update()

        avancado_flag = "--avancado" if checkbox_avancado.value else ""
        agrupamento_flag = f"--agrupar={dropdown_agrupamento.value}"

        async def run_analise():
            return await executar_analise_async(
                project_path.value,
                avancado_flag=avancado_flag,
                agrupamento_flag=agrupamento_flag
            )

        def callback(result):
            resultados_field.value = result
            status_bar.value = "Análise concluída!" if "✅" in result else "Erro na análise."
            status_bar.color = ft.Colors.GREEN if "✅" in result else ft.Colors.RED
            page.update()

        run_async(run_analise(), callback)

    btn_selecionar_pasta = ft.ElevatedButton("Selecionar Pasta", on_click=on_selecionar_pasta)
    btn_analisar = ft.ElevatedButton("Analisar", on_click=on_analisar)

    filtros_controles = ft.Row([
        btn_selecionar_pasta,
        checkbox_avancado,
        dropdown_agrupamento,
        btn_analisar,
    ], alignment=ft.MainAxisAlignment.START, spacing=15)

    page.add(
        ft.Column([
            filtros_controles,
            ft.Text("Projeto:", weight=ft.FontWeight.BOLD),
            project_path,
            resultados_field,
            status_bar,
        ], expand=True)
    )
