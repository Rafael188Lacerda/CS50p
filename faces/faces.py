def main():
    phrase = input()
    phrase = convert(phrase)
    print(phrase)

def convert(phrase):
    phrase1 = phrase.replace(":)", '🙂')
    phrase2 = phrase1.replace(":(", '🙁')
    return phrase2

main()




emoji = str(input("Input: "))

if emoji == ':1st_place_medal:':
    print("Output: ", '🥇')

elif emoji == ':money_bag:':
    print("Output: ", '💰')

elif emoji == ':candy:':
    print("Output: ", '🍬')