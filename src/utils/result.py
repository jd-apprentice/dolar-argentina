## Imports
from utils.prices import view_blue, view_oficial

def to_string(response): ## Convert to string
    if response == 1:
        dolares = view_blue()
        return f"A valor de dolar blue tenes ${dolares} dolares"
    elif response == 2:
        dolares = view_oficial()
        return f"A valor de dolar oficial tenes ${dolares} dolares"
    elif response == 3:
        return "Hasta luego!"
    else:
        return "Opcion invalida"