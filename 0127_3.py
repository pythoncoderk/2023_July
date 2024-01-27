s = input()
counts = 0
if s[0].isupper():
    counts += 1

for i in range(1, len(s)):
    if s[i].islower():
        counts += 1

if len(s) == counts:
    print("Yes")
else:
    print("No")