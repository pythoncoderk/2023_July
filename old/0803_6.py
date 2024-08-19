n = int(input())
s = list(input())

l = []
for i in range(26):
    x = i + 97
    l.append(s.count(chr(x)))

print(*l)