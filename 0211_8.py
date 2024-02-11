s = input()
# print(s)
total = 0
for i in range(len(s)):
    if s[i] == "0":
        total += 12
    elif s[i] == "-":
        pass
    elif 1 <= int(s[i]) <= 9:
        total += int(s[i]) + 2
print(total * 2)
