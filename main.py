from values import getValues

def toString():
    dolares = getValues()
    print("Tenes $" + str(dolares) + " dolares")

if __name__ == "__main__":
    toString()