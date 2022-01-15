## Imports
from services.fetch import dolar_blue, dolar_oficial
from utils.values import get_values

def view_blue() -> int: ## Get the dolar blue
    try:
        dolar_value = dolar_blue().get("sell_price")
        dolars = get_values() / dolar_value
        return round(dolars, 2)
    except ValueError:
        print("No se pudo obtener el dolar blue")

def view_oficial() -> int: ## Get the dolar oficial
    dolar_value = dolar_oficial().get("venta")
    dolars = get_values() / dolar_value
    return round(dolars, 2)
