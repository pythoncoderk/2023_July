s = input()
l = []
for i in range(len(s)):
    if s[i] == ".":
        l.append(i)
print(s[l[-1]+1:])