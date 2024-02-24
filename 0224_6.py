n = int(input())
p = list(map(int, input().split()))
q = int(input())
a = [list(map(int, input().split())) for i in range(q)]

# print(n)
# print(p)
# print(q)
# print(a)

for i in range(q):
    x = p.index(a[i][0])
    y = p.index(a[i][1])
    if x < y:
        print(a[i][0])
    else:
        print(a[i][1])
