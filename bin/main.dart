import 'package:args/args.dart';
import 'package:dart_function_analyzer/dart_function_analyzer.dart';

void main(List<String> args) {
  final parser = ArgParser()
    ..addFlag('avancado', abbr: 'a', help: 'Modo avançado de análise')
    ..addOption('funcao', help: 'Analisar função específica')
    ..addOption('output', abbr: 'o', defaultsTo: 'mapa_funcional.md', help: 'Arquivo de saída')
    ..addOption('agrupar', 
      defaultsTo: 'modulo',  // ← MUDADO de 'arquivo' para 'modulo'
      allowed: ['modulo', 'funcao'],  // ← MUDADO de ['arquivo', 'funcao'] para ['modulo', 'funcao']
      help: 'Agrupar resultados por: [modulo|funcao]');

  final results = parser.parse(args);

  if (results.rest.isEmpty) {
    print('Uso: dart run bin/main.dart [caminho/do/projeto] [opções]');
    print(parser.usage);
    return;
  }

  final projectPath = results.rest[0];
  final modoAvancado = results['avancado'] as bool;
  final funcaoEspecifica = results['funcao'] as String?;
  final outputFile = results['output'] as String;
  final agruparPor = results['agrupar'] as String? ?? 'modulo';  // ← MUDADO de 'arquivo' para 'modulo'

  print('Analisando projeto em: $projectPath');
  print('Modo avançado: ${modoAvancado ? 'Sim' : 'Não'}');
  print('Agrupar por: $agruparPor');
  if (funcaoEspecifica != null) {
    print('Função específica: $funcaoEspecifica');
  }

  try {
    final analyzer = ProjectAnalyzer(projectPath);
    analyzer.analyze(
      modoAvancado: modoAvancado,
      funcaoEspecifica: funcaoEspecifica,
      outputFile: outputFile,
      agruparPor: agruparPor,
    );
  } catch (e) {
    print('❌ Erro durante a análise: $e');
  }
}