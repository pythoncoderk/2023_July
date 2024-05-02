s1 = list(input().split())
s2 = list(input())

for i in range(len(s1)):
    s1[i] = int(s1[i])

# print(s1)
# print(s2)
total = ""
for i in range(len(s2)):
    x = ord(s2[i])-97
    if s1[x] >= 1:
        total += s2[i]
        s1[x] -= 1
print(total)