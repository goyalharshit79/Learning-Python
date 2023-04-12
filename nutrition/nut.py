import csv

def main():
    name = "nut.csv"
    data = parser(name)
    enter = input("Item : ").lower().strip()
    print(data)

    if enter in data:
        print(data[enter])
    else:
        exit

def parser(name):
    file = open(name,"r")
    file = csv.reader(file)

    fruits = dict()

    for _ in file:
        fruits[_[0].lower()] = _[1]
    return fruits

main()
