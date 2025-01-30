import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    elif sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                line = 0
                for i in file:
                    if not i.lstrip().startswith("#") and not i.isspace():
                        line += 1
                print(line)
        except FileNotFoundError:
            sys.exit("File does not exist")

