# Dict
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

bill = 0

# Prompt the user for the order
while True:
    try:
        food = input("Order: ").title()

        if food in menu:
            bill += menu[food]
            print("Total Bill: $", end="")
            print("{:.2f}".format(bill))

    except EOFError:
        print()
        break