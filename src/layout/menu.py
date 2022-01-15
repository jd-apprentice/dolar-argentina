def Menu(options): ## Create the menu
    print("\n")
    for key, value in options.items():
        print(f"{key}. {value}")
    print("\n")
    response = input("Que deseas consultar? -> ")
    return int(response)