n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l2 = l[::]

# print(l2)

g = max(l)

for i in range(n):
    if l[i] == g:
        l2[i] = "G"
        l[i] = 0
count_g = l2.count("G")
s = max(l)

if count_g == 1:
    for i in range(n):
        if l[i] == s:
            l2[i] = "S"
            l[i] = 0

count_up = l2.count("G") + l2.count("S")
b = max(l)
if count_up == 2:
    for i in range(n):
        if l[i] == b:
            l2[i] = "B"
            l[i] = 0

l3 = ["N" if l2[i] != "G" and l2[i] != "S" and l2[i] != "B" else l2[i] for i in range(len(l2))]

# print(l2)
# print(l3)

for i in l3:
    print(i)