import inflect

p = inflect.engine()

"""mylist = p.join(["apple", "banana", "carrot"])
print(mylist)"""

names = list()
while True:
    try:
        i = input("Enter: ")
        names.append(i)
    except EOFError:
        print("\n")
        print(f"Adieu, adieu, to {p.join(names)}")
        break