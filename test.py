import re

email = input(">")
shit =  re.search("^((\w+)(@))(\w+)(\.edu)$",email)
print(shit.group(3))