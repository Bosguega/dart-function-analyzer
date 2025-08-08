# backend_controller.py

import os
from datetime import datetime
from cli_analyzer import AnalyzerBackend

backend = AnalyzerBackend()

class BackendController:
    def __init__(self):
        self.analysis_in_progress = False

    async def analyze_project(self, path: str, filter_func: str, group_by: str):
        if self.analysis_in_progress:
            return "Análise já em andamento"

        if not path or path == "Nenhum projeto selecionado":
            return "⚠️ Nenhum projeto selecionado."

        self.analysis_in_progress = True
        options = {
            "modo_avancado": True,
            "funcao_especifica": filter_func or None,
            "agrupar_por": group_by,
        }
        try:
            result = await backend.analyze(path, options)
            return result
        except Exception as e:
            return f"❌ Erro durante análise: {type(e).__name__}: {e}"
        finally:
            self.analysis_in_progress = False

    def save_result_to_file(self, path: str, content: str):
        if not path or not content:
            return False, "Caminho ou conteúdo inválido"
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return True, f"💾 Salvo em: {os.path.basename(path)}"
        except Exception as e:
            return False, f"❌ Falha ao salvar: {e}"
