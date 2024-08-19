s = list(input())
s2 = list(input())

l = []
for i in range(len(s)):
    for j in range(len(s2)):
        if s[i] == s2[j]:
            l.append(j + 1)
            s2[j] = "*"

print(*l)