# Mapa Funcional do Projeto

## 📁 Módulo: clock_widget.dart

### 🔧 Função: backgroundCallback
- **Tipo:** `void`
- **Módulo:** `clock_widget.dart`
- **Assinatura:** `void backgroundCallback(Uri? uri)`
- **Parâmetros:**
  - `Uri? uri` (opcional, posicional)
- **Invoca:**
  - updateClockWidget – clock_widget.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  updateClockWidget
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    updateWidget
      updateWidget
        updateWidget (recursão detectada)

### 🔧 Função: initializeWidget
- **Tipo:** `Future<void>`
- **Módulo:** `clock_widget.dart`
- **Assinatura:** `Future<void> initializeWidget()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - setAppGroupId – home_widget_wrapper.dart
  - registerBackgroundCallback – home_widget_wrapper.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  setAppGroupId
    setAppGroupId
      setAppGroupId (recursão detectada)
  registerBackgroundCallback
    registerBackgroundCallback
      registerBackgroundCallback (recursão detectada)

### 🔧 Função: updateClockWidget
- **Tipo:** `Future<void>`
- **Módulo:** `clock_widget.dart`
- **Assinatura:** `Future<void> updateClockWidget()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - saveWidgetData – home_widget_wrapper.dart
  - saveWidgetData – home_widget_wrapper.dart
  - saveWidgetData – home_widget_wrapper.dart
  - updateWidget – home_widget_wrapper.dart
- **É invocada por:**
  - backgroundCallback – clock_widget.dart
  - callbackDispatcher – main.dart
  - build – main.dart
  - initState – main.dart
  - _widgetClicked – main.dart
- **Árvore de invocações:**
  saveWidgetData
    saveWidgetData
      saveWidgetData (recursão detectada)
  saveWidgetData
    saveWidgetData
      saveWidgetData (recursão detectada)
  saveWidgetData
    saveWidgetData
      saveWidgetData (recursão detectada)
  updateWidget
    updateWidget
      updateWidget (recursão detectada)

## 📁 Módulo: home_widget_patch.dart

### 🔧 Função: createViewConfiguration
- **Tipo:** `ViewConfiguration`
- **Módulo:** `home_widget_patch.dart`
- **Assinatura:** `ViewConfiguration createViewConfiguration(Size logicalSize, double devicePixelRatio)`
- **Parâmetros:**
  - `Size logicalSize` (opcional, posicional)
  - `double devicePixelRatio` (opcional, posicional)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**

## 📁 Módulo: home_widget_wrapper.dart

### 🔧 Função: registerBackgroundCallback
- **Tipo:** `Future<bool>`
- **Módulo:** `home_widget_wrapper.dart`
- **Assinatura:** `Future<bool> registerBackgroundCallback(Function callback)`
- **Parâmetros:**
  - `Function callback` (opcional, posicional)
- **Invoca:**
  - registerBackgroundCallback – home_widget_wrapper.dart
- **É invocada por:**
  - initializeWidget – clock_widget.dart
  - registerBackgroundCallback – home_widget_wrapper.dart
- **Árvore de invocações:**
  registerBackgroundCallback
    registerBackgroundCallback (recursão detectada)

### 🔧 Função: saveWidgetData
- **Tipo:** `Future<bool>`
- **Módulo:** `home_widget_wrapper.dart`
- **Assinatura:** `Future<bool> saveWidgetData(String id, T data)`
- **Parâmetros:**
  - `String id` (opcional, posicional)
  - `T data` (opcional, posicional)
- **Invoca:**
  - saveWidgetData – home_widget_wrapper.dart
- **É invocada por:**
  - updateClockWidget – clock_widget.dart
  - updateClockWidget – clock_widget.dart
  - updateClockWidget – clock_widget.dart
  - saveWidgetData – home_widget_wrapper.dart
- **Árvore de invocações:**
  saveWidgetData
    saveWidgetData (recursão detectada)

### 🔧 Função: setAppGroupId
- **Tipo:** `Future<bool>`
- **Módulo:** `home_widget_wrapper.dart`
- **Assinatura:** `Future<bool> setAppGroupId(String groupId)`
- **Parâmetros:**
  - `String groupId` (opcional, posicional)
- **Invoca:**
  - setAppGroupId – home_widget_wrapper.dart
- **É invocada por:**
  - initializeWidget – clock_widget.dart
  - setAppGroupId – home_widget_wrapper.dart
- **Árvore de invocações:**
  setAppGroupId
    setAppGroupId (recursão detectada)

### 🔧 Função: updateWidget
- **Tipo:** `Future<bool>`
- **Módulo:** `home_widget_wrapper.dart`
- **Assinatura:** `Future<bool> updateWidget(String? name, String? androidName, String? iOSName, String? qualifiedAndroidName)`
- **Parâmetros:**
  - `String? name` (opcional, posicional)
  - `String? androidName` (opcional, posicional)
  - `String? iOSName` (opcional, posicional)
  - `String? qualifiedAndroidName` (opcional, posicional)
- **Invoca:**
  - updateWidget – home_widget_wrapper.dart
- **É invocada por:**
  - updateClockWidget – clock_widget.dart
  - updateWidget – home_widget_wrapper.dart
- **Árvore de invocações:**
  updateWidget
    updateWidget (recursão detectada)

## 📁 Módulo: main.dart

### 🔧 Função: _widgetClicked
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void _widgetClicked(Uri? uri)`
- **Parâmetros:**
  - `Uri? uri` (opcional, posicional)
- **Invoca:**
  - updateClockWidget – clock_widget.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  updateClockWidget
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    updateWidget
      updateWidget
        updateWidget (recursão detectada)

### 🔧 Função: build
- **Tipo:** `Widget`
- **Módulo:** `main.dart`
- **Assinatura:** `Widget build(BuildContext context)`
- **Parâmetros:**
  - `BuildContext context` (opcional, posicional)
- **Invoca:**
  - updateClockWidget – clock_widget.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  updateClockWidget
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    updateWidget
      updateWidget
        updateWidget (recursão detectada)

### 🔧 Função: callbackDispatcher
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void callbackDispatcher()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - updateClockWidget – clock_widget.dart
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**
  updateClockWidget
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    updateWidget
      updateWidget
        updateWidget (recursão detectada)

### 🔧 Função: createState
- **Tipo:** `State<ClockHomePage>`
- **Módulo:** `main.dart`
- **Assinatura:** `State<ClockHomePage> createState()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**

### 🔧 Função: dispose
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void dispose()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - dispose – main.dart
- **É invocada por:**
  - dispose – main.dart
- **Árvore de invocações:**
  dispose
    dispose (recursão detectada)

### 🔧 Função: initState
- **Tipo:** `void`
- **Módulo:** `main.dart`
- **Assinatura:** `void initState()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - initState – main.dart
  - updateClockWidget – clock_widget.dart
- **É invocada por:**
  - initState – main.dart
- **Árvore de invocações:**
  initState
    initState (recursão detectada)
  updateClockWidget
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    saveWidgetData
      saveWidgetData
        saveWidgetData (recursão detectada)
    updateWidget
      updateWidget
        updateWidget (recursão detectada)

## 📁 Módulo: widget_test.dart

### 🔧 Função: main
- **Tipo:** `void`
- **Módulo:** `widget_test.dart`
- **Assinatura:** `void main()`
- **Parâmetros:**
  - (nenhum)
- **Invoca:**
  - (nenhuma)
- **É invocada por:**
  - (nenhum)
- **Árvore de invocações:**

