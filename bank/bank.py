def main():
    greet = input("Greeting : ")
    greet = greet.strip().lower()
    greet = punc_remover(greet)
    print(greet)

    if greet[0] == "h":
        words = greet.split()
        if words[0] == "hello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


def punc_remover(s):
    #initially the presence of a punctuation was causing an issue
    #the following solution has been tried
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    processed_greet = ""

    for _ in s:
        if _ in punc:
            _ = ""
        processed_greet = processed_greet + _
    return(processed_greet)

main()