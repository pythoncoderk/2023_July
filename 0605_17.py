s = list(input())

l = []
x = 0
for i in range(len(s)):
    if s[i] == "R":
        x += 1
        l.append(x)
    else:
        x = 0

if l == []:
    print(0)
    exit()

print(max(l))