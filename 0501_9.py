h, w, x = map(int, input().split())
l = [input() for i in range(h)]

# print(h, w, x)
# print(l)

total = ""
for i in range(h):
    total += l[i]

count = 0
total2 = ""
while len(total) != 0:
    if count < x:
        total2 += total[0]
        count += 1
        total = total[1:]
    else:
        print(total2)
        total2 = ""
        count = 0
if len(total2) != 0:
    print(total2)