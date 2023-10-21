l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
x = 0
for i in range(l[1]-1, l[2]):
    x += l2[i]
print(x)