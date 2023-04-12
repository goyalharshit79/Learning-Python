while True:
    fuel = input("Enter : ")
    try:
        fuel = fuel.split("/")
        div = int(fuel[0]) / int(fuel[1])
        if div > 1:
            print("Fuel level can't be over 100%")
        elif div * 100 < 1:
            print("E")
            break
        elif div * 100 > 99:
            print("F")
            break
        else:
            per = round(div*100)
            print(f"{per}%" )
            break

    except (ValueError, ZeroDivisionError):
        print("Usage : Fuel level in the form of x/y")
        continue

    except:
        print("Usage : Fuel level in the form of x/y, where x and y are integers")
        continue
