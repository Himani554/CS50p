groceries = {}
while True:
    try:
        item = input().upper().strip()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        for item in sorted(groceries):
            print(groceries[item],item)
        break
