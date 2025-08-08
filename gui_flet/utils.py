import os
import subprocess
import threading
import webbrowser
from typing import Optional, Callable

def run_command_async(
    command: str,
    on_success: Callable[[str], None],
    on_error: Callable[[str], None],
    cwd: Optional[str] = None
) -> threading.Thread:
    """
    Executa um comando em uma thread separada e notifica via callbacks.
    
    Args:
        command: Comando a ser executado
        on_success: Callback chamado em caso de sucesso
        on_error: Callback chamado em caso de erro
        cwd: Diretório de trabalho
    """
    def _execute():
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd=cwd,
                encoding='utf-8',
                errors='replace'
            )
            
            if result.returncode == 0:
                on_success(result.stdout)
            else:
                on_error(result.stderr)
                
        except Exception as e:
            on_error(str(e))
    
    thread = threading.Thread(target=_execute, daemon=True)
    thread.start()
    return thread

def open_file_dialog(
    title: str = "Selecionar arquivo",
    file_types: list = [("Todos os arquivos", "*.*")],
    initial_dir: Optional[str] = None
) -> Optional[str]:
    """
    Abre um diálogo de seleção de arquivo.
    
    Args:
        title: Título do diálogo
        file_types: Lista de tipos de arquivo
        initial_dir: Diretório inicial
    
    Returns:
        Caminho do arquivo selecionado ou None
    """
    try:
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        
        file_path = filedialog.askopenfilename(
            title=title,
            filetypes=file_types,
            initialdir=initial_dir
        )
        
        root.destroy()
        return file_path if file_path else None
        
    except Exception as e:
        print(f"Erro ao abrir diálogo de arquivo: {e}")
        return None

def save_file_dialog(
    content: str,
    default_name: str = "resultado.md",
    file_types: list = [("Markdown", "*.md"), ("Todos os arquivos", "*.*")],
    initial_dir: Optional[str] = None
) -> Optional[str]:
    """
    Salva conteúdo em um arquivo via diálogo.
    
    Args:
        content: Conteúdo a ser salvo
        default_name: Nome padrão do arquivo
        file_types: Lista de tipos de arquivo
        initial_dir: Diretório inicial
    
    Returns:
        Caminho do arquivo salvo ou None
    """
    try:
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        
        file_path = filedialog.asksaveasfilename(
            initialfile=default_name,
            filetypes=file_types,
            initialdir=initial_dir
        )
        
        root.destroy()
        
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return file_path
            
        return None
        
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return None

def open_directory_dialog(title: str = "Selecionar diretório") -> Optional[str]:
    """
    Abre um diálogo de seleção de diretório.
    
    Args:
        title: Título do diálogo
    
    Returns:
        Caminho do diretório selecionado ou None
    """
    try:
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        
        folder_path = filedialog.askdirectory(title=title)
        
        root.destroy()
        return folder_path if folder_path else None
        
    except Exception as e:
        print(f"Erro ao abrir diálogo de diretório: {e}")
        return None

def open_in_browser(file_path: str) -> bool:
    """
    Abre um arquivo no navegador.
    
    Args:
        file_path: Caminho do arquivo
    
    Returns:
        True se sucesso, False caso contrário
    """
    try:
        if os.path.exists(file_path):
            webbrowser.open(f'file://{os.path.abspath(file_path)}')
            return True
        return False
    except Exception as e:
        print(f"Erro ao abrir no navegador: {e}")
        return False

def validate_dart_project(project_path: str) -> tuple[bool, str]:
    """
    Valida se o diretório contém um projeto Dart/Flutter válido.
    
    Args:
        project_path: Caminho do projeto
    
    Returns:
        Tupla (é_válido, mensagem)
    """
    if not os.path.exists(project_path):
        return False, "Diretório não existe"
    
    if not os.path.isdir(project_path):
        return False, "Caminho não é um diretório"
    
    # Verifica se tem pubspec.yaml (projeto Flutter/Dart)
    pubspec_path = os.path.join(project_path, "pubspec.yaml")
    if os.path.exists(pubspec_path):
        return True, "Projeto válido"
    
    # Verifica se tem pelo menos um arquivo .dart
    dart_files = [f for f in os.listdir(project_path) if f.endswith('.dart')]
    if dart_files:
        return True, "Projeto Dart básico"
    
    return False, "Nenhum arquivo Dart encontrado"