s = list(input())

l = [int(s[i]) for i in range(len(s)) if s[i].isdecimal()]

# print(l)

total = 0
for i in range(len(l)):
    if l[i] == 0:
        total += 12
    else:
        total += l[i] + 2

print(total * 2)