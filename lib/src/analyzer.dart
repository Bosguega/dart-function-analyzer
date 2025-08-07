import 'dart:io';
import 'package:analyzer/dart/analysis/utilities.dart';
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart';
import 'package:analyzer/dart/analysis/features.dart';
import 'package:path/path.dart' as path;
import 'models.dart';
import 'markdown_generator.dart';

class ProjectAnalyzer {
  final String projectPath;
  final List<String> excludedFolders = [
    '.dart_tool',
    'build',
    '.git',
    'android',
    'ios',
    'web',
    'linux',
    'windows',
    'macos'
  ];

  ProjectAnalyzer(this.projectPath) {
    print("ProjectAnalyzer criado para: $projectPath");
  }

  Future<void> analyze({
    required bool modoAvancado,
    String? funcaoEspecifica,
    required String outputFile,
    required String agruparPor,
  }) async {
    print("=== INICIANDO MÉTODO ANALYZE ===");
    try {
      final dartFiles = await _collectDartFiles();
      print('📁 Encontrados ${dartFiles.length} módulos Dart');
      
      final functions = <String, FuncaoInfo>{};

      for (final file in dartFiles) {
        print('⚙️ Analisando: $file');
        
        // Verifica se o arquivo existe e tem conteúdo
        final fileObj = File(file);
        if (!await fileObj.exists()) {
          print('❌ Arquivo não existe: $file');
          continue;
        }
        
        final content = await fileObj.readAsString();
        print('📄 Conteúdo do módulo (${content.length} caracteres):');
        print('---');
        print(content);
        print('---');
        
        final parseResult = parseFile(
          path: file,
          featureSet: FeatureSet.latestLanguageVersion(),
        );
        
        // Verifica erros de parsing
        if (parseResult.errors.isNotEmpty) {
          print('❌ Erros de parsing:');
          for (final error in parseResult.errors) {
            final lineNumber = parseResult.lineInfo.getLocation(error.offset).lineNumber;
            print('   - ${error.message} (linha $lineNumber)');
          }
        }
        
        final visitor = FunctionVisitor(file);
        parseResult.unit.accept(visitor);
        functions.addAll(visitor.functions);
        print('   → ${visitor.functions.length} funções encontradas');
      }

      print('🔗 Construindo grafo de dependências...');
      final dependencyGraph = _buildDependencyGraph(functions);
      print('   → Grafo com ${dependencyGraph.length} funções');
      
      print('📝 Gerando Markdown em: $outputFile');
      await MarkdownGenerator.generate(
        functions: dependencyGraph,
        modoAvancado: modoAvancado,
        funcaoEspecifica: funcaoEspecifica,
        outputFile: outputFile,
        agruparPor: agruparPor,
      );
      
      print('✅ Análise concluída! Arquivo salvo em: ${Directory.current.path}\\$outputFile');
    } catch (e, stackTrace) {
      print('❌ ERRO EM ANALYZE: $e');
      print('Stack trace: $stackTrace');
    }
  }

  Future<List<String>> _collectDartFiles() async {
    final files = <String>[];
    final directory = Directory(projectPath);
    
    await for (final entity in directory.list(recursive: true, followLinks: false)) {
      if (entity is File && entity.path.endsWith('.dart')) {
        final relativePath = path.relative(entity.path, from: projectPath);
        final parts = path.split(relativePath);
        
        if (!excludedFolders.contains(parts.first)) {
          files.add(entity.path);
        }
      }
    }
    
    return files;
  }

  Map<String, FuncaoInfo> _buildDependencyGraph(Map<String, FuncaoInfo> functions) {
    // Criamos um mapa rápido para busca
    final functionMap = <String, FuncaoInfo>{};
    for (final func in functions.values) {
      functionMap['${func.arquivo}:${func.nome}'] = func;
    }

    // Criamos um novo mapa para não modificar o original durante a iteração
    final newFunctions = <String, FuncaoInfo>{};

    // Agora resolvemos as dependências
    for (final func in functions.values) {
      // Criamos uma nova lista de invocações com os módulos corretos
      final novasInvocacoes = <FunctionCall>[];
      
      for (final call in func.invocacoes) {
        // Procuramos a função invocada
        for (final target in functions.values) {
          if (target.nome == call.nome) {
            // Criamos um novo FunctionCall com o módulo correto
            novasInvocacoes.add(FunctionCall(
              nome: call.nome,
              arquivo: target.arquivo,
            ));
            break;
          }
        }
      }
      
      // Criamos um novo FuncaoInfo com as invocações atualizadas
      newFunctions['${func.arquivo}:${func.nome}'] = FuncaoInfo(
        nome: func.nome,
        arquivo: func.arquivo,
        tipoRetorno: func.tipoRetorno,
        parametros: func.parametros,
        invocacoes: novasInvocacoes,
        invocadores: [], // Inicialmente vazio, será preenchido depois
      );
    }

    // Agora adicionamos os invocadores corretos
    for (final entry in newFunctions.entries) {
      final func = entry.value;
      final invocadoresAtualizados = <FunctionCall>[];
      
      // Procuramos por todas as invocações que apontam para esta função
      for (final otherFunc in newFunctions.values) {
        for (final call in otherFunc.invocacoes) {
          if (call.nome == func.nome && call.arquivo == func.arquivo) {
            invocadoresAtualizados.add(FunctionCall(
              nome: otherFunc.nome,
              arquivo: otherFunc.arquivo,
            ));
          }
        }
      }
      
      // Atualizamos a função com os invocadores corretos
      newFunctions[entry.key] = FuncaoInfo(
        nome: func.nome,
        arquivo: func.arquivo,
        tipoRetorno: func.tipoRetorno,
        parametros: func.parametros,
        invocacoes: func.invocacoes,
        invocadores: invocadoresAtualizados,
      );
    }
    
    return newFunctions;
  }
}

class FunctionVisitor extends RecursiveAstVisitor<void> {
  final String filePath;
  final Map<String, FuncaoInfo> functions = {};

  FunctionVisitor(this.filePath);

  @override
  void visitMethodDeclaration(MethodDeclaration node) {
    _processFunction(
      nome: node.name.lexeme,
      retorno: node.returnType?.toSource(),
      corpo: node.body,
      parametros: node.parameters,
    );
    super.visitMethodDeclaration(node);
  }

  @override
  void visitFunctionDeclaration(FunctionDeclaration node) {
    _processFunction(
      nome: node.name.lexeme,
      retorno: node.returnType?.toSource(),
      corpo: node.functionExpression.body,
      parametros: node.functionExpression.parameters,
    );
    super.visitFunctionDeclaration(node);
  }

  void _processFunction({
    required String nome,
    required String? retorno,
    required AstNode? corpo,
    required FormalParameterList? parametros,
  }) {
    print('🔍 Função encontrada: $nome no módulo $filePath');
    
    // Extrai parâmetros
    final listaParametros = <ParametroInfo>[];
    if (parametros != null) {
      for (final param in parametros.parameters) {
        listaParametros.add(_extrairParametro(param));
      }
    }
    
    // Extrai invocações
    final invocacoes = <FunctionCall>[];
    corpo?.accept(FunctionCallVisitor(invocacoes));
    
    print('   → Tipo de retorno: ${retorno ?? "dynamic"}');
    print('   → Parâmetros: ${listaParametros.length}');
    print('   → Invocações encontradas: ${invocacoes.length}');
    
    functions[nome] = FuncaoInfo(
      nome: nome,
      arquivo: filePath,
      tipoRetorno: retorno ?? 'dynamic',
      parametros: listaParametros,
      invocacoes: invocacoes,
      invocadores: [],
    );
  }

  ParametroInfo _extrairParametro(FormalParameter param) {
  String nome = '';
  String tipo = 'dynamic';
  String valorPadrao = '';
  bool ehObrigatorio = true;
  bool ehNomeado = false;

  try {
    if (param is SimpleFormalParameter) {
      // Parâmetro simples: int x
      nome = param.name?.lexeme ?? '';
      tipo = param.type?.toSource() ?? 'dynamic';
      ehObrigatorio = param.requiredKeyword != null;
    } else if (param is DefaultFormalParameter) {
      // Parâmetro com valor padrão: int x = 10
      final normalParam = param.parameter;
      if (normalParam is SimpleFormalParameter) {
        nome = normalParam.name?.lexeme ?? '';
        tipo = normalParam.type?.toSource() ?? 'dynamic';
      }
      valorPadrao = param.defaultValue?.toSource() ?? '';
      ehObrigatorio = false;
    } else if (param is FieldFormalParameter) {
      // Parâmetro nomeado: this.x
      nome = param.name?.lexeme ?? '';
      tipo = param.type?.toSource() ?? 'dynamic';
      ehNomeado = true;
      ehObrigatorio = param.requiredKeyword != null;
    } else if (param is FunctionTypedFormalParameter) {
      // Parâmetro que é função: void Function() callback
      nome = param.name?.lexeme ?? '';
      tipo = param.returnType?.toSource() ?? 'dynamic';
      final params = param.parameters?.parameters.map((p) => p.toSource()).join(', ') ?? '';
      tipo += ' Function($params)';
    }
  } catch (e) {
    print('⚠️ Erro ao extrair parâmetro: $e');
    nome = 'unknown';
    tipo = 'dynamic';
  }

  return ParametroInfo(
    nome: nome.isNotEmpty ? nome : 'unnamed',
    tipo: tipo,
    valorPadrao: valorPadrao,
    ehObrigatorio: ehObrigatorio,
    ehNomeado: ehNomeado,
  );
}


}

class FunctionCallVisitor extends RecursiveAstVisitor<void> {
  final List<FunctionCall> calls;

  FunctionCallVisitor(this.calls);

  @override
  void visitMethodInvocation(MethodInvocation node) {
    calls.add(FunctionCall(
      nome: node.methodName.name,
      arquivo: '', // Será preenchido depois
    ));
    super.visitMethodInvocation(node);
  }
}