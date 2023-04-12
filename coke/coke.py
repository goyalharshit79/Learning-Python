amount = 50

paid = 0

while True:
    if amount == 0:
        print("Change Owed : 0")
        break
    if amount < 0:
        print("Change Owed : ", paid - 50)
        break
    enter = int(input("Insert coin : "))
    if enter in [25,10,5]:
        paid = paid + enter
        amount = amount - enter
        if amount <= 0:
            continue
        else:
            print("Amount Due : ", amount)
    else:
        print("Amount due : ",amount)
        continue

