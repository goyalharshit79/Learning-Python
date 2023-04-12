def main():
    msg = input("Enter the input : ")
    cnvrtd = emoji_covertor(msg)
    print(cnvrtd)

def emoji_covertor(msg):
    words = msg.split()

    output = ""

    for _ in words:
        if _ == ":)":
            _ = "🙂"

        if _ == ":(":
            _ = "🙁"
        output = output + _ + " "
    return(output)

main()