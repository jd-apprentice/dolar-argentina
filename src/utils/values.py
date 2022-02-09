def get_values(): ## Get amount of pesos
    try:
        argentine_pesos = float(input("¿Cuantos pesos tenes? -> "))
        return argentine_pesos
    except TypeError:
        print("Tipo de dato incorrecto")