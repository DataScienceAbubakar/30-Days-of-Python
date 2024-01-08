# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the completed models."""
    print("\nCompleted models:")
    for model in completed_models:
        print(model)