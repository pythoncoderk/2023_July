s = list(input())

# print(s)
for i in range(len(s)):
    if s[i] == "1":
        s[i] = int(s[i])

x = s.pop(0)
while s:
    if s[0] == "+":
        s.pop(0)
        x += s.pop(0)
    else:
        s.pop(0)
        x -= s.pop(0)
print(x)