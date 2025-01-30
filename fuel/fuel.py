def main():
    per = percent()
    if per >= 99:
        print("F")
    elif per <= 1:
        print("E")
    else:
        print(f"{per}%")
def percent():
    while True:
        try:
            s = input("Fraction: ").strip()
            x, y = s.split("/")
            f = int(x)/int(y)
            percent = round(f*100)
            if percent > 100:
                pass
            elif percent < 0:
                pass
            else:
                return percent

        except (ValueError, ZeroDivisionError):
            pass

main()
