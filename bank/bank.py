greet = input("Hello!\n")

greet = greet.strip().lower()

if 'hello' in greet:
    print('$0')

elif 'h' == greet[0]:
    print('$20')

else:
    print('$100')
