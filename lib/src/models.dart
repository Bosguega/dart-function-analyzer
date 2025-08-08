class ParametroInfo {
  final String nome;
  final String tipo;
  final String valorPadrao;
  final bool ehObrigatorio;
  final bool ehNomeado;

  ParametroInfo({
    required this.nome,
    required this.tipo,
    this.valorPadrao = '',
    this.ehObrigatorio = true,
    this.ehNomeado = false,
  });
}

class FuncaoInfo {
  final String nome;
  final String arquivo;
  final String tipoRetorno;
  final List<ParametroInfo> parametros;
  final List<FunctionCall> invocacoes;
  final List<FunctionCall> invocadores;

  FuncaoInfo({
    required this.nome,
    required this.arquivo,
    required this.tipoRetorno,
    required this.parametros,
    required this.invocacoes,
    required this.invocadores,
  });
}

class FunctionCall {
  final String nome;
  final String arquivo;

  FunctionCall({required this.nome, required this.arquivo});
}

