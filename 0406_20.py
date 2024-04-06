n = int(input())
l = list(map(int, input().split()))
d = [{i+1: l[i], "rank": ""} for i in range(n)]
# print(n)
# print(l)
# print(d)

max_l1 = max(l)
if l.count(max_l1) == len(l):
    for i in range(n):
        print("G")
    exit()

max_l = max(l)
for i in range(n):
    if d[i][i+1] == max_l:
        d[i]["rank"] = "G"

iii = 0
g_count = 0
while max_l in l:
    if l[iii] == max_l:
        l.pop(iii)
        g_count += 1
    else:
        iii += 1
# print(l)

max_l = max(l)
for i in range(n):
    if g_count == 1:
        if d[i][i+1] == max_l:
            d[i]["rank"] = "S"

iiii = 0
s_count = 0
while max_l in l:
    if l[iiii] == max_l:
        l.pop(iiii)
        s_count += 1
    else:
        iiii += 1
# print(l)
# print(d)

max_l = max(l)
for i in range(n):
    if g_count + s_count == 2:
        if d[i][i+1] == max_l:
            d[i]["rank"] = "B"

iiiii = 0
b_count = 0
while max_l in l:
    if l[iiiii] == max_l:
        l.pop(iiiii)
        b_count += 1
    else:
        iiiii += 1

# print(d)

for i in range(n):
    if d[i]["rank"] == "":
        d[i]["rank"] = "N"

for i in range(n):
    print(d[i]["rank"])