import re

inp = "12/23/233"

if f1 := re.search("^[a-z]+ [0-9]+, [0-9]+$" , inp):
    print("ss")
elif f2 := re.search("^[0-9]+[/][0-9]+[/][0-9]+$" , inp):
    print("s2")
else:
    print("ff")