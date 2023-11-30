# Prompt the user for a camelCase
camelCase = input("Place your camelCase variable here: ")

# Print snake_case
print("snake_case: ", end="")

# Remember String is a List, so
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")

print()