from utils.values import get_values

def to_string():
    dolares = get_values()
    print("Tenes $" + str(dolares) + " dolares")

if __name__ == "__main__":
    to_string()