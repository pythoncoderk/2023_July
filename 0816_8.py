n, k, f = map(int, input().split())
l = [int(input()) for i in range(k)]


l2 = l[f:]



l3 = []
for i in l2:
    if i not in l3:
        l3.append(i)

for i in l3:
    print(i)