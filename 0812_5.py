s = input()
t = int(input())

if t == 0:
    print(0)
    exit()

total = ""
upper = 0
for i in range(len(s) -1, -1, -1):
    x = (int(s[i])) * t
    x2 = (x % 10) + upper
    upper = x // 10
    total = str(x2) + total

    if i == 0 and upper != 0:
        total = str(upper) + total
print(total)
