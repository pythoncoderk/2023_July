l = list(map(str, input().split()))
l3 = []
# print(l)
# print(l2)

for i in l:
    if i not in l3:
        l3.append(i)
        print(f"{i} {l.count(i)}")