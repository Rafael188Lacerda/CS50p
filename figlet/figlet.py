import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = choice(list)
    figlet.setFont(font=random_font)
    x = input("Input: ")
    print(figlet.renderText(x))

elif sys.argv[1] == '-f'or sys.argv[1] == '--font':
    figlet.setFont(font=sys.argv[2])
    x = input("Input: ")
    print(figlet.renderText(x))

else:
    sys.exit("Error")