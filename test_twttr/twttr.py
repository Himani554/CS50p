def main():
    twitter = input("Input: ").strip()
    twttr = shorten(twitter)
    print(twttr)

def shorten(twitter):
    for letter in twitter:
        if letter in ["a","e","i","o","u","A","E","I","O","U"]:
            twitter = twitter.replace(letter,"")
    return(twitter)


if __name__ == "__main__":
    main()
