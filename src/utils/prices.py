## Imports
from services.fetch import dolar_blue, dolar_oficial
from utils.values import get_values
import sys

def view_blue(): ## Get the dolar blue
    try:
        dolar_value = float(dolar_blue().get("venta"))
        dolars = get_values() / dolar_value
        return round(dolars, 2)
    except ValueError:
        print("No se permiten letras")
        return view_blue()

def view_oficial(): ## Get the dolar oficial
    try:
        dolar_value = float(dolar_oficial().get("venta"))
        dolars = get_values() / dolar_value
        return round(dolars, 2)
    except ValueError:
        print("No se permiten letras")
        return view_oficial()
