from async_tasks import selecionar_projeto_async, executar_analise_async, run_async

def on_selecionar_projeto(e, project_path, page):
    def callback(result):
        if result:
            project_path.value = result
            page.update()

    run_async(selecionar_projeto_async(), callback)

def on_analisar(e, project_path, results_field, page):
    if not project_path.value or project_path.value == "Nenhum projeto selecionado":
        results_field.value = "Selecione um projeto primeiro!"
        page.update()
        return
    
    results_field.value = "Analisando..."
    page.update()

    def callback(result):
        results_field.value = result
        page.update()

    run_async(executar_analise_async(project_path.value), callback)
