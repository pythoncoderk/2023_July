s = input()

count_A = 0
count_a = 0
for i in range(len(s)):
    if s[i].isupper():
        count_A += 1
    else:
        count_a += 1

for i in range(len(s)):
    if count_A > count_a:
        x = s.upper()
    else:
        x = s.lower()

print(x)