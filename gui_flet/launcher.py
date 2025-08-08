# gui_flet/launcher.py

import flet as ft
import asyncio
import os
from datetime import datetime
from backend_controller import BackendController

controller = BackendController()

def main(page: ft.Page):
    page.title = "Dart Function Analyzer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1000
    page.window_height = 750
    page.window_resizable = True
    page.padding = 20
    page.fonts = {"Monospace": "Consolas, 'Courier New', monospace"}

    current_theme = True

    project_path = ft.Ref[ft.Text]()
    results_field = ft.Ref[ft.TextField]()
    loading = ft.Ref[ft.ProgressRing]()
    status_label = ft.Ref[ft.Text]()
    function_filter = ft.Ref[ft.TextField]()
    group_by_dropdown = ft.Ref[ft.Dropdown]()
    theme_button = ft.Ref[ft.IconButton]()

    def update_status(text: str):
        if status_label.current:
            status_label.current.value = text
            page.update()

    def show_snack(message: str, color=ft.Colors.GREEN_400):
        page.snack_bar = ft.SnackBar(
            ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=color,
            duration=3000,
        )
        page.snack_bar.open = True
        page.update()

    def on_folder_picked(e: ft.FilePickerResultEvent):
        if e.path:
            if project_path.current:
                project_path.current.value = e.path
            update_status(f"Projeto selecionado: {os.path.basename(e.path)}")
        page.update()

    file_picker = ft.FilePicker(on_result=on_folder_picked)
    page.overlay.append(file_picker)

    async def analisar(_):
        path = project_path.current.value if project_path.current else None
        filter_value = function_filter.current.value.strip() if function_filter.current else None
        group_value = group_by_dropdown.current.value if group_by_dropdown.current else "modulo"

        if loading.current:
            loading.current.visible = True
        page.update()

        resultado = await controller.analyze_project(path, filter_value, group_value)

        if not isinstance(resultado, str):
            import json
            resultado = json.dumps(resultado, indent=2, ensure_ascii=False)

        if results_field.current:
            results_field.current.value = resultado

        update_status(f"✅ Análise concluída em {datetime.now().strftime('%H:%M:%S')}")
        show_snack("✅ Análise concluída!")

        if loading.current:
            loading.current.visible = False
        page.update()

    def on_save_result(e: ft.FilePickerResultEvent):
        if not e.path or not results_field.current:
            return
        sucesso, msg = controller.save_result_to_file(e.path, results_field.current.value)
        show_snack(msg, color=ft.Colors.GREEN_400 if sucesso else ft.Colors.RED_400)

    save_file_dialog = ft.FilePicker(on_result=on_save_result)
    page.overlay.append(save_file_dialog)

    async def exportar_resultados(_):
        if not results_field.current or not results_field.current.value.strip():
            show_snack("Nada para exportar.", color=ft.Colors.AMBER)
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_file_dialog.save_file(
            file_name=f"dart_analysis_{timestamp}.txt",
            initial_directory=os.path.expanduser("~")
        )

    async def copiar_resultados(_):
        if results_field.current and results_field.current.value.strip():
            await page.set_clipboard_async(results_field.current.value)
            show_snack("📋 Copiado para a área de transferência!")

    def toggle_theme(_):
        nonlocal current_theme
        current_theme = not current_theme
        page.theme_mode = ft.ThemeMode.LIGHT if not current_theme else ft.ThemeMode.DARK
        if theme_button.current:
            theme_button.current.icon = (
                ft.Icons.WB_SUNNY_OUTLINED if not current_theme else ft.Icons.NIGHTLIGHT_OUTLINED
            )
            theme_button.current.tooltip = "Tema Claro" if not current_theme else "Tema Escuro"
        page.update()

    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("Dart Function Analyzer", size=28, weight=ft.FontWeight.BOLD),
                ft.Container(expand=True),
                ft.IconButton(ft.Icons.CONTENT_COPY_OUTLINED, tooltip="Copiar resultados", on_click=copiar_resultados),
                ft.IconButton(ft.Icons.DOWNLOAD_OUTLINED, tooltip="Exportar resultados", on_click=exportar_resultados),
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, tooltip="Alternar tema", on_click=toggle_theme, ref=theme_button),
            ],
            spacing=10,
        ),
        padding=10,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.OUTLINE)),
    )

    filters = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                [
                    ft.Text("Filtros", size=16, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.TextField(label="Função específica (opcional)", hint_text="build", width=300, ref=function_filter),
                            ft.Dropdown(
                                label="Agrupar por",
                                width=200,
                                options=[
                                    ft.dropdown.Option("modulo"),
                                    ft.dropdown.Option("arquivo"),
                                    ft.dropdown.Option("classe"),
                                ],
                                value="modulo",
                                ref=group_by_dropdown,
                            ),
                            ft.ElevatedButton("Analisar", icon=ft.Icons.ANALYTICS_OUTLINED, on_click=analisar),
                        ]
                    ),
                ]
            ),
        )
    )

    loading.current = ft.ProgressRing(visible=False, width=20, height=20)
    results_field.current = ft.TextField(
        value="Aguardando análise...",
        multiline=True,
        read_only=True,
        expand=True,
        border=ft.InputBorder.NONE,
        text_style=ft.TextStyle(font_family="Monospace", size=11),
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        border_radius=8,
    )
    project_path.current = ft.Text("Nenhum projeto selecionado", selectable=True, italic=True, color=ft.Colors.BLUE_300)
    status_label.current = ft.Text("Pronto", size=13)

    content = ft.Column(
        controls=[
            ft.Text("Projeto Dart/Flutter", size=18, weight=ft.FontWeight.W_500),
            ft.Row([
                ft.ElevatedButton("📁 Selecionar Projeto", on_click=lambda e: file_picker.get_directory_path()),
                ft.Text("Caminho:", size=12, color=ft.Colors.ON_SURFACE_VARIANT),
                project_path.current,
            ]),
            filters,
            ft.Divider(),
            ft.Text("Resultados", size=18, weight=ft.FontWeight.W_500),
            ft.Container(
                content=results_field.current,
                expand=True,
                border=ft.border.all(1, ft.Colors.OUTLINE_VARIANT),
                border_radius=8,
            ),
            ft.Row([loading.current], alignment=ft.MainAxisAlignment.CENTER),
        ],
        spacing=15,
        expand=True,
    )

    status_bar = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINED, size=16, color=ft.Colors.ON_SURFACE_VARIANT),
            status_label.current,
            ft.Container(expand=True),
            ft.Text("v1.0", size=12, color=ft.Colors.ON_SURFACE_VARIANT),
        ]),
        height=30,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        border=ft.border.only(top=ft.BorderSide(1, ft.Colors.OUTLINE)),
        padding=10,
    )

    page.add(ft.Column([header, content, ft.Container(expand=True), status_bar], expand=True, spacing=0))
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
