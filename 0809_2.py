s = input()
s1 = s[0]
s2 = s[1:]
total = int(s1)

while s2:
    if s2[0] == "+":
        total += int(s2[1])
        s2 = s2[2:]
    else:
        total -= int(s2[1])
        s2 = s2[2:]
print(total)