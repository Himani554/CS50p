def main():
    time = input("What time is it? ").strip()
    ftime = convert(time)
    if ftime > 6.99 and ftime < 8.01:
        print("breakfast time")
    elif ftime > 11.99 and ftime < 13.01:
        print("lunch time")
    elif ftime > 17.99 and ftime < 19.01:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minute = minutes/60
    return float(f"{(hours + minute):.2f}")



if __name__ == "__main__":
    main()
