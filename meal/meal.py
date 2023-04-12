def main():
    time = input("Enter the time : ")
    t = convert(time)

    if t >= 7 and t <= 8 :
        print("Breakfast time")

    if t >= 12 and t <= 13 :
        print("Lunch time")

    if t >= 18 and t <= 19 :
        print("Dinner time")

def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    minutes = minutes/60
    t = hours + minutes
    return(t)

if __name__ == "__main__":
    main()