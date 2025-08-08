import flet as ft
from .theme import (
    ThemeColors, TextStyles, ButtonStyles, 
    Spacing, ComponentStyles
)

class ProjectSelector(ft.Card):
    """Componente para seleção do projeto."""
    
    def __init__(self, on_select, project_path_text):
        super().__init__(**ComponentStyles.CARD)
        
        self.content = ft.Container(
            ft.Column([
                ft.Text("Selecionar Projeto", style=TextStyles.SECTION_TITLE),
                ft.Row([
                    ft.ElevatedButton(
                        "Selecionar Diretório",
                        on_click=on_select,
                        icon=ft.Icons.FOLDER_OPEN,
                        style=ButtonStyles.OUTLINED
                    ),
                    ft.Container(width=Spacing.ELEMENT_SPACING),
                    ft.Expanded(project_path_text),
                ], alignment=ft.MainAxisAlignment.START),
            ]),
            **ComponentStyles.CONTAINER
        )

class AnalysisConfig(ft.Card):
    """Componente para configuração da análise."""
    
    def __init__(self, modo_avancado, agrupar_por, funcao_especifica, output_file, on_analyze):
        super().__init__(**ComponentStyles.CARD)
        
        self.content = ft.Container(
            ft.Column([
                ft.Text("Configurações da Análise", style=TextStyles.SECTION_TITLE),
                ft.Row([
                    modo_avancado,
                    ft.Container(width=Spacing.ELEMENT_SPACING * 3),
                    agrupar_por,
                    ft.Container(width=Spacing.ELEMENT_SPACING * 3),
                    funcao_especifica,
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=Spacing.ELEMENT_SPACING),
                ft.Row([
                    output_file,
                    ft.ElevatedButton(
                        "Analisar",
                        on_click=on_analyze,
                        icon=ft.Icons.SEARCH,
                        style=ButtonStyles.PRIMARY
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]),
            **ComponentStyles.CONTAINER
        )

class ResultsSection(ft.Card):
    """Componente para exibição dos resultados."""
    
    def __init__(self, results_field, on_open_browser, on_save_as):
        super().__init__(**ComponentStyles.CARD)
        
        self.content = ft.Container(
            ft.Column([
                ft.Row([
                    ft.Text("Resultados da Análise", style=TextStyles.SECTION_TITLE),
                    ft.Row([
                        ft.ElevatedButton(
                            "Abrir no Navegador",
                            on_click=on_open_browser,
                            icon=ft.Icons.OPEN_IN_BROWSER,
                            style=ButtonStyles.SECONDARY
                        ),
                        ft.Container(width=Spacing.ELEMENT_SPACING),
                        ft.ElevatedButton(
                            "Salvar Como...",
                            on_click=on_save_as,
                            icon=ft.Icons.SAVE,
                            style=ButtonStyles.SUCCESS
                        ),
                    ], alignment=ft.MainAxisAlignment.END),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=Spacing.ELEMENT_SPACING),
                results_field,
            ]),
            **ComponentStyles.CONTAINER
        )

class StatusIndicator(ft.Container):
    """Componente para indicar status da análise."""
    
    def __init__(self, status_text, progress_bar):
        super().__init__(
            content=ft.Column([
                status_text,
                progress_bar,
            ]),
            alignment=ft.MainAxisAlignment.CENTER,
            margin=Spacing.SECTION_SPACING
        )

class Header(ft.Container):
    """Cabeçalho da aplicação."""
    
    def __init__(self):
        super().__init__(
            content=ft.Column([
                ft.Text("Dart Function Analyzer", style=TextStyles.TITLE),
                ft.Text("Ferramenta para análise de projetos Dart/Flutter", style=TextStyles.SUBTITLE),
            ]),
            padding=Spacing.HEADER_PADDING
        )

class Footer(ft.Container):
    """Rodapé da aplicação."""
    
    def __init__(self):
        super().__init__(
            content=ft.Text(
                "Dart Function Analyzer v1.0 • Desenvolvido com ❤️ usando Flet",
                size=12,
                color=ThemeColors.TEXT_SECONDARY
            ),
            padding=Spacing.FOOTER_PADDING
        )

class StyledTextField(ft.TextField):
    """TextField com estilo padronizado."""
    
    def __init__(self, **kwargs):
        super().__init__(
            **ComponentStyles.TEXT_FIELD,
            **kwargs
        )

class StyledDropdown(ft.Dropdown):
    """Dropdown com estilo padronizado."""
    
    def __init__(self, **kwargs):
        super().__init__(
            **ComponentStyles.DROPDOWN,
            **kwargs
        )