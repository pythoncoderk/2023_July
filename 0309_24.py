s = input()

x1 = 0
for i in range(len(s)):
    if s[i] == "|":
        x1 = i
        break

for i in range(x1+1, len(s)):
    if s[i] == "|":
        x2 = i
        break

print(s[:x1] + s[x2+1:])
