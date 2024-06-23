l = list(map(int, input().split()))

l2 = [l.count(l[i]) for i in range(len(l))]

# print(l2)

min_l2 = min(l2)
if min_l2 == 3:
    print(l[0])
    exit()

answer = 0
for i in range(3):
    if l2[i] == 1:
        answer = l[i]

print(answer)