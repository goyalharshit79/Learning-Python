camelCase = input("Enter : ")

list = []

for _ in camelCase:
    if _.isupper() == True:
        list.append("_")
        list.append(_)
    else:
        list.append(_)

print("".join(list).lower())