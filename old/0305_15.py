n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]
for i in range(k):
    l2[i][0] = int(l2[i][0])

# print(l)
# print(l2)

def changeName(x, y):
    l[x-1][0] = y
    return y


for i in range(k):
    changeName(l2[i][0], l2[i][1])

for i in l:
    print(*i)