from pidar_api.pidar_modelo import run_model_pidar

def evaluate_form(pidar_form):
    print("evaluate_form 4", pidar_form)
    probability = run_model_pidar(pidar_form)
    return {'evaluate': probability}