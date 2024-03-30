s = input()

s1 = s

f = []
for i in range(len(s1)):
    while s1:
        f.append(s1)
        s1 = s1[:-1]
    s1 = s[1:]
    s = s1
f = set(f)
print(len(f))