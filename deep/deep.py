asw = input("What's the answer to the Great Question of Life, the Universe and Everything ? ")

asw = asw.strip().lower()

if asw == '42' or asw == 'forty-two' or asw == 'forty two':
    print("Yes")

else:
    print("No")