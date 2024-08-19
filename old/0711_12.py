a, b = map(str, input().split())

a2 = list(a)
a_total = 0
for i in range(len(a2)):
    a_total += int(a2[i])

b2 = list(b)
b_total = 0
for i in range(len(b2)):
    b_total += int(b2[i])

print(a_total if a_total > b_total else b_total)