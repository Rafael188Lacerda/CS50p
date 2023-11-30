def main():
    inp: str = input("Input: ")
    print(shorten(inp))

def shorten(word: str):
    for i in range(len(word)):
        if word[i].lower() in ["a", "e", "i", "o", "u"]:
            word = word[:i] + "u" + word[i+1:]

    return word.replace("u", "")

if __name__ == "__main__":
    main()