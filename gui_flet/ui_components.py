import flet as ft


def criar_cabecalho(theme):
    return ft.Container(
        ft.Column([
            ft.Text("Dart Function Analyzer", size=32, weight=ft.FontWeight.BOLD, color=theme["primary"]),
            ft.Text("Ferramenta para análise de projetos Dart/Flutter", size=16, color=ft.Colors.GREY_600),
        ]),
        padding=ft.padding.only(top=20, bottom=30)
    )


def criar_selecao_projeto(on_click, project_path, theme):
    return ft.Card(
        ft.Container(
            ft.Column([
                ft.Text("Selecionar Projeto", size=18, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.ElevatedButton(
                        "Selecionar Diretório",
                        on_click=on_click,
                        icon=ft.Icons.FOLDER_OPEN,
                        style=ft.ButtonStyle(bgcolor=ft.Colors.with_opacity(0.1, theme["primary"]))
                    ),
                    ft.Container(width=20),
                    ft.Container(project_path, expand=True),  # Correção aqui
                ], alignment=ft.MainAxisAlignment.START),
            ]),
            padding=20
        ),
        elevation=2,
        margin=ft.margin.only(bottom=20)
    )


def criar_configuracoes(modo_avancado, agrupar_por, funcao_especifica, output_file, on_analisar, theme):
    return ft.Card(
        ft.Container(
            ft.Column([
                ft.Text("Configurações da Análise", size=18, weight=ft.FontWeight.BOLD),
                ft.Row([
                    modo_avancado,
                    ft.Container(width=30),
                    agrupar_por,
                    ft.Container(width=30),
                    funcao_especifica,
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=10),
                ft.Row([
                    output_file,
                    ft.ElevatedButton(
                        "Analisar",
                        on_click=on_analisar,
                        icon=ft.Icons.SEARCH,
                        style=ft.ButtonStyle(bgcolor=theme["primary"], color=ft.Colors.WHITE)
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]),
            padding=20
        ),
        elevation=2,
        margin=ft.margin.only(bottom=20)
    )


def criar_status(status_text, progress_bar):
    return ft.Container(
        ft.Column([
            status_text,
            progress_bar,
        ]),
        alignment=ft.MainAxisAlignment.CENTER,
        margin=ft.margin.only(bottom=10)
    )


def criar_resultados(results_field, on_abrir_resultado, on_salvar_resultado, theme):
    return ft.Card(
        ft.Container(
            ft.Column([
                ft.Row([
                    ft.Text("Resultados da Análise", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.ElevatedButton(
                            "Abrir no Navegador",
                            on_click=on_abrir_resultado,
                            icon=ft.Icons.OPEN_IN_BROWSER,
                            style=ft.ButtonStyle(bgcolor=theme["secondary"])
                        ),
                        ft.Container(width=10),
                        ft.ElevatedButton(
                            "Salvar Como...",
                            on_click=on_salvar_resultado,
                            icon=ft.Icons.SAVE,
                            style=ft.ButtonStyle(bgcolor=theme["success"])
                        ),
                    ], alignment=ft.MainAxisAlignment.END),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=10),
                results_field,
            ]),
            padding=20
        ),
        elevation=2,
        margin=ft.margin.only(bottom=20)
    )


def criar_rodape():
    return ft.Container(
        ft.Text(
            "Dart Function Analyzer v1.0 • Desenvolvido com ❤️ usando Flet",
            size=12,
            color=ft.Colors.GREY_500
        ),
        padding=ft.padding.only(bottom=20)
    )
