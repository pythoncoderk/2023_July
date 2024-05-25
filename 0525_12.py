l = list(map(int, input().split()))
l2 = [1, 2, 3]

l = set(l)
l2 = set(l2)

x = l ^ l2
x = list(x)
if len(x) == 1:
    print(x[0])
else:
    print(-1)