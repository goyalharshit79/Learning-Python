msg = input("Enter the message : ")

output = ""

for _ in msg:
    if _ == " ":
        _ = "..."
    output = output + _
print(output)


