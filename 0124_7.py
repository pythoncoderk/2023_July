import sys

m, n = map(int, input().split())
l = [int(input()) for i in range(m)]
# print(l)

l2 = [n % l[i] for i in range(m)]
# print(l2)

min_l = min(l2)
if l2.count(min_l) == 1:
    print(l2.index(min_l)+1)
    sys.exit()

final_l = []
for i in range(m):
    if l2[i] == min_l:
        final_l.append(l[i])
    else:
        final_l.append(0)
max_f = max(final_l)

for i in range(m):
    if max_f == final_l[i]:
        print(i+1)
        break