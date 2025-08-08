from abc import ABC, abstractmethod

class AnalyzerInterface(ABC):
    @abstractmethod
    async def analyze(self, project_path: str, options: dict) -> str:
        """
        Executa a análise do projeto.

        :param project_path: Caminho da pasta do projeto Dart.
        :param options: Dicionário com opções do filtro/agrupamento etc.
        :return: Resultado da análise como string (ex: conteúdo markdown).
        """
        pass
