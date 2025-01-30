import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    abc= re.search(r"^([0-1]?[0-9]?):?([0-5]?[0-9]?) (AM|PM) to ([0-1]?[0-9]?):?([0-5]?[0-9]?) (AM|PM)$",s)
    if abc:
        abz=abc.groups()
        a = int(abz[0])
        b= int(abz[3])
        if (a <= 12) and (abz[2]=='AM') and (abz[5]=='PM') and (b<=12):
            if a == 12 or b==12:
                return  f"{12-a:02}:{abz[1]:02} to {b:02}:{abz[4]:02}"
            return f"{a:02}:{abz[1]:02} to {b+12:02}:{abz[4]:02}"
        elif (a <= 12) and (abz[2]=='AM') and (abz[5]=='AM') and (b<=12):
            if a == 12 or b==12:
                return  f"{12-a:02}:{abz[1]:02} to {b:02}:{abz[4]:02}"
            return f"{a:02}:{abz[1]:02} to {b:02}:{abz[4]:02}"
        elif (a <= 12) and (abz[2]=='PM') and (abz[5]=='AM') and (b<=12):
            if a == 12 or b==12:
                return  f"{12+a:02}:{abz[1]:02} to {b:02}:{abz[4]:02}"
            return f"{a+12:02}:{abz[1]:02} to {b:02}:{abz[4]:02}"
        elif (a <= 12) and (abz[2]=='PM') and (abz[5]=='PM') and (b<=12):
            if a == 12 or b==12:
                return  f"{12+a:02}:{abz[1]:02} to {b+12:02}:{abz[4]:02}"
            return f"{a+12:02}:{abz[1]:02} to {b+12:02}:{abz[4]:02}"
        else:
             raise ValueError
    else:
        raise ValueError




if __name__ == "__main__":
    main()
