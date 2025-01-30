import sys
import csv
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open (sys.argv[1]) as file:
                reader = csv.reader(file)
                file = tabulate.tabulate(reader,headers="firstrow",tablefmt="grid")
                for row in file:
                    print(row,end="")
                print()
        except FileNotFoundError:
            sys.exit("File does not exit")



