# Prompt the user for fraction
while True:
    fuel = input("Fraction: ")

# Condition for input
    try:
        x, y = fuel.split("/")

        x = int(x)
        y = int(y)

        fuel_tank = x / y

        if fuel_tank <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

# Define %
fuel_tank = round(fuel_tank * 100)

# Output
if fuel_tank >= 99:
    print("F")

elif fuel_tank <= 1:
    print("E")

else:
    print(f"{fuel_tank}%")