# Mapa Funcional do Projeto

## 📁 Módulo: main.dart

### 🔧 Função: main
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void main(List<String> args)`
- **Parâmetros:**
  - `List<String> args` (opcional, posicional)
- **Invoca:**
  - analyze – analyzer.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  analyze
    _collectDartFiles
    _buildDependencyGraph
    generate
      _gerarPorModulo
        _escreverFuncao
          _gerarAssinatura
          _escreverArvoreDeInvocacoes
            _escreverArvoreDeInvocacoes
              _escreverArvoreDeInvocacoes (recursão detectada)
      _gerarPorFuncao
        _escreverFuncao
          _gerarAssinatura
          _escreverArvoreDeInvocacoes
            _escreverArvoreDeInvocacoes
              _escreverArvoreDeInvocacoes (recursão detectada)

## 📁 Módulo: analyzer.dart

### 🔧 Função: _buildDependencyGraph
- **Tipo:** `Map<String, FuncaoInfo>`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `Map<String, FuncaoInfo> _buildDependencyGraph(Map<String, FuncaoInfo> functions)`
- **Parâmetros:**
  - `Map<String, FuncaoInfo> functions` (opcional, posicional)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - analyze – analyzer.dart
- **Árvore de invocações:**

### 🔧 Função: _collectDartFiles
- **Tipo:** `Future<List<String>>`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `Future<List<String>> _collectDartFiles()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - analyze – analyzer.dart
- **Árvore de invocações:**

### 🔧 Função: _extrairParametro
- **Tipo:** `ParametroInfo`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `ParametroInfo _extrairParametro(FormalParameter param)`
- **Parâmetros:**
  - `FormalParameter param` (opcional, posicional)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - _processFunction – analyzer.dart
- **Árvore de invocações:**

### 🔧 Função: _processFunction
- **Tipo:** `void`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `void _processFunction(String nome, String? retorno, AstNode? corpo, FormalParameterList? parametros)`
- **Parâmetros:**
  - `String nome` (opcional, posicional)
  - `String? retorno` (opcional, posicional)
  - `AstNode? corpo` (opcional, posicional)
  - `FormalParameterList? parametros` (opcional, posicional)
- **Invoca:**
  - _extrairParametro – analyzer.dart
- **É invocada por:**
  - visitMethodDeclaration – analyzer.dart
  - visitFunctionDeclaration – analyzer.dart
- **Árvore de invocações:**
  _extrairParametro

### 🔧 Função: analyze
- **Tipo:** `Future<void>`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `Future<void> analyze(bool modoAvancado, String? funcaoEspecifica, String outputFile, String agruparPor)`
- **Parâmetros:**
  - `bool modoAvancado` (opcional, posicional)
  - `String? funcaoEspecifica` (opcional, posicional)
  - `String outputFile` (opcional, posicional)
  - `String agruparPor` (opcional, posicional)
- **Invoca:**
  - _collectDartFiles – analyzer.dart
  - _buildDependencyGraph – analyzer.dart
  - generate – markdown_generator.dart
- **É invocada por:**
  - main – main.dart
- **Árvore de invocações:**
  _collectDartFiles
  _buildDependencyGraph
  generate
    _gerarPorModulo
      _escreverFuncao
        _gerarAssinatura
        _escreverArvoreDeInvocacoes
          _escreverArvoreDeInvocacoes
            _escreverArvoreDeInvocacoes (recursão detectada)
    _gerarPorFuncao
      _escreverFuncao
        _gerarAssinatura
        _escreverArvoreDeInvocacoes
          _escreverArvoreDeInvocacoes
            _escreverArvoreDeInvocacoes (recursão detectada)

### 🔧 Função: visitFunctionDeclaration
- **Tipo:** `void`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `void visitFunctionDeclaration(FunctionDeclaration node)`
- **Parâmetros:**
  - `FunctionDeclaration node` (opcional, posicional)
- **Invoca:**
  - _processFunction – analyzer.dart
  - visitFunctionDeclaration – analyzer.dart
- **É invocada por:**
  - visitFunctionDeclaration – analyzer.dart
- **Árvore de invocações:**
  _processFunction
    _extrairParametro
  visitFunctionDeclaration
    visitFunctionDeclaration (recursão detectada)

### 🔧 Função: visitMethodDeclaration
- **Tipo:** `void`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `void visitMethodDeclaration(MethodDeclaration node)`
- **Parâmetros:**
  - `MethodDeclaration node` (opcional, posicional)
- **Invoca:**
  - _processFunction – analyzer.dart
  - visitMethodDeclaration – analyzer.dart
- **É invocada por:**
  - visitMethodDeclaration – analyzer.dart
- **Árvore de invocações:**
  _processFunction
    _extrairParametro
  visitMethodDeclaration
    visitMethodDeclaration (recursão detectada)

### 🔧 Função: visitMethodInvocation
- **Tipo:** `void`
- **Módulo:** `analyzer.dart`
- **Assinatura:** `void visitMethodInvocation(MethodInvocation node)`
- **Parâmetros:**
  - `MethodInvocation node` (opcional, posicional)
- **Invoca:**
  - visitMethodInvocation – analyzer.dart
- **É invocada por:**
  - visitMethodInvocation – analyzer.dart
- **Árvore de invocações:**
  visitMethodInvocation
    visitMethodInvocation (recursão detectada)

## 📁 Módulo: markdown_generator.dart

### 🔧 Função: _escreverArvoreDeInvocacoes
- **Tipo:** `void`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `void _escreverArvoreDeInvocacoes(StringBuffer buffer, FuncaoInfo func, Map<String, FuncaoInfo> allFunctions, int indent, Set<String>? visitados)`
- **Parâmetros:**
  - `StringBuffer buffer` (opcional, posicional)
  - `FuncaoInfo func` (opcional, posicional)
  - `Map<String, FuncaoInfo> allFunctions` (opcional, posicional)
  - `int indent` (opcional, posicional)
  - `Set<String>? visitados` (opcional, posicional)
- **Invoca:**
  - _escreverArvoreDeInvocacoes – markdown_generator.dart
- **É invocada por:**
  - _escreverFuncao – markdown_generator.dart
  - _escreverArvoreDeInvocacoes – markdown_generator.dart
- **Árvore de invocações:**
  _escreverArvoreDeInvocacoes
    _escreverArvoreDeInvocacoes (recursão detectada)

### 🔧 Função: _escreverFuncao
- **Tipo:** `void`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `void _escreverFuncao(StringBuffer buffer, FuncaoInfo func, bool modoAvancado, Map<String, FuncaoInfo> allFunctions)`
- **Parâmetros:**
  - `StringBuffer buffer` (opcional, posicional)
  - `FuncaoInfo func` (opcional, posicional)
  - `bool modoAvancado` (opcional, posicional)
  - `Map<String, FuncaoInfo> allFunctions` (opcional, posicional)
- **Invoca:**
  - _gerarAssinatura – markdown_generator.dart
  - _escreverArvoreDeInvocacoes – markdown_generator.dart
- **É invocada por:**
  - _gerarPorModulo – markdown_generator.dart
  - _gerarPorFuncao – markdown_generator.dart
- **Árvore de invocações:**
  _gerarAssinatura
  _escreverArvoreDeInvocacoes
    _escreverArvoreDeInvocacoes
      _escreverArvoreDeInvocacoes (recursão detectada)

### 🔧 Função: _gerarAssinatura
- **Tipo:** `String`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `String _gerarAssinatura(FuncaoInfo func)`
- **Parâmetros:**
  - `FuncaoInfo func` (opcional, posicional)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - _escreverFuncao – markdown_generator.dart
- **Árvore de invocações:**

### 🔧 Função: _gerarPorFuncao
- **Tipo:** `void`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `void _gerarPorFuncao(StringBuffer buffer, Map<String, FuncaoInfo> functions, bool modoAvancado)`
- **Parâmetros:**
  - `StringBuffer buffer` (opcional, posicional)
  - `Map<String, FuncaoInfo> functions` (opcional, posicional)
  - `bool modoAvancado` (opcional, posicional)
- **Invoca:**
  - _escreverFuncao – markdown_generator.dart
- **É invocada por:**
  - generate – markdown_generator.dart
- **Árvore de invocações:**
  _escreverFuncao
    _gerarAssinatura
    _escreverArvoreDeInvocacoes
      _escreverArvoreDeInvocacoes
        _escreverArvoreDeInvocacoes (recursão detectada)

### 🔧 Função: _gerarPorModulo
- **Tipo:** `void`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `void _gerarPorModulo(StringBuffer buffer, Map<String, FuncaoInfo> functions, bool modoAvancado)`
- **Parâmetros:**
  - `StringBuffer buffer` (opcional, posicional)
  - `Map<String, FuncaoInfo> functions` (opcional, posicional)
  - `bool modoAvancado` (opcional, posicional)
- **Invoca:**
  - _escreverFuncao – markdown_generator.dart
- **É invocada por:**
  - generate – markdown_generator.dart
- **Árvore de invocações:**
  _escreverFuncao
    _gerarAssinatura
    _escreverArvoreDeInvocacoes
      _escreverArvoreDeInvocacoes
        _escreverArvoreDeInvocacoes (recursão detectada)

### 🔧 Função: generate
- **Tipo:** `Future<void>`
- **Módulo:** `markdown_generator.dart`
- **Assinatura:** `Future<void> generate(Map<String, FuncaoInfo?> functions, bool modoAvancado, String? funcaoEspecifica, String outputFile, String agruparPor)`
- **Parâmetros:**
  - `Map<String, FuncaoInfo?> functions` (opcional, posicional)
  - `bool modoAvancado` (opcional, posicional)
  - `String? funcaoEspecifica` (opcional, posicional)
  - `String outputFile` (opcional, posicional)
  - `String agruparPor` (opcional, posicional)
- **Invoca:**
  - _gerarPorModulo – markdown_generator.dart
  - _gerarPorFuncao – markdown_generator.dart
- **É invocada por:**
  - analyze – analyzer.dart
- **Árvore de invocações:**
  _gerarPorModulo
    _escreverFuncao
      _gerarAssinatura
      _escreverArvoreDeInvocacoes
        _escreverArvoreDeInvocacoes
          _escreverArvoreDeInvocacoes (recursão detectada)
  _gerarPorFuncao
    _escreverFuncao
      _gerarAssinatura
      _escreverArvoreDeInvocacoes
        _escreverArvoreDeInvocacoes
          _escreverArvoreDeInvocacoes (recursão detectada)

