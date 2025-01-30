import random


def main():
    level = get_level()
    score = generate_integer(level)
    print("Score:",score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    total = [0]
    for j in range(10):
        try:
            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
            elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
            else:
                x = random.randint(100,999)
                y = random.randint(100,999)
            i = 0
            while i<3:
                ques = int(input(f"{x} + {y} = "))
                z = x+y
                if ques == z:
                    total[0] += 1
                    break
                else:
                    print("EEE🥶🤮")
                    if i == 2:
                        print(f"{x} + {y} = ",z)
                i=i+1

        except ValueError:
            pass
    return(total[0])

if __name__ == "__main__":
    main()



