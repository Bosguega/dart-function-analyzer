import 'dart:io';
import 'package:path/path.dart' as path;
import 'package:dart_function_analyzer/src/models.dart';

class MarkdownGenerator {
  static Future<void> generate({
    required Map<String, FuncaoInfo?> functions,
    required bool modoAvancado,
    String? funcaoEspecifica,
    required String outputFile,
    required String agruparPor,
  }) async {
    final buffer = StringBuffer();
    
    buffer.writeln('# Mapa Funcional do Projeto\n');
    
    // Filtra funções se especificado e remove nulos
    final funcoesParaExibir = <String, FuncaoInfo>{};
    
    if (funcaoEspecifica != null) {
      final func = functions[funcaoEspecifica];
      if (func != null) {
        funcoesParaExibir[funcaoEspecifica] = func;
      }
    } else {
      for (final entry in functions.entries) {
        if (entry.value != null) {
          funcoesParaExibir[entry.key] = entry.value!;
        }
      }
    }
    
    if (agruparPor == 'modulo') {
      _gerarPorModulo(buffer, funcoesParaExibir, modoAvancado);
    } else {
      _gerarPorFuncao(buffer, funcoesParaExibir, modoAvancado);
    }
    
    final file = File(outputFile);
    await file.writeAsString(buffer.toString());
    print('Mapa funcional gerado em: $outputFile');
  }
  
  static void _gerarPorModulo(StringBuffer buffer, Map<String, FuncaoInfo> functions, bool modoAvancado) {
    final porModulo = <String, List<FuncaoInfo>>{};
    
    for (final func in functions.values) {
      if (!porModulo.containsKey(func.arquivo)) {
        porModulo[func.arquivo] = [];
      }
      porModulo[func.arquivo]!.add(func);
    }
    
    final modulosOrdenados = porModulo.keys.toList()..sort();
    
    for (final modulo in modulosOrdenados) {
      buffer.writeln('## 📁 Módulo: ${path.basename(modulo)}\n');
      
      final funcoesOrdenadas = porModulo[modulo]!
        ..sort((a, b) => a.nome.compareTo(b.nome));
      
      for (final func in funcoesOrdenadas) {
        _escreverFuncao(buffer, func, modoAvancado, functions);
      }
    }
  }
  
  static void _gerarPorFuncao(StringBuffer buffer, Map<String, FuncaoInfo> functions, bool modoAvancado) {
    final funcoesOrdenadas = functions.values.toList()
      ..sort((a, b) => a.nome.compareTo(b.nome));
    
    for (final func in funcoesOrdenadas) {
      _escreverFuncao(buffer, func, modoAvancado, functions);
    }
  }
  
  static void _escreverFuncao(
    StringBuffer buffer,
    FuncaoInfo func,
    bool modoAvancado,
    Map<String, FuncaoInfo> allFunctions,
  ) {
    buffer.writeln('### 🔧 Função: ${func.nome}');
    buffer.writeln('- **Tipo:** `${func.tipoRetorno}`');
    buffer.writeln('- **Módulo:** `${path.basename(func.arquivo)}`');
    
    // Assinatura completa
    final assinatura = _gerarAssinatura(func);
    buffer.writeln('- **Assinatura:** `$assinatura`');
    
    // Parâmetros detalhados
    buffer.writeln('- **Parâmetros:**');
    if (func.parametros.isEmpty) {
      buffer.writeln('  - (nenhum)');
    } else {
      for (final param in func.parametros) {
        final tipoParametro = param.tipo.isNotEmpty ? param.tipo : 'dynamic';
        final valorPadrao = param.valorPadrao.isNotEmpty ? ' = ${param.valorPadrao}' : '';
        final obrigatorio = param.ehObrigatorio ? 'obrigatório' : 'opcional';
        final nomeado = param.ehNomeado ? 'nomeado' : 'posicional';
        
        buffer.writeln('  - `$tipoParametro ${param.nome}`$valorPadrao ($obrigatorio, $nomeado)');
      }
    }
    
    // Invocações
    buffer.writeln('- **Invoca:**');
    if (func.invocacoes.isEmpty) {
      buffer.writeln('  - (nenhuma)');
    } else {
      for (final call in func.invocacoes) {
        buffer.writeln('  - ${call.nome} – ${path.basename(call.arquivo)}');
      }
    }
    
    // Invocadores
    buffer.writeln('- **É invocada por:**');
    if (func.invocadores.isEmpty) {
      buffer.writeln('  - (nenhum)');
    } else {
      for (final caller in func.invocadores) {
        buffer.writeln('  - ${caller.nome} – ${path.basename(caller.arquivo)}');
      }
    }
    
    // Modo avançado
    if (modoAvancado) {
      buffer.writeln('- **Árvore de invocações:**');
      _escreverArvoreDeInvocacoes(buffer, func, allFunctions, indent: 2);
    }
    
    buffer.writeln();
  }
  
  static String _gerarAssinatura(FuncaoInfo func) {
    final parametros = func.parametros.map((param) {
      final valorPadrao = param.valorPadrao.isNotEmpty ? ' = ${param.valorPadrao}' : '';
      return '${param.tipo} ${param.nome}$valorPadrao';
    }).join(', ');
    
    return '${func.tipoRetorno} ${func.nome}($parametros)';
  }
  
  static void _escreverArvoreDeInvocacoes(
    StringBuffer buffer,
    FuncaoInfo func,
    Map<String, FuncaoInfo> allFunctions, {
    required int indent,
    Set<String>? visitados,
  }) {
    visitados ??= {};
    
    if (visitados.contains(func.nome)) {
      buffer.writeln('${' ' * indent}${func.nome} (recursão detectada)');
      return;
    }
    visitados.add(func.nome);
    
    for (final call in func.invocacoes) {
      final targetFunc = allFunctions.values.firstWhere(
        (f) => f.nome == call.nome,
        orElse: () => FuncaoInfo(
          nome: call.nome,
          arquivo: 'externa',
          tipoRetorno: 'desconhecido',
          parametros: [],
          invocacoes: [],
          invocadores: [],
        ),
      );
      
      buffer.writeln('${' ' * indent}${call.nome}');
      
      if (targetFunc.arquivo != 'externa') {
        _escreverArvoreDeInvocacoes(
          buffer,
          targetFunc,
          allFunctions,
          indent: indent + 2,
          visitados: visitados,
        );
      }
    }
    
    visitados.remove(func.nome);
  }
}