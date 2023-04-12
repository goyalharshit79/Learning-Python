enter = input("Enter : ").strip()

s = "aeiouAEIOU"

for _ in enter:
    if _ in s:
        enter = enter.replace(_,"")
print(enter)