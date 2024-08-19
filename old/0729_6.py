x = ""
for i in range(10):
    if i != 9:
        y = input()
        x += y + " "
    else:
        y = input()
        x += y

print(x)