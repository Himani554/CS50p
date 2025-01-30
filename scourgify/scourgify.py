import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")
else:
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")
    else:
        output=[]
        try:
            with open (sys.argv[1],"r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last,first = row['name'].split(",")
                    output.append({'first':first.lstrip(),'last':last.lstrip(),'house':row["house"]})


        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        with open (sys.argv[2],"w") as file:
                writer = csv.DictWriter(file,fieldnames=["first","last","house"])
                writer.writerow({"first":"first","last":"last","house":"house"})
                for row in output:
                    writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})

