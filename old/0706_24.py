s = list(input())

x = 0
for i in range(len(s)):
    if s[i] == "+":
        x += 1
    else:
        x -= 1

print(x)