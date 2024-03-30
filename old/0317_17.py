s = input()

total = 0
for i in range(len(s)):
    if s[i] == "/":
        total += 1
    elif s[i] == "<":
        total += 10
print(total)