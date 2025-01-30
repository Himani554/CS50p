def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = float(d.replace("$",""))
    return dollar


def percent_to_float(p):
    Percnt = float(p.replace("%",""))
    Percent = Percnt/100
    return Percent


main()
