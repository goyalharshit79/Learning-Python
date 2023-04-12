import re

def main():
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    inp = input(">").strip().lower()

    try:
        if f1 := re.search("^[a-z]+ [0-9]+, [0-9]+$" , inp):
            inp = inp.split(" ")

            if inp[0] in months:
                month = months.index(inp[0]) + 1
                day = int(inp[1].replace("," , ""))

                if day > 31:
                    main()
                    exit()
                else:
                    print(f"{inp[2]}-{month:02}-{day:02}")
        elif f2 := re.search("^[0-9]+[/][0-9]+[/][0-9]+$" , inp):
            inp = inp.split("/")
            inp = [int(_) for _ in inp]

            if inp[0] > 12 or inp[1] > 31:
                main()
                exit()
            else:
                print(f"{inp[2]}-{inp[0]:02}-{inp[1]:02}")
        else:
            main()
            exit()
    except:
        main()
        exit()

main()