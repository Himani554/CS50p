
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    abc=re.findall(r"\b\W*um\b\W*",s,re.IGNORECASE)
    return len(abc)





if __name__ == "__main__":
    main()
