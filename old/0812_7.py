s = input()
t = int(input())

if t == 0:
    print(0)
    exit()

upper = 0
total = ""
for i in range(len(s) - 1, -1, -1):
    x = str((t * int(s[i])) + int(upper))
    total = x[-1] + total
    if len(x) == 2:
        upper = x[0]
    else:
        upper = 0

    if i == 0 and upper != 0:
        total = x[-1] + total

print(total)

