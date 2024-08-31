import itertools

n = int(input())
l = list(map(int, input().split()))

l2 = []
for i in range(1, len(l) + 1):
    for p in itertools.combinations(l, i):
        l2.append(p)

print(l2)

count = 0
for i in range(len(l2)):
    if len(l2[i]) == 1 or len(l2[i]) == 2:
        count += 1
    else:
        x = l2[1] - l2[0]
        chk = True
        for j in range(len(l2[i]) - 1):
            if x != l2[i + 1] - l2[i]:
                chk = False
                break
        if chk:
            count += 1
print(count)