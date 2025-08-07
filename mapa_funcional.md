# Mapa Funcional do Projeto

## 📁 Módulo: main.dart

### 🔧 Função: buscarDadosDoBanco
- **Tipo:** `String`
- **Módulo:** `main.dart`
- **Assinatura:** `String buscarDadosDoBanco()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - carregarConfig – main.dart
- **Árvore de invocações:**

### 🔧 Função: carregarConfig
- **Tipo:** `String`
- **Módulo:** `main.dart`
- **Assinatura:** `String carregarConfig()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - buscarDadosDoBanco – main.dart
- **É invocada por:**
  - iniciarApp – main.dart
- **Árvore de invocações:**
  buscarDadosDoBanco

### 🔧 Função: iniciarApp
- **Tipo:** `String`
- **Módulo:** `main.dart`
- **Assinatura:** `String iniciarApp()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - carregarConfig – main.dart
- **É invocada por:**
  - main – main.dart
- **Árvore de invocações:**
  carregarConfig
    buscarDadosDoBanco

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

