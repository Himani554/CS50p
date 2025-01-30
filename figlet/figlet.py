import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

font = figlet.getFonts()
if len(sys.argv) == 1:
    ran = random.choice(figlet.getFonts())
    figlet.setFont(font=ran)
    word = input("Input: ")
    print(figlet.renderText(word),sep="\n")
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in list(font):
    figlet.setFont(font=sys.argv[2])
    word = input("Input: ")
    print(figlet.renderText(word),sep="\n")
else:
    sys.exit("Invalid usage")

