d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

menu = dict()

for _ in d:
    i = _.lower()
    menu[i] = d.get(_)


bill = 0

while True:
    try:
        item = input("Item : ").strip().lower()
        if item in menu:
            bill = bill + menu.get(item)
            print(f"Total : ${bill:.2f}")
        else:
            continue
    except EOFError:
        print("\n")
        break
