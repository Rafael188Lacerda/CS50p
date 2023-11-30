def main():
    shorten(str)


def shorten(str):

    # Prompt for a str
    str = input("What do you want to say: ")

    # Remember a str is also a list
    for letter in str:
        if letter not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            print(letter, end="")

    print()

if __name__ == "__main__":
    main()