zero = ["C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "S", "T", "U", "V", "W", "X", "Y", "Z"]
one = ["A", "D", "O", "P", "Q", "R"]
n = input()
if n in zero:
    print(0)
elif n in one:
    print(1)
else:
    print(2)