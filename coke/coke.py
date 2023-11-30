# Prompt the user for a coin, one at a time
total = 0

while total < 50:
    coin = int(input("Insert a coin: "))

    if coin == 5:
        total = total + coin
        amount_due = 50 - total
        print(f"Amount Due: {amount_due}")

    elif coin == 10:
        total = total + coin
        amount_due = 50 - total
        print(f"Amount Due: {amount_due}")

    elif coin == 25:
        total = total + coin
        amount_due = 50 - total
        print(f"Amount Due: {amount_due}")

    elif coin == 50:
        total = total + coin
        amount_due = 50 - total
        print(f"Amount Due: {amount_due}")

    else:
        amount_due = 50
        print(f"Amount Due: {amount_due}")

if amount_due > 0:
    print(f"Amount Due: {amount_due}")

if total == 50:
    print("Change Owed: 0")

else:
    change_owed = total - 50
    print(f"Change Owed: {change_owed}")