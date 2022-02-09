## Imports
from layout import Menu
from utils import to_string, MENU_OPTIONS

if __name__ == "__main__":
    getResponse = Menu(MENU_OPTIONS) ## Get the response from the menu
    print(to_string(getResponse)) ## Print the response