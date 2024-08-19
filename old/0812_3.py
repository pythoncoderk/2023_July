s = input()
t = input()

up = 0
total = ""
for i in range(len(s) - 1, -1, -1):
    x = int(s[i])
    y = int(t[i])
    ans = str(x + y + up)
    if len(ans) == 2:
        up = int(ans[0])
        total = ans[1] + total
    else:
        total = ans + total
        up = 0

print(total if up == 0 else str(up) + total)
