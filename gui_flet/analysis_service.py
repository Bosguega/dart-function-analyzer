import subprocess
import os


def run_analysis_stream(projeto, avancado, funcao, arquivo_saida, agrupar, on_output):
    """
    Executa a análise e envia logs em tempo real para on_output(line).
    Retorna True se sucesso, False se erro.
    """
    comando_parts = [
        'dart', 'run', 'bin/main.dart',
        f'"{projeto}"'
    ]

    if avancado:
        comando_parts.append('--avancado')

    if funcao:
        comando_parts.append(f'--funcao={funcao}')

    comando_parts.append(f'--output={arquivo_saida}')
    comando_parts.append(f'--agrupar={agrupar}')

    comando = ' '.join(comando_parts)

    process = subprocess.Popen(
        comando,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=os.getcwd(),
        encoding='utf-8',
        errors='replace'
    )

    for line in process.stdout:
        on_output(line.rstrip())

    process.wait()
    return process.returncode == 0
