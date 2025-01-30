def main():
    while True:
        fuel = input("fraction: ").strip()
        try:
            fuelperc = convert(fuel)
            result = gauge(fuelperc)
            print(result)
            break
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zd:
            print(f"Error: {zd}")

def convert(fuel):
    try:
        x, y = map(int, fuel.split("/"))

        if y == 0:
            raise ZeroDivisionError("DivisionErr")
        if x > y:
            raise ValueError("ValErr")

        return round((x / y) * 100)

    except ValueError:
        raise ValueError("ValErr")
    except ZeroDivisionError:
        raise ZeroDivisionError("DivisionErr")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
