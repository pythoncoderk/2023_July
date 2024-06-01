n = int(input())
l = list(map(int, input().split()))
l2 = l[::]
l3 = l[::]

max_g = max(l)
count_g = l.count(max_g)
for i in range(n):
    if l[i] == max_g:
        l2[i] = "G"

# print(l2)
# print(l3)

if l2.count("G") == 1:
    for i in range(len(l3)):
        if l3[i] == max_g:
            l3[i] = 0

# print(l2)
# print(l3)

max_s = max(l3)
if count_g == 1:
    for i in range(n):
        if l3[i] == max_s:
            l2[i] = "S"

for i in range(n):
    if l3[i] == max_s:
        l3[i] = 0

max_b = max(l3)
if l2.count("G") + l2.count("S") == 2:
    for i in range(n):
        if l3[i] == max_b:
            l2[i] = "B"

for i in range(n):
    if l3[i] == max_b:
        l3[i] = 0

# print(l2)
# print(l3)

for i in range(n):
    if l2[i] != "G" and l2[i] != "S" and l2[i] != "B":
        l2[i] = "N"

for i in l2:
    print(i)