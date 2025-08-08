from dataclasses import dataclass
from typing import List

@dataclass
class FunctionCall:
    nome: str
    arquivo: str

@dataclass
class ParametroInfo:
    nome: str
    tipo: str
    valor_padrao: str
    eh_obrigatorio: bool
    eh_nomeado: bool

@dataclass
class FuncaoInfo:
    nome: str
    arquivo: str
    tipo_retorno: str
    parametros: List[ParametroInfo]
    invocacoes: List[FunctionCall]
    invocadores: List[FunctionCall]
