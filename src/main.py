from utils.prices import view_prices

def to_string():
    dolares = view_prices()
    print("Tenes $" + str(dolares) + " dolares")

if __name__ == "__main__":
    to_string()