import asyncio
from analyzer_core import ProjectAnalyzer
from analyzer_interface import AnalyzerInterface

class AnalyzerBackend(AnalyzerInterface):
    async def analyze(self, project_path: str, options: dict) -> str:
        modo_avancado = options.get('modo_avancado', False)
        funcao_especifica = options.get('funcao_especifica', None)
        agrupar_por = options.get('agrupar_por', 'modulo')
        output_file = "mapa_funcional.md"

        analyzer = ProjectAnalyzer(project_path)

        loop = asyncio.get_running_loop()
        # Chama analyze síncrono no executor para não travar o loop async
        await loop.run_in_executor(
            None,
            lambda: analyzer.analyze(
                modoAvancado=modo_avancado,
                funcaoEspecifica=funcao_especifica,
                outputFile=output_file,
                agruparPor=agrupar_por,
            )
        )

        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Erro ao ler arquivo de saída: {e}"
