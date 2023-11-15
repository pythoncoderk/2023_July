x, y = map(int, input().split())
l = list(map(int, input().split()))
l2 = []

while len(l) >= y:
    l2.append(l[:y])
    l.pop(0)

l3 = []
for i in range(len(l2)):
    l3.append(sum(l2[i]))

sss = 1
for i in range(len(l3)):
    if l3[i] == max(l3):
        break
    else:
        sss += 1
print(f"{l3.count(max(l3))} {sss}")