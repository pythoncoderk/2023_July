n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# print(n, m)
# print(l)
# print(l2)

point = 0
for i in range(len(l2)):
    point += l[l2[i]-1]

print(point)