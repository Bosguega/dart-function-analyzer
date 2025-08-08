import asyncio
import os

# Define a raiz do projeto (um nível acima da pasta atual do async_tasks.py)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

async def executar_analise_async(caminho_projeto: str, avancado_flag: str = "", agrupamento_flag: str = "") -> str:
    dart_main_path = os.path.join(ROOT_DIR, "bin", "main.dart")
    if not os.path.isfile(dart_main_path):
        return "❌ Erro: arquivo 'bin/main.dart' não encontrado no projeto."

    comando = f'chcp 65001 && dart run bin/main.dart "{caminho_projeto}" {avancado_flag} {agrupamento_flag}'

    proc = await asyncio.create_subprocess_shell(
        comando,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=ROOT_DIR  # executa no diretório correto
    )
    stdout, stderr = await proc.communicate()

    if proc.returncode == 0:
        try:
            mapa_path = os.path.join(ROOT_DIR, "mapa_funcional.md")
            with open(mapa_path, "r", encoding="utf-8") as f:
                return "✅ Análise concluída!\n\n" + f.read()
        except Exception as e:
            return f"⚠️ Não foi possível ler o arquivo: {e}"
    else:
        return f"❌ Erro na análise:\n{stderr.decode(errors='replace')}"
