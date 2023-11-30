str = input("Place here your arithmetic expression: ")

x, y, z = str.split(" ")

x = float(x)
z = float(z)

if y == '+':
    result = x + z

elif y == '-':
    result = x - z

elif y == '*':
    result = x * z

elif y == '/':
    result = x / z

print(f"{result:.1f}")