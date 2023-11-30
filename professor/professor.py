import random

lvl = 0

def(main):
    get_level()
    

def get_level:
    try:
        lvl = int(input("Level: "))
        if lvl in [1, 2, 3]:
            return lvl

    except:
        raise ValueError

def generate_integer(lvl):
    random_number = random.randint(1, lvl)
    return random_number

if __name__ = "__main__":
    main()