s = list(input())

# print(s)

l = []
for i in range(3):
    s1 = s[:]
    x = s1.pop(i)
    l.append(x + s1[0] + s1[1])
    l.append(x + s1[1] + s1[0])

l = set(l)
print(len(l))

