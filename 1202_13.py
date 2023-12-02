n = int(input())
l = []
l_counts = []
for i in range(n):
    x = int(input())
    l_counts.append(x)
    l2 = [list(map(int, input().split())) for i in range(x)]
    l.append(l2)
print(l)
print(l_counts)
one_no = (l[0])
print(one_no)
del l[0]
print(l)

for i in range(l_counts[0]):
