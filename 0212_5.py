import itertools

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)
total_l = []
def days(x, y):
    l2 = []
    for i in range(x, y+1):
        l2.append(i)
    return l2

for i in range(n):
    total_l.append(days(l[i][0], l[i][1]))
# print(total_l)

final_l = list(itertools.chain.from_iterable(total_l))
# print(final_l)

final_count = []
for i in final_l:
    final_count.append(final_l.count(i))
# print(final_count)

if n in final_count:
    print("OK")
else:
    print("NG")