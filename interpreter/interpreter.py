exp = input("Enter the expression you want to calculate : ")

x,y,z = exp.split(" ")

x = float(x)
z = float(z)


if y == "+":
    r = x + z
if y == "-":
    r = x - z
if y == "*":
    r = x*z
if y == "/":
    r = x / z
print(r)

