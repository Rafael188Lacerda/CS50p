def main():
    fraction = str(input("Fraction: "))
    percentage: int = convert(fraction)

    print(gauge(percentage))

def convert(fraction(str)):
    try:
        _split = fraction.split("/")

        x: int = int(_split[0])
        y: int = int(_split[1])

        return int(round((x/y)*100))

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    return(f"{percentage}%")

if __name__ == "__main__":
    main()