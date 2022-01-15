## Imports
from utils.prices import view_blue, view_oficial

def to_string(response): ## Convert to string
    if response == 1:
        dolares = view_blue()
        return f"El dolar blue es de ${dolares}"
    elif response == 2:
        dolares = view_oficial()
        return f"El dolar oficial es de ${dolares}"
    elif response == 3:
        return "Hasta luego!"
    elif response != type(int):
        return "Opcion invalida"