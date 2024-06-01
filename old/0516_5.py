s = input()
t = input()
s2 = ""
for i in range(len(s)):
    if s[i].islower():
        s2 += s[i].upper()
    else:
        s2 += s[i].lower()

for i in range(len(t)):
    if t[i] in s:
        x = s.index(t[i])
        print(s[x], end="")
    else:
        x = s2.index(t[i])
        print(s[x], end="")
