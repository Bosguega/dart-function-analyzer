import os
from typing import Optional, Dict, Any
from .utils import run_command_async

class AnalysisService:
    """
    Serviço responsável por executar a análise de projetos Dart/Flutter.
    """
    
    def __init__(self, project_path: str):
        """
        Inicializa o serviço de análise.
        
        Args:
            project_path: Caminho do projeto a ser analisado
        """
        self.project_path = project_path
        self.output_file = "mapa_funcional.md"
    
    def analyze(
        self,
        modo_avancado: bool = False,
        funcao_especifica: Optional[str] = None,
        output_file: Optional[str] = None,
        agrupar_por: str = "modulo",
        on_success: Optional[callable] = None,
        on_error: Optional[callable] = None
    ) -> None:
        """
        Executa a análise do projeto.
        
        Args:
            modo_avancado: Se True, usa modo avançado de análise
            funcao_especifica: Nome de uma função específica para analisar
            output_file: Nome do arquivo de saída
            agrupar_por: Como agrupar os resultados ("modulo" ou "funcao")
            on_success: Callback para sucesso
            on_error: Callback para erro
        """
        if output_file:
            self.output_file = output_file
        
        # Constrói o comando
        command_parts = [
            'dart', 'run', 'bin/main.dart',
            f'"{self.project_path}"'
        ]
        
        if modo_avancado:
            command_parts.append('--avancado')
            
        if funcao_especifica:
            command_parts.append(f'--funcao={funcao_especifica}')
            
        command_parts.append(f'--output={self.output_file}')
        command_parts.append(f'--agrupar={agrupar_por}')
        
        command = ' '.join(command_parts)
        
        # Callbacks padrão
        def _default_success(stdout: str):
            try:
                with open(self.output_file, "r", encoding="utf-8") as f:
                    content = f.read()
                if on_success:
                    on_success(content)
            except Exception as e:
                error_msg = f"Erro ao ler arquivo de resultado: {str(e)}"
                if on_error:
                    on_error(error_msg)
        
        def _default_error(stderr: str):
            if on_error:
                on_error(stderr)
        
        # Executa o comando
        run_command_async(
            command=command,
            on_success=_default_success,
            on_error=_default_error,
            cwd=os.getcwd()
        )
    
    def get_analysis_config(self) -> Dict[str, Any]:
        """
        Retorna a configuração atual da análise.
        
        Returns:
            Dicionário com a configuração
        """
        return {
            "project_path": self.project_path,
            "output_file": self.output_file
        }
    
    def cleanup(self) -> None:
        """
        Limpa arquivos temporários gerados pela análise.
        """
        try:
            if os.path.exists(self.output_file):
                os.remove(self.output_file)
        except Exception as e:
            print(f"Erro ao limpar arquivo temporário: {e}")