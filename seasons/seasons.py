
import inflect
from datetime import date
import sys


def main():
    date = input("Date of Birth: ").strip()
    inMin=correctDate(date)
    print(writeInWords(inMin))


def correctDate(s):
    try:
        a,b,c=s.split("-")
        birth_time = date(int(a),int(b),int(c))
        current_time=date.today()
        diff = (current_time - birth_time).total_seconds() /60
        return int(diff)
    except ValueError:
        sys.exit("Invalid Date")

def writeInWords(a):
    a=int(a)
    p=inflect.engine()
    words=p.number_to_words(a,andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
