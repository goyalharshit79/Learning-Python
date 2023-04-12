def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0] not in a or s[1] not in a:
        return False
    i = 0
    for _ in s:
        if _ in "0123456789":
            if s[::-1][0] in a:
                return False
            if s[i] == "0":
                return False
                break
            else:
                break
        i += 1
    for _ in s:
        if _ in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ":
            return False
            break

    return True


main()