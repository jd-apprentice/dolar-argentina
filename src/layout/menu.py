def Menu(options): ## Create the menu
    try:
        print("\n")
        for key, value in options.items():
            print(f"{key}. {value}")
        print("\n")
        response = input("Que deseas consultar? -> ")
        return int(response)
    except ValueError:
        print("Tipo de dato incorrecto")
        return Menu(options)