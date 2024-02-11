s = input()
x = len(s)
for i in range(3):
    if i == 1:
        print(f"+{s}+")
    else:
        print("+" * (x + 2))

