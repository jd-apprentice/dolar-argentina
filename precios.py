from servicios.fetch import dolarBlue
from values import getValues

def verPrecios():
    valor_dolar = dolarBlue().get("sell_price")
    dolares = getValues() / valor_dolar
    redondear = round(dolares, 2)
    return redondear