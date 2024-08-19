s = input()

l = []
for i in range(len(s)):
    l.append(s.count(s[i]))

print("Yes" if l.count(2) == 4 else "No")