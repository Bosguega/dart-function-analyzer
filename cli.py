import argparse
import asyncio
from cli_analyzer import AnalyzerBackend

def main():
    parser = argparse.ArgumentParser(description="Dart Function Analyzer CLI")
    parser.add_argument("project_path", help="Caminho para o projeto Dart")
    args = parser.parse_args()

    options = {
        "modo_avancado": True,
        "agrupar_por": "modulo",
        # adicione mais opções conforme necessidade
    }

    backend = AnalyzerBackend()
    resultado = asyncio.run(backend.analyze(args.project_path, options))
    print(resultado)

if __name__ == "__main__":
    main()
