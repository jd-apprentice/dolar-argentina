## Imports
from layout.menu import Menu
from utils.constants import MENU_OPTIONS
from utils.result import to_string

if __name__ == "__main__":
    getResponse = Menu(MENU_OPTIONS) ## Get the response from the menu
    print(to_string(getResponse)) ## Print the response
