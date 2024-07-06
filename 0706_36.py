n, q = map(int, input().split())
a = {int(input()) for i in range(n)}
k = [int(input()) for i in range(q)]

for i in range(q):
    if k[i] in a:
        print("YES")
    else:
        print("NO")