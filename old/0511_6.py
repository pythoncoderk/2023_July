l = list(map(int, input().split()))
l_s = set(l)

l2 = {i for i in range(3)}

if l[0] != l[1]:
    x = l2 - l_s
    x = list(x)
    print(x[0])
else:
    print(l[0])