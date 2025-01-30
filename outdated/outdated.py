months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        month = month.replace(" ","")
        year = year.replace(" ","")
        if (int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            o_month, o_day, year = date.split(" ")
            for i in range(len(months)):
                if o_month == months[i]:
                    month = i + 1
            if o_day.endswith(","):
                day = o_day.replace(",","").replace(" ","")

            if (int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")


