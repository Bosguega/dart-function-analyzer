# Dart Function Analyzer

[![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)](https://dart.dev)
[![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)](https://flutter.dev)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Uma ferramenta de linha de comando para analisar projetos Dart/Flutter e gerar documentação funcional detalhada em formato Markdown.

## 🎯 Objetivo

O Dart Function Analyzer foi desenvolvido para ajudar desenvolvedores e equipes a:

- **Mapear dependências** entre funções em projetos Dart/Flutter
- **Gerar documentação automática** do fluxo funcional
- **Identificar acoplamentos** e pontos de refatoração
- **Facilitar o entendimento** de código legado ou complexo
- **Documentar o impacto** de mudanças críticas

## ✨ Características Principais

### 🔍 Análise Completa
- **Extração de funções**: Detecta todos os tipos de funções e métodos
- **Parâmetros detalhados**: Tipo, valor padrão, obrigatoriedade e se é nomeado
- **Tipo de retorno**: Identifica o tipo de retorno de cada função
- **Dependências**: Mapeia todas as invocações entre funções

### 📊 Saída Profissional
- **Formato Markdown**: Gera documentação legível e versionável
- **Agrupamento flexível**: Por módulo ou por função
- **Assinaturas completas**: Mostra a assinatura exata de cada função
- **Árvore de invocações**: Visualização completa do fluxo de chamadas

### ⚙️ Modos de Operação
- **Modo Simples**: Mostra apenas dependências diretas
- **Modo Avançado**: Exibe a árvore completa de invocações transitivas
- **Análise específica**: Foco em uma função específica

## 🚀 Instalação

### Pré-requisitos
- [Dart SDK](https://dart.dev/get-dart) versão 3.0 ou superior

### Clonar o projeto
```bash
git clone https://github.com/seu-usuario/dart-function-analyzer.git
cd dart-function-analyzer

Instalar dependências

dart pub get

Opções Disponíveis
Opção
Descrição
Exemplo
--avancado ou -a
Modo avançado com árvore de invocações
--avancado
--funcao
Analisa uma função específica
--funcao=buscarDados
--output ou -o
Arquivo de saída (padrão: mapa_funcional.md)
--output=analise.md
--agrupar
Agrupa resultados por: modulo ou funcao
--agrupar=modulo
Exemplos de Uso
1. Análise básica

dart run bin/main.dart ./meu_projeto_flutter

2. Modo avançado agrupado por módulo

dart run bin/main.dart ./meu_projeto_flutter --avancado --agrupar=modulo

3. Análise de função específica

dart run bin/main.dart ./meu_projeto_flutter --funcao=authenticateUser --avançado

4. Saída customizada

dart run bin/main.dart ./meu_projeto_flutter --output=documentacao.md --agrupar=função

📋 Exemplo de Saída
Agrupado por Módulo

# Mapa Funcional do Projeto

## 📁 Módulo: main.dart

### 🔧 Função: main
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void main()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - iniciarApp – main.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  iniciarApp
    carregarConfig
      buscarDadosDoBanco

### 🔧 Função: iniciarApp
- **Tipo:** `String`
- **Módulo:** `main.dart`
- **Assinatura:** `String iniciarApp()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - carregarConfig – config.dart
- **É invocada por:**
  - main – main.dart
- **Árvore de invocações:**
  carregarConfig
    buscarDadosDoBanco

Agrupado por Função

### 🔧 Função: processarDados
- **Tipo:** `Future<Map<String, dynamic>>`
- **Módulo:** `services.dart`
- **Assinatura:** `Future<Map<String, dynamic>> processarDados(String id, {required bool validar, int timeout = 30})`
- **Parâmetros:**
  - `String id` (obrigatório, posicional)
  - `bool validar` (obrigatório, nomeado)
  - `int timeout = 30` (opcional, nomeado)
- **Invoca:**
  - buscarDados – database.dart
  - validarResposta – validators.dart
- **É invocada por:**
  - main – main.dart

🏗️ Arquitetura

dart-function-analyzer/
├── bin/
│   └── main.dart              # Ponto de entrada CLI
├── gui_flet/
│   └── main.py                 # Só inicializa o app e chama a tela principal
│   └── ui.py                   # Componentes e layout da interface
│   └── actions.py              # Funções que lidam com eventos (botões, cliques, etc.)
│   └── async_tasks.py          # Funções assíncronas de execução de análise
│   └── utils.py                # Funções auxiliares (formatação, logs, etc.)
├── lib/
│   ├── dart_function_analyzer.dart
│   └── src/
│       ├── analyzer.dart      # Lógica de análise
│       ├── models.dart        # Modelos de dados
│       └── markdown_generator.dart # Geração de saída
├── test/                      # Testes unitários
└── README.md                  # Esta documentação

🔧 Tecnologias Utilizadas
Dart: Linguagem principal
Analyzer Package: Análise estática de código Dart
Args: Parse de argumentos de linha de comando
Path: Manipulação de caminhos de arquivo
📊 Casos de Uso
1. Documentação de Projetos

# Gera documentação completa para um novo projeto
dart run bin/main.dart ./novo_projeto --avancado --output=docs/mapa_funcional.md

2. Análise de Impacto

# Verifica quem depende de uma função crítica
dart run bin/main.dart ./projeto --funcao=processarPagamento --avançado

3. Code Review

# Analisa acoplamentos antes de refatorar
dart run bin/main.dart ./projeto --agrupar=modulo > analise_acoplamento.md

4. Onboarding de Novos Desenvolvedores

# Gera mapa funcional para ajudar no entendimento do código
dart run bin/main.dart ./projeto_legado --avançado

🛠️ Desenvolvimento
Executar Testes

dart test

Analisar Código

dart analyze

Formatar Código

dart format .

📈 Roadmap
 Suporte a métodos de classe com namespace (ex: Classe.metodo)
 Análise de impacto de mudanças
 Exportação em múltiplos formatos (JSON, CSV, DOT)
 Integração com IDEs (VS Code, Android Studio)
 Detecção de code smells
 Métricas de complexidade
 Interface web para visualização