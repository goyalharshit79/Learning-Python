import random


def main():
    level = get_level()

    score = 0

    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        ans = num1 + num2

        _ = 1
        while True:
            print(f"{num1} + {num2} = " , end = "")
            a = get_answer()
            if a != ans:
                if _ < 3:
                    print("EEE")
                    pass
                elif _ >= 3:
                    print(f"{num1} + {num2} = {ans}")
                    break
            else:
                score += 1
                break
            _ += 1
    print(f"Your Score : {score}")



def get_answer():
    while True:
        try:
            ans = int(input())
            if type(ans) == int:
                break
        except ValueError:
            return None

    return ans

def get_level():

    while True:
        try:
            level = int(input("Level:  "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass

    return level

def generate_integer(level):

    if level not in [1,2,3]:
        raise ValueError
    else:
        if level == 1:
            start = 0
        else:
            start = 10 ** (level - 1)
        end = (10 ** level) - 1

        return random.randint(start,end)


if __name__ == "__main__":
    main()