from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()
print(len(sys.argv))
if len(sys.argv) == 1:
    inp = input("Enter: ")

    print(figlet.renderText(inp))

elif len(sys.argv) == 3:

    try:
        if (sys.argv[1] != "-f" and sys.argv[1] != "-font"):
            sys.exit("Usage: figlet.py [-t] [font]")

        elif sys.argv[2] not in fonts:
            sys.exit("Usage: figlet.py [-t] [font]")
        else:
            inp = input("Enter: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(inp))
    except:
        sys.exit("Usage: figlet.py [-t] [font]")
else:
    sys.exit("Usage: figlet.py [-t] [font]")