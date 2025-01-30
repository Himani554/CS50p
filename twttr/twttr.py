
twitter = input("Input: ").strip()

for letter in twitter:
    if letter in ["a","e","i","o","u","A","E","I","O","U"]:
        twitter = twitter.replace(letter,"")
    print(twitter,end="")


