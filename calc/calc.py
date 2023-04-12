def recogniser(s):
#returns a list of all the characters in the string entered
    var = []
    i = 0
    for _ in s:
        var.insert(i,_)
        i = i + 1
    return(var)

def main():
    exp = input("Enter the expression you want to calculate : ")
    chars = recogniser(exp)

    opers_list = []

    opers = "+-*/"

    i = 0
    for _ in chars:
        if _ in opers:
            opers_list.insert(i,_)



