import random

def main():

    l = taking_input()

    ans = random.randint(1 , l)

    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess < ans:
                print("Too small!")
            elif guess > ans:
                print("Too large!")
            elif guess == ans:
                print("Just right!")
                break
        except ValueError:
            pass

def taking_input():
    while True:
        try:
            level = input("Enter the level: ")
            if int(level) > 0:
                break
        except ValueError:
            pass

    return int(level)

if __name__ == "__main__":
    main()
