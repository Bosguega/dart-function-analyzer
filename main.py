import flet as ft
import asyncio
from cli_analyzer import CLIAnalyzer

analyzer = CLIAnalyzer()

def main(page: ft.Page):
    page.title = "Dart Function Analyzer"
    page.scroll = ft.ScrollMode.AUTO

    project_path = ft.Text(value="Nenhum projeto selecionado", selectable=True)
    results_field = ft.TextField(
        value="Clique em analisar para iniciar",
        multiline=True,
        read_only=True,
        expand=True,
        height=400,
    )

    async def selecionar_projeto_async():
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        root.destroy()
        return folder_selected

    def on_selecionar_projeto(e):
        async def run():
            path = await selecionar_projeto_async()
            if path:
                project_path.value = path
                page.update()
        asyncio.create_task(run())

    def on_analisar(e):
        async def run():
            if not project_path.value or project_path.value == "Nenhum projeto selecionado":
                results_field.value = "Selecione um projeto primeiro!"
                page.update()
                return
            results_field.value = "Analisando..."
            page.update()

            result = await analyzer.analyze(project_path.value, options={})
            results_field.value = result
            page.update()
        asyncio.create_task(run())

    page.add(
        ft.Column([
            ft.Text("Dart Function Analyzer", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Selecionar Projeto", on_click=on_selecionar_projeto),
            ft.Text("Projeto:", weight=ft.FontWeight.BOLD),
            project_path,
            ft.ElevatedButton("Analisar", on_click=on_analisar),
            ft.Text("Resultados:", weight=ft.FontWeight.BOLD),
            results_field,
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
