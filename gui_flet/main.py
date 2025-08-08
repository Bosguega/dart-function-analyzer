import flet as ft
from .ui_components import (
    ProjectSelector, AnalysisConfig, ResultsSection, 
    StatusIndicator, Header, Footer, StyledTextField, StyledDropdown
)
from .utils import (
    open_directory_dialog, open_in_browser, 
    save_file_dialog, validate_dart_project
)
from .analysis_service import AnalysisService

def main(page: ft.Page):
    # Configuração da página
    page.title = "Dart Function Analyzer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    # Estados
    project_path_text = ft.Text(
        value="Nenhum projeto selecionado", 
        color=ft.Colors.with_opacity(0.7, ft.Colors.GREY)
    )
    progress_bar = ft.ProgressBar(width=400, visible=False)
    results_field = StyledTextField(
        value="Selecione um projeto e configure as opções para iniciar",
        multiline=True,
        read_only=True,
        expand=True,
        height=400,
        text_style=ft.TextStyle(font_family="monospace", size=12)
    )
    
    # Controles de configuração
    modo_avancado = ft.Switch(label="Modo Avançado", value=True)
    agrupar_por = StyledDropdown(
        label="Agrupar por",
        options=[
            ft.dropdown.Option("modulo", "Módulo"),
            ft.dropdown.Option("funcao", "Função"),
        ],
        value="modulo",
        width=200
    )
    funcao_especifica = StyledTextField(
        label="Função específica (opcional)",
        hint_text="Deixe em branco para analisar todas",
        width=300
    )
    output_file = StyledTextField(
        label="Arquivo de saída",
        value="mapa_funcional.md",
        width=300
    )
    
    # Status da análise
    status_text = ft.Text(value="", color=ft.Colors.with_opacity(0.7, ft.Colors.GREY))
    
    # Serviço de análise
    analysis_service: AnalysisService = None
    
    def selecionar_projeto(e):
        """Abre diálogo para selecionar diretório do projeto."""
        try:
            folder_selected = open_directory_dialog("Selecione o projeto Dart/Flutter")
            if folder_selected:
                # Valida o projeto
                is_valid, message = validate_dart_project(folder_selected)
                
                if is_valid:
                    project_path_text.value = folder_selected
                    project_path_text.color = ft.Colors.GREEN
                    status_text.value = f"✅ {message}"
                    analysis_service = AnalysisService(folder_selected)
                else:
                    project_path_text.value = folder_selected
                    project_path_text.color = ft.Colors.RED
                    status_text.value = f"❌ {message}"
                
                page.update()
        except Exception as ex:
            show_error(f"Erro ao selecionar projeto: {str(ex)}")
    
    def analisar(e):
        """Inicia a análise do projeto."""
        if not analysis_service:
            show_error("Selecione um projeto válido primeiro!")
            return
        
        # Atualiza UI para estado de análise
        progress_bar.visible = True
        status_text.value = "Analisando projeto..."
        status_text.color = ft.Colors.BLUE
        results_field.value = "Iniciando análise...\n"
        page.update()
        
        # Inicia análise
        analysis_service.analyze(
            modo_avancado=modo_avancado.value,
            funcao_especifica=funcao_especifica.value if funcao_especifica.value else None,
            output_file=output_file.value,
            agrupar_por=agrupar_por.value,
            on_success=handle_success,
            on_error=handle_error
        )
    
    def handle_success(content: str):
        """Processa resultado de sucesso."""
        output = "✅ Análise concluída com sucesso!\n\n"
        output += f"Arquivo gerado: {output_file.value}\n\n"
        output += content
        
        # Atualiza UI
        page.update_async(lambda: [
            setattr(progress_bar, 'visible', False),
            setattr(status_text, 'value', "Análise concluída!"),
            setattr(status_text, 'color', ft.Colors.GREEN),
            setattr(results_field, 'value', output),
            page.update()
        ])
    
    def handle_error(error_msg: str):
        """Processa erro na análise."""
        output = f"❌ Erro durante a análise:\n\n{error_msg}"
        
        # Atualiza UI
        page.update_async(lambda: [
            setattr(progress_bar, 'visible', False),
            setattr(status_text, 'value', "Erro na análise"),
            setattr(status_text, 'color', ft.Colors.RED),
            setattr(results_field, 'value', output),
            page.update()
        ])
    
    def show_error(message: str):
        """Exibe mensagem de erro."""
        page.update_async(lambda: [
            setattr(status_text, 'value', message),
            setattr(status_text, 'color', ft.Colors.RED),
            setattr(results_field, 'value', message),
            page.update()
        ])
    
    def abrir_resultado(e):
        """Abre o arquivo de resultado no navegador."""
        if os.path.exists(output_file.value):
            success = open_in_browser(output_file.value)
            if not success:
                show_error("Não foi possível abrir o arquivo no navegador")
        else:
            show_error("Arquivo de resultado não encontrado!")
    
    def salvar_resultado(e):
        """Salva o resultado em um arquivo diferente."""
        saved_path = save_file_dialog(
            content=results_field.value,
            default_name="analise_dart.md"
        )
        
        if saved_path:
            show_success(f"Resultado salvo em: {saved_path}")
    
    def show_success(message: str):
        """Exibe mensagem de sucesso."""
        page.update_async(lambda: [
            setattr(status_text, 'value', message),
            setattr(status_text, 'color', ft.Colors.GREEN),
            page.update()
        ])
    
    # Layout da interface
    page.add(
        ft.Column(
            [
                Header(),
                ProjectSelector(selecionar_projeto, project_path_text),
                AnalysisConfig(
                    modo_avancado, agrupar_por, funcao_especifica, 
                    output_file, analisar
                ),
                StatusIndicator(status_text, progress_bar),
                ResultsSection(results_field, abrir_resultado, salvar_resultado),
                Footer()
            ],
            width=800,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)