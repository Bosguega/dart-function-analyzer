import flet as ft
import subprocess
import os

def main(page: ft.Page):
    page.title = "Dart Function Analyzer"
    page.scroll = ft.ScrollMode.AUTO  # Habilita scroll na página inteira, se necessário

    project_path = ft.Text(value="Nenhum projeto selecionado")
    results_field = ft.TextField(
        value="Clique em analisar para iniciar",
        multiline=True,
        read_only=True,
        expand=True,
        height=400,
    )

    def selecionar_projeto(e):
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        root.destroy()

        if folder_selected:
            project_path.value = folder_selected
            page.update()

    def analisar(e):
        if not project_path.value or project_path.value == "Nenhum projeto selecionado":
            results_field.value = "Selecione um projeto primeiro!"
            page.update()
            return

        results_field.value = "Analisando..."
        page.update()

        try:
            comando = f'chcp 65001 && dart run bin/main.dart "{project_path.value}" --avancado --agrupar=modulo'
            result = subprocess.run(
                comando,
                shell=True,
                capture_output=True,
                text=False,
                cwd=os.getcwd()
            )

            stdout = result.stdout.decode('utf-8', errors='replace')
            stderr = result.stderr.decode('utf-8', errors='replace')

            if result.returncode == 0:
                output = "✅ Análise concluída!\n\n"
                try:
                    with open("mapa_funcional.md", "r", encoding="utf-8") as f:
                        output += f.read()
                except Exception as file_error:
                    output += f"\n\n⚠️ Não foi possível ler o arquivo: {str(file_error)}"
            else:
                output = f"❌ Erro na análise:\n{stderr}"

        except Exception as e:
            output = f"❌ Erro ao executar: {str(e)}"

        results_field.value = output
        page.update()

    page.add(
        ft.Column([
            ft.Text("Dart Function Analyzer", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Selecionar Projeto", on_click=selecionar_projeto),
            ft.Text("Projeto:", weight=ft.FontWeight.BOLD),
            project_path,
            ft.ElevatedButton("Analisar", on_click=analisar),
            ft.Text("Resultados:", weight=ft.FontWeight.BOLD),
            results_field,
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
