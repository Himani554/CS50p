import random

def numbers():
    while True:
        try:
            n = int(input("Level: "))
            number = random.randint(1,n)
            if n > 0:
                return number
            else:
                pass
        except ValueError:
            pass
number = numbers()

while True:
    try:
        guess = int(input("Guess: "))

        if guess < number:
            print("Too small!",end="\n")
        elif guess > number:
            print("Too large!",end="\n")
        else:
            print("Just right!",end="\n")
            break
    except ValueError:
        pass

