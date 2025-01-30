expression = input("Expression: ").strip()
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(float(x/z))
else:
    print("Error")

