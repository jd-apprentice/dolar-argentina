from services.fetch import dolar_blue
from utils.values import get_values

def view_prices():
    dolar_value = dolar_blue().get("sell_price")
    dolars = get_values() / dolar_value
    return round(dolars, 2)